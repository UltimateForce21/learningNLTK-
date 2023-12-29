from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("scarves"))


sample_text = "Stupendous scarves absolutely humongous pneumoniaultramicroscopicsilicovolcanioconiosis"

for w in word_tokenize(sample_text):
    print(lemmatizer.lemmatize(w))




