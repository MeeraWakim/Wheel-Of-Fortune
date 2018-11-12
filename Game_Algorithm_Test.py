import unittest
import Game_Algorithm

class TestGameAlgorithm(unittest.TestCase):
	def test_showWord(self):
		self.assertEqual(Game_Algorithm.showWord("Testing phrase",["g", "t", "i", "p", "n", "e"]), "Te __ ting p __  __  __  __ e")
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestGameAlgorithm)
	unittest.TextTestRunner(verbosity=2).run(suite)
	unittest.main()