

#https://www.hackerrank.com/challenges/strange-advertising/problem
class StrangeAdevertising:
    def viralAdvertising(self, n:int) -> int:
        mails_sent = 5
        likes = 0
        for _ in range(n):
            likes_current_day = mails_sent // 2
            likes += likes_current_day
            mails_sent = likes_current_day * 3


        return likes


#https://www.hackerrank.com/challenges/save-the-prisoner/problem
class SaveThePrisioner:
    def saveThePrisoner(self, num_of_prisioners:int, num_of_sweets:int, chair_to_start_from:int) -> int:
        total_positions_to_move = num_of_sweets + chair_to_start_from - 1
        position_awful_sweet = total_positions_to_move % num_of_prisioners

        return position_awful_sweet if position_awful_sweet != 0 else num_of_prisioners  


#https://www.hackerrank.com/challenges/circular-array-rotation/problem
class CircularArrayRotation:
    def circularArrayRotation(self, a:list, k:int, queries:list)->list:
        length = len(a)
        temp = [0] * length

        for i, ele in enumerate(a):
            temp[(i+k)%length]= ele

        return [temp[i] for i in queries]

#https://www.hackerrank.com/challenges/permutation-equation/problem
class PermutationEquation:
    def permutationEquation(self, p:list) -> list:
        temp = []
        for i in range(len(p)):
            index =  p.index(i+1)+1
            index_of_index = p.index(index)+1
            temp.append(index_of_index)

        return temp

#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
class JumpingOnTheClouds:
    def jumpingOnClouds(self, c:list, k:int) -> int:
        n = len(c)
        total_energy = 100
        current_idx = k % n
        total_energy = total_energy -1 - (2*c[current_idx])

        while current_idx:
            current_idx = (current_idx + k) % n
            total_energy = total_energy -1 - (2*c[current_idx])

        return total_energy


#https://www.hackerrank.com/challenges/find-digits/problem
class FindDigits:
    def findDigits(self, n:int) -> int:
        return sum(1 if int(x) > 0 and n%int(x) == 0 else 0 for x in str(n))

#https://www.hackerrank.com/challenges/extra-long-factorials/problem
class ExtralongFactorials:
    def extraLongFactorials(self, n:int) -> int:
        if n == 1: return 1
        return n * self.extraLongFactorials(n-1)


#https://www.hackerrank.com/challenges/append-and-delete/problem
class AppendAndDelete:
    def appendAndDelete(self, s, t, k):
        coincident_chars = 0
        for ele1, ele2 in zip(s,t):
            if ele1 == ele2:
                coincident_chars += 1
            else:
                break
        
        chars_to_delete = len(s)-coincident_chars
        chars_to_append = len(t)-coincident_chars
        
        if (chars_to_delete + chars_to_append) == k:
            return 'Yes'
        elif len(s)==chars_to_delete and  chars_to_delete + chars_to_append < k:
            return 'Yes'
        elif len(s) > chars_to_delete and  chars_to_delete + chars_to_append < k and chars_to_append % 2 == 0:
            return 'Yes'
        else:
            return 'No'

