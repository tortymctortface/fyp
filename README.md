# General project overview

![Landing](https://user-images.githubusercontent.com/48247103/110963710-4e55da80-834a-11eb-9b92-7acee4560760.png)

#### This project uses sense2vec along with other nlp techniques to create an application that is capable of creating a memory palace for a given list of names that a user wishes to remember.

    *Each memory palace output is in the form of an easy to remember list of trigger words that correspond to the user input list of names.
    *This trigger list is designed in a way that each word it contains corresponds directly with one of the words the user wishes to remember.
    *Every trigger list is built using a set of weights defined by the user. These weights each decide how impactful different natural language aspects affect the created trigger list, including phonetics, also considering matching starting letters, and the all important word similarity.
    *There are 3 different versions (detailed below) for the user to choose from, each uses word similarity, based on pre-trained sense2vec vectors, in a different way. V1 also has a different number of weights required than v2 and v3.
    *The user can supply their own vocabulary if they wish to limit the possible words in the output (i.e. a user may wish to build a vr memory palace based off of the output and may want to limit the possible results to a list of objects they can use in their vr palace).
    *After a number of test we have determined that v2 is the solution that builds the stongest most memorable palaces for the majority of users.

# Setup and Installation

This web app was built with Python and Django serving a React/Javascript frontend app. Material-UI was used for styling. 

#### This project requires installation of the following if you wish to run it locally:

[Python 3](https://www.python.org/downloads/)

[Django](https://docs.djangoproject.com/en/3.1/topics/install/)

[spaCy](https://spacy.io/usage/)

[Node.js and npm](https://nodejs.org/)

[React](https://www.liquidweb.com/kb/install-react-js-windows/)

[Material-UI](https://material-ui.com/getting-started/installation/)

[Webpack](https://webpack.js.org/guides/installation/)

You will also need to install the pre-trained vectors (either the 2015 or 2019 set) [here](https://github.com/explosion/sense2vec#pretrained-vectors)

#### Running the cloned project locally

1. After cloning this repo, run `npm install` in your `S2v folder`. This will install all the necessary dependencies.
2. Once you have installed the pre-trained vectors (see above) you will need to copy its filepath and add it to the s2v variable in each of the `v1.py`, `v2.py` and `v3`.py folders file of the version you wish to run
   > `s2v = Sense2VecComponent(nlp.vocab).from_disk("**YOUR_PATH_HERE**")`
3. Open two terminals. In one you will need to start the backend. You can do this from the `MemoryPalace`folder by running `python .\manage.py runserver`.
4. In the second terminal, navigate one level deeper to the `frontend` folder and run `npm run dev`. This will start the React application. 
5. The application will now be running on http://127.0.0.1:8000/


# Versions

#### Note
Only v1, v2 and v3 are in use in the final application
<br>
<br>
<details>

<summary>Screenshot from webapp of version selection page</summary>

![create](https://user-images.githubusercontent.com/48247103/110963852-78a79800-834a-11eb-806e-36f060a5fa27.png)
</details>

<details>
<summary> v0 </summary>

## v01

Version 01 and 02 are not in use in the final project, rather they show the progression from where the project began. 

<br>
Version 01 only provides a console output and is not connected to the React app.

#### How it works

1. Add a list of anything you wish to remeber to the `S2V Project\backend\v.00\input_list\input_list.txt` file - as an example I have added the Nobel Peace Prize Winners from 2000 to 2020. The file should have each item you wish to remember separated by a **,** and if there are multiple parts to an item (for example more than one Nobel Peace Prize Winner in a single year) then each part should be separated with the word **and**
2. Add the vocabulary you wish to be considered for use in the memory map to the `S2V Project\backend\v.00\vocab\vocab.txt` file - remember the bigger the better (I have added the 10,000 most common English words as an example)
3. - When you run the main.py you will create multiple text documents that consist of only words that each start with the same letter as the first letter of every word in the list you wish to remember.
   - This narrows our search for us to then find and return a list of words each starting with the first letter of your input list to remember.
   - The user will then be asked to supply a theme (one word such as food, art, sport or any other non-proper noun)
   - A list will be printed and it will contain a word that starts with every letter in the input list but is also the most similar unique word to fit the theme within the provided vocabulary.

#### Issues

There are multiple obvious issues right now even before rigorous testing

1. Multiple nested for loops, this program could be much more efficient
2. Use of only functions in one main class - again cleaner code would read much easier
3. Now in regards the output list I have some passing observations
   - The input and output are to the terminal
   - The output list does not account for words begining with letters that are not in the vocabulary - x is a big problem as there isn't a single word begining with x in the top 10000 most common english words
   - The program throws a warning about the use of `.similarity`

<br>

## v02

<br>
Version 02 provides two outputs. It will present both your ouput list of words based on the given weightings of each of the three scores, as well as an output of the top three scoring words to a csv file. v02 is also not connected to the React app but it has had many more features added, including a weighted scoring function, along with testing a new way to calaculate word similarity. It also now finds the common most similar verb to connect each neighbouring word in the create list. The errors from handling empty vectors from version 1 are also fixed and the code is much more readable. The theme is no longer a user input, it is set along with the other weights in the code. 

#### How it works

As of now it works almost the same as version 1 (see above for general instructions). The main differences for the end user are :
   1. It outputs a second list which attempts to connect each trigger word with a common verb.
   2. There is now a CSV file output to track individual word scores and this displays the top three possible word matches
   3. Users can edit the three weights in `app.py` at the top of the file : theme, phonetic weight and second letter weight.

</details>

<details>

## v1

<summary> v1 </summary>
   <br>
    Version 1 requires a theme. The list of "trigger words" it produces will all follow as closely as possible to this theme. In this version every "trigger word" will have the same first letter as its corresponding "name to remember". The user can  choose the `theme`, the `phonetic weight` (how important it is for each "trigger word" to rhyme with its "word to remember") and the `secound letter weight` (how important it is for the second letter of each "trigger word" to be the same as the second letter for its corresponding "word to remember").
</details>

<details>

## v2

<summary> v2 </summary>
<br>
   Version 2 removes the requirement of a theme and now allows the user to decide how important it is for each "trigger word" to have the same `starting letter` as its corresponding "name to remember". It still considers the `phonetic` and `second letter weights` the same as Version 1 , but now it also consider `how similar` each word in the "trigger list" is to its predecessor in the "trigger list", therefore allowing the output to find a theme of its own. 

</details>



<details>

## v3


<summary> v3 </summary>
   <br>
   Version 3 is `identical to Version 2` apart from how it calculates each "trigger words" similarity to its predecessor. In this version the weight the user inputs determines `how dissimilar` each word in the "trigger list" is to its predecessor in the "trigger list" to allow for a more unusual, and hopefully more memorable, output.
</details>


# Testing 

To run all backend tests navigate to the `MemoryPalace`folder and run `python -m unittest api/tests/test_all_versions.py`


# Extra Learning

To learn more about the technolgies used in this project here are some useful links:

[spaCy 101](https://course.spacy.io/en) - NLP

[Python 101](https://www.youtube.com/watch?v=rfscVS0vtbw) - For the backend

[Django](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg) - Backend Framework

[JavaScript](https://www.youtube.com/watch?v=W6NZfCO5SIk&t=101s&ab_channel=ProgrammingwithMosh) - For the frontend

[React basics](https://reactjs.org/tutorial/tutorial.html) - Frontend framework
