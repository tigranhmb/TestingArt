print('wordcount and frequency')
# with open we are reading text.txt file that in our Homework3 folder 'r' open file for reading.
with open('text.txt', 'r') as f:
    f_cotents = f.read()
    #splitting words
    word_list=(f_cotents.split())
    #checking if this worked
    print(word_list)
    #init dictionary
    ### make empty dictionary
    d = {}
    for word in word_list:
        if word not in d:
            d[word]=1
        else:
            d[word]+=1
        #d[word]=d.get(word, 0) + 1
        #empty wordfreq
        word_freq = []
        for key, value in d.items():
            word_freq.append((value, key))
            #Sorting from high number to the lowest.
            word_freq.sort(reverse=True)
print(word_freq)


