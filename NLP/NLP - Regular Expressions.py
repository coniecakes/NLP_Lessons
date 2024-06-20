import re

str1 = ''' This chapter is divided into sections that skip between two quite different styles. 
In the "computing with language" sections we will take on some linguistically motivated 
programming tasks without necessarily explaining how they work. 
In the "closer look at Python" sections we will systematically review key programming 
concepts. We'll flag the two styles in the section titles, but later chapters 
will mix both styles without being so up-front about it. We hope this style of 
introduction gives you an authentic taste of what will come later, while covering a range of elementary concepts in linguistics and computer science. 
If you have basic familiarity with both areas, you can skip to 5; we will repeat 
any important points in later chapters, and if you miss anything you can easily 
consult the online reference material at http://nltk.org/. If the material is 
completely new to you, this chapter will raise more questions than it answers, 
questions that are addressed in the rest of this book.'''



words = re.findall("you", str1)
print (words)

#find all words that end in 'er'
words2 = re.findall("\w+er", str1)
print (words2)
#
# #find all urls in the string
# words3 = re.findall("https?://\w+\.\w+\.?\w*", str1)
# print (words3)
#
# #search function finds the first occurrence of the pattern
# words3a = re.search("https?://\w+\.\w+\.?\w*", str1)
# print (words3a)
#
# #find all words that end in m, me, men
# words4 = re.findall("\w+men*", str1)
# print (words4)

words5 = re.findall("\w+th", str1)
print(words5)