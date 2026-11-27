import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "validate-metadata.py"
)

VALID_METADATA = {
    "name": "Example Skill",
    "category": "software-engineering",
    "version": "1.0.0",
    "author": "Test Author",
    "difficulty": "Beginner",
}


class TestMetadataValidator(unittest.TestCase):

    def run_validator(self, metadata_content):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            metadata_file = root / "skills" / "example" / "metadata.json"
            metadata_file.parent.mkdir(parents=True)

            metadata_file.write_text(
                metadata_content,
                encoding="utf-8",
            )

            return subprocess.run(
                ["python3", str(SCRIPT)],
                cwd=root,
                capture_output=True,
                text=True,
            )

    def test_valid_metadata_passes(self):
        result = self.run_validator(json.dumps(VALID_METADATA))

        self.assertEqual(result.returncode, 0)
        self.assertIn("All module metadata files passed", result.stdout)

    def test_missing_required_field_fails(self):
        metadata = VALID_METADATA.copy()
        del metadata["author"]

        result = self.run_validator(json.dumps(metadata))

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing fields author", result.stdout)

    def test_empty_required_field_fails(self):
        metadata = VALID_METADATA.copy()
        metadata["name"] = "   "

        result = self.run_validator(json.dumps(metadata))

        self.assertEqual(result.returncode, 1)
        self.assertIn("empty fields name", result.stdout)

    def test_invalid_difficulty_fails(self):
        metadata = VALID_METADATA.copy()
        metadata["difficulty"] = "Expert"

        result = self.run_validator(json.dumps(metadata))

        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid difficulty", result.stdout)

    def test_malformed_json_fails(self):
        result = self.run_validator('{"name": "Example"')

        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid JSON", result.stdout)

    def test_non_object_json_fails(self):
        result = self.run_validator(json.dumps(["not", "an", "object"]))

        self.assertEqual(result.returncode, 1)
        self.assertIn("metadata must be a JSON object", result.stdout)


if __name__ == "__main__":
    unittest.main()
