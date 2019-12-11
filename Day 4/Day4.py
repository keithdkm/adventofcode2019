'''
accepts range of posssible values and returns the number a values in the range that
meet the criteria for a password
'''

    # PART 1
    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    # PART 2
    # Two adjacent digits can't part of a larger group

class passwordCounter():

    def __init__(self,range_):
        start,finish = range_.split('-')
        self.start = int(start)
        self.finish = int(finish)
    

    def run_lengths(s):
        
        res = []
        count = 1
        for i in range(len(s)-1):
 
            if s[i]==s[i+1]:
                count += 1 
            else:
                res.append(count)
                count = 1
        res.append(count)
            
        return res    

    def count(self):
        cnt = 0

        for n in range(self.start,self.finish+1):
            s = str(n)
            a,b,c,d,e,f = s
            rle = passwordCounter.run_lengths(s)
            if a<=b<=c<=d<=e<=f and\
               (2 in rle):
               cnt+=1
               print(n)
        
        return cnt



a = passwordCounter('347312-805915')

print(a.count())
# print(a.RLE('123456'))