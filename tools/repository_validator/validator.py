from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re

from .contract import RepositoryContract, load_contract
from .markdown import extract_headings, inline_code_bullets_under_heading
from .registry import RegistryParseError, SourceRecord, parse_source_registry


@dataclass(frozen=True)
class Issue:
    path: str
    code: str
    message: str
    line: int | None = None

    def text(self) -> str:
        location = self.path
        if self.line is not None:
            location += f":{self.line}"
        return f"{location}: [{self.code}] {self.message}"

    def github_annotation(self) -> str:
        location = f"file={self.path}"
        if self.line is not None:
            location += f",line={self.line}"
        message = (
            self.message.replace("%", "%25")
            .replace("\r", "%0D")
            .replace("\n", "%0A")
        )
        return f"::error {location}::[{self.code}] {message}"


class RepositoryValidator:
    def __init__(self, root: Path, contract: RepositoryContract):
        self.root = root.resolve()
        self.contract = contract

    def validate(self) -> tuple[Issue, ...]:
        issues: list[Issue] = []
        issues.extend(self._validate_required_files())
        issues.extend(self._validate_required_headings())
        issues.extend(self._validate_status_model())
        issues.extend(self._validate_source_registry())
        unique = {
            (issue.path, issue.code, issue.message, issue.line): issue
            for issue in issues
        }
        return tuple(
            sorted(
                unique.values(),
                key=lambda issue: (
                    issue.path,
                    issue.line if issue.line is not None else 0,
                    issue.code,
                    issue.message,
                ),
            )
        )

    def _path(self, relative: str) -> Path:
        return self.root / relative

    def _validate_required_files(self) -> list[Issue]:
        issues: list[Issue] = []
        for relative in self.contract.required_files:
            path = self._path(relative)
            if not path.is_file():
                issues.append(
                    Issue(
                        relative,
                        "required-file-missing",
                        "required file does not exist",
                    )
                )
            elif path.stat().st_size == 0:
                issues.append(
                    Issue(relative, "required-file-empty", "required file is empty")
                )
        return issues

    def _validate_required_headings(self) -> list[Issue]:
        issues: list[Issue] = []
        for requirement in self.contract.documents:
            path = self._path(requirement.path)
            if not path.is_file():
                continue
            headings = set(extract_headings(path.read_text(encoding="utf-8")))
            for heading in requirement.required_headings:
                if heading not in headings:
                    issues.append(
                        Issue(
                            requirement.path,
                            "required-heading-missing",
                            f"required heading is missing: {heading}",
                        )
                    )
        return issues

    def _validate_status_model(self) -> list[Issue]:
        requirement = self.contract.status_model
        path = self._path(requirement.path)
        if not path.is_file():
            return []

        text = path.read_text(encoding="utf-8")
        evidence = inline_code_bullets_under_heading(
            text, requirement.evidence_heading
        )
        integration = inline_code_bullets_under_heading(
            text, requirement.integration_heading
        )
        issues: list[Issue] = []
        if evidence != self.contract.evidence_review_statuses:
            issues.append(
                Issue(
                    requirement.path,
                    "evidence-status-model-drift",
                    "allowed Evidence review statuses do not match "
                    "repository-contract.toml",
                )
            )
        if integration != self.contract.integration_audit_statuses:
            issues.append(
                Issue(
                    requirement.path,
                    "integration-status-model-drift",
                    "allowed Integration audit statuses do not match "
                    "repository-contract.toml",
                )
            )
        return issues

    def _validate_source_registry(self) -> list[Issue]:
        relative = self.contract.source_registry
        path = self._path(relative)
        if not path.is_file():
            return []

        try:
            records = parse_source_registry(
                path.read_text(encoding="utf-8"),
                self.contract.registry.required_columns,
            )
        except RegistryParseError as exc:
            return [Issue(relative, "source-registry-parse", str(exc))]

        issues: list[Issue] = []
        seen: dict[str, int] = {}
        for record in records:
            issues.extend(self._validate_source_record(record))
            if record.source_id in seen:
                issues.append(
                    Issue(
                        relative,
                        "duplicate-source-id",
                        f"duplicate Source ID {record.source_id}; "
                        f"first seen on line {seen[record.source_id]}",
                        record.line,
                    )
                )
            else:
                seen[record.source_id] = record.line
        return issues

    def _validate_source_record(self, record: SourceRecord) -> list[Issue]:
        relative = self.contract.source_registry
        registry = self.contract.registry
        issues: list[Issue] = []

        fields = {
            "ID": record.source_id,
            "Source": record.source,
            "Evidence review": record.evidence_review,
            "Integration audit": record.integration_audit,
            "Last verified": record.last_verified,
            "Can support": record.can_support,
            "Current use": record.current_use,
        }
        for column in registry.required_nonempty_columns:
            if not fields[column]:
                issues.append(
                    Issue(
                        relative,
                        "source-registry-empty-field",
                        f"{record.source_id or 'source row'} has an empty {column} field",
                        record.line,
                    )
                )

        if not re.fullmatch(registry.source_id_pattern, record.source_id):
            issues.append(
                Issue(
                    relative,
                    "invalid-source-id",
                    f"Source ID does not match {registry.source_id_pattern}: "
                    f"{record.source_id}",
                    record.line,
                )
            )

        if record.evidence_review not in self.contract.evidence_review_statuses:
            issues.append(
                Issue(
                    relative,
                    "invalid-evidence-status",
                    f"unsupported Evidence review status: {record.evidence_review}",
                    record.line,
                )
            )
        if record.integration_audit not in self.contract.integration_audit_statuses:
            issues.append(
                Issue(
                    relative,
                    "invalid-integration-status",
                    f"unsupported Integration audit status: {record.integration_audit}",
                    record.line,
                )
            )

        if record.integration_audit == registry.verified_status:
            if not re.fullmatch(registry.date_pattern, record.last_verified):
                issues.append(
                    Issue(
                        relative,
                        "verified-date-required",
                        f"{record.source_id} is Verified but Last verified is not "
                        "YYYY-MM-DD",
                        record.line,
                    )
                )
            else:
                try:
                    date.fromisoformat(record.last_verified)
                except ValueError:
                    issues.append(
                        Issue(
                            relative,
                            "invalid-verification-date",
                            f"{record.source_id} has an invalid calendar date: "
                            f"{record.last_verified}",
                            record.line,
                        )
                    )
        elif record.last_verified != registry.empty_date:
            issues.append(
                Issue(
                    relative,
                    "unverified-date-prohibited",
                    f"{record.source_id} is not Verified, so Last verified must be "
                    f"{registry.empty_date}",
                    record.line,
                )
            )

        if record.evidence_review in registry.local_brief_link_required_for:
            if not record.brief_link:
                issues.append(
                    Issue(
                        relative,
                        "reviewed-brief-link-required",
                        f"{record.source_id} is {record.evidence_review} but has no "
                        "local evidence-brief link",
                        record.line,
                    )
                )
            elif "://" in record.brief_link or record.brief_link.startswith("#"):
                issues.append(
                    Issue(
                        relative,
                        "reviewed-brief-link-not-local",
                        f"{record.source_id} must link to a repository evidence brief",
                        record.line,
                    )
                )
            else:
                brief_path = (
                    self._path(relative).parent / record.brief_link
                ).resolve()
                try:
                    brief_path.relative_to(self.root)
                except ValueError:
                    issues.append(
                        Issue(
                            relative,
                            "reviewed-brief-link-escapes-repository",
                            f"{record.source_id} evidence-brief link escapes the "
                            "repository",
                            record.line,
                        )
                    )
                else:
                    if not brief_path.is_file():
                        issues.append(
                            Issue(
                                relative,
                                "reviewed-brief-missing",
                                f"{record.source_id} linked evidence brief does not "
                                f"exist: {record.brief_link}",
                                record.line,
                            )
                        )

        return issues


def validate_repository(
    root: Path,
    contract_path: Path | None = None,
) -> tuple[Issue, ...]:
    root = root.resolve()
    path = contract_path or root / "governance/repository-contract.toml"
    contract = load_contract(path)
    return RepositoryValidator(root, contract).validate()
