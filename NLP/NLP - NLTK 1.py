from nltk.book import *

print('name of the book = ', text1.name)
print ('length of book =', len(text1))


#to know what is UTF-8 look at lecture slides
my_file = open("Moby Dick by Herman Melville 1851.txt", "r", encoding="utf-8")
raw = my_file.read()
print (raw)