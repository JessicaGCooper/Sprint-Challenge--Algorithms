'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word = 'thingith'

def count_th(word):
    
    # result = word.find('th')
    # return result
    # TBC
    count = 0
    i = -2
    print(len(word) - 1)
    if i == -1:
        return count
    elif i < len(word):
        i = word.find('th')
        print(i)
        if i >= 0:
            count += 1
            word = word[i+2:]
            print(word)
        
    count_th(word)

print(count_th(word))