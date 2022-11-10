

#https://www.hackerrank.com/challenges/strange-advertising/problem
class StrangeAdevertising:
    def viralAdvertising(self, n:int) -> int:
        mails_sent = 5
        likes = 0
        for _ in range(n):
            likes_this_days = mails_sent // 2
            likes += likes_this_days
            mails_sent = likes_this_days * 3


        return likes