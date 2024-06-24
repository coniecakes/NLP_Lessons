import nltk
from nltk.book import text6

#use the freqDist fucntion in nltk to obtain the frequencey distribution
text6_freqdist = nltk.FreqDist(text6)
print (text6_freqdist,'\n')

hapax = text6_freqdist.hapaxes()

text6_set = set(text6) #first order the text so it removes the duplicates
print (text6_set)
long_words = [w for w in text6_set if len(w) > 12]
print ('\nNumber of long words is: ',len(long_words), sorted(long_words))
#
common = []
for i in hapax:
    if i in long_words:
        common.append(i)
print ("\nCommon to hapax and long are:", common)
# #words that occur together - ex-Sperm Whale; Moby Dick; White Whale; old man; Captain Ahab;
print ('\nCOLLOCATIONS in the text are:')
text6.collocations()
# #