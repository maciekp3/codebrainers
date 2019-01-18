#!/usr/bin/env python

f = open("./proust.txt")
text = f.read()
words = text.split()

#for word in words:
 #   if word == "the":
  #      print(word)

freq = {}

for word in words:
    word = word.lower().strip(".?!,-")
    if not word in freq:
        freq[word] = 1
    else:
        freq[word] += 1

#print(d)

#freq_list = list(freq.items.())
#freg_list.sort(key=itemgetter(1))
#print(freq_list)

results = {}

for kword, val in freq.items():
    #f = freq[kword]
    if val in results:
        results[val].append(kword)
    else:
        results[val] = [kword]

print(len(results))
print(sorted(results.items()))


