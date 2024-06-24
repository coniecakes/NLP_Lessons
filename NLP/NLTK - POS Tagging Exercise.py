import nltk
import io

my_file = io.open("The_Three_Musketeers.txt", "r", encoding="utf-8")
raw = my_file.read()
tokens = nltk.word_tokenize(raw)
my_text_obj = nltk.Text(tokens)

sent_tokens = nltk.sent_tokenize(raw)

tok1 = nltk.word_tokenize(sent_tokens[100])
tagged_tok1 = nltk.pos_tag(tok1)
print (tagged_tok1)
print()
tok2 = nltk.word_tokenize(sent_tokens[101])
tagged_tok2 = nltk.pos_tag(tok2)
print (tagged_tok2)
print()
tok3 = nltk.word_tokenize(sent_tokens[102])
tagged_tok3 = nltk.pos_tag(tok3)
print (tagged_tok3)