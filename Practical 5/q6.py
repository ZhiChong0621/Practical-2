while True:
    condition1 = False
    condition2 = False
    condition3 = False

    pw1 = input("Enter a password: ")

    if(len(pw1)>= 8 and len(pw1) <= 12):
        condition1 = True

    else:
        (print("The password must be at least 8 character and most 12 character"))

    non_alnum = [character for character in pw1 if not character.isalnum]

    if len(non_alnum) == 0:
        condition2 = True
    else:
        (print("The password must consist only letters and digits"))

    digit = 0
    letter = 0
    for character in pw1:
        if character.isdigit():
            digit += 1
        if character.isalpha():
            letter += 1
    if digit >0 and letter > 0:
        condition3 = True
    else:
        print("The password must contain at least one letter and one digit.")

    if condition1 and condition2 and condition3:
        pw2 = input("Enter the password again :")

        if pw1 == pw2:
            print("Congratulations! Your password is created successfully!")
        else:
            print("The two passwords do not match each other...")
            break

else:
    print(

    )