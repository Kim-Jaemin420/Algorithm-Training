import itertools


def combination(menus, num, course):
  it = list(itertools.combinations(menus, num))

  for key in it:
    if key in course:
      course[key] += 1
    else:
      course[key] = 1

def solution(orders, course):
    answer = []
    orders = [sorted(order) for order in orders]
    

    while course:
      course_dict = {}
      menu_num = course.pop(0)

      for i in range(len(orders)):
        if len(orders[i]) >= menu_num:
          combination(orders[i], menu_num, course_dict)
      courses = sorted(course_dict.items(), key=(lambda x:x[1]), reverse=True)
      
      if not courses or courses[0][1] < 2:
        continue
      for c in courses:
        if c[1] == courses[0][1]:
          answer.append(''.join(c[0]))


    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], 	[2,3,4]))
print(solution(["XYZ", "XWY", "WXA"], 	[2,3,4]))