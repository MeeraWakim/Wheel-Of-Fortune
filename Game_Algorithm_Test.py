import unittest
import Game_Algorithm

class TestGameAlgorithm():
    def test_showWord(self):
        self.AssertEqual(showWord("Testing phrase",["g", "t", "i", "p", "n", "e"]), "T __  __ ting p __ __ __ __ e")

if __name__ == '__main__':
	unittest.main()