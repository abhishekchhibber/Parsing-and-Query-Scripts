import nltk
from nltk.tag import pos_tag

sentence = "I have a doll at home, her name is Sugandha. She is super cute"

tokens = nltk.word_tokenize(sentence)
#print (tokens)

posTags = nltk.pos_tag(tokens)
pT = [ ]
for posTag in posTags:
	#print(posTag)
	if posTag[1] == 'NNP':
		pT.append(posTag[0])

x = " ".join(str(x) for x in pT)
print (x)
