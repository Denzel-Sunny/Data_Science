print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

def count_vowels(string):
    # Define a dictionary to store the count of each vowel
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convert the input string to lowercase to handle both uppercase and lowercase vowels
    string = string.lower()

    # Iterate through the string and update the vowel count
    for char in string:
        if char in vowel_count:
            vowel_count[char] += 1

    return vowel_count

# Example usage:

input_string = input("Enter a string: ")
result = count_vowels(input_string)

    # Print the count of each vowel
for vowel, count in result.items():
    print(f'{vowel}: {count}')
