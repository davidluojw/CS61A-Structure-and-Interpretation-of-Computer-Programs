def has_digit(n, k):
     """Returns whether K is a digit in N.
 >>> has_digit(10, 1)
 True
 >>> has_digit(12, 7)
False
 """
 while n >0:
 last_digit = n%10
 n = n//10
if last_digit == k:
 return True
 return False

def has_digit_not_working(n, k):
 """Returns whether K is a digit in N.
 >>> has_digit_not_working(10, 1)
True
 >>> has_digit_not_working(12, 7)
 False
 """
 true_false = False
 while n >0:
last_digit = n%10
n = n//10
 if last_digit == k:
 true_false = True
 return true_false