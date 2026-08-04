from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any
import tomllib


REQUIRED_REGISTRY_COLUMNS = (
    "ID",
    "Source",
    "Evidence review",
    "Integration audit",
    "Last verified",
    "Can support",
    "Current use",
)


class ContractError(ValueError):
    """Raised when the executable contract is malformed."""


@dataclass(frozen=True)
class DocumentRequirement:
    path: str
    required_headings: tuple[str, ...]


@dataclass(frozen=True)
class RegistrySectionRequirement:
    heading: str
    id_prefix: str
    brief_directory: str
    minimum_rows: int


@dataclass(frozen=True)
class RegistryRequirement:
    sections: tuple[RegistrySectionRequirement, ...]
    required_columns: tuple[str, ...]
    required_nonempty_columns: tuple[str, ...]
    source_id_pattern: str
    date_pattern: str
    empty_date: str
    verified_status: str
    verified_requires_evidence_status: str
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


def _nonnegative_int(data: dict[str, Any], key: str) -> int:
    value = data.get(key)
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ContractError(f"{key} must be a non-negative integer")
    return value


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


def _safe_directory_name(value: str, key: str) -> str:
    normalized = _safe_relative_path(value, key)
    path = Path(normalized)
    if len(path.parts) != 1 or normalized in {"", "."}:
        raise ContractError(f"{key} must be one evidence-class directory name")
    return normalized


def _registry_sections(data: dict[str, Any]) -> tuple[RegistrySectionRequirement, ...]:
    raw_sections = data.get("sections")
    if not isinstance(raw_sections, list) or not raw_sections:
        raise ContractError("registry.sections must contain at least one table")

    sections: list[RegistrySectionRequirement] = []
    headings: set[str] = set()
    prefixes: set[str] = set()
    brief_directories: set[str] = set()
    for index, item in enumerate(raw_sections):
        if not isinstance(item, dict):
            raise ContractError(f"registry.sections[{index}] must be a table")
        heading = _string(item, "heading")
        id_prefix = _string(item, "id_prefix")
        brief_directory = _safe_directory_name(
            _string(item, "brief_directory"),
            f"registry.sections[{index}].brief_directory",
        )
        minimum_rows = _nonnegative_int(item, "minimum_rows")
        if heading in headings:
            raise ContractError(f"duplicate registry section heading: {heading}")
        if id_prefix in prefixes:
            raise ContractError(f"duplicate registry section ID prefix: {id_prefix}")
        if brief_directory in brief_directories:
            raise ContractError(
                f"duplicate registry section brief directory: {brief_directory}"
            )
        headings.add(heading)
        prefixes.add(id_prefix)
        brief_directories.add(brief_directory)
        sections.append(
            RegistrySectionRequirement(
                heading=heading,
                id_prefix=id_prefix,
                brief_directory=brief_directory,
                minimum_rows=minimum_rows,
            )
        )
    return tuple(sections)


def load_contract(path: Path) -> RepositoryContract:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as exc:
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
    if len(required_files) != len(set(required_files)):
        raise ContractError("required_files contains duplicate normalized paths")

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
        sections=_registry_sections(registry_data),
        required_columns=_string_list(registry_data, "required_columns"),
        required_nonempty_columns=_string_list(
            registry_data, "required_nonempty_columns"
        ),
        source_id_pattern=_regex(registry_data, "source_id_pattern"),
        date_pattern=_regex(registry_data, "date_pattern"),
        empty_date=_string(registry_data, "empty_date"),
        verified_status=_string(registry_data, "verified_status"),
        verified_requires_evidence_status=_string(
            registry_data, "verified_requires_evidence_status"
        ),
        local_brief_link_required_for=_string_list(
            registry_data, "local_brief_link_required_for"
        ),
    )

    if registry.required_columns != REQUIRED_REGISTRY_COLUMNS:
        raise ContractError(
            "registry.required_columns must match the Source Registry parser schema"
        )
    unknown_nonempty_columns = set(registry.required_nonempty_columns) - set(
        registry.required_columns
    )
    if unknown_nonempty_columns:
        raise ContractError(
            "required_nonempty_columns contains columns absent from required_columns: "
            + ", ".join(sorted(unknown_nonempty_columns))
        )
    if registry.verified_status not in integration_statuses:
        raise ContractError(
            "registry.verified_status must be an allowed Integration audit status"
        )
    if registry.verified_requires_evidence_status not in evidence_statuses:
        raise ContractError(
            "registry.verified_requires_evidence_status must be an allowed "
            "Evidence review status"
        )
    unknown_brief_statuses = set(registry.local_brief_link_required_for) - set(
        evidence_statuses
    )
    if unknown_brief_statuses:
        raise ContractError(
            "local_brief_link_required_for contains unsupported Evidence review "
            "statuses: "
            + ", ".join(sorted(unknown_brief_statuses))
        )
    if (
        registry.verified_requires_evidence_status
        not in registry.local_brief_link_required_for
    ):
        raise ContractError(
            "the Evidence review status required for Verified integration must also "
            "require a local evidence-brief link"
        )
    for section in registry.sections:
        sample_id = f"{section.id_prefix}2000-01"
        if not re.fullmatch(registry.source_id_pattern, sample_id):
            raise ContractError(
                f"registry section prefix {section.id_prefix!r} is incompatible "
                "with source_id_pattern"
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

    protected_references = {
        policy_authority,
        source_registry,
        status_model.path,
        *seen_paths,
    }
    unprotected_references = protected_references - set(required_files)
    if unprotected_references:
        raise ContractError(
            "contract references files that are absent from required_files: "
            + ", ".join(sorted(unprotected_references))
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
