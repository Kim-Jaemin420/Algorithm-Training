import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemonBooks = {}
pokemonList = []

for i in range(1, N + 1):
  pokemonName = input().rstrip()
  pokemonList.append(pokemonName)
  pokemonBooks[pokemonName] = i

for _ in range(M):
  test = input().rstrip()
  
  if test.isdigit():
    print(pokemonList[int(test) - 1])
  else:
    print(pokemonBooks[test])