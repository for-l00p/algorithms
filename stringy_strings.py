# https://www.codewars.com/kata/563b74ddd19a3ad462000054

# write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

# the string should start with a 1.

# a string with size 6 should return :'101010'.

# with size 4 should return : '1010'.

# with size 12 should return : '101010101010'.

# The size will always be positive and will only use whole numbers.

def stringy(size):
  if size == 1:
    return '1'
  if size % 2 == 0:
    return size / 2 * '10'
  return '1' + ((size - 1) / 2 * '01')