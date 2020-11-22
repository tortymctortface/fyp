# FYP - Matthew Duffy
```
### Setup
This project requires installation of the following if you wish to run it locally:
> [Python 3](https://www.python.org/downloads/)
> [spaCy](https://spacy.io/usage/)
> You will also need to install the pre-trained set of vectors (either the 2015 or 2019 set) [here](https://github.com/explosion/sense2vec#pretrained-vectors)
***Note***
Once you have installed the pre-trained vectors you will need to copy the file address to where they are stored and paste it into `line 7` of the `main.py` file
>`s2v = Sense2VecComponent(nlp.vocab).from_disk("**YOUR_PATH_HERE**")`
```
```
### Extra Learning
To learn more about the technolgies used in building this project here are some useful links to tutorials:
>[Python 101]()
>[spaCy 101](https://course.spacy.io/en)
```
```
### General project overview

This project aims to create a memory map that will act as a pneumonic device to help you remember any given list. 
The given list is passed in along with the vocabulary that you want to possibly be used in the memory map. 
```
```
### How it works - for now

Save 
```