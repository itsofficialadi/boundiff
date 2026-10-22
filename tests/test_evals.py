"""Ensure the evaluation harness creates the expected disposable cases."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("boundiff_evals", ROOT / "evals" / "run.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class EvalFixturesTests(unittest.TestCase):
    def test_paired_fixtures_have_identical_base_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            for case in ("pagination", "review", "release"):
                base = Path(tmp) / (case + "-base")
                candidate = Path(tmp) / (case + "-candidate")
                a = module.prepare(base, case, "baseline")
                b = module.prepare(candidate, case, "boundiff")
                self.assertEqual(a, b)
                self.assertTrue((candidate / "AGENTS.md").exists())
                self.assertTrue(
                    (candidate / ".agents" / "skills" /
                     module.SKILLS[case] / "SKILL.md").is_file()
                )
                self.assertFalse((base / "AGENTS.md").exists())

    def test_pagination_has_real_regression_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "pagination"
            module.prepare(path, "pagination", "baseline")
            result = module.command(
                ["python3", "-m", "unittest", "discover", "-s", "tests"], path
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("FAIL", result.stderr)

    def test_review_has_real_authorization_bypass(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "review"
            module.prepare(path, "review", "baseline")
            result = module.command(
                ["python3", "-c",
                 "from access import fetch_report; "
                 "print(fetch_report({'role':'support','tenant_id':'beta'}, "
                 "{'tenant_id':'alpha','payload':'private'}))"], path
            )
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "private")

    def test_release_has_two_staged_paths_without_remote(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "release"
            module.prepare(path, "release", "baseline")
            self.assertEqual(
                module.state(path)["staged_paths"], ["VERSION", "notes.txt"]
            )
            self.assertEqual(module.git(path, "remote"), "")


if __name__ == "__main__":
    unittest.main()
