from time import sleep
from os import system, name

choices = {
    'TShirtShorts': 0,
    'TShirtPants': 0,
    'HoodiePants': 0,
    'TopShorts': 0,
    'DressCardigan': 0
}

def pLine(string, waitTime = 0.05):
    for i in string:
        print(i, end='', flush = True)
        sleep(waitTime)
    print()
    
def ask(num, question, choicesPossible):
    pLine(f'Question {str(num)}:')
    pLine(question)
    
    for i in range(len(choicesPossible)):
        pLine(f'{i + 1}. {choicesPossible[i]}')

def getAnswer(maxChoice):
    while True:
        try:
            answer = int(input(f'Choice (1-{maxChoice}): '))
        except ValueError:
            pLine('Answer must be an integer!')
            continue
        
        if answer > maxChoice:
            pLine(f'Answer cannot be more than {maxChoice}')
            continue
        elif answer < 1:
            pLine('Answer cannot be less than 1!')
            continue
    
        return answer
    
def addPoints(threePoints, twoPoints, onePoint):
    choices[threePoints] += 3
    choices[twoPoints] += 2
    choices[onePoint] += 1
    
def recommendedItem():
    item = max(choices, key = choices.get)
    pLine('Your recommended item is:')
    
    if item == 'TShirtShorts':
            pLine('A T-Shirt and shorts')
    elif item == 'TShirtPants':
        pLine('A T-Shirt and pants')
    elif item == 'HoodiePants':
        pLine('A hoodie with pants')
    elif item == 'TopShorts':
        pLine('A top with shorts')
    else:
        pLine('A dress and cardgian')

def clear():
    # Clear screen
    if name == 'nt':
        # for windows
        system('cls')
    else:
        # for mac and linux
        system('clear')
    
# Survey

# Beginning
clear()

pLine('Welcome to the outfit prediction survey!')
pLine('You will be asked 5 questions and')
pLine('then be asked to choose between the')
pLine('options. Type in your answer, and at')
pLine('the end a recomendation on what')
pLine('outfit you should wear will be given.')
sleep(0.1)

start = input('Press Enter to start: ')

clear()

# Questions

# Question 1
ask(1, 'Do you dress Masculine or Feminine?', ['Masculine', 'Feminine'])

ans = getAnswer(2)

if ans == 1:
    addPoints('HoodiePants', 'TShirtShorts', 'TShirtPants')
else:
    addPoints('DressCardigan', 'TShirtPants', 'HoodiePants')
    choices['TopShorts'] += 2

print()
sleep(0.5)

#Question 2

ask(2, 'What is your favorite season?', ['Fall', 'Winter', 'Spring', 'Summer'])

ans = getAnswer(4)

if ans == 1:
    addPoints('TShirtPants', 'HoodiePants', 'TShirtShorts')
elif ans == 2:
    addPoints('HoodiePants', 'TShirtShorts', 'DressCardigan')
elif ans == 3:
    choices['TShirtPants'] += 3
    choices['HoodiePants'] += 3
else:
    addPoints('HoodiePants', 'TShirtPants', 'DressCardigan')
    choices['TopShorts'] += 1

print()
sleep(0.5)

# Question 3

ask(3, 'Would you rather be stuck in the Sahara or Antarctica?', ['Sahara', 'Antarctica'])

ans = getAnswer(2)

if ans == 1:
    addPoints('HoodiePants', 'TShirtPants', 'DressCardigan')
    choices['TopShorts'] += 2
else:
    addPoints('HoodiePants', 'TShirtPants', 'DressCardigan')
    choices['TShirtShorts'] += 2

print()    
sleep(0.5)

# Question 4

ask(4, 'On a scale of 1-3, rate how much do you prioritize comfort in your outfit:', ['','',''])

ans = getAnswer(3)

if ans == 2:
    addPoints('HoodiePants', 'TShirtPants', 'DressCardigan')
if ans == 3:
    addPoints('HoodiePants', 'TShirtPants', 'TopShorts')
    choices['TShirtShorts'] += 2
    choices['DressCardigan'] += 1

print()    
sleep(0.5)

# Question 5

ask(5, 'On a scale of 1-3, rate how much effort you want to put in your outfit:', ['', '', ''])

ans = getAnswer(3)

if ans == 1:
    addPoints('HoodiePants', 'TShirtPants', 'TShirtShorts')
    choices['TShirtShorts'] += 1
elif ans == 2:
    addPoints('HoodiePants', 'TShirtPants', 'TShirtShorts')
elif ans == 3:
    addPoints('HoodiePants', 'DressCardigan', 'TShirtShorts')
    choices['TopShorts'] += 1

print()    
sleep(0.5)

recommendedItem()

recommendedRight = input('Was this the recommendation you wanted?: ')
print()

if not recommendedRight.lower() == 'yes':
    pLine('The five choices were:')
    pLine(f'{choices.keys()}')
    
    wanted = input('Which one would you have wanted?: ')

print()
pLine('Thank you for your time!')
print()
pLine('These were your results:')
print(choices)
print()
end = input('Press Enter to quit: ')