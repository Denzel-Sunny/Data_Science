from nltk import ngrams

sentence='I reside in Bengaluru'
n=3
unigrams=ngrams(sentence.split(),n)
for grams in unigrams:
    print(grams)