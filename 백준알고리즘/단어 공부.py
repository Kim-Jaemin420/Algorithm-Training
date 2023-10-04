import sys
input = sys.stdin.readline

words = input().rstrip().upper()
unique_word = list(set(words))

count_alphabet = []
for word in unique_word:
  count = words.count
  count_alphabet.append(count(word))

if count_alphabet.count(max(count_alphabet)) > 1:
  print("?")

else:
  print(unique_word[(count_alphabet.index(max(count_alphabet)))])
