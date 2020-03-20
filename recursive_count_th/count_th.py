'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word = 'thingith'

def count_th(word):
    count = 0
    # result = word.find('th')
    # return result
    # TBC
    
    if len(word) < 2:
        return count
    else:
        if word[0] == 't' and word[1] == 'h':
            count += 1
            word = word[2:]
        else:
            word = word[1:]
        
    count_th(word)

print(count_th(word))

# word = 'thingith'

# def count_th(word, count=0, i=-2):
    
#     # result = word.find('th')
#     # return result
#     # TBC
#     print(len(word) - 1)
#     if len(word) < 2:
#         return count
#     elif i == -1:
#         return count
#     elif i < len(word):
#         i = word.find('th')
#         print(i)
#         if i >= 0:
#             count += 1
#             word = word[i+2:]
#             print(word)
        
#     count_th(word, count, i)

# print(count_th(word))
