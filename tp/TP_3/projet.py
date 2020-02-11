import nltk

nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "It's works !"

print(word_tokenize(text))