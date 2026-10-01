# SPDX-License-Identifier: Apache-2.0
"""Behavioral and adversarial checks for the bounded local RI adapter."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("local_ri", REPO / "tools/repository_intelligence.py")
ri = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ri)


class NavigationSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.cfg = "governance/config.json"
        self.config = {
            "schema_version": 1, "repository": "example/research",
            "output": "governance/repository-intelligence/agent-context.json",
            "glossaries": ["GLOSSARY.md"], "registries": ["evidence/SOURCES.md"],
            "owners": [{"concern": "source status", "path": "evidence/SOURCES.md",
                        "queries": ["source registry", "джерела"]}],
            "cross_repository": [],
        }
        self.write("AGENTS.md", "# Root instructions\n")
        self.write("evidence/AGENTS.md", "# Evidence instructions\n")
        self.write("evidence/SOURCES.md",
                   "# Sources\n\n| ID | Source | Evidence review | Integration audit | Last verified | Can support | Current use |\n"
                   "| --- | --- | --- | --- | --- | --- | --- |\n"
                   "| **P-2025-01** | A null finding | Registered | Not started | — | Bounded observation | Report |\n"
                   "| **DS-2026-01** | Dataset | Registered | Not started | — | Dataset | None |\n")
        self.write("GLOSSARY.md", "# Glossary\n\n## Technical Bankruptcy\nDefinition\n")
        self.write(ri.SCRIPT, (REPO / ri.SCRIPT).read_text())
        self.save_config()

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def save_config(self):
        self.write(self.cfg, json.dumps(self.config))

    def materialize(self):
        data = ri.build(self.root, self.cfg)
        self.write(self.config["output"], json.dumps(data))
        return data

    def test_deterministic_complete_inventory_and_scopes(self):
        first = self.materialize()
        self.assertEqual(first, ri.build(self.root, self.cfg))
        paths = {a["path"] for a in first["artifacts"]}
        self.assertEqual(paths, {"AGENTS.md", "GLOSSARY.md", "evidence/AGENTS.md",
                                 "evidence/SOURCES.md", self.cfg, ri.SCRIPT})
        evidence = next(a for a in first["artifacts"] if a["path"] == "evidence/SOURCES.md")
        self.assertEqual(evidence["instructions"], ["AGENTS.md", "evidence/AGENTS.md"])
        glossary = next(a for a in first["artifacts"] if a["path"] == "GLOSSARY.md")
        self.assertEqual(glossary["instructions"], ["AGENTS.md"])
        self.assertEqual(ri.verify(self.root, self.cfg), first)

    def test_add_modify_and_remove_each_invalidate_context(self):
        operations = [
            lambda: self.write("NEW.md", "# New\n"),
            lambda: self.write("GLOSSARY.md", "# Glossary\n## Changed term\n"),
            lambda: (self.root / "GLOSSARY.md").unlink(),
        ]
        for op in operations:
            with self.subTest(op=op):
                self.materialize()
                op()
                with self.assertRaises(ValueError):
                    ri.verify(self.root, self.cfg)
                if not (self.root / "GLOSSARY.md").exists():
                    self.write("GLOSSARY.md", "# Glossary\n")

    def test_context_is_portable_between_checkout_and_worktree(self):
        self.write(".git/config", "[core]\nrepositoryformatversion = 0\n")
        original = self.materialize()
        (self.root / ".git/config").unlink()
        (self.root / ".git").rmdir()
        self.write(".git", "gitdir: /example/repo/.git/worktrees/review\n")
        self.assertEqual(ri.verify(self.root, self.cfg), original)
        self.write(".git", "gitdir: /another/repo/.git/worktrees/review\n")
        self.assertEqual(ri.verify(self.root, self.cfg), original)
        (self.root / ".git").unlink()
        self.write(".git/config", "[core]\nrepositoryformatversion = 0\n")
        self.assertEqual(ri.verify(self.root, self.cfg), original)

    def test_config_and_producer_edits_invalidate(self):
        self.materialize()
        self.config["owners"][0]["queries"].append("new alias")
        self.save_config()
        with self.assertRaises(ValueError):
            ri.verify(self.root, self.cfg)
        self.materialize()
        self.write(ri.SCRIPT, "# Changed interpreter\n")
        with self.assertRaises(ValueError):
            ri.verify(self.root, self.cfg)

    def test_missing_and_tampered_context_fail_visibly(self):
        with self.assertRaisesRegex(ValueError, "Missing RI context"):
            ri.verify(self.root, self.cfg)
        data = self.materialize()
        data["repository"] = "wrong/owner"
        self.write(self.config["output"], json.dumps(data))
        with self.assertRaisesRegex(ValueError, "Stale or altered"):
            ri.verify(self.root, self.cfg)

    def test_source_identity_and_status_are_not_promoted(self):
        data = self.materialize()
        result = ri.lookup(data, "P-2025-01")
        self.assertEqual(result["owner_candidates"][0]["path"], "evidence/SOURCES.md")
        self.assertEqual(result["sources"][0]["integration_audit"], "Not started")
        self.assertEqual(result["sources"][0]["last_verified"], "—")
        self.assertEqual({s["id"] for s in data["sources"]}, {"P-2025-01", "DS-2026-01"})
        self.assertEqual(ri.lookup(data, "джерела")["owner_candidates"][0]["path"], "evidence/SOURCES.md")

    def test_miss_and_generic_matches_do_not_invent_owners(self):
        data = self.materialize()
        self.assertEqual(ri.lookup(data, "completely unrelated")["status"], "unresolved-use-direct-search")
        self.assertEqual(ri.lookup(data, "AGENTS")["owner_candidates"], [])
        self.assertEqual(data["repository"], "example/research")
        self.assertNotIn("00-doctrine/glossary.md", {a["path"] for a in data["artifacts"]})

    def test_symlink_input_and_directory_escape_rejected(self):
        for path, target in [("alias.md", self.root / "GLOSSARY.md"),
                             ("external", self.root.parent)]:
            with self.subTest(path=path):
                (self.root / path).symlink_to(target, target_is_directory=target.is_dir())
                with self.assertRaisesRegex(ValueError, "Symlink"):
                    ri.build(self.root, self.cfg)
                (self.root / path).unlink()

    def test_output_path_cannot_overwrite_owner_or_escape(self):
        for output in ["AGENTS.md", "../repository-intelligence/agent-context.json",
                       "/tmp/repository-intelligence/agent-context.json"]:
            self.config["output"] = output
            self.save_config()
            with self.subTest(output=output), self.assertRaises(ValueError):
                ri.build(self.root, self.cfg)

    def test_unrepresented_owner_and_oversize_text_fail(self):
        self.config["owners"][0]["path"] = "missing.md"
        self.save_config()
        with self.assertRaisesRegex(ValueError, "Missing represented"):
            ri.build(self.root, self.cfg)
        self.config["owners"][0]["path"] = "evidence/SOURCES.md"
        self.save_config()
        self.write("large.md", "x" * (ri.MAX_FILE_BYTES + 1))
        with self.assertRaisesRegex(ValueError, "bound exceeded"):
            ri.build(self.root, self.cfg)

    def test_inactive_terms_and_sources_are_not_indexed(self):
        self.write("GLOSSARY.md", "# Glossary\n~~~md\n## Fake term\n~~~\n<!--\n## Comment term\n-->\n## Real term\n")
        data = self.materialize()
        self.assertEqual([t["term"] for t in data["terms"]], ["Real term"])


    def test_code_comment_markers_cannot_hide_active_terms(self):
        tick = chr(96) * 3
        examples = [
            "# Glossary\n" + tick + "html\n<!--\n" + tick + "\n## Real term\nDefinition",
            "# Glossary\n    <!--\n## Real term\nDefinition",
        ]
        for body in examples:
            self.write("GLOSSARY.md", body)
            with self.subTest(body=body):
                self.assertEqual([x["term"] for x in ri.build(self.root, self.cfg)["terms"]],
                                 ["Real term"])

    def test_invalid_closer_keeps_fenced_heading_inactive(self):
        tick = chr(96) * 3
        body = "# Glossary\n" + tick + "md\n" + tick + "not-a-closing-fence\n## Fake term\n" + tick + "\n## Real term\n"
        self.write("GLOSSARY.md", body)
        self.assertEqual([x["term"] for x in ri.build(self.root, self.cfg)["terms"]], ["Real term"])

    def test_fence_info_and_inline_span_comment_literals_are_inert(self):
        tick = chr(96)
        examples = [
            "# Glossary\n" + tick * 3 + "html <!--\nExample\n" + tick * 3 + "\n## Real term\n",
            "# Glossary\nLiteral " + tick + "<!--" + tick + "\n## Real term\n",
        ]
        for body in examples:
            self.write("GLOSSARY.md", body)
            with self.subTest(body=body):
                self.assertEqual([x["term"] for x in ri.build(self.root, self.cfg)["terms"]],
                                 ["Real term"])

    def test_comment_bearing_multiline_span_is_visibly_unavailable(self):
        tick = chr(96)
        self.write("GLOSSARY.md", "# Glossary\nLiteral " + tick + "<!--\n" + tick + "\n## Real term\n")
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            ri.build(self.root, self.cfg)

    def test_unknown_registry_schema_and_source_identity_fail(self):
        original = (self.root / "evidence/SOURCES.md").read_text()
        for changed in [original.replace("Integration audit", "Audit"),
                        original.replace("P-2025-01", "P-2025-100")]:
            self.write("evidence/SOURCES.md", changed)
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                ri.build(self.root, self.cfg)

    def test_binary_inventory_does_not_claim_content_freshness(self):
        (self.root / "deck.pdf").write_bytes(b"version one")
        first = self.materialize()
        (self.root / "deck.pdf").write_bytes(b"version two")
        self.assertEqual(ri.verify(self.root, self.cfg), first)
        record = next(x for x in first["source_identity"]["inputs"] if x["path"] == "deck.pdf")
        self.assertEqual(record, {"path": "deck.pdf", "identity_mode": "existence"})

    def test_real_adapter_owners_and_cross_repo_isolation(self):
        configs = [REPO / "governance/repository-intelligence-config.json",
                   REPO / ".github/repository-intelligence-config.json"]
        path = next(p for p in configs if p.exists())
        surface = ri.build(REPO, path.relative_to(REPO).as_posix())
        self.assertNotIn(surface["repository"],
                         {x["repository"] for x in surface["cross_repository"]})
        for item in surface["owners"]:
            self.assertTrue((REPO / item["path"]).is_file())
        if surface["repository"].endswith("The-Subprime-Code-Crisis"):
            s = next(s for s in surface["sources"] if s["id"] == "P-2026-01")
            self.assertEqual(s["integration_audit"], "Verified")
            self.assertEqual(ri.lookup(surface, "P-2026-01")["owner_candidates"][0]["path"],
                             "evidence/SOURCES.md")
        else:
            self.assertEqual(surface["sources"], [])
            self.assertEqual(ri.lookup(surface, "pmday")["owner_candidates"][0]["path"], "BACKLOG.md")


if __name__ == "__main__":
    unittest.main()
