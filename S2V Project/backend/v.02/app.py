import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span
from sense2vec import Sense2VecComponent
import phonetics
import enchant


nlp = spacy.load("en_core_web_lg")
s2v = Sense2VecComponent(nlp.vocab).from_disk("C:/fyp/s2v_reddit_2019_lg")
nlp.add_pipe(s2v)
with open("backend/v.02/input_list/input_list.txt","r", encoding="utf-8") as f:
        TEXT = f.read()
doc = nlp(TEXT)

#################################################################
#set theme to be used for similarity comparison (between -2 and 2)
theme = "food"
#set the max value of weighting associated to a perfectly matched rhyming word
rhyme_weighting  = 0.3
#set the value associated with a matching secound letter
second_letter_weight = 0.1
#################################################################

def list_of_files (doc):
    #find all first letters in the doc and create only unique a list of unique text file names to use
    text_files = list()
    for token in doc:
        if token.text.isalpha():
            text_files.append ("text" + (str(token.text[0])).lower() + ".txt")
    return set(text_files)
    
def find_all_begining_with (doc):
    #take your entire vocab and find all words in it that begin with the same letter that each of the text_files (created in list_of_files) end with
    # ..and create each text file and populate it with its own vocab
    with open("backend/v.02/vocab/vocab.txt","r", encoding="utf-8") as f:
        vocab_list=list(f.readlines())
        #vocab_list =["ant", "apple", "arch", "arm", "army", "baby", "bag", "ball", "band", "basin", "basket", "bath", "bed", "bee", "bell", "berry", "bird", "blade", "board", "boat", "bone", "book", "boot", "bottle", "box", "boy", "brain", "brake", "branch", "brick", "bridge", "brush", "bucket", "bulb", "button", "cake", "camera","card", "cart", "carriage", "cat", "chain", "cheese", "chest", "chin", "church", "circle", "clock", "cloud", "coat", "collar", "comb", "cord", "cow", "cup", "curtain", "cushion", "dog", "door", "drain", "drawer", "dress", "drop", "ear", "egg", "engine", "eye", "face", "farm", "feather", "finger", "fish", "flag", "floor", "fly", "foot", "fork", "fowl", "frame", "garden", "girl", "glove", "goat", "gun", "hair", "hammer", "hand", "hat", "head", "heart", "hook", "horn", "horse", "hospital", "house", "island", "jewel", "kettle", "key", "knee", "knife", "knot", "leaf", "leg", "library", "line", "lip", "lock", "map", "match", "monkey", "moon", "mouth", "muscle", "nail", "neck", "needle", "nerve", "net", "nose", "nut", "office", "orange", "oven", "parcel", "pen", "pencil", "picture", "pig", "pin", "pipe", "plane", "plate", "plough", "pocket", "pot", "potato", "prison", "pump", "rail", "rat", "receipt", "ring", "rod", "roof", "root", "sail", "school", "scissors", "screw", "seed", "sheep", "shelf", "ship", "shoe", "skin", "snake", "sock", "spade", "sponge", "spoon", "spring", "square", "stamp", "star", "station", "stem", "stick", "stocking", "stomach", "store", "street", "sun", "table", "tail", "thread", "throat", "thumb", "ticket", "toe", "tongue", "tooth", "town", "train", "tray", "tree", "trousers", "umbrella", "wall", "watch", "wheel", "whip", "whistle", "window", "wing", "wire", "worm"]
        text_files = list_of_files(doc)
        for file in text_files:
            with open(("backend/v.02/textfiles/"+ file) , "w+", encoding="utf-8") as f:
                for string in vocab_list:
                    if string[0].lower() == file[4]:
                        f.write(string + " ")
    return text_files
                        
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
    #this asks for a one word theme from the user and returns the most similar unique word that starts with the same letter for every word in the input list
    #there is currently an unrequired for loop, and it throws warnings about the .simalrity 
    result = list()
    #theme = input("Please enter the one word theme you wish the ouput list to have(for example food or art): ")
    for lst in div_in_list:
        doc = nlp(str(lst))
        docu = nlp(theme)
        main_token = docu[0]
        x = 0
        for in_token in doc:
            word_to_append = in_token
            similarity = 0
            if not in_token.text.isalpha():
                x=x
            elif x == 0:
                x = 1
                with open(("backend/v.02/textfiles/text" + (str(in_token.text[0])).lower() + ".txt") , "r", encoding="utf-8") as f:
                    avail_vocab = nlp(f.read())
                    for token in avail_vocab:
                        if token.i == (len(avail_vocab)-1):
                            if (main_token.similarity(token) + phonetic_similarity(main_token.text, token.text)+ secound_letter_value(main_token.text, token.text)) > similarity and result.count(token.text) == 0:
                                similarity = main_token.similarity(token)
                                word_to_append = token
                                result.append(word_to_append.text)
                            else:
                                result.append(word_to_append.text)
                        elif(main_token.similarity(token) + phonetic_similarity(main_token.text, token.text)+ secound_letter_value(main_token.text, token.text))> similarity and not token.is_punct and result.count(token.text) == 0:
                            similarity = main_token.similarity(token)
                            word_to_append = token
            else:
                with open(("backend/v.02/textfiles/text" + (str(in_token.text[0])).lower() + ".txt") , "r", encoding="utf-8") as f:
                    avail_vocab = nlp(f.read())
                    for token in avail_vocab:
                        if token.i == (len(avail_vocab)-1):
                            if (main_token.similarity(token) + phonetic_similarity(main_token.text, token.text)+ secound_letter_value(main_token.text, token.text)) > similarity and result.count(token.text) == 0:
                                similarity = main_token.similarity(token)
                                word_to_append = token
                                result.append(word_to_append.text)
                            else:
                                result.append(word_to_append.text)
                        elif (main_token.similarity(token) + phonetic_similarity(main_token.text, token.text)+ secound_letter_value(main_token.text, token.text))> similarity and not token.is_punct and result.count(token.text) == 0:
                            similarity = main_token.similarity(token)
                            word_to_append = token
    return result

def secound_letter_value(wordone, wordtwo):
    if (len(wordone) > 1) and (len(wordtwo) > 1):
        if (wordone[1] == wordtwo[1]):
            return second_letter_weight
        else:
            return 0
    else:
        return 0

def phonetic_similarity(wordone, wordtwo):
    #provide a score for the phonetic similarity of two words using double metaphone and damaru levenshtein
    w1 = phonetics.dmetaphone(wordone)
    w2 = phonetics.dmetaphone(wordtwo)
    score = enchant.utils.levenshtein(w1, w2)
    if score == 0:
        return rhyme_weighting
    elif score == 1:
        return (rhyme_weighting/2)
    else:
        return 0


find_all_begining_with (doc)
the_list = find_similar(divide_inputs (doc))
print(the_list)

def only_verbs_please ():
    #find all available verbs in the given vocab
    with open("backend/v.02/vocab/vocab.txt","r", encoding="utf-8") as f:
        vocab = nlp(f.read())
        with open(("backend/v.02/textfiles/verbs") , "w+", encoding="utf-8") as f:
                for token in vocab:
                    if token.pos_ == "VERB":
                        f.write(token.lemma_ + " ")

only_verbs_please()

def fill_story_with_verbs(the_list):
    outlist = list()
    the_list = nlp(str(the_list))
    numword = 0
    for word in the_list:
        similarity = 0
        numword += 1
        if not word.text.isalpha():
            numword = numword
        elif numword == (len(the_list)):
            outlist.append(word.text)
            break
        else:
            outlist.append(word.text)
            with open(("backend/v.02/textfiles/verbs") , "r", encoding="utf-8") as f:
                vocab = nlp(f.read())
                for token in vocab:
                    if token.i == (len(vocab)-1):
                        if (word.similarity(token)) > similarity:
                            similarity = word.similarity(token)
                            word_to_append = token
                            outlist.append(word_to_append.text)
                            print (outlist)
                            break
                        else:
                            outlist.append(word_to_append.text)
                            print (outlist)
                            break
                    elif (word.similarity(token)) > similarity:
                        similarity = word.similarity(token)
                        word_to_append = token
    return outlist

print(fill_story_with_verbs(the_list))
                    


            


             
#freq = doc[0:1]._.s2v_freq
#vector = doc[0:1]._.s2v_vec
#most_similar = doc[0:1]._.s2v_most_similar(10)
#vocab_list = list(nlp.vocab.strings)