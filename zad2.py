import time

#for a large amount of data we can use a set
#it has a search time of O(1), as it uses a hash table

def word_in_set(word_set,user_input):
    start=time.time()
    if user_input in word_set:
        result="the word is in the set"
    else:
        result="the word is not in the set"
    end=time.time()
    elapsed=end-start
    print(result+" in "+str(elapsed))

words_list=["tablet","phone","clock"]
word_set=set(words_list)
user_input=str(input())
word_in_set(word_set,user_input)
