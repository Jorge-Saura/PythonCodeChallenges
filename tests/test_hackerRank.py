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

        def test_squares(self):
            sq = hackerRank.Squares()
            self.assertEqual(sq.squares(3,9),2)
            self.assertEqual(sq.squares(17,24),0)
            self.assertEqual(sq.squares(24,49),3)

        def test_magic_square(self):
            ms = hackerRank.MagicSquare()
            self.assertEqual(len(ms.all_ms), 8)
            s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
            self.assertEqual(ms.formingMagicSquare(s), 7)
            s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
            self.assertEqual(ms.formingMagicSquare(s), 1)
            s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
            self.assertEqual(ms.formingMagicSquare(s), 4)            

        def test_picking_numbers(self):
            pn = hackerRank.PickingNumbers()
            self.assertEqual(pn.pickingNumbers([1,1,2,2,4,4,5,5,5]), 5)
            self.assertEqual(pn.pickingNumbers([4,6,5,3,3,1]), 3)
            self.assertEqual(pn.pickingNumbers([1,2,2,3,1,2]), 5)
            a = [4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5, 97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5, 97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]
            self.assertEqual(pn.pickingNumbers(a), 50)
            a= [66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
            self.assertEqual(pn.pickingNumbers(a), 100)

        def test_climbing_leaderboard(self):
            cl = hackerRank.ClimbingLeaderboard()
            self.assertEqual(cl.climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[5, 25, 50, 120]),[6,4,2,1])
            self.assertEqual(cl.climbingLeaderboard([100, 90, 90, 80, 75, 60],[50, 65, 77, 90, 102]),[6,5,4,2,1])

        def test_designer_PDFViewer(self):
            dp = hackerRank.DesignerPDFViewer()
            h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
            self.assertEqual(dp.designerPdfViewer(h,'abc'), 9)
            h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
            self.assertEqual(dp.designerPdfViewer(h,'zaba'), 28)

        def test_utopian_tree(self):
            ut = hackerRank.UtopianTree()
            self.assertEqual(ut.utopianTree(0),1)
            self.assertEqual(ut.utopianTree(1),2)
            self.assertEqual(ut.utopianTree(4),7)


        def test_library_fine(self):
            lf = hackerRank.LibraryFine()
            self.assertEqual(lf.libraryFine(14,7,2018,5,7,2018),135)
            self.assertEqual(lf.libraryFine(9,6,2015,6,6,2015),45)
            self.assertEqual(lf.libraryFine(9,6,2015,6,6,2014),10000)
            self.assertEqual(lf.libraryFine(9,8,2015,6,6,2015),1000)
            self.assertEqual(lf.libraryFine(9,5,2015,6,6,2015),0)
            self.assertEqual(lf.libraryFine(9,5,2015,9,5,2015),0)
            self.assertEqual(lf.libraryFine(2,7,2014,1,1,2015),0)

        def test_cut_the_sticks(self):
            cs = hackerRank.CutTheSticks()
            self.assertEqual(cs.cutTheSticks([1]),[1])
            self.assertEqual(cs.cutTheSticks([1,2,3]),[3,2,1]) 
            self.assertEqual(cs.cutTheSticks([5, 4, 4, 2, 2, 8]),[6, 4, 2, 1])   
            self.assertEqual(cs.cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]),[8, 6, 4, 1])

        def test_non_divisible_subset(self):
            nds = hackerRank.NonDivisibleSubset()

            self.assertEqual(nds._get_all_possible_subsets(3,[5,3,7]),[[5,3],[3,7],[7]])

            self.assertEqual(nds._get_all_possible_subsets(3,[1, 7, 2, 4]),[[1,7,4],[7,4],[2],[4]])

            self.assertEqual(nds.get_subset(3,[1, 7, 2, 4]),3)

        def test_fruit_counter(self):
            fc = hackerRank.FruitCounter()
            self.assertEqual(fc.countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6]),[1,1])


if __name__ == '__main__':

    unittest.main()
