

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