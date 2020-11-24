# FYP - Matthew Duffy

### Setup
This project requires installation of the following if you wish to run it locally:

 [Python 3](https://www.python.org/downloads/)

 [spaCy](https://spacy.io/usage/)

 You will also need to install the pre-trained vectors (either the 2015 or 2019 set) [here](https://github.com/explosion/sense2vec#pretrained-vectors)

***Note***
Once you have installed the pre-trained vectors you will need to copy its filepath and paste it into `line 7` of the `main.py` file
>`s2v = Sense2VecComponent(nlp.vocab).from_disk("**YOUR_PATH_HERE**")`


### Extra Learning
To learn more about the technolgies used in this project here are some useful links:

 [Python 101]()

 [spaCy 101](https://course.spacy.io/en)

### General project overview
This project aims to create a memory map that will act as a pneumonic device to help you remember any given list you wish. 
The given list is passed in along with the vocabulary that you want to use in the memory map. A larger vocabulary generally correlates in a more creative result.

### How it works - for now
1. Add a list of anything you wish to remeber to the `\memorypalace\to_remember\input_list.txt` file - as an example I have added the Nobel Peace Prize Winners from 2000 to 2020. The file should have each item you wish to remember separated by a **,** and if there are multiple parts to an item (for example more than one Nobel Peace Prize Winner in a single year) then each part should be separated with the word **and**
2. Add the vocabulary you wish to be considered for use in the memory map to the `\memorypalace\vocab\vocab.txt` file - remember the bigger the better (I have added the 10,000 most common English words as an example)
3. ***For now*** 
-When you run the main.py you will create multiple text documents that consist of only words that each start with the same letter as the first letter of every word in the list you wish to remember. 
-This narrows our search for us to then find and return a list of words each starting with the first letter of your input list to remember.
-The programme will also consider each word in each item of the list and try to return similar words for words in the same item. This is to aid in developing the memory palace.
- The output seems to fit the input list but I have not spent time evaluating it just yet.

### Issues

There are multiple obvious issues right now even before rigorous testing
1) Multiple nested for loops, this program could be much more efficient
2) Use of only functions in one main class - again cleaner code would read much easier
3) Now in regards the output list I have some passing observations
    - The random function which is supposed to currentlyt allow for a different list with each run of the program doesn't seem to work as "to" is always at index 0 of the output list
    - The output list does not account for words begining with letters that are not in the vocabulary
    - Words are repeated


