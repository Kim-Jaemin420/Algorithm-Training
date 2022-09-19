









def solution(s):
    answer = []
    
    s = s.lower()
    
    sToList = s.split(' ')
    
    for word in sToList:
        if word:
            answer.append(word[0].upper() + word[1:] + ' ')
        if not word:
            answer.append(' ')

        
    return ''.join(answer)[:-1]





# def solution(s):
#     answer = ''
#     words_list = s.lower().split(' ')
    
#     for i in range(len(words_list)):
#         if words_list[i] == '':
#             words_list[i] == ' '
#         else:
#             words_list[i] = words_list[i][0].upper() + words_list[i][1:]

#     return ' '.join(words_list)