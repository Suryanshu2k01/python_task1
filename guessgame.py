#GuessGame 

import random
def code_gen():
    code = random.randint(1000, 9999)
    return code

def user_input():
    inputcode = int(input("Enter your 4-digit code:"))
    return inputcode

def guessgame():
    a = str(code_gen())
    i = 0
    
    while(i < 10):
        result = ""
        b = str(user_input())
        if len(b) != 4:
            print("Enter 4-digit number only!")
            continue;
        if b == a:
            print("You have guessed it right!!", a)
            break;

        for element in b:
            if element in a:
                if b.index(element) == a.index(element):
                    result += "R"
                else:
                    result += "A"
            else:
                result += "W"

        print(result)
        i += 1
    else:
        print("You are out of choices.", a)

guessgame()        

      

