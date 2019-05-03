# phone-tree-wizard
A call menu navigation software tool

# Abstract
Automated phone menus have long frustrated callers. Confronted with a labyrinth of automated voice systems at a fixed pace, callers generally have an unpleasant interaction experience.  To solve these issues, this software development project creates an auto-caller bot utilizing voice recognition tools to generate a business’ phone tree diagram for callers.  This project assesses this software opportunity, discusses proposed approaches, and compares the current advances and technologies with a proposed solution.  Overall, this project explores the problem domain, applies existing libraries to build individual modules, proposes solutions to issue identified for future work, and develops a prototype with phone navigation capabilities. 

#  Tools
To build Phone Tree Wizard’s functionalities, the following APIs and libraries were used:

Twilio, which is a developer platform for communications with APIs to add capabilities such as voice, video, and messaging to personal applications.  Phone Tree Wizard utilizes Twilio’s built-in APIs and libraries to program auto-dial, keypad input, and speech-to-text parsing functionalities.

Ngrok, which is a web-tunnelling application that allows local machines to create a network service port.  Phone Tree Wizard uses Ngrok to create a temporary web server because Twilio sends an HTTP GET or POST to make outbound phone calls. 

Flask, which is a microframework for Python projects. Phone Tree Wizard uses Flask in order to run a webhook with Ngrok and post Twilio library instructions.  This creates a communication channel between Twilio’s Python library in Phone Tree Wizard and Twilio’s API. 

NLTK (Natural Language Toolkit), which is a Python-based text processing library for classification, tokenization, parsing, tagging and sentiment analysis.  Phone Tree Wizard applies NLTK in speech-to-text parsing to tag parts of speech and appropriately remove irrelevant text such as phone menu introductions.

Pydot, which is an interface to Graphviz that renders graphs as PDF or PNG files.  Phone Tree Wizard uses Pydot to output the phone tree diagram based on the stored data dictionary. This enables users to view the phone menu diagram outputted in a PDF file. 

# How to Run
Part I:  Open a Local Port
1. Install and download ngrok (https://ngrok.com/download)
2. cd [project folder]
3. python -m SimpleHTTPServer 5000
4. ./ngrok http 5000

Part II:  Create a virtual environment
1. In your terminal, create a virtual environment
2. virtualenv [project folder]
3. source [project folder]/bin/activate
4. cd phone-tree-wizard
5. python main.py
