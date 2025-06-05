# Reverse a string without using slicing.
def reverseString(s):
    result = ""
    for eachChar in s:
        result = eachChar + result
    return result
print(reverseString("Heellow"))

# # Slicing method to reverse a string
# txt = "Hello"
# print(txt[::-1])


# Check if a given string is a palindrome.
                    # if a string = reverse of that string
def isPalindrome(string):
    return string == string[::-1]

print(isPalindrome("madam"))
print(isPalindrome("hello"))


# Remove all vowels from a string.
def removeVowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)
print(removeVowels("Beauty"))

# Alternate approach
s = "Willlaw"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for eachChar in s:
    if eachChar not in vowels:
        result = result + eachChar
print(result)


# Find the most frequent character in a string.
def mostFreq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get)

print(mostFreq("Success"))


# Remove duplicate characters from a string.
def removeDuplicates(s):
    result = ""
    seen = set()
    for eachChar in s:
        if eachChar not in seen:
            seen.add(eachChar)
            result += eachChar
    return result
print(removeDuplicates("bananna"))


# Extract digits separately from a string that contains letters and digits.
def extract_digits(s):
    return [eachChar for eachChar in s if eachChar.isdigit()]
print(extract_digits("a1b2c3"))


# Find all words that start with a capital letter in a sentence.
def wordcapt(s):
    words = s.split()  #separate each word into a new string
    return [eachWord for eachWord in words if eachWord[0].upper()]

print(wordcapt("Qillwo thw novicela"))


# Create an acronym from a sentence (e.g., “World Health Organization” → “WHO”).



# Count the number of words in a sentence.
def countwordsNumber(s):
    a = s.split() #separate each word in to a new string
    b = len(a)
    return b
print(countwordsNumber("Hello wordl"))

# Short approach
# def count_words(sentence):
#     return len(sentence.split())
# print(count_words("Hello World"))



#  Find the longest word in a sentence.
def longestWord(s):
    words = s.split()
    return(max(words, key=len))
print(longestWord("I love competitive programming"))