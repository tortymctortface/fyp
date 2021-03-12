import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent
import phonetics
import enchant
import warnings
import csv

#################################################################
# Weights to be used in each of the following functions
#################################################################
start_word = "Not_Considered"
#set start_word weight
pwsw = 1
#set the max value of weighting associated to a perfectly matched rhyming word
pw  = 0.8
#set the value associated with a matching first letter
flw = 0.19
#set the value associated with a matching secound letter
slw = 0.01

#################################################################

#Instantiate English pipeline object
nlp = spacy.load("en_core_web_lg")
#load pre-trained sense2vec vectors
s2v = Sense2VecComponent(nlp.vocab).from_disk("C:/fyp/s2v_reddit_2019_lg")
#add vectors to the procesing pipeline
#nlp.add_pipe(s2v)
#read in and process the input list the user wants to remember
#with open("api/v2/input_list/input_list.txt","r", encoding="utf-8") as f:
 #   TEXT = f.read()
#doc = nlp(TEXT)

def create_output_list_v2(doc, in_start_word,pw,slw,flw, pwsw):
    #this takes in a one word start_word from the user and returns the most similar unique word to it that starts with the same letter for every word in the input list
    #there is currently an unrequired for loop, and it throws warnings about the .simalrity
    doc = nlp(doc)
    result = list()
    docu = nlp(in_start_word)
    previous_word = docu[0]
    #make sure to empty csv file from previous runs
    with open("api/v2/output/scores.csv", mode='w+') as f:
        f.close()
    #start_word = input("Please enter the one word start_word you wish the ouput list to have(for example food or art): ")
    for in_token in doc:
        word_to_append = in_token
        word2 = ""
        word3 = ""
        current_highest_score = 0
        if (in_token.text.isalpha()) and (not(in_token.pos_ == "SPACE")):
            with open("api/v2/vocab/nouns.txt","r", encoding="utf-8") as f:
                vocab_list=nlp(f.read())
                for token in vocab_list:
                    if not result:
                        similarity = 0.5
                    else:
                        try:
                            warnings.filterwarnings("ignore", category=UserWarning)
                            #using the .similarity here instead of ._.s2v_similarity as Ive noticed faster and better results from it
                            similarity = previous_word.similarity(token)
                        except: 
                            similarity = 0
                    phonetic_score = phonetic_weight(in_token.text, token.text, pw)
                    secound_letter_score = secound_letter_weight(in_token.text, token.text, slw)
                    first_letter_score = first_letter_weight(in_token.text, token.text, flw)
                    #total weighted similarity score - stored so that it does not need to be computed more than once as .similarity is computationally quite heavy
                    total_similarity = (pwsw*similarity) + phonetic_score+ secound_letter_score +first_letter_score
                    #print(total_similarity)
                    #if else to handle filling the output list with the words with the highest total_similarity score
                    if token.i == (len(vocab_list)-1): 
                        if total_similarity > current_highest_score and result.count(token.text) == 0:
                            current_highest_score = total_similarity
                            word3 = word2
                            word2 = word_to_append
                            word_to_append = token
                            create_output_csv(in_token.text, word_to_append,word2,word3,previous_word,pw,slw,flw,pwsw)
                            previous_word = word_to_append
                            result.append(word_to_append.text)
                        else:
                            create_output_csv(in_token.text, word_to_append,word2,word3,previous_word,pw,slw,flw, pwsw)
                            previous_word = word_to_append
                            result.append(word_to_append.text)
                    elif total_similarity > current_highest_score and not token.is_punct and result.count(token.text) == 0:
                        current_highest_score = total_similarity
                        word3 = word2
                        word2 = word_to_append
                        word_to_append = token
                f.close()
    with open("api/v2/output/output.txt", mode='w+') as f:
        f.write("Output List:")
        f.write("\n")
        f.write(str(result))
        f.close()
    return result

def create_output_csv(original,w1,w2,w3,previous_word,pw,slw,flw,pwsw):
    topthreelist = list()
    topthreelist.append(w1)
    topthreelist.append(w2)
    topthreelist.append(w3)
    topthreelist = nlp(str(topthreelist))
    x = 1
    with open("api/v2/output/scores.csv", mode='a') as csv_file:
        fieldnames = ['Original Word', 'Previous Word']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Original Word':original,'Previous Word': previous_word.text})
    for word in topthreelist:
        if word.is_alpha:
            if previous_word.text == "Not_Considered":
                similarity = 0.5
            else:
                similarity = (float(previous_word.similarity(word)) * pwsw)
            phonetic_score = phonetic_weight(original, word.text, pw)
            secound_letter_score = secound_letter_weight(original, word.text,slw)
            first_letter_score = first_letter_weight(original, word.text,flw)
            #total weighted similarity score - stored so that it does not need to be computed more than once as .similarity is computationally quite heavy
            total_similarity = similarity + phonetic_score+ secound_letter_score
            with open("api/v2/output/scores.csv", mode='a') as csv_file:
                fieldnames = ['Rated','Output Word', 'Total', 'Word and Previous Word Similarity', 'Phonetic Similarity','First letter weight', 'Secound letter weight']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Rated':x,'Output Word':word.text, 'Total': total_similarity, 'Word and Previous Word Similarity': similarity, 'Phonetic Similarity': phonetic_score, 'First letter weight' : first_letter_score, 'Secound letter weight': secound_letter_score})
                csv_file.close()
            x += 1
        csv_file.close()

def first_letter_weight(wordone, wordtwo, flw):
    #The weight of this score can be set above.If the secons letter is a match between the input word and the word that will possibly be used to represent it then a smal positive weighting is applied
    if (len(wordone) > 1) and (len(wordtwo) > 1):
        if (wordone[0] == wordtwo[0]):
            return 1 * flw
        else:
            return 0
    else:
        return 0

def secound_letter_weight(wordone, wordtwo, slw):
    #The weight of this score can be set above.If the secons letter is a match between the input word and the word that will possibly be used to represent it then a smal positive weighting is applied
    if (len(wordone) > 1) and (len(wordtwo) > 1):
        if (wordone[1] == wordtwo[1]):
            return 1 * slw
        else:
            return 0
    else:
        return 0

def phonetic_weight(wordone, wordtwo,pw):
    #provide a score for the phonetic s2v_similarity of two words using double metaphone and damaru levenshtein. The weight of this score can be set above.
    w1 = phonetics.metaphone(wordone)
    w2 = phonetics.metaphone(wordtwo)
    score = enchant.utils.levenshtein(w1, w2)
    if score == 0:
        return 1*pw
    elif score == 1:
        return (1*pw)/2
    elif score == 2:
        return (1*pw)/3
    else: 
        return 0

#the_list = ['alcohol', 'agriculture', 'drink', 'meal', 'accommodation', 'nutrition', 'meat', 'inedible', 'cooking', 'takeout', 'animal', 'nutrient', 'wheat', 'junk', 'medicine', 'soup', 'toothpaste', 'needy', 'dish', 'quail', 'ketchup', 'seafood', 'asparagus', 'milk', 'yogurt', 'transportation', 'oatmeal', 'food', 'tea', 'pork', 'omelette', 'cuisine', 'wine', 'tuna', 'eaten', 'upbrining', 'entertainment', 'jewellery', 'soda', 'appetizing', 'loaf', 'gourmet', 'amenity', 'tobacco', 'kitchen', 'liquor', 'booze', 'onion', 'morsel', 'agricultural', 'aid', 'goods', 'appetite', 'tomato', 'urine', 'iodine', 'poultry', 'oil', 'coffee', 'condiment', 'meatloaf', 'yummy', 'ammunition', 'tongs', 'gruel', 'bread', 'ingredient', 'allowance', 'edible', 'affection', 'antibiotic', 'mutton', 'eatable', 'waiter', 'margarine', 'steak', 'electricity', 'jobless', 'cutlery', 'knives', 'aroma', 'appliance', 'tasting', 'unhealthy', 'nanny', 'kitty', 'dinner', 'juice']
#the_list = create_output_list_v2(doc,start_word, pw, slw, flw, pwsw)

                    