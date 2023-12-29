from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

""" for w in example_words:
    print(ps.stem(w)) """

new_text = "It is very imortant to be pythonly while you are pythoning wiht python. All pythoners have pythoned at least once."


words = word_tokenize(new_text)
for w in word_tokenize(new_text):
    print(ps.stem(w))


