# count lenght
# name = input("Enter a name: ")
# count = 0;
# for i in name:
#     count+=1
# print("Total counnt is : ", count)


#  count vowels 
# name = input("Enter a name: ")
# vowels = 0
# consonants = 0

# for ch in name.lower():
#     if ch in "aeiou":
#         vowels += 1
#     elif ch.isalpha():
#         consonants += 1

# print("Total vowels:", vowels)
# print("Total consonants:", consonants)


#  reverse se string
# name = input("Enter Name : ")
# result = ""
# for i in range(len(name) - 1, -1, -1):
#     ch = name[i]
#     result+= ch  
# print(result)

# using slicing
# name = input("Enter names: ")
# result = name[::-1];
# print(result)


# palimdrome check
# name = input("Enter names: ")
# i = 0
# j= len(name)-1;
# is_palimdrome = True
# while i < j:
#     if name[i] == name[j]:
#         i +=1
#         j -=1
#     else:
#         is_palimdrome = False
#         print("this is not palimdrome.")
#         break
# if is_palimdrome :
#     print("this is palimdrome")
    
    
# uppercase to lowecase count
# name = input("Enter a string: ")

# ucount = 0
# lcount = 0

# for char in name:
#     if char.isupper():      
#         ucount += 1
#     elif char.islower():    
#         lcount += 1

# print("Uppercase letters:", ucount)
# print("Lowercase letters:", lcount)


# reverse character
# name = input("Enter a string: ")
# old = input("Enter the character to replace: ")
# new = input("Enter the new character: ")

# result = name.replace(old, new)

# print("Modified string: " ,result)


#  ramove sapce
# name = input("Enter a names: ")
# result = ""
# for i in name:
#     if i != " ":
#         result+=i
# print("Removed space " + result)


#  Frequency of a Character
def freq(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1

    return count


#  First and Last Character
def first_and_last_character(s):
    if len(s) == 0:
        return None

    return s[0], s[-1]


#  ASCII Values
def ascii_values(s):
    for ch in s:
        print(ch, "->", ord(ch))


# 4. Word Count
def word_count(sentence):
    words = sentence.split()
    return len(words)


#  Longest Word
def longest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


#  Shortest Word
def shortest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    return shortest


#  Title Case
def title_case(sentence):
    words = sentence.split()
    result = []

    for word in words:
        result.append(word[0].upper() + word[1:])

    return " ".join(result)


#  Duplicate Characters
def duplicate_characters(s):
    frequency = {}
    duplicates = []

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in frequency:
        if frequency[ch] > 1:
            duplicates.append(ch)

    return duplicates


#  Character Frequency
def character_frequency(s):
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    return frequency


#  Anagram Check
def anagram_check(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    frequency = {}

    for ch in s1:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in s2:
        if ch not in frequency:
            return False

        frequency[ch] -= 1

        if frequency[ch] < 0:
            return False

    return True


#  Remove Duplicate Characters
def remove_duplicates(s):
    seen = set()
    result = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    return "".join(result)


#  Substring Search
def substring_search(main_string, substring):
    return substring in main_string


#  Count Occurrences of a Word
def count_word_occurrences(sentence, target):
    words = sentence.split()
    count = 0

    for word in words:
        if word == target:
            count += 1

    return count


# Password Validator
def password_validator(password):

    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:

        if ch.isupper():
            has_upper = True

        elif ch.islower():
            has_lower = True

        elif ch.isdigit():
            has_digit = True

        else:
            has_special = True

    return has_upper and has_lower and has_digit and has_special


# Run-Length Encoding
def run_length_encoding(s):

    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            count += 1

        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)

    return result


# String Compression
def string_compression(s):

    compressed = run_length_encoding(s)

    if len(compressed) < len(s):
        return compressed

    return s


# Most Frequent Character
def most_frequent_character(s):

    if not s:
        return None

    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    max_char = s[0]

    for ch in frequency:
        if frequency[ch] > frequency[max_char]:
            max_char = ch

    return max_char


#  Second Most Frequent Character
def second_most_frequent_character(s):

    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    if len(frequency) < 2:
        return None

    sorted_chars = sorted(
        frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_chars[1][0]


#  Caesar Cipher
def caesar_cipher(text, shift):

    result = ""

    for ch in text:

        if ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

        elif ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += ch

    return result


#  Email Validator
def email_validator(email):

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    if " " in email:
        return False

    return True


#  Word Frequency Dictionary
def word_frequency_dictionary(paragraph):

    words = paragraph.lower().split()
    frequency = {}

    for word in words:
        # Remove common punctuation
        word = word.strip(".,!?;:")

        frequency[word] = frequency.get(word, 0) + 1

    return frequency


# Sentence Reversal
def sentence_reversal(sentence):

    words = sentence.split()

    words.reverse()

    return " ".join(words)


#  String Rotation
def string_rotation(s1, s2):

    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)