import time

def print_delay(text):
    time.sleep(1.5)
    print(text)
    return

COUNT = 0
def increment():
    global COUNT
    COUNT = COUNT + 1
    print("Your score is" , COUNT)

def introduction():
    print("Time to test your knowledge on the world with a variety of geography questions.")
    print_delay("This quiz contains 10 fill in and multiple choice questions.")
    print_delay("You will get 3 chances for the fill in questions, and 1 for the multiple choice.")
    user_name = input("Let's start by entering your name: ")
    print("Good luck," , user_name)

def ask_question(qtitle, question, ans):
    print_delay(qtitle)
    guesses = 0
    while True:
        uans = input(question)
        uans = uans.capitalize()
        if uans == ans:
            print(ans, "is correct")
            increment()
            break
        else:
            print(uans, "is incorrect")
            guesses +=1
            if guesses == 3: 
                print("You ran out of tries! The answer is", ans)
                break

def multiple_choice(qtitle, question, correctmsg, falsemsg, ans):
    print(qtitle)
    uans = input(question)  
    uans = uans.capitalize()
    while uans != "A" and uans != "B" and uans != "C" and uans != "D":
        print("You can only choose A, B, C, or D. Please try again")
        uans = input(question)
    if uans == ans:
        print(correctmsg)
        increment()
    else:
        print(falsemsg)

def end_message():
    print("Thanks for playing. Your final score is", COUNT)

def main():
    introduction()
    ask_question("Question 1", "Which country has the largest coastline: ", "Canada")
    ask_question("Question 2", "Which country in the world has the least population density: ", "Mongolia")
    ask_question("Question 3", "What is the name of largest ocean in the world: ", "Pacific")
    ask_question("Question 4", "Which country formally ruled Iceland: ", "Denmark")
    ask_question("Question 5", "What autonomous country is the world's largest island: ", "Greenland")
    print_delay("\nNow let's move into multiple choice. You will have one try")

    multiple_choice("\nQuestion 6",
    "Which country has the most time zones: \n(A)China\n(B)US\n(C)Canada\n(D)France\n", 
    "Correct! France has the most time zones due to its various territories worldwide.",
    "Incorrect. France has the most time zones due to its various territories worldwide.", 
    "D")
    multiple_choice("\nQuestion 7", 
    "\nHow many countries are there in Africa?\n(A) 62\n(B) 35\n(C) 45\n(D) 54\n", 
    "Correct! Africa has 54 countries with Nigeria having the highest population!", 
    "Incorrect. Africa has 54 countries with Nigeria having the highest population!", 
    "D")
    multiple_choice("\nQuestion 8", "What is the capital of Mozambique?\n(A) Harare\n(B) Maputo\n(C) Niamey\n(D) Bamako\n", 
    "Correct! Did you know Mozambique has the only national flag with a modern weapon on it?",
    "Incorrect. The capital of Mozambique is Maputo. Did you know Mozambique has the only national flag with a modern weapon on it!",
    "B")
    multiple_choice("\nQuestion 9", 
    "Which country has the most volcanos?\n(A) Indonesia\n(B) United States\n(C) Japan\n(D) Philippines\n", 
    "Correct! The USA has the most volcanos, with Alaska having the largest amount of active volcanos",
    "Incorrect. The United States has the most volcanos, with Alaska having the largest amount of active volcanos.",
    "B")
    multiple_choice("\nQuestion 10", 
    "Which country has the most islands(inhabited and unihabitated combined)?\n(A) Japan\n(B) Canada\n(C) Indonesia\n(D) Sweden\n",
    "Correct! Did you know Sweden has 267,570 islands, with Norway in second place.",
    "Incorrect. The correct answer is Sweden with 267,570 islands, with Norway in second place.",
    "D")

if __name__ == "__main__":
    main()
    end_message()
