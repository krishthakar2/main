import time


# This function when it is called will create a new quiz game.
def new_game():
    answer_tried = []
    correct_guesses = 0
    number_questions = 1  # represents the first questions

    for key in questions:  # loops the questions
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  # seperates the questions with a line
        print(key)  # prints the questions
        for i in answers[number_questions - 1]:  # for loop prints and lists the questions,-1 so receive 0 as index
            print(i)
        answer = input(" Please Enter (A,  B, C, or D): ")  # lets the user what to enter
        if answer == "":  # if the user enters nothing and just enters the code prints Please Enter A,  B, C, or D next time
            print("Please Enter A,  B, C, or D next time")
        print("")  # prints blank like to make it look nicer
        answer = answer.upper()  # if the user rights the letter in lowercase this line makes the letter into uppercase
        answer_tried.append(answer)

        correct_guesses += check_answer(questions.get(key),
                                        answer)  # receive the answer of the questions as well as the answer written by the user
        number_questions += 1


score = 0


# This function will allow the user to replay the quiz
def play_again():  # allows the user to play the game again and try get higher score

    """
    Asks the user if they want to play again.
    :return:
    """
    while True:
        quiz_again = str(input(
            "Would you like to play again? (yes/no)\n").lower().strip())  # asks the user if they would like to play again
        if quiz_again == "no":  # is user says no it prints thanks for playing
            print("")
            return False  # if the return value is false/no it will block the run
        elif quiz_again == "yes":  # is the user the  prints yes it replays the quiz
            print("")
            return True  # if the return value is true/yes it will continue the run
        else:
            print(
                "I'm sorry, I didn't understand that. Please try again.")  # is the user writes anything but a yes or no the quiz prints this and asks the user to re enter a answer (yes/no)


# checks the answer entered by the user with the correct answer and gives the points and prints the statement
# This function will compare the answer tried by the user with the real answer which is then passed.
def check_answer(answer,
                 answer_tried):
    global score

    if answer == answer_tried:  # checks the answer written by user but the real answer
        print("That's correct! Good job")  # prints this statement if the answer is correct
        score = score + 1  # when the answer is correct user gets one point
        print("Your score is:", score)
        return 1  # gives player one point per correct question
    else:
        print("Incorrect! Better luck next question")
        print("Your score is:", score)
        return 0  # gives player no points of answer is wrong

    #  introduction and start of the questions


# This function will ask for their name and also print what the code will be able then the questions will be played.
def main(name):
    print("Welcome, ")  # prints a welcome statement when the user starts the game


# ask for name and make sure it is not left blank
name = ""
while name == "":
    name = input("Please enter your name: ")  # asks for the name

    print("Hi", name)  # says hi to the user with the name provided above
    # give an error message if the name is left blank
    if name == "":  # if the name is left empty it prints the statement
        print("Please enter your name - you cannot leave it blank")
        print("")
time.sleep(2)  # adds a 2 second stop before the next line is printed
print("This is a Poverty awareness quiz where you will be able to answer multiple questions")
print("Hopefully you can learn a bit about poverty around the world ")
print("Good luck and lets start")

time.sleep(5)  # adds a 5 second stop before the next line is printed

time.sleep(1)  # adds a 1 second stop before the next line is printed
#
questions = {"Q1. Which country has the highest poverty rate?": 'A',
             # key has a question which is being asked with the associated value
             "Q2. Which country has the lowest poverty rate?": 'D',
             "Q3. Which racial demographic has the highest likelihood of living in poverty?": 'D',
             "Q4. What age group has the highest poverty rate in the US?": 'B',
             "Q5. Out of 100 people in a village how many people wouldn't have clean water": 'C',
             "Q6. Out of 100 people in a village how many people would live on 2$ or less?": 'D',
             "Q7. What is one of the biggest causes of poverty? ": 'A',
             }
# 2d list to hold all the possible questions
answers = [["A. South Sudan", "B. India ", "C. London  ", "D. United States"],
           ["A. China", "B. India", "C. New Zealand", "D. Iceland"],
           ["A. White", "B. African American", "C. Indian", "D. Native American"],
           ["A. Adults", "B. Children", "C. Elderly", "D. Infant"],
           ["A. 33", "B. 16", "C. 18", "D. 0"],
           ["A. 23", "B. 15", "C. 88", "D. 53"],
           ["A. Lack of jobs", "B. Climate Change", "C. Over population", "D. Inflation "], ]

time.sleep(2)  # adds a 2 second stop before the next line is printed

new_game()  # calls the new game function

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  # prints a line to seperate the sections

print("Hi", name, "Your final score is: ", score,
      "Out of 7")  # prints your name and what your final score is out of the 7 questions

time.sleep(1)  # adds a 1 second stop before the next line is printed
print("If you would like to better your score, give the quiz another go.")

while play_again():  # this will return either true or false
    new_game()  # starts the new game
    exit()

    time.sleep(1)  # adds a 1 second stop before the next line is printed
print("Hope you enjoyed and now know a little bit more about poverty then before")
print("""
        ################################
         Thank you for using my program
        ################################
        """)
print(
    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

