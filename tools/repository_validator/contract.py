from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any
import tomllib


class ContractError(ValueError):
    """Raised when the executable contract is malformed."""


@dataclass(frozen=True)
class DocumentRequirement:
    path: str
    required_headings: tuple[str, ...]


@dataclass(frozen=True)
class RegistryRequirement:
    table_sections: tuple[str, ...]
    required_columns: tuple[str, ...]
    required_nonempty_columns: tuple[str, ...]
    source_id_pattern: str
    date_pattern: str
    empty_date: str
    verified_status: str
    local_brief_link_required_for: tuple[str, ...]


@dataclass(frozen=True)
class StatusModelRequirement:
    path: str
    evidence_heading: str
    integration_heading: str


@dataclass(frozen=True)
class RepositoryContract:
    version: int
    policy_authority: str
    source_registry: str
    required_files: tuple[str, ...]
    evidence_review_statuses: tuple[str, ...]
    integration_audit_statuses: tuple[str, ...]
    status_model: StatusModelRequirement
    registry: RegistryRequirement
    documents: tuple[DocumentRequirement, ...]


def _string(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{key} must be a non-empty string")
    return value


def _string_list(data: dict[str, Any], key: str) -> tuple[str, ...]:
    value = data.get(key)
    if not isinstance(value, list) or not value:
        raise ContractError(f"{key} must be a non-empty array")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ContractError(f"{key} must contain only non-empty strings")
    if len(value) != len(set(value)):
        raise ContractError(f"{key} must not contain duplicates")
    return tuple(value)


def _regex(data: dict[str, Any], key: str) -> str:
    value = _string(data, key)
    try:
        re.compile(value)
    except re.error as exc:
        raise ContractError(f"{key} must be a valid regular expression: {exc}") from exc
    return value


def _safe_relative_path(value: str, key: str) -> str:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ContractError(f"{key} must be a safe repository-relative path")
    return path.as_posix()


def load_contract(path: Path) -> RepositoryContract:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise ContractError(f"cannot read contract {path}: {exc}") from exc

    version = data.get("contract_version")
    if version != 1:
        raise ContractError("contract_version must be 1")

    policy_authority = _safe_relative_path(
        _string(data, "policy_authority"), "policy_authority"
    )
    if policy_authority != "AGENTS.md":
        raise ContractError("policy_authority must remain AGENTS.md")

    source_registry = _safe_relative_path(
        _string(data, "source_registry"), "source_registry"
    )
    required_files = tuple(
        _safe_relative_path(item, "required_files")
        for item in _string_list(data, "required_files")
    )

    statuses = data.get("status_enums")
    if not isinstance(statuses, dict):
        raise ContractError("status_enums table is required")
    evidence_statuses = _string_list(statuses, "evidence_review")
    integration_statuses = _string_list(statuses, "integration_audit")

    status_model_data = data.get("status_model")
    if not isinstance(status_model_data, dict):
        raise ContractError("status_model table is required")
    status_model = StatusModelRequirement(
        path=_safe_relative_path(_string(status_model_data, "path"), "status_model.path"),
        evidence_heading=_string(status_model_data, "evidence_heading"),
        integration_heading=_string(status_model_data, "integration_heading"),
    )

    registry_data = data.get("registry")
    if not isinstance(registry_data, dict):
        raise ContractError("registry table is required")
    registry = RegistryRequirement(
        table_sections=_string_list(registry_data, "table_sections"),
        required_columns=_string_list(registry_data, "required_columns"),
        required_nonempty_columns=_string_list(
            registry_data, "required_nonempty_columns"
        ),
        source_id_pattern=_regex(registry_data, "source_id_pattern"),
        date_pattern=_regex(registry_data, "date_pattern"),
        empty_date=_string(registry_data, "empty_date"),
        verified_status=_string(registry_data, "verified_status"),
        local_brief_link_required_for=_string_list(
            registry_data, "local_brief_link_required_for"
        ),
    )

    unknown_nonempty_columns = set(registry.required_nonempty_columns) - set(
        registry.required_columns
    )
    if unknown_nonempty_columns:
        raise ContractError(
            "required_nonempty_columns contains columns absent from required_columns: "
            + ", ".join(sorted(unknown_nonempty_columns))
        )

    documents_data = data.get("documents")
    if not isinstance(documents_data, list) or not documents_data:
        raise ContractError("at least one [[documents]] table is required")
    documents: list[DocumentRequirement] = []
    seen_paths: set[str] = set()
    for index, item in enumerate(documents_data):
        if not isinstance(item, dict):
            raise ContractError(f"documents[{index}] must be a table")
        document_path = _safe_relative_path(
            _string(item, "path"), f"documents[{index}].path"
        )
        if document_path in seen_paths:
            raise ContractError(f"duplicate document requirement: {document_path}")
        seen_paths.add(document_path)
        documents.append(
            DocumentRequirement(
                path=document_path,
                required_headings=_string_list(item, "required_headings"),
            )
        )

    return RepositoryContract(
        version=version,
        policy_authority=policy_authority,
        source_registry=source_registry,
        required_files=required_files,
        evidence_review_statuses=evidence_statuses,
        integration_audit_statuses=integration_statuses,
        status_model=status_model,
        registry=registry,
        documents=tuple(documents),
    )
