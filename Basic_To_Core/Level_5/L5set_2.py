# Find the first occurrence of a substring in a string.
text = "Python Programming is professional"
x = "on"
print(f"'{x}' first appeared on index: ",text.find(x))

# Count how many times a specific letter appears in a string.
print(text.lower().count("p"))

# Split a sentence into a list of words.
listOfWords = text.split()
print(listOfWords)

# Join a list of words into a single string separated by commas.
joinListWords = ", ".join(listOfWords)
print(joinListWords)



# Remove leading and trailing whitespaces from a string.
messy = "  Hello "
print(messy)
print(messy.strip())

# Center a string with asterisks (`*`) padding to make it 20 
# characters wide.
string = "Willow the bot"
print(string.center(20, "*"))   
                    #add aestrik before and after and 
                    # make it 20 characters wide


# Check if a string contains only digits.
num = "12345"
print(num.isdigit())

# Check if a string contains only alphabetic characters.
alphabet = "willaw"
print(alphabet.isalpha())


# Swap the case of all letters in a string.(up to low and vice-versa)
text = "Willow The novice"
print(text.swapcase())


#  Replace vowels in a string with a special character (`*`).
input_string = "camouflage"
vowels = "aeiou"
replaced = "".join(["*" if eachChar in vowels else eachChar for eachChar in input_string])
print(replaced)


