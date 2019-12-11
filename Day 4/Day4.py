'''
accepts range of posssible values and returns the number a values in the range that
meet the criteria for a password
'''

    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

class passwordCounter():

    def __init__(self,range_):
        start,finish = range_.split('-')
        self.start = int(start)
        self.finish = int(finish)


    def count(self):
        cnt = 0

        for n in range(self.start,self.finish+1):
            a,b,c,d,e,f = str(n)
            if a<=b<=c<=d<=e<=f and\
               (a==b or b==c or c==d or d==e or e==f):
               cnt+=1
        
        return cnt

a = passwordCounter('347312-805915')

print(a.count())