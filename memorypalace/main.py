import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent
import random; 

nlp = spacy.load("en_core_web_md")
s2v = Sense2VecComponent(nlp.vocab).from_disk("C:/FinalYear/FYP/s2v_old")
nlp.add_pipe(s2v)
with open("memorypalace/to_remember/input_list.txt","r", encoding="utf-8") as f:
        TEXT = f.read()
doc = nlp(TEXT)

def list_of_files (doc):
    #find all first letters in the doc and create only unique a list of unique text file names to use
    text_files = list()
    for token in doc:
        if token.text.isalpha():
            text_files.append ("text" + (str(token.text[0])).lower() + ".txt")
    print(set(text_files))
    return set(text_files)
    
def find_all_begining_with (doc):
    #take your entire vocab and find all words in it that begin with the same letter that each of the text_files (created in list_of_files) end with
    # ..and create each text file and populate it with its own vocab
    with open("memorypalace/vocab/vocab.txt","r", encoding="utf-8") as f:
        vocab_list = list(f.readlines())
        text_files = list_of_files(doc)
        for file in text_files:
            with open(("memorypalace/textfiles/"+ file) , "w+", encoding="utf-8") as f:
                for string in vocab_list:
                    if string[0].lower() == file[4]:
                        f.write(string + " ")
    return text_files

def only_verbs_please (doc):
    #for every text file populated in find_all_begining_with process each one in the nlp pipeline
    #... and re-populate each file, this time only using the available verbs
    for file in find_all_begining_with(doc):
        with open(("memorypalace/textfiles/"+ file),"r", encoding="utf-8") as f:
            TEXT = f.read()
            docu = nlp(TEXT)
        with open(("memorypalace/textfiles/"+ file),"w", encoding="utf-8") as f:
            for token in docu:
                if token.pos_ == "VERB":
                    f.write(token.lemma_ + " ")
                        
def divide_inputs (doc):
    #divides the input list into a list of lists , each smaller list consisting of the list of words in one item you wish to remember from the original larger list
    divided_input_list = list()
    start = -1
    end = -1
    for token in doc:
        if token.text == ",":
            end = token.i
            divided_input_list.append(list(doc[start:end]))
            start = -1
            end = -1
        elif start == -1:
            start = token.i
        elif token.i == (len(doc)-1):
            end = token.i + 1
            divided_input_list.append(list(doc[start:end]))
            return divided_input_list

def find_similar(div_in_list):
    #For each element in the divided list it aims to find a random first word with the same first letter to the first word of the input list and..
    # ...the words similar to that first word but with the same first letter as the rest of the input list
    #(I know its hard for me to make sense of that comment too but once I properly test the function out I'll fix it)
    result = list()
    for lst in div_in_list:
        doc = nlp(str(lst))
        main_token = doc[(random.randrange(0,len(lst)))]
        x = 0
        for token in doc:
            similarity = 0
            if token.is_punct or token.text == "'s":
                x=x
            else:
                with open(("memorypalace/textfiles/text" + (str(token.text[0])).lower() + ".txt") , "r", encoding="utf-8") as f:
                    avail_vocab = nlp(f.read())
                    if x == 0:
                        token = avail_vocab[0]
                        result.append(token.text)
                        x = 1 
                    else:
                        for token in avail_vocab:
                            if token.i == (len(doc)-1):
                                if main_token.similarity(token) > similarity:
                                    similarity = main_token.similarity(token)
                                    word_to_append = token
                                    result.append(word_to_append.text)
                                else:
                                    result.append(word_to_append.text)
                            elif main_token.similarity(token) > similarity and not token.is_punct:
                                similarity = main_token.similarity(token)
                                word_to_append = token
    return result


find_all_begining_with (doc)
print (find_similar((divide_inputs (doc))))  
                        
                        
#freq = doc[0:1]._.s2v_freq
#vector = doc[0:1]._.s2v_vec
#most_similar = doc[0:1]._.s2v_most_similar(10)
#vocab_list = list(nlp.vocab.strings)