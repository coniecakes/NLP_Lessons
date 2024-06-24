import nltk
import io
from nltk.corpus import wordnet

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
wnl = nltk.WordNetLemmatizer()

my_file = io.open("The_Three_Musketeers.txt", "r", encoding="utf-8")
raw = my_file.read()
tokens = nltk.word_tokenize(raw)
my_text_obj = nltk.Text(tokens)

porterlist = [porter.stem(t) for t in tokens]
lancasterlist = [lancaster.stem(t) for t in tokens]
wnllist = [wnl.lemmatize(t) for t in tokens]
porter_count = []
lancaster_count = []
wnl_count = []

# print(f'This is the Porter Lemmatization: \n {porterlist[:11]}')
# print(f'This is the Lancaster Lemmatization: \n {lancasterlist[:11]}')
# print(f' This is the wnl Lemmatization: \n {wnllist[:11]}')

print("This is the Porter Lemmatization:")
for i in porterlist:
    porter_count.append(i)
    if len(porter_count) > 10:
        break
    print(i)
print()
print("This is the Lancaster Lemmatization:")
for i in lancasterlist:
    lancaster_count.append(i)
    if len(lancaster_count) > 10:
        break
    print(i)
print()
print("This is the WNL Lemmatization:")
for i in wnllist:
    wnl_count.append(i)
    if len(wnl_count) > 10:
        break
    print(i)