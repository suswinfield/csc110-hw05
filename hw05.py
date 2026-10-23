"""
Name: Susannah Winfield
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """  recieves user input A B or C
Recieves asks for a single uppercase letter,
if that letter is not A B or C then it asks again.
once input is valid it will return the input in the variable input_letter

Example:
 
Give a single uppercase letter: 3
Error: You provided the wrong character.
Give a single uppercase letter: rt
Error: it needs to be a single character.
Give a single uppercase letter: B

returns: input_letter
"""
    global input_letter
    input_letter = input("Give a single uppercase letter: ")
    #while loop will repeat until user_input = A, B, or C
    while True:
        #repeats if input is not one character
        if len(input_letter) != 1:
            print("Error: it needs to be a single character.")
            input_letter = input("Give a single uppercase letter: ")
            continue
        #repeats if input is not A B or C
        if input_letter not in ["A","B","C"]:
            print("Error: You provided the wrong character.")
            input_letter = input("Give a single uppercase letter: ")
            continue
        #breaks out of the loop if input is A,B, or C
        if input_letter in ["A","B","C"]:
            break
    return input_letter

def get_digit():
    """ recieves a user inputed number between 1 and 3
asks for a single number character,
if that character is 1,2, or 3 it will return, otherwise it prints an error.

Example output:

Give an single number character: g
Error: your input should be only digits.
Give an single number character: 5
Error: a single digit needs to be in [1,3].
Give an single number character: 2

returns: input_number
"""
    global input_number
    input_number = input("Give an single number character: ")
    #loop will repeat unit input_number is a digit between 1 and 3
    while True:
        #repeats loop if input is not a digit
        if input_number.isdigit() == False :
            print("Error: your input should be only digits.")
            input_number = input("Give an single number character: ")
            continue
        #repeats loop if input is not between 1 and 3
        if input_number not in ["1","2","3"]:
            print("Error: a single digit needs to be in [1,3].")
            input_number = input("Give an single number character: ")
            continue
        #breaks the loop when input is a digit between 1 and 3
        if input_number in ["1","2","3"]:
            break    
    return input_number


def check_pattern(letter, digit, lst):
    """ Checking for <letter, digit> pattern in the elements of a given list
takes inputs for letter, digit , and lst
nested for loop creates a new temporary list without @ symbols by running through each letter,
checking if it is an @, if not it adds those letters to a word that gets added to the temporary list.
if the pattern is found in the temporary list, the corresponding element in the original list will be printed.

example output:

letter = A
digit = 1

Strings with the pattern:
AA@1


"""
    print("Strings with the pattern:")
    lst_temp = []
    for elem in lst:
        word = ""
        for i in elem :
            if i != "@" :
               word = word + i
        lst_temp.append(word)
    for elem,i in zip(lst_temp,lst):
        if letter + digit in elem:
            print(f"{i}",end =" ")
    print()

    # remove the default pass and add your code
    return


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""
    global st_list
    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    while True:
        get_letter()
        get_digit()
        check_pattern(input_letter,input_number,st_list)
        ask_repeat = input("Try Again? (y/n): ")
        if ask_repeat != "y" :
            break
    
    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()