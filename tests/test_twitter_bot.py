import unittest
from meme_bot import twitter_bot
import os


class test_twitter_bot(unittest.TestCase):
    def test_getlastid(self):
        with open("test.txt", "w") as f:
            f.write("1234")

        self.assertEqual(twitter_bot.getlastid("test.txt"), 1234)
        os.remove("test.txt")

    def test_putid(self):

        twitter_bot.putid(4321, "test2.txt")
        fread = open("test2.txt","r")
        x = int(fread.read().strip())
        self.assertEqual(x, 4321)
        fread.close()
        os.remove("test2.txt")


if __name__ == "__main__":
    unittest.main()
