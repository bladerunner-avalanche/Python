numbers = []
for x in range(3):
    numbers.append([int(input(f"Enter number {x+1}: "))])

output_text = "The highest value in the field is: "

# Compare first number with the other two.
if numbers[0] > numbers[1] and numbers[2]:
    print(output_text, numbers[0])

elif numbers[1] > numbers[2]:
    print(output_text, numbers[1])

else:
    print(output_text, numbers[2])

