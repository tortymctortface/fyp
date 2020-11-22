import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent

nlp = spacy.load("en_core_web_md")
s2v = Sense2VecComponent(nlp.vocab).from_disk("C:/FinalYear/FYP/s2v_old")
nlp.add_pipe(s2v)
with open("memorypalace/vocab/vocab.txt","r", encoding="utf-8") as f:
        TEXT = f.read()
NPPW = nlp(TEXT)

def list_of_files (doc):
    text_files = list()
    for token in doc:
        if token.text.isalpha():
            text_files.append ("text" + (str(token.text[0])).lower() + ".txt")
    print(set(text_files))
    return set(text_files)

def find_all_begining_with (doc):
    #vocab_list = list(nlp.vocab.strings)
    with open("memorypalace/vocab/vocab.txt","r", encoding="utf-8") as f:
        vocab_list = list(f.readlines())
        text_files = list_of_files(doc)
        for file in text_files:
            with open(("memorypalace/textfiles/"+ file) , "w+", encoding="utf-8") as f:
                for string in vocab_list:
                    if string[0].lower() == file[4]:
                        f.write(string + " ")
    return text_files

def remove_uneeded (doc):
    for file in find_all_begining_with(doc):
        with open(("memorypalace/textfiles/"+ file),"r", encoding="utf-8") as f:
            TEXT = f.read()
            docu = nlp(TEXT)
        with open(("memorypalace/textfiles/"+ file),"w", encoding="utf-8") as f:
            for token in docu:
                if token.pos_ == "VERB":
                    f.write(token.lemma_ + " ")
                        
remove_uneeded(NPPW)
with open("memorypalace/textfiles/texto.txt","r", encoding="utf-8") as f:
            TEXT = f.read()
print(TEXT)
#with open("C:/FinalYear/FYP/fyp/text.txt", encoding="utf-8") as f:
 #   TEXT = f.read()
 
#docu =nlp(text_file)

#for line in text_file:
    #for match_ID, start, end in matcher(docu):
      #  line = line.replace(str(Span(docu,start,end)), "")
       # text_file.write(line)
#for token in docu:
  #  if token.pos_ == ("VERB" or "ADJ"):
       # print (token.text)

#freq = doc[0:1]._.s2v_freq
#vector = doc[0:1]._.s2v_vec
#most_similar = doc[0:1]._.s2v_most_similar(10)
