import nltk
from nltk.book import text1

#use the freqDist fucntion in nltk to obtain the frequencey distribution
text1_freqdist = nltk.FreqDist(text1)
print (text1_freqdist,'\n')
# #
# # #or print it in a tabulated format
#text1_freqdist.tabulate()
#
#now find the 10 most common words in the text
most_common = (text1_freqdist.most_common(100))
print (most_common,'\n')
# #
# # #what about words that occur only once - such words are known as hapaxes
hapax = text1_freqdist.hapaxes()
print ('The hapaxes in the text are: ', hapax)
#
# #how many times do the two protagonists appear in the book
moby = text1_freqdist['Moby']
ahab = text1_freqdist['Ahab']
print ('Number of time Moby occurs: ', moby, 'and Number of times Ahab occurs: ',ahab)
# #
# #which are the longest words in this text
text1_set = set(text1) #first order the text so it removes the duplicates
# print (text1_set)
long_words = [w for w in text1_set if len(w) > 15]
print ('Number of long words is: ',len(long_words), sorted(long_words))

common = []
for i in hapax:
    if i in long_words:
        common.append(i)
print ("common to hapax and long are:", common)
#words that occur together
print ('COLLOCATIONS in the text are:')
text1.collocations()
#collocations