import unittest
from unittest.mock import patch, MagicMock
from davinci_resolve_studio_mod_suite.resolve_mod import ResolveMod

class TestResolveMod(unittest.TestCase):
    @patch("subprocess.run")
    def test_unlock_studio_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)
        mod = ResolveMod("/fake/path/Resolve.exe")
        self.assertTrue(mod.unlock_studio())

    @patch("subprocess.run")
    def test_unlock_studio_failure(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd")
        mod = ResolveMod("/fake/path/Resolve.exe")
        self.assertFalse(mod.unlock_studio())

if __name__ == "__main__":
    unittest.main()