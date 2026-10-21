import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import main

class TestFluttershyRice(unittest.TestCase):
    def test_version(self):
        self.assertEqual(main.VERSION, "1.0.0")

    def test_banner_content(self):
        self.assertIn("Fluttershy", main.ASCII_BANNER)
        self.assertIn("Arch Linux", main.ASCII_BANNER)

    def test_configs_exist(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        kitty_cfg = os.path.join(base_dir, "configs", "kitty", "kitty.conf")
        alacritty_cfg = os.path.join(base_dir, "configs", "alacritty", "alacritty.toml")
        archiso_profile = os.path.join(base_dir, "archiso", "profiledef.sh")
        self.assertTrue(os.path.exists(kitty_cfg), "kitty.conf should exist")
        self.assertTrue(os.path.exists(alacritty_cfg), "alacritty.toml should exist")
        self.assertTrue(os.path.exists(archiso_profile), "profiledef.sh should exist")

if __name__ == "__main__":
    unittest.main()
