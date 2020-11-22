import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent

nlp = spacy.load("en_core_web_md")
s2v = Sense2VecComponent(nlp.vocab).from_disk("C:/FinalYear/FYP/s2v_old")
nlp.add_pipe(s2v)
with open("/memorypalace/to_remember/input_list.txt","r", encoding="utf-8") as f:
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
                        
remove_uneeded(doc)

#freq = doc[0:1]._.s2v_freq
#vector = doc[0:1]._.s2v_vec
#most_similar = doc[0:1]._.s2v_most_similar(10)
#vocab_list = list(nlp.vocab.strings)