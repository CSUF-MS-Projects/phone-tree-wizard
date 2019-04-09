import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
# nltk.download('averaged_perceptron_tagger')
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


introPhrases = [
        'For',
        'for',
        'reach',
        'Reach',
    ]
# 1) find index to introduction's beginning
def introIndex(text_list):
    storage = []
    for i in range(len(text_list)):
        for word in text_list[i]:
            if (word in introPhrases) and (text_list[i + 1][1] == 'NNP'):
            #if (word == 'for') and (text_list[i+1][1] == 'NNP'):
                print("found!")
                storage.append(word)
                return i
                break

#  2) remove introduction --> returns string of the first entry without intro
def removeIntro(startIndex, text_list):
    start = startIndex
    for i in range(len(text_list)):
        if text_list[i][1] == 'CD':
            print("index is: ")
            print(i)
            end = i # i = where the first cardinal digit is found
            break
    indices = []
    for i in range(start, end): # store first entry into l (after removing intro)
        indices.append(i)
    l = " ".join([text_list[i][0] for i in indices])
    return l

#  3)  find all other indices with digits --> return a list of indices where cardinal digits are found
def findDigits(text_list):
    digitIndices_list = []
    for i in range(len(text_list)):
        if text_list[i][1] == 'CD':
            #digitIndices.append(text_list[i][0])
            digitIndices_list.append(i)
    return digitIndices_list

#  4)  Create new dictionary with:
"""
level_selection = 
1_1 = { 
    1 :"source savings catcher program or the Walmart credit card",
    2: "to track a walmart.com order",
    3: "for all other walmart.com related questions"
    }
"""
def storeInDictionary(listOfDigits, firstEntry, t):
    d = {}
    i = 1
    d[i] = firstEntry
    i+=1
    length = len(listOfDigits)
    print(length)
    for i in range(len(listOfDigits)):
        if i < len(listOfDigits)-1:
            start = listOfDigits[i] + 1 #26
            end = listOfDigits[i+1] # 32 + 32 - 25 = 39
            print("show start // end")
            print(start)
            print(end)
            indices = []
            for i2 in range(start, end):
                indices.append(i2)
            l = " ".join([t[i2][0] for i2 in indices])
            d[i+2] = l
    return d

# def storeInDictionary(listOfDigits):
#     d = {}
#     i = 1
#     d[i] = first_entry
#     i+=1
#     length = len(listOfDigits)
#     print(length)
#     for i in range(len(listOfDigits)):
#         if i < len(listOfDigits)-1:
#             start = listOfDigits[i] + 1 #26
#             end = listOfDigits[i+1] # 32 + 32 - 25 = 39
#             print("show start // end")
#             print(start)
#             print(end)
#             indices = []
#             for i2 in range(start, end):
#                 indices.append(i2)
#             l = " ".join([t[i2][0] for i2 in indices])
#             d[i+2] = l
#     return d

# t = convert_pos(sample_text)
# i = introIndex(t)
# print(i)
# first_entry = removeIntro(i, t)
# print(type(first_entry))
# print(first_entry)
# print("digit indices: ")
# di = findDigits(t)
# print(di)
# print("stored dictionary is: ")
# print("TEST")
# dict_ = storeInDictionary(di)
# print(dict_)


def parseText(text):
    t = convert_pos(text)
    i = introIndex(t)
    print(i)
    first_entry = removeIntro(i, t)

    print("digit indices: ")
    di = findDigits(t)
    print(di)
    print("stored dictionary is: ")
    print("TEST")
    dict_ = storeInDictionary(di, first_entry, t)
    print(dict_)
    return dict_

d = parseText(sample_text)