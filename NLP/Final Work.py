import nltk
from nltk.book import text9
text9_freqdist = nltk.FreqDist(text9)
hapax = text9_freqdist.hapaxes()
long_hapaxes = []
for i in hapax:
    if len(i) >= 15:
        long_hapaxes.append(i)
    else:
        continue
print (f'The long hapaxes in the text are: {long_hapaxes}')
