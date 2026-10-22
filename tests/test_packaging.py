"""Local smoke tests. Run with python3 -m unittest discover -s tests -v."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackagingTests(unittest.TestCase):
    def run_script(self, filename, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / filename), *map(str, args)],
            text=True, capture_output=True, check=False,
        )

    def test_pack_validator(self):
        p = self.run_script("check_pack.py")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("skills", p.stdout)

    def test_preview_has_no_side_effects(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            p = self.run_script("install.py", "--target", target, "--skills", "all")
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertFalse((target / "AGENTS.md").exists())
            self.assertFalse((target / ".agents").exists())

    def test_selective_apply_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            args = ("--target", target, "--skills", "surgical-change", "--apply")
            first = self.run_script("install.py", *args)
            self.assertEqual(first.returncode, 0, first.stderr)
            policy = target / "AGENTS.md"
            self.assertTrue(policy.exists())
            self.assertTrue((target / ".agents/skills/surgical-change/SKILL.md").exists())
            original = policy.read_bytes()
            second = self.run_script("install.py", *args)
            self.assertEqual(second.returncode, 2)
            self.assertEqual(policy.read_bytes(), original)

    def test_conflict_blocks_all_selected_files(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "AGENTS.md").write_text("user policy\n")
            p = self.run_script("install.py", "--target", target, "--skills", "all", "--apply")
            self.assertEqual(p.returncode, 2)
            self.assertFalse((target / ".agents").exists())
            self.assertEqual((target / "AGENTS.md").read_text(), "user policy\n")

    def test_no_policy_mode(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "AGENTS.md").write_text("existing\n")
            p = self.run_script("install.py", "--target", target, "--policy", "none",
                                "--skills", "independent-review", "--apply")
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertEqual((target / "AGENTS.md").read_text(), "existing\n")
            self.assertTrue((target / ".agents/skills/independent-review/SKILL.md").exists())

    def test_unknown_skill_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            p = self.run_script("install.py", "--target", temp, "--skills", "nonexistent", "--apply")
            self.assertEqual(p.returncode, 2)
            self.assertFalse((Path(temp) / "AGENTS.md").exists())

    def test_all_skills_apply_to_clean_target(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            p = self.run_script("install.py", "--target", target, "--skills", "all", "--apply")
            self.assertEqual(p.returncode, 0, p.stderr)
            source_names = {x.name for x in (ROOT / ".agents/skills").iterdir() if x.is_dir()}
            installed_names = {x.name for x in (target / ".agents/skills").iterdir() if x.is_dir()}
            self.assertEqual(installed_names, source_names)
            for name in source_names:
                self.assertEqual((target / f".agents/skills/{name}/SKILL.md").read_bytes(),
                                 (ROOT / f".agents/skills/{name}/SKILL.md").read_bytes())

    def test_refuses_symlink_in_skill_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            target.mkdir()
            external = Path(temp) / "external"
            external.mkdir()
            agents = target / ".agents"
            agents.mkdir()
            link = agents / "skills"
            try:
                link.symlink_to(external, target_is_directory=True)
            except OSError:
                self.skipTest("Symlink not supported on this filesystem")
            p = self.run_script("install.py", "--target", target, "--policy", "none",
                                "--skills", "surgical-change", "--apply")
            self.assertEqual(p.returncode, 2)
            self.assertFalse((external / "surgical-change").exists())

    def test_refuses_symlink_target(self):
        with tempfile.TemporaryDirectory() as temp:
            real = Path(temp) / "real"
            real.mkdir()
            link = Path(temp) / "link"
            try:
                link.symlink_to(real, target_is_directory=True)
            except OSError:
                self.skipTest("Symlink not supported on this filesystem")
            p = self.run_script("install.py", "--target", link, "--skills", "surgical-change", "--apply")
            self.assertEqual(p.returncode, 2)
            self.assertFalse((real / "AGENTS.md").exists())


if __name__ == "__main__":
    unittest.main()
