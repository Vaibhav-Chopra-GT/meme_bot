import unittest
from meme_bot import download_image
import os


class test_download_image(unittest.TestCase):
    def test_downloadmeme(self):
        download_image.downloadmeme()
        self.assertEqual(os.path.exists("meme.jpg"), True)
        os.remove("meme.jpg")


if __name__ == "__main__":
    unittest.main()
