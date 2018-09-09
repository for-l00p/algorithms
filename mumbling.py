# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd");    // "A-Bb-Ccc-Dddd"
# accum("RqaEzty"); // "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt");    // "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
  power = 1
  answer = ""
  for x in s[:-1]:
    answer += str(x*power) + '-'
    power += 1
  answer += str((s[-1])*power)
  return answer.title()