import nltk
from nltk.book import text6

#use the freqDist fucntion in nltk to obtain the frequencey distribution
# text6_freqdist = nltk.FreqDist(text6)
# print (text6_freqdist,'\n')
# #
# # #or print it in a tabulated format
#text6_freqdist.tabulate()
#
#now find the 10 most common words in the text
# most_common = (text6_freqdist.most_common(100))
# print (most_common,'\n')
print()
# # #what about words that occur only once - such words are known as hapaxes
# hapax = text6_freqdist.hapaxes()
# print (f'The hapaxes in the text are: {hapax}')
#
# #how many times do the two protagonists appear in the book
# swallow = text6_freqdist['swallow']
# wound = text6_freqdist['wound']
# print ('Number of time swallow occurs: ', swallow, 'and Number of times wound occurs: ', wound)
# # #
# # #which are the longest words in this text
text6_set = set(text6) #first order the text, so it removes the duplicates
print (text6_set)
long_words = [w for w in text6_set if len(w) > 12]
print ('Number of long words is: ',len(long_words), sorted(long_words))
#
# common = []
# for i in hapax:
#     if i in long_words:
#         common.append(i)
# print ("common to hapax and long are:", common)
# #words that occur together
# print ('COLLOCATIONS in the text are:')
# text1.collocations()
# #collocations