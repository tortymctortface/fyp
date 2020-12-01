#v.2
from flask import Flask
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': 1600}
