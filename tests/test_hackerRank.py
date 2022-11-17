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
            
        def test_permutation_equation(self):
            pe = hackerRank.PermutationEquation()
            self.assertEqual(pe.permutationEquation([2,3,1]),[2,3,1])
            self.assertEqual(pe.permutationEquation([4,3,5,1,2]),[1,3,5,4,2])


        def test_jumping_on_the_clouds(self):
            jc = hackerRank.JumpingOnTheClouds()
            self.assertEqual(jc.jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0],2),92)
            self.assertEqual(jc.jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0],3),80)
            self.assertEqual(jc.jumpingOnClouds([1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],19),97)

        def test_finding_digits(self):
            fd = hackerRank.FindDigits()
            self.assertEqual(fd.findDigits(123),2)
            self.assertEqual(fd.findDigits(12),2)
            self.assertEqual(fd.findDigits(1012),3)

        def test_extra_long_factorials(self):
            ef = hackerRank.ExtralongFactorials()
            self.assertEqual(ef.extraLongFactorials(25),15511210043330985984000000)
            self.assertEqual(ef.extraLongFactorials(45),119622220865480194561963161495657715064383733760000000000)

        def test_append_and_delete(self):
            ad = hackerRank.AppendAndDelete()
            self.assertEqual(ad.appendAndDelete('hackerhappy','hackerrank',9),'Yes')
            self.assertEqual(ad.appendAndDelete('aba','aba',7),'Yes')
            self.assertEqual(ad.appendAndDelete('ashley','ash',2),'No')
            self.assertEqual(ad.appendAndDelete('','',2),'Yes')
            self.assertEqual(ad.appendAndDelete('y','yu',2),'No')


if __name__ == '__main__':

    unittest.main()
