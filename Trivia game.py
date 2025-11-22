import random

print("\n\nWelcome to the Trivia Game!\n")
questions = ['\nWhat is the capital of France?',
             '\nWhat is 2 + 2?',
             '\nWhat is the largest planet in our solar system?',
             '\nWhat is the fastest land animal?',
             '\nWhich ocean is the largest? (Full name)',
             '\nWhat is the longest river in the world? (Full name)',
             '\nWhat is the hardest natural substance on Earth?',
             '\nWho was the first person to walk on the moon?',
             '\nWhat is the largest country in the world by area?'
            ]

fbquestions = ['\nHow many ballondors has Lionel Messi won?',
             '\nWho is the player with the most goals? (Full name)',
             '\nHow many Champions league has Real Madrid won?',
             '\nWhich country won the first FIFA World Cup?',
             '\nWho is the all-time top scorer in the UEFA Champions League? (Full name)',
             '\nWhich country has won the most FIFA World Cups?',
             '\nWhich English club has won the most Premier League titles?',
             '\nWho is the only goalkeeper to win the Ballon dOr (Full name)',
             '\nWho is the all-time top scorer for the England national team? (Full name)'
            ]

C1questions = []
C2questions = []
C3questions = []

C1answers = []
C2answers = []
C3answers = []
answers = ['Paris', '4', 'Jupiter','Cheetah','Pacific Ocean','Nile River','Diamond','Neil Armstrong','Russia']
fbanswers = ['7', 'Cristiano Ronaldo', '15', 'Uruguay', 'Cristiano Ronaldo', 'Brazil', 'Manchester United', 'Lev Yashin', 'Harry Kane']
Points = 0
QT = ''


while True:
    Action = input('\nWhat do you want to do?\n1. Play Trivia Game\n2. Add questions\nChoose 1 or 2: ')

    if Action == '1':

        if any(len(lst) > 0 for lst in [C1questions, C2questions, C3questions]):
            QT = input("\nChoose your trivia category - General (G) or Football (F) or Custom (C): ").upper()

        else:
            QT = input("\nChoose your trivia category - General (G) or Football (F): ").upper()

        
        if QT == 'C':
            Ctype = input("\nChoose your custom trivia set - Set 1 (1) or Set 2 (2) or Set 3 (3): ")
            
            if Ctype == '1':
                answers = C1answers
                questions = C1questions

                while len(questions) > 0:

                    CQ= random.choice(questions)
                    ansP = answers[questions.index(CQ)]
                    print("\n> "+ CQ)
                    Answer = input("Your answer: ").title()
                    if Answer == ansP:
                        print("Correct!\n")
                        Points += 1
                    else:
                        print("Incorrect! The correct answer is:", ansP, "\n")
                    questions.remove(CQ)
                    answers.remove(ansP)
                    print("Current Points:", Points)


            elif Ctype == '2':
                answers = C2answers
                questions = C2questions
                while len(questions) > 0:
                    CQ= random.choice(questions)
                    ansP = answers[questions.index(CQ)]
                    print("\n> "+ CQ)
                    Answer = input("Your answer: ").title()
                    if Answer == ansP:
                        print("Correct!\n")
                        Points += 1
                    else:
                        print("Incorrect! The correct answer is:", ansP, "\n")
                    questions.remove(CQ)
                    answers.remove(ansP)
                    print("Current Points:", Points)

            elif Ctype == '3':
                answers = C3answers
                questions = C3questions
                while len(questions) > 0:
                    CQ= random.choice(questions)
                    ansP = answers[questions.index(CQ)]
                    print("\n> "+ CQ)
                    Answer = input("Your answer: ").title()
                    if Answer == ansP:
                        print("Correct!\n")
                        Points += 1
                    else:
                        print("Incorrect! The correct answer is:", ansP, "\n")
                    questions.remove(CQ)
                    answers.remove(ansP)
                    print("Current Points:", Points)

        elif QT == 'F':
            answers = fbanswers
            questions = fbquestions
            
            while len(questions) > 0:
                CQ= random.choice(questions)
                ansP = answers[questions.index(CQ)]
                print(CQ)
                Answer = input("Your answer: ").title()
                if Answer == ansP:
                    print("Correct!\n")
                    Points += 1
                else:
                    print("Incorrect! The correct answer is:", ansP, "\n")
                questions.remove(CQ)
                answers.remove(ansP)
                print("Current Points:", Points)
            
        else:
            while len(questions) > 0:
                CQ= random.choice(questions)
                ansP = answers[questions.index(CQ)]
                print(CQ)
                Answer = input("Your answer: ").title()
                if Answer == ansP:
                    print("Correct!\n")
                    Points += 1
                else:
                    print("Incorrect! The correct answer is:", ansP, "\n")
                questions.remove(CQ)
                answers.remove(ansP)

                print("Current Points:", Points)


    if Action == '2':
        QIType = input("\nChoose your trivia category to add question - General (G) or Football (F) or Custom (C): ").upper()

        if QIType == 'F':
            newQ = input("\nEnter your question: ")
            newA = input("Enter the answer: ").title()
            fbquestions.append(newQ)
            fbanswers.append(newA)

        elif QIType == 'G':
            newQ = input("\nEnter your question: ")
            newA = input("Enter the answer: ").title()
            questions.append(newQ)
            answers.append(newA)

        elif QIType == 'C':
            Cinsert = input("\nChoose your custom trivia set to add question - Set 1 (1) or Set 2 (2) or Set 3 (3): ")

            if Cinsert == '1':
                newQ = input("\nEnter your question: ")
                newA = input("Enter the answer: ").title()
                C1questions.append(newQ)
                C1answers.append(newA)

            elif Cinsert == '2':
                newQ = input("\nEnter your question: ")
                newA = input("Enter the answer: ").title()
                C2questions.append(newQ)
                C2answers.append(newA)

            elif Cinsert == '3':
                newQ = input("\nEnter your question: ")
                newA = input("Enter the answer: ").title()
                C3questions.append(newQ)
                C3answers.append(newA)
        