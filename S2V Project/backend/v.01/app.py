#v.2
from flask import Flask
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

nlp = spacy.load("en_core_web_md")
s2v = Sense2VecComponent(nlp.vocab).from_disk("C:/FinalYear/FYP/s2v_old")
nlp.add_pipe(s2v)
with open("v.00/input_list/input_list.txt","r", encoding="utf-8") as f:
        TEXT = f.read()
doc = nlp(TEXT)

def list_of_files (doc):
    #find all first letters in the doc and create only unique a list of unique text file names to use
    text_files = list()
    for token in doc:
        if token.text.isalpha():
            text_files.append ("text" + (str(token.text[0])).lower() + ".txt")
    return set(text_files)