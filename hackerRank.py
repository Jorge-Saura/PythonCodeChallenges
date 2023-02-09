

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


#https://www.hackerrank.com/challenges/sherlock-and-squares/problem
class Squares:
    def squares(self,start:int, end:int) -> int:
        start_root = start**.5
        start_root = int(start_root) if start_root.is_integer() else int(start_root) + 1
        end_root = int(end**.5 )
        return end_root-start_root+1


#https://www.hackerrank.com/challenges/magic-square-forming/problem

class MagicSquare:
    ms_h = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    ms_v = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    all_ms = None

    def __init__(self):
        self.all_ms = list()
        self._add_ms(self.ms_h)
        self._add_ms(self.ms_v)

    def _add_ms(self, ms:list):
        self.all_ms.append(ms)
        self.all_ms.append([ms[2], ms[1], ms[0]])
        new_ms = []
        for row in ms:
            new_ms.append([row[2],row[1],row[0]])
        
        self.all_ms.append(new_ms)
        self.all_ms.append([new_ms[2], new_ms[1], new_ms[0]])

    def formingMagicSquare(self, s: list) -> int:
        min_cost = 1000
        for square in self.all_ms:
            current_cost = 0
            for row1, row2 in zip(square,s):
                row_cost = sum([abs(a-b) for a,b in zip(row1,row2)])
                current_cost += row_cost
            
            min_cost = current_cost if current_cost < min_cost else min_cost
        return min_cost


#https://www.hackerrank.com/challenges/picking-numbers/problem
class PickingNumbers:

    def pickingNumbers(self, a:list) -> int:
        a.sort()
        last_digit = 0
        last_digit_count = 0

        count_of_digits = 0
        while a:

            current_digit = a.pop(0)
            current_digit_count = 1
            while a and a[0] == current_digit:
                a.pop(0)
                current_digit_count += 1
                
            if current_digit - last_digit == 1:
                count_of_digits = last_digit_count + current_digit_count if last_digit_count + current_digit_count > count_of_digits else count_of_digits

            if current_digit - last_digit >= 1:
                last_digit = current_digit
                last_digit_count = current_digit_count
                count_of_digits = current_digit_count if current_digit_count > count_of_digits else count_of_digits
                

        return count_of_digits


#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
class ClimbingLeaderboard:

    def climbingLeaderboard(self, ranked:list, player:list) -> list:
        player_scores = len(player)
        ranked_scores = len(ranked)
        player_rankings = [0]*player_scores
        ranked_pointer = 0
        ranked_position = 1

        i = player_scores - 1 

        while i>=0:
            current = player[i]

            if ranked_pointer >= ranked_scores or current >= ranked[ranked_pointer]:
                player_rankings[i] = ranked_position
                
            elif ranked_pointer < ranked_scores:
                #move pointer until next position
                current_ranked = ranked[ranked_pointer]
                while ranked_pointer<ranked_scores and current_ranked == ranked[ranked_pointer]:
                    ranked_pointer += 1
                ranked_position += 1
                i = i + 1 
            i -= 1
        return player_rankings

#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
class DesignerPDFViewer:
    def designerPdfViewer(self, h:list, word:str) -> int:
        #a is 97 in ascii
        numbers = [h[ord(letter)-97] for letter in word]
        return max(numbers)* len(word.strip())


#https://www.hackerrank.com/challenges/utopian-tree/problem
class UtopianTree:
    def utopianTree(self, n: int) -> int:
        init_height = 1
        for i in range(n):
            init_height = init_height + 1 if i% 2 == 1 else init_height*2

        return init_height

#https://www.hackerrank.com/challenges/library-fine/problem
class LibraryFine:
    def libraryFine(self, d1:int, m1:int, y1:int, d2:int, m2:int, y2:int) -> int:
        if y1>y2:
            return 10000
        elif m1>m2 and y1 == y2:
            return (m1-m2)*500
        elif d1>d2 and m1==m2 and y1==y2:
            return (d1-d2)*15
        else:
            return 0

#https://www.hackerrank.com/challenges/cut-the-sticks/problem

class CutTheSticks:
    def cutTheSticks(self, arr:list[int]) -> list[int]:
        #get shortest
        result = list()  
        while arr:
            result.append(len(arr))
            shortest = min(arr)
            arr = [x-shortest for x in arr if x-shortest > 0]

        return result
        

#https://www.hackerrank.com/challenges/non-divisible-subset/problem

class NonDivisibleSubset:

    def _get_all_possible_subsets(self, k:int, s:list[int]) -> dict:
        result = []
        for idx, current in enumerate(s):
            l = [current]
            for ele in s[idx+1:]:
                
                if (current + ele) % k:
                    l.append(ele)
            if l:
                result.append(l)

        return result

    def get_max_subset(self, subset:list, k:int) -> int:
        max_subset = 0
        if len(subset)==1:
            return 1
        else:
            return 1 + self.get_subset(k, subset[1:])

    def get_subset(self, k:int, s:list[int]) -> int:
        possible_subsets = self._get_all_possible_subsets(k,s)

        max_subset = 0
        for subset in possible_subsets:
            current_max = self.get_max_subset(subset, k)
            max_subset = max(max_subset, current_max)

        return max_subset

    def get_subset2(self, k:int, s:list[int]) -> int:
        l = []
        for idx, ele in s:
            l.append(ele)
            

        return 1


# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

class FruitCounter:

    def  countApplesAndOranges(self, s:int, t:int, a:int, b:int, apples:int, oranges:int) -> int:

        total_apples = sum(1 if s <= apple + a <= t else 0 for apple in apples)
        total_oranges = sum(1 if s <= orange + b <= t else 0 for orange in oranges)

        return [total_apples,total_oranges]