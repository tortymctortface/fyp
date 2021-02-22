import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent
import phonetics
import enchant
import warnings

#################################################################
# Weights to be used in each of the following functions
#################################################################
#set theme to be used for s2v_similarity comparison (between -2 and 2)
theme = "sex"
#set the max value of weighting associated to a perfectly matched rhyming word
rhyme_weighting  = 0.1
#set the value associated with a matching secound letter
second_letter_weight = 0.05
#################################################################

#Instantiate English pipeline object
nlp = spacy.load("en_core_web_lg")
#load pre-trained sense2vec vectors
s2v = Sense2VecComponent(nlp.vocab).from_disk("C:/fyp/s2v_reddit_2019_lg")
#add vectors to the procesing pipeline
nlp.add_pipe(s2v)
#read in and process the input list the user wants to remember
with open("backend/v.02/input_list/input_list.txt","r", encoding="utf-8") as f:
        TEXT = f.read()
doc = nlp(TEXT)

def create_first_letter_files(doc):
    #find all first letters in the doc and create only unique a list of unique text file names to use
    text_files = list()
    for token in doc:
        if token.text.isalpha():
            text_files.append ("text" + (str(token.text[0])).lower() + ".txt")
    with open("backend/v.02/vocab/vocab.txt","r", encoding="utf-8") as f:
        vocab_list=nlp(f.read())
        #vocab_list =["ant", "apple", "arch", "arm", "army", "baby", "bag", "ball", "band", "basin", "basket", "bath", "bed", "bee", "bell", "berry", "bird", "blade", "board", "boat", "bone", "book", "boot", "bottle", "box", "boy", "brain", "brake", "branch", "brick", "bridge", "brush", "bucket", "bulb", "button", "cake", "camera","card", "cart", "carriage", "cat", "chain", "cheese", "chest", "chin", "church", "circle", "clock", "cloud", "coat", "collar", "comb", "cord", "cow", "cup", "curtain", "cushion", "dog", "door", "drain", "drawer", "dress", "drop", "ear", "egg", "engine", "eye", "face", "farm", "feather", "finger", "fish", "flag", "floor", "fly", "foot", "fork", "fowl", "frame", "garden", "girl", "glove", "goat", "gun", "hair", "hammer", "hand", "hat", "head", "heart", "hook", "horn", "horse", "hospital", "house", "island", "jewel", "kettle", "key", "knee", "knife", "knot", "leaf", "leg", "library", "line", "lip", "lock", "map", "match", "monkey", "moon", "mouth", "muscle", "nail", "neck", "needle", "nerve", "net", "nose", "nut", "office", "orange", "oven", "parcel", "pen", "pencil", "picture", "pig", "pin", "pipe", "plane", "plate", "plough", "pocket", "pot", "potato", "prison", "pump", "rail", "rat", "receipt", "ring", "rod", "roof", "root", "sail", "school", "scissors", "screw", "seed", "sheep", "shelf", "ship", "shoe", "skin", "snake", "sock", "spade", "sponge", "spoon", "spring", "square", "stamp", "star", "station", "stem", "stick", "stocking", "stomach", "store", "street", "sun", "table", "tail", "thread", "throat", "thumb", "ticket", "toe", "tongue", "tooth", "town", "train", "tray", "tree", "trousers", "umbrella", "wall", "watch", "wheel", "whip", "whistle", "window", "wing", "wire", "worm"]
        text_files = set(text_files)
        for file in text_files:
            with open(("backend/v.02/textfiles/"+ file) , "w+", encoding="utf-8") as f:
                for token in vocab_list:
                    if (token.text[0].lower() == file[4]) and not (token.pos_=="SPACE" or token.pos_=="CCONJ" or token.pos_=="DET" or token.pos_=="ADP" or token.pos_=="SCONJ" or token.pos_=="AUX" or token.pos_=="ADV" or token.pos_=="VERB"  or token.pos_=="PRON" or token.pos_=="PUNCT"):
                        f.write(token.lemma_  + " ")
                        
def split_input_list (doc):
    #divides the input list into a list of lists , each smaller list consisting of the list of words in one item you wish to remember from the original larger list
    #each input word or phrase or name and surname should be divided by commas. 
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

def create_output_list(doc, in_theme):
    #this takes in a one word theme from the user and returns the most similar unique word to it that starts with the same letter for every word in the input list
    #there is currently an unrequired for loop, and it throws warnings about the .simalrity 
    create_first_letter_files (doc)
    div_in_list = split_input_list (doc)
    result = list()
    docu = nlp(in_theme)
    theme = docu[0]
    #theme = input("Please enter the one word theme you wish the ouput list to have(for example food or art): ")
    for lst in div_in_list:
        doc = nlp(str(lst))
        x = 0
        for in_token in doc:
            word_to_append = in_token
            s2v_similarity = 0
            if not in_token.text.isalpha():
                x=x
            else:
                x = 1
                with open(("backend/v.02/textfiles/text" + (str(in_token.text[0])).lower() + ".txt") , "r", encoding="utf-8") as f:
                    avail_vocab = nlp(f.read())
                    for token in avail_vocab:
                        #try catch to handle the possibility that a comparison between to words (the theme word and the current word from the vocab) has never occured before
                        try:
                            warnings.filterwarnings("ignore", category=UserWarning)
                            #using the .similarity here instead of ._.s2v_similarity as Ive noticed faster and better results from it
                            similarity = theme.similarity(token)
                        except: 
                            similarity = 0
                        #total weighted similarity score - stored so that it does not need to be computed more than once as .similarity is computationally quite heavy
                        total_similarity = similarity + phonetic_weight(theme.text, token.text)+ secound_letter_weight(theme.text, token.text)
                        #if else to handle filling the output list with the words with the highest total_similarity score
                        if token.i == (len(avail_vocab)-1): 
                            if total_similarity > s2v_similarity and result.count(token.text) == 0:
                                s2v_similarity = total_similarity
                                word_to_append = token
                                result.append(word_to_append.text)
                            else:
                                result.append(word_to_append.text)
                        elif total_similarity > s2v_similarity and not token.is_punct and result.count(token.text) == 0:
                            s2v_similarity = total_similarity
                            word_to_append = token
    return result

def secound_letter_weight(wordone, wordtwo):
    #The weight of this score can be set above.If the secons letter is a match between the input word and the word that will possibly be used to represent it then a smal positive weighting is applied
    if (len(wordone) > 1) and (len(wordtwo) > 1):
        if (wordone[1] == wordtwo[1]):
            return second_letter_weight
        else:
            return 0
    else:
        return 0

def phonetic_weight(wordone, wordtwo):
    #provide a score for the phonetic s2v_similarity of two words using double metaphone and damaru levenshtein. The weight of this score can be set above.
    w1 = phonetics.dmetaphone(wordone)
    w2 = phonetics.dmetaphone(wordtwo)
    score = enchant.utils.levenshtein(w1, w2)
    if score == 0:
        return rhyme_weighting
    elif score == 1:
        return (rhyme_weighting/2)
    else:
        return 0

def create_verbs_only_file ():
    #find all available verbs in the given vocab and add them to a text file to reduce the search space for add_similar_verbs_to_output_list.
    with open("backend/v.02/vocab/vocab.txt","r", encoding="utf-8") as f:
        vocab = nlp(f.read())
        with open(("backend/v.02/textfiles/verbs") , "w+", encoding="utf-8") as f:
                for token in vocab:
                    if token.pos_ == "VERB":
                        f.write(token.lemma_ + " ")

def add_similar_verbs_to_output_list(the_list):
    #verbs added to pre-created output list. Verbs added are unique and will take into account the preceeding and succeding word in the list.
    outlist = list()
    midlist = list()
    create_verbs_only_file ()
     #process the list created in create_output_list
    string_list=str(the_list)
    the_list = nlp(string_list)
    #filter non alphabetic characters such as - , ' ...
    for item in the_list:
        if item.is_alpha:
            midlist.append(item)
    #for every word in the list created in create_output_list
    x = 0
    for word in midlist:
        s2v_similarity = 0
        x += 1
        if x == (len(midlist)):
            outlist.append(word.text)
        else:
            next_word = midlist[x]
            verb_to_append = next_word
            outlist.append(word.text)
            with open(("backend/v.02/textfiles/verbs") , "r", encoding="utf-8") as f:
                vocab = nlp(f.read())
                for token in vocab:
                     #try catch to handle the possibility that a comparison between to words (the theme word and the current word from the vocab) has never occured before
                    try:
                        warnings.filterwarnings("ignore", category=UserWarning)
                        #using the .similarity here instead of ._.s2v_similarity as Ive noticed faster and better results from it
                        similarity = (word.similarity(token) + next_word.similarity(token))
                    except:
                        similarity = 0
                    if token.i == (len(vocab)-1):
                        if (similarity > s2v_similarity) and string_list.count(token.text) == 0 and outlist.count(token.text) == 0:
                            s2v_similarity = similarity
                            verb_to_append = token
                            outlist.append(verb_to_append.text)
                            break
                        else:
                            outlist.append(verb_to_append.text)
                            break
                    elif (similarity > s2v_similarity) and outlist.count(token.text) == 0 and string_list.count(token.text) == 0:
                        s2v_similarity = similarity
                        verb_to_append = token
    return outlist

#the_list = ['alcohol', 'agriculture', 'drink', 'meal', 'accommodation', 'nutrition', 'meat', 'inedible', 'cooking', 'takeout', 'animal', 'nutrient', 'wheat', 'junk', 'medicine', 'soup', 'toothpaste', 'needy', 'dish', 'quail', 'ketchup', 'seafood', 'asparagus', 'milk', 'yogurt', 'transportation', 'oatmeal', 'food', 'tea', 'pork', 'omelette', 'cuisine', 'wine', 'tuna', 'eaten', 'upbrining', 'entertainment', 'jewellery', 'soda', 'appetizing', 'loaf', 'gourmet', 'amenity', 'tobacco', 'kitchen', 'liquor', 'booze', 'onion', 'morsel', 'agricultural', 'aid', 'goods', 'appetite', 'tomato', 'urine', 'iodine', 'poultry', 'oil', 'coffee', 'condiment', 'meatloaf', 'yummy', 'ammunition', 'tongs', 'gruel', 'bread', 'ingredient', 'allowance', 'edible', 'affection', 'antibiotic', 'mutton', 'eatable', 'waiter', 'margarine', 'steak', 'electricity', 'jobless', 'cutlery', 'knives', 'aroma', 'appliance', 'tasting', 'unhealthy', 'nanny', 'kitty', 'dinner', 'juice']
the_list = create_output_list(doc,theme)
print(the_list)
print(add_similar_verbs_to_output_list(the_list))
                    


            


             
#freq = doc[0:1]._.s2v_freq
#vector = doc[0:1]._.s2v_vec
#most_similar = doc[0:1]._.s2v_most_similar(10)
#vocab_list = list(nlp.vocab.strings)