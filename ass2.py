import nltk
import csv


def generate_tokens_freq(tokens):
    dct = {}
    for i in tokens:
        dct[i] = 0
    for i in tokens:
        dct[i] += 1
    return dct


def generate_ngrams(tokens, k):
    l = []
    i = 0
    while i < len(tokens):
        l.append(tokens[i:i + k])
        i = i + 1
    l = l[:-1]
    return l


def generate_ngram_freq(bigram):
    ngramsFreq = {}
    for bi in bigram:
        words = " ".join(bi)
        ngramsFreq[words] = 0
    for bi in bigram:
        # print(i)
        words = " ".join(bi)
        ngramsFreq[words] += 1
    return ngramsFreq


def findWords(words, dct1):
    try:
        return dct1[words]
    except:
        return 0


def print_probability_table(uniqueWords, wordFreq, togetherFreq):
    sizeOfWords = len(uniqueWords)
    table = [[] * sizeOfWords for _ in range(sizeOfWords)]
    for word in range(sizeOfWords):
        probFirst = wordFreq[uniqueWords[word]]
        # print(probFirst)
        for j in range(sizeOfWords):
            probAll = findWords(uniqueWords[word] + " " + uniqueWords[j], togetherFreq)
            # print(distinct_tokens[i] + " " + distinct_tokens[j])
            # print(probAll)
            table[word].append(float("{:.3f}".format(probAll / probFirst)))
    return table


def sortDic(dic1, ref):
    dic = {}
    for i in range(len(ref)):
        if dic1[i] != 0.0:
            dic[ref[i]] = dic1[i]

    res = {key: val for key, val in sorted(dic.items(), key=lambda ele: ele[1], reverse=True)}
    return list(res.keys())[:8]


def finList(word, finalSen):
    for i in range(len(finalSen)):
        if finalSen[i] != word:
            finalSen[i] = word + " " + finalSen[i]
    return finalSen


file = open("new.txt", "r")
file = file.read()
lower = file.lower()
removee = lower.replace(".", '')
removee = removee.replace(",", '')
removee = removee.replace(";", '')
removee = removee.replace("(", '')
removee = removee.replace(")", '')
removee = removee.replace("``", '')
removee = removee.replace("''", '')
removee = removee.replace(":", '')
removee = removee.replace('"', '')
removee = removee.replace('”', '')
removee = removee.replace('“', '')
removee = removee.replace('¬', '')
removee = removee.replace('•', '')
# removee = removee.replace('–', ' ')

tokens = nltk.word_tokenize(removee)
print(len(tokens))
distinct_tokens = list(set(sorted(tokens)))
print("Tokens in the corpus = \n", distinct_tokens)

singleWordFreq = nltk.FreqDist(tokens)  # generate_tokens_freq(tokens)
print("Frequency of each tokens = ")
for i in singleWordFreq.items():
    print(i[0], "\t:", i[1])

bigram = nltk.bigrams(tokens)  # generate_ngrams(tokens, 2)
bi = list(bigram)

twoWordsFreq = generate_ngram_freq(bi)
print("Frequency of n-grams = ")
for i in twoWordsFreq.items():
    print(i[0], ":", i[1])

###############################
# write to file
writeFile = open("output.csv", "w")

print("Probability table = \n")
probability_table = print_probability_table(distinct_tokens, singleWordFreq, twoWordsFreq)
print(probability_table)

finDicFreqRef = {}
ref = []
n = len(distinct_tokens)
print(n)
print("\t", end="")
for i in range(n):
    ref.append(distinct_tokens[i])
    print(distinct_tokens[i], end="\t")
print("\n")

for i in range(n):
    finDicFreqRef[distinct_tokens[i]] = []
    print(distinct_tokens[i], end="\t")
    for j in range(n):
        finDicFreqRef[distinct_tokens[i]].append(probability_table[i][j])
        print(probability_table[i][j], end="\t")
    print("\n")

print(finDicFreqRef)
print(ref)
print(len(ref))
refFin = list(set(ref))
print(refFin)
print(len(refFin))

finSug = sortDic(finDicFreqRef["development"], refFin)
print(finSug)

s = finList("development", finSug)
print(s)

writer = csv.writer(writeFile)
row = refFin
writer.writerow(row)

for i in finDicFreqRef:
    li = []
    li.append(i)
    for j in finDicFreqRef[i]:
        li.append(j)
    writer.writerow(li)

writeFile.close()
