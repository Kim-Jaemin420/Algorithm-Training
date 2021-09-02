import sys
import re

input = sys.stdin.readline
word = input()
croatia = re.findall('c=|c-|dz=|d-|lj|nj|s=|z=', word)
del_croatia = list(re.sub('c=|c-|dz=|d-|lj|nj|s=|z=', '', word))

print(len(croatia) + len(del_croatia))
# https://bingorithm.tistory.com/9
