#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Bounded local RI navigation adapter derived from UA's projection pattern.

Source: UncertaintyArchitectureGroup/uncertainty-architecture at
345c8f50745e5fde1303d0d7952634f7899220c9. See RI-NOTICE.md.
No candidate execution, remote state, semantic authority or full UA graph.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path, PurePosixPath

VERSION = 1
IGNORED = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "public"}
TEXT_SUFFIXES = {".md", ".json", ".toml", ".yml", ".yaml", ".py", ".cff", ".txt"}
MAX_FILES = 5000
MAX_FILE_BYTES = 2_000_000
MAX_TOTAL_BYTES = 50_000_000
SCRIPT = "tools/repository_intelligence.py"


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(root, relative):
    """Reject path traversal and every symlink, including inside-root aliases."""
    p = PurePosixPath(relative)
    if not relative or p.is_absolute() or any(x in {"", ".", ".."} for x in relative.split("/")):
        raise ValueError(f"Unsafe repository path: {relative}")
    current = root
    for part in p.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Symlink is not a repository input/output: {relative}")
    current.resolve().relative_to(root)
    return current


def active_markdown(text):
    """Extract a bounded active Markdown view without treating code as comments.

    Balanced single-line code spans are supported. A comment-bearing unmatched
    span is visibly unsupported instead of silently losing following inventory.
    """
    lines, fence, comment = [], None, False
    for line in text.splitlines():
        if fence is not None:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(fence[1]) + r",}[ \t]*", line):
                fence = None
            continue
        if not comment:
            if line.startswith(("    ", "\t")):
                continue
            opening = re.match(r"^ {0,3}(\x60{3,}|~{3,})(.*)$", line)
            if opening:
                marker, info = opening.groups()
                if marker[0] != chr(96) or chr(96) not in info:
                    fence = (marker[0], len(marker))
                    continue
        remainder, visible = line, ""
        while remainder:
            if comment:
                end = remainder.find("-->")
                if end < 0:
                    remainder = ""
                else:
                    comment = False
                    remainder = remainder[end + 3:]
            else:
                start = remainder.find("<!--")
                span = re.search(r"\x60+", remainder)
                if start >= 0 and span and span.start() < start:
                    delimiter = span.group()
                    closing = re.search(r"(?<!\x60)" + re.escape(delimiter) + r"(?!\x60)",
                                        remainder[span.end():])
                    if closing is None:
                        raise ValueError("Unsupported comment-bearing multiline/unmatched code span")
                    end = span.end() + closing.end()
                    visible += remainder[:end]
                    remainder = remainder[end:]
                    continue
                if start < 0:
                    visible += remainder
                    remainder = ""
                else:
                    visible += remainder[:start]
                    comment = True
                    remainder = remainder[start + 4:]
        lines.append(visible)
    return "\n".join(lines)


def scan(root, output):
    """Complete admitted text inventory; binary assets are existence-only."""
    records, texts, size_total = [], {}, 0
    for parent, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED)
        for d in dirs:
            safe_path(root, (Path(parent) / d).relative_to(root).as_posix())
        for name in sorted(files):
            path = Path(parent) / name
            relative = path.relative_to(root).as_posix()
            # A worktree has a .git file where a regular checkout has a directory.
            if name == ".git" or relative == output or name.endswith((".pyc", ".tmp")):
                continue
            path = safe_path(root, relative)
            if not path.is_file():
                raise ValueError(f"Unsupported input: {relative}")
            if len(records) >= MAX_FILES:
                raise ValueError("RI file bound exceeded; use direct repository reading")
            if path.suffix.lower() in TEXT_SUFFIXES:
                size = path.stat().st_size
                size_total += size
                if size > MAX_FILE_BYTES or size_total > MAX_TOTAL_BYTES:
                    raise ValueError(f"RI text bound exceeded at {relative}")
                data = path.read_bytes()
                texts[relative] = data.decode("utf-8")
                records.append({"path": relative, "identity_mode": "content", "sha256": digest(data)})
            else:
                records.append({"path": relative, "identity_mode": "existence"})
    return sorted(records, key=lambda x: x["path"]), texts


def load_config(root, config_path):
    config = json.loads(safe_path(root, config_path).read_text(encoding="utf-8"))
    if config.get("schema_version") != VERSION:
        raise ValueError("Unsupported RI config schema")
    output = config["output"]
    if not output.endswith("/repository-intelligence/agent-context.json"):
        raise ValueError("Projection output must be a dedicated repository-intelligence/agent-context.json")
    safe_path(root, output)
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", config["repository"]):
        raise ValueError("Invalid repository identity")
    for key in ("glossaries", "registries"):
        for path in config.get(key, []):
            safe_path(root, path)
    for owner in config["owners"]:
        safe_path(root, owner["path"])
        if not owner["concern"].strip() or not owner["queries"]:
            raise ValueError("Owner needs a concern and explicit query aliases")
    if len({x["concern"] for x in config["owners"]}) != len(config["owners"]):
        raise ValueError("Duplicate owner concern")
    for link in config.get("cross_repository", []):
        if not link["url"].startswith("https://github.com/"):
            raise ValueError("Cross-repository links must explicitly point to GitHub")
    return config


def build(root, config_path):
    config = load_config(root, config_path)
    records, texts = scan(root, config["output"])
    required = [config_path, SCRIPT] + config.get("glossaries", []) + config.get("registries", [])
    required += [x["path"] for x in config["owners"]]
    missing = sorted(set(required) - texts.keys())
    if missing:
        raise ValueError("Missing represented owner/input: " + ", ".join(missing))
    instructions = [
        {"path": p, "scope_root": PurePosixPath(p).parent.as_posix()}
        for p in texts if PurePosixPath(p).name == "AGENTS.md"
    ]
    if not any(x["path"] == "AGENTS.md" for x in instructions):
        raise ValueError("Root AGENTS.md is required")
    terms = []
    for p in config.get("glossaries", []):
        for title in re.findall(r"^#{2,3}\s+(.+?)\s*$", active_markdown(texts[p]), re.M):
            terms.append({"term": title, "path": p})
    sources = []
    for p in config.get("registries", []):
        headers = 0
        for line in active_markdown(texts[p]).splitlines():
            if line.startswith("|"):
                fields = [x.strip() for x in line.strip().strip("|").split("|")]
                if fields[0] == "ID":
                    if fields != ["ID", "Source", "Evidence review", "Integration audit",
                                  "Last verified", "Can support", "Current use"]:
                        raise ValueError(f"Unsupported source-registry header in {p}")
                    headers += 1
                    continue
                if all(re.fullmatch(r":?-+:?", x) for x in fields):
                    continue
                if len(fields) != 7:
                    raise ValueError(f"Unsupported source-registry row in {p}")
                if not re.fullmatch(r"\*\*(?:P|D|S|M|DS)-\d{4}-\d{2}\*\*", fields[0]):
                    raise ValueError(f"Unsupported source identity in {p}: {fields[0]}")
                source_id = fields[0].strip("*")
                brief = re.search(r"\]\(([^)]+)\)", fields[2])
                brief_path = None
                if brief:
                    joined = str(PurePosixPath(p).parent / brief.group(1))
                    safe_path(root, joined)
                    if joined not in texts:
                        raise ValueError(f"Missing represented brief: {joined}")
                    brief_path = joined
                sources.append({
                    "id": source_id, "path": p, "source": fields[1],
                    "evidence_review": re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", fields[2]),
                    "integration_audit": fields[3], "last_verified": fields[4],
                    "can_support": fields[5], "current_use": fields[6],
                    "brief_path": brief_path,
                })
        if not headers:
            raise ValueError(f"Missing supported source-registry schema in {p}")
    if len({x["id"] for x in sources}) != len(sources):
        raise ValueError("Duplicate source ID in represented registries")
    artifacts = []
    for path, body in sorted(texts.items()):
        title = re.search(r"^#\s+(.+)$", active_markdown(body), re.M) if path.endswith(".md") else None
        scopes = [x["path"] for x in instructions if x["scope_root"] == "."
                  or path == x["path"] or path.startswith(x["scope_root"] + "/")]
        artifacts.append({"path": path, "title": title.group(1) if title else path,
                          "instructions": sorted(scopes)})
    return {
        "schema_version": VERSION, "repository": config["repository"],
        "capabilities": ["local-owner-candidates", "complete-admitted-inventories", "freshness"],
        "limitations": [
            "Navigation only; read owning sources and current GitHub state.",
            "No semantic graph, impact traversal or trusted tested-merge comparison.",
            "Excluded build/cache directories are not represented; binary assets are existence-only.",
            "Lexical miss or untranslated query does not establish absence.",
        ],
        "source_identity": {"algorithm": "sha256-path-content-v1",
                            "digest": digest(canonical(records).encode()), "inputs": records},
        "producer": {"path": SCRIPT, "sha256": digest(safe_path(root, SCRIPT).read_bytes()),
                     "config_path": config_path,
                     "config_sha256": digest(safe_path(root, config_path).read_bytes())},
        "owners": config["owners"], "terms": terms, "sources": sources,
        "instructions": sorted(instructions, key=lambda x: x["path"]),
        "artifacts": artifacts, "cross_repository": config.get("cross_repository", []),
    }


def verify(root, config_path):
    expected = build(root, config_path)
    config = load_config(root, config_path)
    path = safe_path(root, config["output"])
    if not path.is_file():
        raise ValueError("Missing RI context; build it or use direct repository reading")
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual != expected:
        raise ValueError("Stale or altered RI context; rebuild or use direct repository reading")
    return expected


def lookup(surface, query):
    q = " ".join(query.casefold().split())
    if not q:
        raise ValueError("Empty query")
    # Explicit aliases are explainable candidates; generic matches cannot claim ownership.
    owners = [o for o in surface["owners"]
              if any(q in a.casefold() or a.casefold() in q for a in o["queries"])]
    terms = [t for t in surface["terms"] if q in t["term"].casefold()]
    sources = [s for s in surface["sources"]
               if q in s["id"].casefold() or q in s["source"].casefold()]
    artifacts = [a for a in surface["artifacts"]
                 if q in (a["title"] + " " + a["path"]).casefold()]
    if sources and not owners:
        owners = [o for o in surface["owners"] if o["path"] in {s["path"] for s in sources}]
    if terms and not owners:
        owners = [o for o in surface["owners"] if o["path"] in {t["path"] for t in terms}]
    return {"repository": surface["repository"], "query": query,
            "status": "candidates-read-sources" if owners or terms or sources or artifacts
                      else "unresolved-use-direct-search",
            "owner_candidates": owners, "terms": terms, "sources": sources, "artifacts": artifacts}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--config", required=True, help="Repository-relative config path")
    parser.add_argument("command", choices=("build", "verify", "query"))
    parser.add_argument("query_text", nargs="?")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        if args.command == "build":
            surface = build(root, args.config)
            target = safe_path(root, load_config(root, args.config)["output"])
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix(".tmp")
            safe_path(root, temporary.relative_to(root).as_posix())
            temporary.write_text(json.dumps(surface, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            os.replace(temporary, target)
            print(f"Built {target.relative_to(root)}: {len(surface['artifacts'])} represented texts")
        else:
            surface = verify(root, args.config)
            if args.command == "query":
                if not args.query_text:
                    raise ValueError("query requires text")
                print(json.dumps(lookup(surface, args.query_text), ensure_ascii=False, indent=2))
            else:
                print("Repository Intelligence context is fresh.")
    except (ValueError, OSError, UnicodeError, KeyError, TypeError) as exc:
        print(f"RI unavailable: {exc}. Read authoritative sources directly.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
