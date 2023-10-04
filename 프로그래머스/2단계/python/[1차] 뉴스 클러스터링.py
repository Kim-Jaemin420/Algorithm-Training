def solution(str1, str2):
    arr1 = []
    arr2 = []
    str1 = str1.upper()
    str2 = str2.upper()
    
    for i in range(len(str1) - 1):
      tmp = str1[i] + str1[i + 1]
      if tmp.isalpha():
        arr1.append(tmp)

    for i in range(len(str2) - 1):
      tmp = str2[i] + str2[i + 1]
      if tmp.isalpha():
        arr2.append(tmp)

    if arr1 == [] and arr2 == []:
        return 65536

    union = 0

    combination = 0
    tmp_c = arr2[:]

    for s in arr1:
      if s in tmp_c:
        union += 1
        tmp_c.remove(s)
      combination += 1
    
    combination += len(tmp_c)

    return int(65536 * (union / combination))

print(solution('E=M*C^2', 'e=m*c^2'))
print(solution('FRANCE', 'french'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('handshake', 'shake hands'))
print(solution('aabbb', 'aaabb'))

nums1 = [1,2,3]
def s(nums):
  nums = nums[1:]

s(nums1)
print(nums1)