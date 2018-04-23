# -*- coding: utf-8 -*-
import sys


def main(filename):
    # read file into lines
    txtfile = open(filename,"r")
    lines = txtfile.readlines()

    


    # declare a word list
    all_words = []
    words=[]
    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        words.append(line.split())

        
        # check the format of words and append it to "all_words" list
    for word in words:
        # then, remove (strip) unwanted punctuations from every word
        # "dream." => "dream"
        for a in word:
        # check if word is not empty
            if len(a)==0:
                continue
            else:
                a=a.strip(',.!-:"?')
                if len(a)!=0:
                    all_words.append(a)
                # append the word to "all_words" list

    # compute word count from all_words
    print(len(all_words))
    count={}
    for data in all_words:
        if data not in count:
            count[data]=1
        else:
            count[data]=count[data]+1

    


    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    import csv
    with open('wordcount.csv','w',newline='') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file, dialect='excel')
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        for a in count:
            writer.writerow([a,count[a]])


    list1=[]

    for a in count:
        temp=[]
        temp=[a,count[a]]
        list1.append(temp)

    print(list1)

    # dump to a json file named "wordcount.json"
    import json
    f=open('wordcount.json','w')
    json.dump(list1,f)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly


if __name__ == '__main__':
    main("i_have_a_dream.txt")