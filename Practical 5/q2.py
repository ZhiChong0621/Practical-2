message = input("Enter a string :  ").strip()

words = message.split()

print("\nNO of Words :",len(words))

vowel = "aeiou"

message = message.lower()
print()
for character in vowel:
    print("NO of {}: {:d}".format(character, message.count(character)))

total = 0

for word in words:
    total += len(words)

print("\nAverage: {:.2f}".format(total/len(word)))