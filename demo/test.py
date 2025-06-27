



def demo():
    words = ["apple", "bat", "bar", "atom", "book"]
    dic = {word[0]:[] for word in words}
    for word in words:
        
        dic[word[0]].append(word)

    print(dic)
    return


demo()
