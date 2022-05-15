import time

def print_delay(text):
    time.sleep(1)
    print(text)
    return

def validate_input(question):
    ans = input(question)
    ans = ans.capitalize()
    while ans != "A" and ans != "B" and ans != "C" and ans != "D":
        print("You can only choose A, B, C, or D. Please try again")
        ans = input(question)
    return ans

COUNT = 0
def increment():
    global COUNT
    COUNT = COUNT + 1
    print("Your score is" , COUNT)

def introduction():
    print("Time to test your knowledge on the world with a variety of geography questions.")
    print_delay("This quiz contains five fill in questions.")
    print_delay("You will get 3 chances for the fill in questions.")
    user_name = input("Let's start by entering your name: ")
    print("Hi" , user_name, "Good luck!")

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
            print(ans, "is incorrect")
            guesses +=1
            if guesses == 3: 
                print("You ran out of tries! The answer is", ans)
                break

def end_message():
    print("Thanks for playing. Your final score is", COUNT)

def main():
    introduction()
    ask_question("Question 1", "Which country has the largest coastline: ", "Canada")
    ask_question("Question 2", "Which country in the world has the least population density: ", "Mongolia")
    ask_question("Question 3", "What is the smallest country in the world: ", "Vatican City")
    ask_question("Question 4", "Which country formally ruled Iceland: ", "Denmark")
    ask_question("Question 5", "What autonomous country is the world's largest island: ", "Greenland")
    end_message()

if __name__ == "__main__":
    main()