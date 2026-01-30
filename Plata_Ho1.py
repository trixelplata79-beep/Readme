def get_average(num_list):
    total = 0
    for trix in num_list:
        total += trix
    return  len(num_list)


def compare_length_and_average(word_len, avg):
    if word_len > avg:
        return "The word length is greater than the average."
    elif word_len < avg:
        return "The word length is less than the average."
    else:
        return "The word length is equal to the average."

word = input("Enter a word: ")
word_length = len(word)

numbers = []
print(f"Enter {word_length} numbers:")

for plata in range(word_length):
    num = float(input(f"Number {plata + 1}: "))
    numbers.append(num)

average = get_average(numbers)
result = compare_length_and_average(word_length, average)

print("\nResults:")
print("List of numbers:", numbers)
print("Length of the word:", word_length)
print("Average of the numbers:", average)
print(result)