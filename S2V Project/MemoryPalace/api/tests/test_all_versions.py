import unittest
from ..v3 import v3
from ..v2 import v2
from ..v1 import v1
import spacy
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent

nlp = spacy.load("en_core_web_lg")

class TestV3(unittest.TestCase):

    def test_phonetics(self):
        self.assertEqual(v3.phonetic_weight("town","crown",1),1)
        self.assertEqual(v3.phonetic_weight("jordan","garden",0.9),0.6)
        self.assertEqual(v3.phonetic_weight("phelps","penguins",0.9),0.18)
        self.assertEqual(v2.phonetic_weight("town","crown",1),1)
        self.assertEqual(v2.phonetic_weight("jordan","garden",0.9),0.6)
        self.assertEqual(v2.phonetic_weight("phelps","penguins",0.9),0.18)
        self.assertEqual(v1.phonetic_weight("town","crown",1),1)
        self.assertEqual(v1.phonetic_weight("jordan","garden",0.9),0.6)
        self.assertEqual(v1.phonetic_weight("phelps","penguins",0.9),0.18)

    def test_flw(self):
        self.assertEqual(v3.first_letter_weight("dog","dark",1),1)
        self.assertEqual(v3.first_letter_weight("bog","dark",1),0)
        self.assertEqual(v2.first_letter_weight("dog","dark",1),1)
        self.assertEqual(v2.first_letter_weight("bog","dark",1),0)

    def test_slw(self):
        self.assertEqual(v3.secound_letter_weight("dog","dork",1),1)
        self.assertEqual(v3.secound_letter_weight("dig","dark",1),0)
        self.assertEqual(v2.secound_letter_weight("dog","dork",1),1)
        self.assertEqual(v2.secound_letter_weight("dig","dark",1),0)
        self.assertEqual(v1.secound_letter_weight("dog","dork",1),1)
        self.assertEqual(v1.secound_letter_weight("dig","dark",1),0)

    def test_similarity(self):
        self.assertEqual(v3.similarity_weight("jam","cream",1),0)
        self.assertEqual(float(format((v3.similarity_weight(nlp("collar"),nlp("collar"),1)),'.4f')),0.000)
        self.assertEqual(v2.similarity_weight("jam","cream",1),0)
        self.assertEqual(float(format((v2.similarity_weight(nlp("collar"),nlp("collar"),1)),'.4f')),1.000)
        

    def test_create_v1(self):
        self.assertEqual(len(v1.create_output_list_v1(("hey, you"),"food", 1, 1)),2)
        self.assertEqual(len(v1.create_output_list_v1((""),"food", 1, 1)),0)

    def test_create_v2(self):
        self.assertEqual(len(v2.create_output_list_v2(("hey, you"),"Not_Considered", 1,1,1,1)),2)
        self.assertEqual(len(v2.create_output_list_v2((""),"Not_Considered", 1,1,1,1)),0)

    def test_create_v3(self):
        self.assertEqual(len(v3.create_output_list_v3(("hey, you"),"Not_Considered", 1, 1,1,1)),2)
        self.assertEqual(len(v3.create_output_list_v3((""),"Not_Considered", 1,1,1,1)),0)
        


if __name__ == '__main__':
    unittest.main()