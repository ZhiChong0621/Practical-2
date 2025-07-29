while True:
    score = input("Enter a score or 'Q'/'q' to exit: ")

    if score == "Q" or score =="q":
        break
    
    elif not score.replace(".","").isnumeric():
        print("Only Positive Number is Allowed\n")

    else:
        score = float(score)
        if not(score >= 0 and score  <= 100):
            print("Only 0 ≤ number ≤ 100 inclusive are allowed!\n")
        else:
            if score >=90 and score <= 100:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"

            match grade:
             case "A" | "F" :
                print("You got an", grade, "for the test\n")
             case "B" | "C" | "D":
                print("You got an", grade, "for the test\n")


print("Thank You")
    