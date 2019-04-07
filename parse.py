import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
# nltk.download('averaged_perceptron_tagger')
#from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

sample_text = "Thank you for calling walmart.com for Walmart and Sam's Club store locations questions about our source savings catcher program or the Walmart credit card, press 1 to track a walmart.com order, press 2 for all other walmart.com related questions, press 3. To hear this message again, press star."

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


"""
function: assign each word to parts of speech
"""
def convert_pos(raw_text):
    my_list = []
    for word in raw_text.split():
        my_list.append(word)
    tagged = nltk.pos_tag(my_list)
    # convert list of tuples to list of lists
    list_of_lists = [list(elem) for elem in tagged]

    return list_of_lists

# a = [[1, 3, 4], [2, 4, 4], [3, 4, 5]]
# print(a)
# for list in a:
#     for number in list:
#         #print(number)
#         if number == 5:
#             print(number)

t = convert_pos(sample_text)
introPhrases = [
        'For',
        'To reach',
    ]
# 1) find index to introduction's beginning
def introIndex(text_list):
    storage = []
    for i in range(len(text_list)):
        for word in text_list[i]:
            if (word == 'for') and (text_list[i+1][1] == 'NNP'):
                print("found!")
                storage.append(word)
                return i
                break

#  2) remove introduction
def removeIntro(startIndex, text_list):
    start = startIndex
    for i in range(len(text_list)):
        if text_list[i][1] == 'CD':
            print("index is: ")
            print(i)
            end = i
            break
    indices = []
    for i in range(start, end):
        print(i)
        indices.append(i)
    l = " ".join([text_list[i][0] for i in indices])
    return l

#  3)  find all other indices with digits
def findDigits(text_list):
    digitIndices = []
    for i in range(len(text_list)):
        if text_list[i][1] == 'CD':
            digitIndices.append(text_list[i][0])
    return digitIndices

i = introIndex(t)
print(i)
new_list = removeIntro(i, t)
print(new_list)
print("digit indices: ")
di = findDigits(t)
print(di)

#  4)  Create new list with:  [selection, number]
store = []
for i in range(len(di)):
    store.append()

# def parse_sentence():
#     storage = []
#     try:
#         for i in tokenized:
#             words = nltk.word_tokenize(i)
#             print("WORD IS: ")
#             print(words)
#             tagged = nltk.pos_tag(words)
#             print(tagged)
#             storage.append(tagged)
#
#     except Exception as e:
#         print(str(e))
#         print("EXCEPTION")
#     return storage
#
# t = parse_sentence()
# print(type(t))
# print(t)
#
#
