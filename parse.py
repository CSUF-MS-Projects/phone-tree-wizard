"""
Purpose:  Process and store parsed speech text
"""

# import libraries
import nltk
from nltk.tokenize import PunktSentenceTokenizer


class ParseText(object):
    def parse(self, company, parsedSpeech):
        #pass
        return self.dict_

class parse_PS(ParseText):
    def __init__(self):
        super(parse_PS, self).__init__()
        self.dict_ = {}

    def parse(self, company, parsedSpeech):
        self.dict_ = {}
        introPhrases = [
            'For',
            'for',
            'reach',
            'Reach',
        ]

        def convert_pos(raw_text):
            my_list = []
            for word in raw_text.split():
                my_list.append(word)
            tagged = nltk.pos_tag(my_list)  # nltk tagging
            # convert list of tuples to list of lists
            list_of_lists = [list(elem) for elem in tagged]

            return list_of_lists

        # 1) find index to introduction's beginning
        def introIndex(text_list):
            storage = []
            for i in range(len(text_list)):
                for word in text_list[i]:
                    if (word in introPhrases) and (text_list[i + 1][1] == 'NNP'):
                        storage.append(word)
                        return i
                        break

        #  2) remove introduction --> returns string of the first entry without intro
        def removeIntro(startIndex, text_list):
            start = startIndex
            for i in range(len(text_list)):
                if text_list[i][1] == 'CD':
                    end = i  # i = where the first cardinal digit is found
                    break
            indices = []
            for i in range(start, end):  # store first entry into l (after removing intro)
                indices.append(i)
            l = " ".join([text_list[i][0] for i in indices])
            return l

        #  3)  find all other indices with digits --> return a list of indices where cardinal digits are found
        def findDigits(text_list):
            digitIndices_list = []
            for i in range(len(text_list)):
                if text_list[i][1] == 'CD':
                    digitIndices_list.append(i)
            return digitIndices_list

        #  4)  Create new dictionary with:
        def storeInDictionary(listOfDigits, firstEntry, t):
            d = {}
            i = 1
            d[i] = firstEntry
            i += 1
            length = len(listOfDigits)
            for i in range(len(listOfDigits)):
                if i < len(listOfDigits) - 1:
                    start = listOfDigits[i] + 1
                    end = listOfDigits[i + 1]
                    indices = []
                    for i2 in range(start, end):
                        indices.append(i2)
                    l = " ".join([t[i2][0] for i2 in indices])
                    d[i + 2] = l
            return d

        def parseText(text):
            t = convert_pos(text)
            i = introIndex(t)
            first_entry = removeIntro(i, t)
            di = findDigits(t)
            dict_ = storeInDictionary(di, first_entry, t)
            return dict_


        self.dict_ = parseText(parsedSpeech)
        return self.dict_