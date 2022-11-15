

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
    
        # for _ in range(k % length):
        #     temp = [a[-1]]
        #     temp.extend(a[:-1])
        #     a = temp

        for i, ele in enumerate(a):
            temp[(i+k)%length]= ele

        return [temp[i] for i in queries]
