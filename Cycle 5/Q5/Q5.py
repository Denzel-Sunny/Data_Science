import nltk
from nltk import ngrams
from nltk.corpus import stopwords
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize


text1 = "the data set given satisfies the requirement for model generation."
print("sentence tokenization")
print(sent_tokenize(text1))
print("")
print("word tokenization")
print(word_tokenize(text1))
text = word_tokenize(text1)
text2 = [word for word in text if word not in stopwords.words('english') ]
print("")
print("removing stop words")
print(text2)
print("")
print("n grams")
unigrams = ngrams(text2,3)
for grams in unigrams:
    print(grams)