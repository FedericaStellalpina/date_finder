#Interactive quiz
'''
STATEMENT:
We want to create an app that indicates what personality you are when answering 10 questions that deliver a score.
- ask for name
- total 10 questions with 3 options
- add points for each question
- according to total, 1 out of 5 murderous bunny personality

This could surely be done with classes, but how?

Possible classes:
- User
- Question
- Score
- Profile

'''

ze_score = []

def start():
    name=input('Hello! What is your name? ')

    print("So",name,", let's take a test. Answer the following 10 questions,and find your murderous bunny totem.")
    total_score=0
    questions(total_score)
    final_score()

def score1 (total_score,question):
    if question == 'a':
        total_score += 2
    elif question == 'b':
        total_score += 3
    elif question == 'c':
        total_score += 4
    else:
        print('That is no valid answer') 
    ze_score.append(total_score)

def score2 (total_score,question):
    if question == 'a':
        total_score += 3
    elif question == 'b':
        total_score += 2
    elif question == 'c':
        total_score += 4
    else:
        print('That is no valid answer')
    ze_score.append(total_score)

def score3 (total_score,question):
    if question == 'a':
        total_score += 4
    elif question == 'b':
        total_score += 2
    elif question == 'c':
        total_score += 1
    else:
        print('That is no valid answer')
    ze_score.append(total_score)
    
def questions (total_score):
    question = input('''
    What is your favourite color?
    a) blue
    b) red
    c) purple

    Answer: ''')
    score1(total_score,question)

    question = input('''
    What is your favourite animal?
    a) snake
    b) unicorn
    c) narwhale

    Answer: ''')
    score2(total_score,question)

    question = input('''
    What is your favourite dessert?
    a) strawberry cake
    b) tiramisu
    c) apple pie

    Answer: ''')
    score3(total_score,question)

    question = input('''
    What is your favourite book?
    a) 100 yesra of solitude
    b) the master and margherita
    c) the ocean at the end of the lane

    Answer: ''')
    score1(total_score,question)

    question = input('''
    What is your favourite number?
    a) 7
    b) 6
    c) 01

    Answer: ''')
    score2(total_score,question)

    question = input('''
    What is your favourite artist?
    a) Monet
    b) Manet
    c) Gaugin

    Answer: ''')
    score3(total_score,question)

    question = input('''
    What is your favourite sport?
    a) running
    b) diving
    c) squash

    Answer: ''')
    score1(total_score,question)

    question = input('''
    What is your favourite series?
    a) Adventure time
    b) Final Space
    c) Lucifer

    Answer: ''')
    score2(total_score,question)

    question = input('''
    What is your favourite dish?
    a) lasagne
    b) pink soup
    c) steak

    Answer: ''')
    score3(total_score,question)

    question = input('''
    What is your favourite language?
    a) python
    b) ruby
    c) java

    Answer: ''')
    score3(total_score,question)
    
def final_score():
    sum_score = sum(ze_score)
    print('Final score: ',sum_score)
    profile(sum_score)

def profile(sum_score):
    if sum_score <= 8:
        print('Profile1')
    if 9 <= sum_score <= 16:
        print('Profile2')
    if 17 <= sum_score <= 24:
        print('Profile3')
    if 25 <= sum_score <= 32:
        print('Profile4')
    if 33 <= sum_score <= 40:
        print('Profile5')

start()

