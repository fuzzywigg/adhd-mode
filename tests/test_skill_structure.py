"""Offline structure locks for the adhd-mode skill package.

Reads skills/adhd-mode/SKILL.md and agents/openai.yaml as data.
Does not execute skill content or invent product behavior.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = REPO_ROOT / "skills" / "adhd-mode" / "SKILL.md"
OPENAI_YAML = REPO_ROOT / "skills" / "adhd-mode" / "agents" / "openai.yaml"

FRONTMATTER_RE = re.compile(
    r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z",
    re.DOTALL,
)

REQUIRED_BODY_HEADINGS = (
    "Priority order",
    "Explicit ND directives",
    "Answer",
    "Action",
    "Artifact",
    "Project update",
)


def parse_skill_md(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise AssertionError("SKILL.md must start with YAML frontmatter delimited by ---")
    frontmatter = yaml.safe_load(match.group(1))
    if not isinstance(frontmatter, dict):
        raise AssertionError("SKILL.md frontmatter must parse to a mapping")
    return frontmatter, match.group(2)


class SkillStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill_text = SKILL_MD.read_text(encoding="utf-8")
        cls.frontmatter, cls.body = parse_skill_md(cls.skill_text)
        cls.openai = yaml.safe_load(OPENAI_YAML.read_text(encoding="utf-8"))

    def test_skill_md_exists(self) -> None:
        self.assertTrue(SKILL_MD.is_file(), f"missing {SKILL_MD}")

    def test_openai_yaml_exists(self) -> None:
        self.assertTrue(OPENAI_YAML.is_file(), f"missing {OPENAI_YAML}")

    def test_frontmatter_name(self) -> None:
        self.assertEqual(self.frontmatter.get("name"), "adhd-mode")

    def test_frontmatter_required_top_level_keys(self) -> None:
        for key in ("name", "description", "license", "compatibility", "metadata"):
            with self.subTest(key=key):
                self.assertIn(key, self.frontmatter)
                value = self.frontmatter[key]
                if isinstance(value, str):
                    self.assertTrue(value.strip(), f"{key} must be non-empty")

    def test_frontmatter_license_and_compatibility(self) -> None:
        self.assertEqual(self.frontmatter.get("license"), "MIT")
        compatibility = self.frontmatter.get("compatibility")
        self.assertIsInstance(compatibility, str)
        self.assertIn("Instruction-only", compatibility)

    def test_frontmatter_metadata_keys(self) -> None:
        metadata = self.frontmatter.get("metadata")
        self.assertIsInstance(metadata, dict)
        for key in ("version", "author", "keywords"):
            with self.subTest(key=key):
                self.assertIn(key, metadata)
                self.assertTrue(str(metadata[key]).strip(), f"metadata.{key} must be non-empty")
        self.assertEqual(metadata.get("author"), "fuzzywigg")

    def test_body_required_sections(self) -> None:
        for heading in REQUIRED_BODY_HEADINGS:
            with self.subTest(heading=heading):
                pattern = re.compile(
                    rf"^#{{2,3}}\s+.*{re.escape(heading)}",
                    re.MULTILINE | re.IGNORECASE,
                )
                self.assertRegex(
                    self.body,
                    pattern,
                    f"SKILL.md body missing heading containing {heading!r}",
                )

    def test_openai_yaml_interface_keys(self) -> None:
        self.assertIsInstance(self.openai, dict)
        self.assertIn("interface", self.openai)
        interface = self.openai["interface"]
        self.assertIsInstance(interface, dict)
        for key in ("display_name", "short_description", "default_prompt"):
            with self.subTest(key=key):
                self.assertIn(key, interface)
                self.assertIsInstance(interface[key], str)
                self.assertTrue(interface[key].strip(), f"interface.{key} must be non-empty")

    def test_openai_yaml_policy_key(self) -> None:
        self.assertIn("policy", self.openai)
        policy = self.openai["policy"]
        self.assertIsInstance(policy, dict)
        self.assertIn("allow_implicit_invocation", policy)
        self.assertIs(policy["allow_implicit_invocation"], True)


if __name__ == "__main__":
    unittest.main()
