size = int(input("Enter the number of student:"))

highest = -1
second_high= -2
total = 0.0

for count in range(1,size+1):
    if count >= 11 and count <= 13:
        suffix = "th"
    else:
        match(count % 10):
            case 1:
                suffix = "st"
            case 2:
                suffix = "nd"
            case 3:
                suffix = "rd"
            case _:
                suffix = "th"

    message = "Enter the score of the {}{} student:".format(str(count),suffix)

    score = float(input (message))
    total += score

    if score > highest:
        second_high = highest
        highest = score

    else:
        if score > second_high:
            second_high = score

print("\nThe highest score        :{:.0f}%".format(highest))
print("\nThe second highest score :{:.2f}%".format(second_high))
print("\nThe average score        :{:.2f}%".format(total/size))