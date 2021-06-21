#Interactive quiz
'''
STATEMENT:
We want to create an app that indicates what personality you are when answering 10 questions that deliver a score.
- ask for name
- ask for age
- total 10 questions with 3 options
- add points for each question
- according to total, 1 out of 5 murderous bunny personality

This could surely be done with classes, but how?

Possible classes:
- User
- Age(?)
- Question
- Score
- Profile

'''

ze_score = []

def start():
    name=input('Hello! What is your name? ')

    print('So',name,', let us take a test. Answer the following 10 questions.')
    total_score=0
    questions(total_score)
    final_score()

def score1 (total_score,question):
    if question == 'a':
        total_score += 2
    if question == 'b':
        total_score += 3
    if question == 'c':
        total_score += 4
    else:
        print('That is no valid answer') #this one is always printed - why?
    ze_score.append(total_score)
    print (total_score)

def score2 (total_score,question):
    if question == 'a':
        total_score += 3
    if question == 'b':
        total_score += 2
    if question == 'c':
        total_score += 4
    else:
        print('That is no valid answer')
    ze_score.append(total_score)
    print (total_score)

def score3 (total_score,question):
    if question == 'a':
        total_score += 4
    if question == 'b':
        total_score += 2
    if question == 'c':
        total_score += 1
    else:
        print('That is no valid answer')
    ze_score.append(total_score)
    print (total_score)
    
def questions (total_score):
    question = input('''
    What is your favourite color?
    a) blue
    b) red
    c) purple

    Answer: ''')
    score1(total_score,question)

    question = input('''
    What is your favourite color?
    a) blue
    b) red
    c) purple

    Answer: ''')
    score2(total_score,question)

    question = input('''
    What is your favourite color?
    a) blue
    b) red
    c) purple

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

