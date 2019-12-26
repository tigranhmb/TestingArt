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
    def create_dictionary(word_list):
        word_count = {}
        for word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
                for key, value in sorted(word_count.items())
                    print(key, value)
