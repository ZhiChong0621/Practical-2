score = []

while True:
    number = input("Enter the number of students: ")

    if number.isdigit():
        number = int(number)
        if number == 0:
            print("Only Positive Integer is Allowed!\n")
            continue
        else:
            count = 1
            scores = []
            print("\n Enter the {:s}".format("student scores"if number >1 else "student's sroce"))
            while count <= number:
                match(count %10):
                    case 1:
                        suffix = "st"
                    case 2:
                        suffix = "nd"
                    case 3:
                        suffix = "rd"
                    case _:
                        suffix = "th"
                message = "{:>3s}{} student: ".format(str(count),suffix)

                try:
                    score = float(input(message))
                    if score<0:
                        print("Onlu zero or positive value is allowed!")
                    else:
                        scores.append(score)
                        count +=1
                except ValueError:
                    print("Onlly number is Allowed")
            if count > number:
                break
    else:
        print("Only Positive Integer is Allowed!\n")

scores.sort(reverse = True)

print("\n The highest score        :{:.0f}%".format(scores[0]))
print("\n The second highest score :{:.2f}%".format(scores[1]))
print("\n The average score        :{:.2f}%".format(sum(scores)/len(scores)))