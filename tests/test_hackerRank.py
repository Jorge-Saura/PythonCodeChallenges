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

        def test_circular_array_rotation(self):
            car = hackerRank.CircularArrayRotation()
            self.assertEqual(car.circularArrayRotation([1,2,3],2,[0,1,2]),[2,3,1])

            self.assertEqual(car.circularArrayRotation([3,2,4],1,[0,2]),[4,2])
            


if __name__ == '__main__':

    unittest.main()
