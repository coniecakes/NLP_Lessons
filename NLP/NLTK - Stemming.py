import nltk
import io

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

my_file = io.open("The_Three_Musketeers.txt", "r", encoding="utf-8")
raw = my_file.read()
tokens = nltk.word_tokenize(raw)
my_text_obj = nltk.Text(tokens)

porterlist = [porter.stem(t) for t in tokens]
lancasterlist = [lancaster.stem(t) for t in tokens]
# print (f'This is the Porter List: \n{porterlist[:11]}')
# print (f'This is the Lancaster List: \n{lancasterlist[:11]}')
print('This is the Porter List:\n\t' + '\n\t'.join(porterlist[:11]))
print()
print('This is the Lancaster List:\n\t' + '\n\t'.join(lancasterlist[:11]))