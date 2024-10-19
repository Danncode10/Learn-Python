def splitComma(word):
    wordList = []
    j = 0
    temp = 0
    for i in word:
        if word[i] == ",":
            wordList[j] = word[temp,i]
            j+=1

w = "Dann, Lester, Lopez"
splitComma(w)

