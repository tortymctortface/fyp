# FYP - Matthew Duffy

### Setup
This project requires installation of the following if you wish to run it locally:

 [Python 3](https://www.python.org/downloads/)

 [spaCy](https://spacy.io/usage/)

 You will also need to install the pre-trained set of vectors (either the 2015 or 2019 set) [here](https://github.com/explosion/sense2vec#pretrained-vectors)

***Note***
Once you have installed the pre-trained vectors you will need to copy the file address to where they are stored and paste it into `line 7` of the `main.py` file
>`s2v = Sense2VecComponent(nlp.vocab).from_disk("**YOUR_PATH_HERE**")`


### Extra Learning
To learn more about the technolgies used in building this project here are some useful links to tutorials:

 [Python 101]()

 [spaCy 101](https://course.spacy.io/en)

### General project overview
This project aims to create a memory map that will act as a pneumonic device to help you remember any given list. 
The given list is passed in along with the vocabulary that you want to possibly be used in the memory map. The larger the vocabulary generally correlates in a more creative result.

### How it works - for now
1. Add a list of anything you wish to remeber to the `\memorypalace\to_remember\NPPW_20-00` file - as an example I have added the Nobel Peace Prize Winners from 2000 to 2020
2. Add the vocabulary you wish to be considered for use in the memory map to the `\memorypalace\vocab\vocab.txt` file - remember the bigger the better
3. ***For now*** When you run the main.py you will create multiple text documents that consist of only verbs, each starting with the same letter as the first letter of every word in the list you wish to remember.

