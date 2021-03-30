import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2Vec
from sense2vec import Sense2VecComponent
import phonetics
import enchant
import warnings
import csv
import random
import pronouncing
import numpy as np
#################################################################
# Weights to be used in each of the following functions
#################################################################
start_word = "Not_Considered"
#set the previous word similarity weight
pwsw = 0.7
#set the max value of weighting associated to a perfectly matched rhyming word
pw  = 0.9
#set the value associated with a matching first letter
flw = 0.3
#set the value associated with a matching secound letter
slw = 0.1

#################################################################

nlp = spacy.load("en_core_web_lg")
s2v = Sense2Vec().from_disk("C:/fyp/s2v_reddit_2019_lg")
#read in and process the input list the user wants to remember
#with open("api/v2/input_list/input_list.txt","r", encoding="utf-8") as f:
#    TEXT = f.read()
#doc = nlp(TEXT)

def create_output_list_v2(doc,in_start_word,pw,slw,flw, pwsw):
    #this takes in a one word start_word from the user and returns the most similar unique word to it that starts with the same letter for every word in the input list
    doc = nlp(doc)
    highest_scoring_list = []
    second_best_list=[]
    third_best_list=[]
    result = list()
    docu = nlp(in_start_word)
    previous_word = docu[0]
    #make sure to empty csv file from previous runs
    with open("api/v2/output/scores.csv", mode='w+') as f:
        f.close()
    #start_word = input("Please enter the one word start_word you wish the ouput list to have(for example food or art): ")
    for name in doc:
        word_to_append = "" 
        word2 = ""
        word3 = ""
        current_highest_score = 0
        if (name.text.isalpha()) and (not(name.pos_ == "SPACE")):
            with open("api/v2/vocab/nouns.txt","r", encoding="utf-8") as f:
                vocab_list=nlp(f.read())
                for possible_trigger_word in vocab_list:
                    if (possible_trigger_word.pos_ == "SPACE") or (possible_trigger_word.text=='\n') or (not(possible_trigger_word.text.isalpha())) or (name.text == possible_trigger_word.text):
                        total_simiarity=0
                    else:
                        if not result:
                            similarity_score = 0.1
                        else:
                            similarity_score = similarity_weight(previous_word, possible_trigger_word, pwsw)
                        phonetic_score = phonetic_weight(name.text, possible_trigger_word.text, pw)
                        secound_letter_score = secound_letter_weight(name.text, possible_trigger_word.text, slw)
                        first_letter_score = first_letter_weight(name.text, possible_trigger_word.text, flw)
                        #total weighted similarity score - stored so that it does not need to be computed more than once as 
                        total_similarity = (similarity_score + phonetic_score+ secound_letter_score + first_letter_score)

                    #if else to handle filling the output list with the words with the highest total_similarity score
                    if possible_trigger_word.i == (len(vocab_list)-1): 
                        if total_similarity > current_highest_score and result.count(possible_trigger_word.text) == 0:
                            current_highest_score = total_similarity
                            word3 = word2
                            word2 = word_to_append
                            word_to_append = possible_trigger_word
                            third_best_list = second_best_list
                            second_best_list = highest_scoring_list
                            highest_scoring_list = [(possible_trigger_word.text)]
                            create_output_csv(name.text, word_to_append,word2,word3,highest_scoring_list,second_best_list,third_best_list,previous_word,pw,slw,flw,pwsw)
                            previous_word = word_to_append
                            result.append(word_to_append.text)
                        else:
                            highest_scoring_from_list = (random.choice(highest_scoring_list))
                            word_to_append = nlp(highest_scoring_from_list)
                            create_output_csv(name.text, word_to_append,word2,word3,highest_scoring_list,second_best_list,third_best_list,previous_word,pw,slw,flw, pwsw)
                            previous_word = word_to_append
                            result.append(word_to_append.text)
                    elif total_similarity > current_highest_score and not possible_trigger_word.is_punct and not(possible_trigger_word.text=='\n') and result.count(possible_trigger_word.text) == 0:
                        current_highest_score = total_similarity
                        word3 = word2
                        word2 = word_to_append
                        word_to_append = possible_trigger_word
                        third_best_list = second_best_list
                        second_best_list = highest_scoring_list
                        highest_scoring_list = [(possible_trigger_word.text)]
                    elif total_similarity == current_highest_score and not(possible_trigger_word.text=='\n'):
                        highest_scoring_list.append(possible_trigger_word.text)
                        
                f.close()
    with open("api/v2/output/output.txt", mode='w+') as f:
        f.write("Output List:")
        f.write("\n")
        f.write(str(result))
        f.close()
    return result

def create_output_csv(original,w1,w2,w3,l1,l2,l3,previous_word,pw,slw,flw,pwsw):
    listoflists = list()
    listoflists.append(l1)
    listoflists.append(l2)
    listoflists.append(l3)
    topthreelist = list()
    topthreelist.append(w1)
    topthreelist.append(w2)
    topthreelist.append(w3)
    topthreelist = nlp(str(topthreelist))
    x = 1
    with open("api/v2/output/scores.csv", mode='a') as csv_file:
        fieldnames = ['***Original Word***', '***Chosen output***']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'***Original Word***':original,'***Chosen output***': w1.text})
    for word in topthreelist:
        if word.is_alpha:
            if previous_word.text == "Not_Considered":
                similarity = 0
            else:
                similarity = float(similarity_weight(previous_word,word,pwsw))
            phonetic_score = phonetic_weight(original, word.text, pw)
            secound_letter_score = secound_letter_weight(original, word.text,slw)
            first_letter_score = first_letter_weight(original, word.text,flw)
            #total weighted similarity score - stored so that it does not need to be computed more than once as .similarity is computationally quite heavy
            total_similarity = similarity + phonetic_score+ secound_letter_score +first_letter_score
            with open("api/v2/output/scores.csv", mode='a') as csv_file:
                fieldnames = ['Rated','Output Word', 'Total', 'Word and Previous Word Similarity', 'Phonetic Similarity','First letter weight', 'Secound letter weight',]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Rated':x,'Output Word':word.text, 'Total': total_similarity, 'Word and Previous Word Similarity': similarity, 'Phonetic Similarity': phonetic_score, 'First letter weight' : first_letter_score, 'Secound letter weight': secound_letter_score})
                csv_file.close()
            with open("api/v2/output/scores.csv", mode='a') as csv_file:
                fieldnames = ['Chosen at random form the list of words with equal total scores:']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Chosen at random form the list of words with equal total scores:':listoflists[x-1]}  )
                csv_file.close()
            x += 1
        csv_file.close()

def similarity_weight(previous_word,current_trigger_word, pwsw):
    try:
        warnings.filterwarnings("ignore", category=UserWarning)
        #convert both words into keys..
        #.. then convert each of the keys into their s2v vector representations
        a = s2v[str(current_trigger_word.text + "|NOUN")]
        b = s2v[str(previous_word.text + "|NOUN")]
        #manualy calcualte the cosine similarity as the built in .similarity only accepts spaCy tokens
        def cosine_similarity(x,y):
            root_x=np.sqrt(sum([i**2 for i in x]))
            root_y=np.sqrt(sum([i**2 for i in y]))
            return sum([i*j for i,j in zip(x,y)])/root_x/root_y
        similarity = cosine_similarity(a,b)
        #Weight the score using the user input pwsw (previous word similarity weight)
        similarity_score = similarity*pwsw
        return similarity_score
    except: 
        return 0


def first_letter_weight(name_to_remember, current_trigger_word, flw):
    #The weight of this score can be set above.If the secons letter is a match between the input word and the word that will possibly be used to represent it then a smal positive weighting is applied
    name_to_remember = name_to_remember.lower()
    current_trigger_word = current_trigger_word.lower()
    if (len(name_to_remember) > 1) and (len(current_trigger_word) > 1):
        if (name_to_remember[0] == current_trigger_word[0]):
            return 1 * flw
        else:
            return 0
    else:
        return 0

def secound_letter_weight(name_to_remember, current_trigger_word, slw):
    #The weight of this score can be set above.If the secons letter is a match between the input word and the word that will possibly be used to represent it then a smal positive weighting is applied
    name_to_remember = name_to_remember.lower()
    current_trigger_word = current_trigger_word.lower()
    if (len(name_to_remember) > 1) and (len(current_trigger_word) > 1):
        if (name_to_remember[1] == current_trigger_word[1]):
            return 1 * slw
        else:
            return 0
    else:
        return 0

def phonetic_weight(name_to_remember, current_trigger_word,pw):
#create metaphone codes without the first unnecessary letters
    if name_to_remember[0] == ('w' or 'q'):
        w1_without_fl = phonetics.metaphone(name_to_remember[2:])
    else:
        w1_without_fl = phonetics.metaphone(name_to_remember[1:]) 
    if current_trigger_word[0] == ('w' or 'q'):
        w2_without_fl = phonetics.metaphone(current_trigger_word[2:])
    else: 
        w2_without_fl = phonetics.metaphone(current_trigger_word[1:]) 
#calculate the levenshtein distance between the two metaphone codes
    score_without_fl = enchant.utils.levenshtein(w1_without_fl, w2_without_fl)

#create a list of all known rhyming words from the pronouncing library
    checklist = pronouncing.rhymes(name_to_remember)

#check if the candidate trigger word is in the list of know rhyming words 
    if current_trigger_word in checklist:
        return pw
#otherwise calculate its phonetic similarity using the users pw(phonetic weight) and ..
#..the levenshtein/metaphone score
    elif score_without_fl == 0:
        return pw/1.5
    else: 
        return pw/(score_without_fl+1)

#the_list = create_output_list_v2(doc,start_word, pw, slw, flw, pwsw)
