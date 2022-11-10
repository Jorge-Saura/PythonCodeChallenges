import unittest

import hackerRank 

class TestBasics(unittest.TestCase):

        def test_strange_advertisign(self):
            ad = hackerRank.StrangeAdevertising()
            self.assertEqual(ad.viralAdvertising(1),2)
            self.assertEqual(ad.viralAdvertising(2),5)
            self.assertEqual(ad.viralAdvertising(3),9)
            self.assertEqual(ad.viralAdvertising(4),15)
            self.assertEqual(ad.viralAdvertising(5),24)

            
        def test_save_the_prisioner(self):
            sp = hackerRank.SaveThePrisioner()
            self.assertEqual(sp.saveThePrisoner(5,2,1),2)
            self.assertEqual(sp.saveThePrisoner(5,2,2),3)


if __name__ == '__main__':

    unittest.main()
