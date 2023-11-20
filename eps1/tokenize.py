from nltk.tokenize import sent_tokenize, word_tokenize 

example_text = "Hello Mr. Smith, how are you? The weather is great and Python is awasome. The sky is blue and python is awesome."

print(sent_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)