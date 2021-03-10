import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent

#Instantiate English pipeline object
nlp = spacy.load("en_core_web_lg")
#load pre-trained sense2vec vectors
s2v = Sense2VecComponent(nlp.vocab).from_disk("C:/fyp/s2v_reddit_2019_lg")
#add vectors to the procesing pipeline
nlp.add_pipe(s2v)

def nouns_only():
    with open("backend/v.03/vocab/vocab.txt","r", encoding="utf-8") as f:
        vocab_list=nlp(f.read())
        f.close()
    with open("backend/v.03/vocab/nouns.txt","a", encoding="utf-8") as f:
        for word in vocab_list:
            if word.pos_ == "NOUN":
                with open("backend/v.03/vocab/nouns.txt","a", encoding="utf-8") as f:
                    f.write(word.text + "\n")

nouns_only()


        