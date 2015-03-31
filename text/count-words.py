from collections import Counter

def read(filename):
    txt = open(filename)
    words = []
    for line in txt:
        for word in line.split():
            words.append(word)
    counts = Counter(words)
    for k, v in counts.most_common():
        print k + ": " + str(v)

filename = raw_input("Please enter the .txt filename: ")
read(filename)