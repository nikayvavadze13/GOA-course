letter = ["G"]
while True:
    user_input = input("enter a word that starts with G")
    if user_input[0] in letter:
        print("your word is correct")
    else:
        print("incorrect!")
        break