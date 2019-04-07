# Import Libraries


# Store parsed speech and break it apart
def storeSpeech(parsedSpeech):
    # break parsed speech based on its numerical option
    storage = []
    phrases = [
        'Press',
        'Select',
        'press',
        'select',
        '.'
    ]
    introPhrases = [
        'For',
        'To reach',
    ]
    """
    Iterate through every word in parsedSpeech
    1) remove commas
    2) tokenize based on identifying key phrases 
    2) remove list entries that do not have digits
    """

    # 1) cut out introduction
    for word in parsedSpeech.split():
        if word in introPhrases:
            storage.append(word)

    # 2) tokenize based on identifying key phrases
    for word in parsedSpeech.split():
        # # iterate through the word's characters to locate punctuation
        # if (word.find('.'))!=-1:
        #     storage = parsedSpeech.split('.')
        # iterate through the word to check if it is in the phrase list
        if word in phrases:
            storage = parsedSpeech.split(word)
            print("found special word")
            print(storage)

    # 3)  remove list entries that do not have digits
    storage2 = []
    for i in range(len(storage)-1):
        if (any(char.isdigit() for char in storage[i]))==True:
            print("found digit")
            print(i)
            storage2.append(storage[i])
            print(storage2)

    # 4) tokenize





    return storage2

# store into list
# [
#   (ID, option number, function description),
#   (ID, option number, function description),
#   ...
#  ]



def main():
    #test = "For Accounting, press 1. For Parks, press 2.  For Billing, press 3."
    #test = "Thank you for calling The Operations Tech Company, where Technology and business come together. If you know your party's extension, you may dial it at any time. Otherwise, choose from one of the following options. For Customer Service, press 1. For Technical Support, press 2. For our regular business hours, press 3. For accounting, press 4. For Purchasing, press 5. To find a location near you, press 6. Otherwise, press 0 for the receptionist or stay on the line and somebody will assist you shortly."
    test = "Thank you for calling walmart.com for Walmart and Sam's Club store locations questions about our source savings catcher program or the Walmart credit card, press 1 to track a walmart.com order, press 2 for all other walmart.com related questions, press 3. To hear this message again, press star."
    t = storeSpeech(test)
    print(t)

main()