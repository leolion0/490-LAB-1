# import these modules
from copy import deepcopy

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.util import trigrams
import operator

#https://www.machinelearningplus.com/nlp/lemmatization-examples-python/
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

lem = WordNetLemmatizer()
f = open('nlp_input.txt', 'r')
perm_conts = f.read()
contents = deepcopy(perm_conts)


#Remove weird chars from contents
bad_chars = ['(', ')', ',', '?', '!', '=', ':', ';']
for i in bad_chars:
    contents = contents.replace(i, ' ')

cont_list = contents.split()#list of each word in contents
for word in cont_list:
    no_dot = word.replace('.', '')
    temp = no_dot
    if (not (temp.isdigit()) and (not (temp == ''))):
        temp2 = lem.lemmatize(temp, get_wordnet_pos(temp))
        word.replace(no_dot, temp2)

contents = " ".join(cont_list)



#Find trigram sentences
tris = list(trigrams(cont_list))
count_tris = dict()
for key in tris:
    if key not in count_tris:
        count_tris[key] = 1
    else:
        count_tris[key] += 1

sorted_count = sorted(count_tris.items(), key=operator.itemgetter(1))

top_10 = list()
for i in range(10):
    top_10.append(sorted_count.pop()[0])

#Top 10 trigrams now in list top_10



cont_sent = contents.split('.')
extr_sent = list()
for sentence in cont_sent:
    for top in top_10:
        sub = top[0] + " " + top[1] + " " + top[2]
        if sentence.find(sub) is not -1:
            extr_sent.append(sentence)
            break

outstr = ""
for sent in extr_sent:
    outstr += sent + "."
print(outstr)

# print(top_10)

# print(cont_list)

tokens = dict()
for word in cont_list:
    key = lem.lemmatize(word, get_wordnet_pos(word))
    if key not in tokens:
        tokens[key] = 1
    else:
        tokens[key] += 1

# print(tokens)








# a denotes adjective in "pos"
# print("better :", lemmatizer.lemmatize("better", pos="a"))