#!/usr/bin/env python3
"""Read-only Markdown projection and a pinned Quartz HTML package producer.

No deployment, source-state mutation, PDF/Chromium install or automatic upgrade.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import tempfile
import time
import tomllib
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
OWNER = Path("tools/report_web")
ENGINE_REPO = "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture.git"
ENGINE_PIN = "989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3"
OVERLAYS = {"quartz.config.ts": "quartz.config.ts", "quartz.layout.ts": "quartz.layout.ts",
            "report-components.tsx": "report-components.tsx", "prepare.mjs": "prepare.mjs",
            "report-indexes.ts": "report-indexes.ts",
            "report.scss": "quartz/styles/custom.scss"}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(value).hexdigest()


def safe_path(root, relative):
    if not isinstance(relative, str) or not relative or relative.startswith("/") or "\\" in relative:
        raise ValueError(f"Unsafe path: {relative}")
    if any(p in {"", ".", ".."} for p in relative.split("/")):
        raise ValueError(f"Unsafe path: {relative}")
    result = Path(root)
    if result.is_symlink():
        raise ValueError(f"Symlink root: {root}")
    for part in PurePosixPath(relative).parts:
        result /= part
        if result.is_symlink():
            raise ValueError(f"Symlink: {relative}")
    return result


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def run(args, cwd):
    subprocess.run([str(a) for a in args], cwd=cwd, check=True)


def load_manifest(root):
    data = json.loads(safe_path(root, str(OWNER / "publication.json")).read_text())
    if (data.get("schema_version") != 1 or data.get("mount") != "/subprime/"
            or data.get("canonical_base") != "https://vitaliioborskyi.ai/subprime/"
            or data.get("engine", {}).get("repository") != ENGINE_REPO
            or data["engine"].get("commit") != ENGINE_PIN):
        raise ValueError("Unknown report contract or engine pin")
    sources, slugs = set(), set()
    for p in data["pages"]:
        source, slug = p["source"], p["slug"]
        if source in sources or slug.casefold() in slugs or not re.fullmatch(r"[a-z0-9]+(?:[-/][a-z0-9]+)*", slug):
            raise ValueError(f"Duplicate/invalid publication route: {source} -> {slug}")
        if not (source.endswith(".md") and (source.startswith(("report/", "evidence/", "protocols/"))
                or "/" not in source or source == "tools/report_web/landing.md")):
            raise ValueError(f"Ineligible source: {source}")
        path = safe_path(root, source)
        if not path.is_file():
            raise ValueError(f"Missing source: {source}")
        sources.add(source)
        slugs.add(slug.casefold())
    if "index" not in slugs:
        raise ValueError("Report index missing")
    for slug in slugs:
        if slug.split("/", 1)[0] in {"media", "static", "notices"} or any(other.startswith(slug + "/") for other in slugs):
            raise ValueError(f"File/directory clean-URL collision or reserved route: {slug}")
    for asset in data["assets"]:
        if not asset.startswith("assets/") or not safe_path(root, asset).is_file():
            raise ValueError(f"Missing/unsafe asset: {asset}")
    return data


def engine_path():
    # Outside the research tree, so the dependency checkout never pollutes RI.
    return Path(os.environ.get("SUBPRIME_QUARTZ_ENGINE", str(Path.home() / ".cache/subprime-quartz" / ENGINE_PIN))).absolute()


def verify_engine(engine, require_dependencies=True):
    if engine.is_symlink() or git(engine, "rev-parse", "HEAD") != ENGINE_PIN:
        raise ValueError("Engine absent or wrong pin; run setup")
    allowed = set(OVERLAYS.values())
    changes = git(engine, "diff", "--name-only", "HEAD").splitlines()
    untracked = git(engine, "ls-files", "--others", "--exclude-standard").splitlines()
    if (set(changes) | set(untracked)) - allowed:
        raise ValueError("Pinned engine implementation/lockfile was modified")
    for path in allowed:
        safe_path(engine, path)
    if require_dependencies and not (engine / "node_modules/.package-lock.json").is_file():
        raise ValueError("Engine dependencies absent; run setup")


def setup(engine):
    if not engine.exists():
        engine.mkdir(parents=True)
        run(["git", "init", "--quiet"], engine)
        run(["git", "remote", "add", "origin", ENGINE_REPO], engine)
        run(["git", "fetch", "--depth=1", "origin", ENGINE_PIN], engine)
        run(["git", "checkout", "--detach", "FETCH_HEAD"], engine)
    if git(engine, "rev-parse", "HEAD") != ENGINE_PIN:
        raise ValueError("Existing cache has another engine; use a fresh cache")
    verify_engine(engine, require_dependencies=False)
    run(["npm", "ci", "--no-audit", "--no-fund"], engine)
    verify_engine(engine)


def split_frontmatter(text):
    if text.startswith("+++\n"):
        end = text.find("\n+++", 4)
        if end < 0 or text[end + 4:end + 5] not in {"", "\n", "\r"}:
            raise ValueError("Unclosed TOML metadata")
        metadata = tomllib.loads(text[4:end])
        return metadata, text[end + 4:].lstrip("\r\n")
    if text.startswith("---\n"):
        raise ValueError("YAML source metadata needs an explicit adapter contract")
    return {}, text


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.assets = set(), [], []
        self.canonical, self.robots, self.has_article = [], [], False
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "article":
            self.has_article = True
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in {"img", "script", "source"} and a.get("src"):
            self.assets.append(a["src"])
        if tag == "link" and a.get("rel") == "stylesheet":
            self.assets.append(a["href"])
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a["href"])
        if tag == "meta" and a.get("name") == "robots":
            self.robots.append(a.get("content"))


def fingerprint(site, mount):
    resources = ["index.css", "prescript.js", "postscript.js", "static/contentIndex.json"]
    replacements = {}
    for relative in resources:
        source = safe_path(site, relative)
        output = "_assets/" + digest(source.read_bytes()) + source.suffix
        target = safe_path(site, output)
        target.parent.mkdir(exist_ok=True)
        shutil.copyfile(source, target)
        replacements[relative] = mount + output
    # Only resource attributes and Quartz's known index-fetch expression change;
    # quoted words inside rendered research/code must remain intact.
    class Rewrite(HTMLParser):
        def __init__(self, text):
            super().__init__(convert_charrefs=False)
            self.text, self.edits, self.script = text, [], False
            self.lines = [0]
            for match in re.finditer("\n", text):
                self.lines.append(match.end())
            self.feed(text)

        def absolute_offset(self):
            line, col = self.getpos()
            return self.lines[line - 1] + col

        def handle_starttag(self, tag, attrs):
            self.script = tag == "script"
            raw = self.get_starttag_text()
            for match in re.finditer(r'''\b(?:src|href)=(['"])(.*?)\1''', raw):
                value = match.group(2)
                key = re.sub(r"^(?:\./|\.\./)*", "", value)
                if key in replacements:
                    self.edits.append((self.absolute_offset() + match.start(2), self.absolute_offset() + match.end(2), replacements[key]))

        def handle_endtag(self, tag):
            if tag == "script":
                self.script = False

        def handle_data(self, data):
            if self.script:
                for match in re.finditer(r'''fetch\("((?:\./|\.\./)*static/contentIndex\.json)"\)''', data):
                    self.edits.append((self.absolute_offset() + match.start(1), self.absolute_offset() + match.end(1), replacements["static/contentIndex.json"]))

        def result(self):
            text = self.text
            for start, end, value in sorted(self.edits, reverse=True):
                text = text[:start] + value + text[end:]
            return text

    for page in site.rglob("*.html"):
        page.write_text(Rewrite(page.read_text()).result())
    for relative in resources:
        safe_path(site, relative).unlink()
    return replacements


def verify_site(site, record):
    mount = record["mount"]
    pages = {}
    for p in record["pages"]:
        output = safe_path(site, p["slug"] + ".html")
        if not output.is_file():
            raise ValueError(f"Omitted page: {p['slug']}")
        page = Page(output.read_text())
        canonical_url = record["canonical_base"] + p["route"][len(mount):]
        if not page.has_article or page.canonical != [canonical_url]:
            raise ValueError(f"Invalid document/canonical: {p['slug']}")
        if page.robots != ["noindex, nofollow" if record["mode"] == "preview" else "index, follow"]:
            raise ValueError(f"Wrong indexing mode: {p['slug']}")
        pages[p["route"]] = page
    found = {p.relative_to(site).as_posix() for p in site.rglob("*.html")}
    expected = {p["slug"] + ".html" for p in record["pages"]}
    if found != expected:
        raise ValueError("Unexpected/excluded HTML in package")
    for route, page in pages.items():
        for url in page.links + page.assets:
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue
            parsed = urlsplit(urljoin("https://report.invalid" + route, url))
            target = unquote(parsed.path)
            if not target.startswith(mount):
                raise ValueError(f"Link/resource escapes mount: {route} -> {url}")
            fragment = unquote(parsed.fragment)
            if target in pages:
                if fragment and fragment not in pages[target].ids:
                    raise ValueError(f"Missing rendered fragment: {route} -> {url}")
            else:
                relative = target[len(mount):]
                if not relative or not safe_path(site, relative).is_file():
                    raise ValueError(f"Missing rendered target: {route} -> {url}")
    index_path = site / record["resources"]["static/contentIndex.json"][len(mount):]
    indexed = set(json.loads(index_path.read_text()))
    if indexed != {p["slug"] for p in record["pages"]}:
        raise ValueError("Search corpus does not match the publication allowlist")
    for file in site.rglob("*"):
        safe_path(site, file.relative_to(site).as_posix())
    return {"pages": len(pages), "local_links": sum(len(p.links) for p in pages.values()), "search_pages": len(indexed)}


def inventory(site):
    result = []
    for file in sorted(site.rglob("*")):
        relative = file.relative_to(site).as_posix()
        safe_path(site, relative)
        if file.is_file():
            result.append({"path": relative, "sha256": digest(file.read_bytes()), "bytes": file.stat().st_size,
                           "mime": mimetypes.guess_type(relative)[0] or "application/octet-stream"})
    return result


def build(root, engine, mode):
    started = time.monotonic()
    manifest = load_manifest(root)
    verify_engine(engine)
    for source, target in OVERLAYS.items():
        shutil.copyfile(safe_path(root, str(OWNER / source)), safe_path(engine, target))
    shallow = git(root, "rev-parse", "--is-shallow-repository") == "true"
    record = {**manifest, "mode": mode, "root": str(root), "source_commit": git(root, "rev-parse", "HEAD"),
              "source_tree": git(root, "rev-parse", "HEAD^{tree}"),
              "working_tree_dirty": bool(git(root, "status", "--porcelain", "--untracked-files=all")),
              "producer": {"run_id": os.environ.get("GITHUB_RUN_ID"), "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT")},
              "adapter": {p: digest((root / OWNER / p).read_bytes()) for p in [*OVERLAYS, "report_web.py", "publication.json", "Quartz-MIT.txt"]}}
    if mode == "public" and record["working_tree_dirty"]:
        raise ValueError("Public candidate requires a clean source checkout")
    pages, before = [], {}
    for p in manifest["pages"]:
        raw = safe_path(root, p["source"]).read_bytes()
        before[p["source"]] = digest(raw)
        metadata, body = split_frontmatter(raw.decode("utf-8"))
        if metadata.get("draft") or metadata.get("publication_status") == "draft":
            raise ValueError(f"Publication draft requires a separate explicit preview contract: {p['source']}")
        modified = None if shallow else git(root, "log", "-1", "--format=%cI", "--", p["source"])
        pages.append({**p, "source_sha256": before[p["source"]], "metadata": metadata, "body": body, "modified": modified})
    record["pages"] = pages
    asset_hashes = {p: digest(safe_path(root, p).read_bytes()) for p in manifest["assets"]}
    immutable_inputs = {**before, **asset_hashes, **{str(OWNER / p): h for p, h in record["adapter"].items()}}
    parent = root / OWNER / "public" / mode
    parent.mkdir(parents=True, exist_ok=True)
    # Work is transactional: no valid previous local package is destroyed by a
    # failing render. Only the dedicated ignored output is replaced on success.
    with tempfile.TemporaryDirectory(prefix="subprime-report-") as tmp:
        workspace = Path(tmp)
        content, site = workspace / "content", workspace / "package/subprime"
        content.mkdir()
        site.parent.mkdir()
        request = workspace / "projection.json"
        request.write_text(json.dumps(record))
        run(["node", "prepare.mjs", request, content], engine)
        record = json.loads(request.read_text())
        run(["node", "quartz/bootstrap-cli.mjs", "build", "-d", content, "-o", site], engine)
        notices = site / "notices"
        notices.mkdir()
        shutil.copyfile(root / OWNER / "Quartz-MIT.txt", notices / "Quartz-MIT.txt")
        shutil.copyfile(engine / "LICENSE-CODE.md", notices / "UA-Apache-2.0.txt")
        (notices / "README.txt").write_text(
            "Subprime report text: CC BY-SA 4.0; attributed third-party material retains its own rights.\n"
            "Original Quartz: jackyzha0/quartz 4923affa7722dfc751f1074348e6dad214fe0c08 (v4.5.2), MIT; see Quartz-MIT.txt.\n"
            f"Maintained renderer: {ENGINE_REPO} at {ENGINE_PIN}; UA code licensing: see UA-Apache-2.0.txt.\n"
            "Local adaptations: selected report config/layout/style/components, explicit indexes, link/metadata projection and resource versioning.\n"
            "Mermaid 11.4.0 is an external browser enhancement loaded from the declared CDN URL, not redistributed in this package.\n"
            "Producer installation dependencies are in the pinned upstream lockfile; the node_modules tree is not distributed.\n"
            "This notice inventory does not replace the required final rights/editorial acceptance.\n")
        record["resources"] = fingerprint(site, manifest["mount"])
        record["checks"] = verify_site(site, record)
        sitemap = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
        for p in record["pages"]:
            item = ET.SubElement(sitemap, "url")
            ET.SubElement(item, "loc").text = manifest["canonical_base"] + p["route"][len(manifest["mount"]):]
            if p["modified"]:
                ET.SubElement(item, "lastmod").text = p["modified"]
        (site / "sitemap.xml").write_bytes(ET.tostring(sitemap, encoding="utf-8", xml_declaration=True))
        record.pop("root")
        record["inputs_sha256"] = digest(canonical({"pages": before, "assets": asset_hashes, "adapter": record["adapter"], "engine": record["engine"]}).encode())
        record["files"] = inventory(site)
        record["payload_sha256"] = digest(canonical(record["files"]).encode())
        record["timing_seconds"] = {"html_producer": round(time.monotonic() - started, 3)}
        record["cache_policy"] = {"assets": "content-addressed immutable dependencies", "consumer_retains": "previous accepted resources for its declared recovery/compatibility window", "headers": "not assumed; measure the actual host"}
        record["rights_review"] = "pending final independent/human inventory acceptance"
        for source, expected in immutable_inputs.items():
            if digest(safe_path(root, source).read_bytes()) != expected:
                raise ValueError(f"Canonical source changed during build: {source}")
        (site.parent / "manifest.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
        destination = parent / "package"
        if destination.exists():
            for p in destination.rglob("*"):
                safe_path(destination, p.relative_to(destination).as_posix())
            shutil.rmtree(destination)
        shutil.copytree(site.parent, destination)
    print(json.dumps({"package": str(destination), "source_commit": record["source_commit"], "dirty": record["working_tree_dirty"], "payload_sha256": record["payload_sha256"], "checks": record["checks"], "timing_seconds": record["timing_seconds"]}, indent=2))
    return destination


def verify_package(package):
    if package.is_symlink() or not package.is_dir() or {p.name for p in package.iterdir()} != {"manifest.json", "subprime"}:
        raise ValueError("Unexpected package-root entries")
    manifest = safe_path(package, "manifest.json")
    site = safe_path(package, "subprime")
    if not manifest.is_file() or not site.is_dir():
        raise ValueError("Invalid package-root file types")
    record = json.loads(manifest.read_text())
    if record.get("schema_version") != 1 or record.get("mount") != "/subprime/":
        raise ValueError("Invalid package contract")
    current = inventory(package / "subprime")
    if current != record["files"] or digest(canonical(current).encode()) != record["payload_sha256"]:
        raise ValueError("Package inventory/digest mismatch")
    return verify_site(package / "subprime", record)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "setup", "build", "verify"])
    parser.add_argument("--mode", choices=["preview", "public"], default="preview")
    parser.add_argument("--package", type=Path)
    args = parser.parse_args()
    if args.command == "check":
        data = load_manifest(ROOT)
        print(f"source-contract: {len(data['pages'])} explicit pages; engine {ENGINE_PIN}")
    elif args.command == "setup":
        setup(engine_path())
    elif args.command == "build":
        build(ROOT, engine_path(), args.mode)
    else:
        if args.package is None:
            parser.error("verify requires --package")
        print(json.dumps(verify_package(args.package)))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"Report build failed: {error}")
