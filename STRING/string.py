# count length

# name = input("Enter a name: ")
# count = 0

# for i in name:
#     count += 1

# print("Total count is:", count)


# count vowels

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


# reverse string

# name = input("Enter Name: ")
# result = ""

# for i in range(len(name) - 1, -1, -1):
#     result += name[i]

# print(result)


# using slicing

# name = input("Enter name: ")
# result = name[::-1]
# print(result)


# palindrome check

# name = input("Enter name: ")

# i = 0
# j = len(name) - 1
# is_palindrome = True

# while i < j:
#     if name[i] == name[j]:
#         i += 1
#         j -= 1
#     else:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("This is palindrome")
# else:
#     print("This is not palindrome")


# uppercase and lowercase count

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


# replace character

# name = input("Enter a string: ")
# old = input("Enter the character to replace: ")
# new = input("Enter the new character: ")

# result = name.replace(old, new)

# print("Modified string:", result)


# remove space

# name = input("Enter a name: ")
# result = ""

# for ch in name:
#     if ch != " ":
#         result += ch

# print("Removed space:", result)


# frequency of a character

# name = input("Enter a string: ")
# ch = input("Enter character: ")

# count = 0

# for c in name:
#     if c == ch:
#         count += 1

# print("Frequency:", count)


# first and last character

# name = input("Enter a string: ")

# if len(name) == 0:
#     print("String is empty")
# else:
#     print("First character:", name[0])
#     print("Last character:", name[-1])


# ASCII values

# name = input("Enter a string: ")

# for ch in name:
#     print(ch, "->", ord(ch))


# word count

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# print("Total words:", len(words))


# longest word

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# if not words:
#     print("No words")
# else:
#     longest = words[0]

#     for word in words:
#         if len(word) > len(longest):
#             longest = word

#     print("Longest word:", longest)


# shortest word

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# if not words:
#     print("No words")
# else:
#     shortest = words[0]

#     for word in words:
#         if len(word) < len(shortest):
#             shortest = word

#     print("Shortest word:", shortest)


# title case

# sentence = input("Enter a sentence: ")

# words = sentence.split()
# result = []

# for word in words:
#     result.append(word[0].upper() + word[1:])

# print("Title case:", " ".join(result))


# duplicate characters

# name = input("Enter a string: ")

# frequency = {}
# duplicates = []

# for ch in name:
#     frequency[ch] = frequency.get(ch, 0) + 1

# for ch in frequency:
#     if frequency[ch] > 1:
#         duplicates.append(ch)

# print("Duplicate characters:", duplicates)


# character frequency

# name = input("Enter a string: ")

# frequency = {}

# for ch in name:
#     frequency[ch] = frequency.get(ch, 0) + 1

# for ch in frequency:
#     print(ch, "->", frequency[ch])


# anagram check

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# s1 = s1.replace(" ", "").lower()
# s2 = s2.replace(" ", "").lower()

# if len(s1) != len(s2):
#     print("Not Anagram")
# else:
#     frequency = {}

#     for ch in s1:
#         frequency[ch] = frequency.get(ch, 0) + 1

#     is_anagram = True

#     for ch in s2:
#         if ch not in frequency:
#             is_anagram = False
#             break

#         frequency[ch] -= 1

#         if frequency[ch] < 0:
#             is_anagram = False
#             break

#     if is_anagram:
#         print("Anagram")
#     else:
#         print("Not Anagram")


# remove duplicate characters

# name = input("Enter a string: ")

# seen = set()
# result = ""

# for ch in name:
#     if ch not in seen:
#         seen.add(ch)
#         result += ch

# print("After removing duplicates:", result)


# substring search

# main_string = input("Enter main string: ")
# substring = input("Enter substring: ")

# if substring in main_string:
#     print("Substring exists")
# else:
#     print("Substring does not exist")


# count occurrences of a word

# sentence = input("Enter a sentence: ")
# target = input("Enter word to search: ")

# words = sentence.split()
# count = 0

# for word in words:
#     if word == target:
#         count += 1

# print("Word occurrences:", count)


# password validator

# password = input("Enter password: ")

# if len(password) < 8:
#     print("Invalid password")
# else:
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False

#     for ch in password:
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_digit = True
#         else:
#             has_special = True

#     if has_upper and has_lower and has_digit and has_special:
#         print("Valid password")
#     else:
#         print("Invalid password")


# run length encoding

# name = input("Enter a string: ")

# if len(name) == 0:
#     print("Empty string")
# else:
#     result = ""
#     count = 1

#     for i in range(1, len(name)):
#         if name[i] == name[i - 1]:
#             count += 1
#         else:
#             result += name[i - 1] + str(count)
#             count = 1

#     result += name[-1] + str(count)

#     print("Compressed string:", result)


# string compression

# name = input("Enter a string: ")

# compressed = ""
# count = 1

# for i in range(1, len(name)):
#     if name[i] == name[i - 1]:
#         count += 1
#     else:
#         compressed += name[i - 1] + str(count)
#         count = 1

# compressed += name[-1] + str(count)

# if len(compressed) < len(name):
#     print("Compressed:", compressed)
# else:
#     print("Original:", name)


# most frequent character

# name = input("Enter a string: ")

# frequency = {}

# for ch in name:
#     frequency[ch] = frequency.get(ch, 0) + 1

# max_char = name[0]

# for ch in frequency:
#     if frequency[ch] > frequency[max_char]:
#         max_char = ch

# print("Most frequent character:", max_char)


# second most frequent character

# name = input("Enter a string: ")

# frequency = {}

# for ch in name:
#     frequency[ch] = frequency.get(ch, 0) + 1

# sorted_chars = sorted(
#     frequency.items(),
#     key=lambda x: x[1],
#     reverse=True
# )

# if len(sorted_chars) < 2:
#     print("Second most frequent character does not exist")
# else:
#     print("Second most frequent character:", sorted_chars[1][0])


# Caesar cipher

# text = input("Enter message: ")
# shift = int(input("Enter shift: "))

# result = ""

# for ch in text:
#     if ch.isupper():
#         result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
#     elif ch.islower():
#         result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
#     else:
#         result += ch

# print("Encrypted message:", result)


# email validator

# email = input("Enter email: ")

# if email.count("@") != 1:
#     print("Invalid Email")
# else:
#     username, domain = email.split("@")

#     if not username or not domain:
#         print("Invalid Email")
#     elif "." not in domain:
#         print("Invalid Email")
#     elif domain.startswith(".") or domain.endswith("."):
#         print("Invalid Email")
#     elif " " in email:
#         print("Invalid Email")
#     else:
#         print("Valid Email")


# word frequency dictionary

# paragraph = input("Enter paragraph: ")

# words = paragraph.lower().split()
# frequency = {}

# for word in words:
#     word = word.strip(".,!?;:")
#     frequency[word] = frequency.get(word, 0) + 1

# for word in frequency:
#     print(word, "->", frequency[word])


# sentence reversal

# sentence = input("Enter sentence: ")

# words = sentence.split()
# words.reverse()

# result = " ".join(words)

# print("Reversed sentence:", result)


# string rotation

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# if len(s1) != len(s2):
#     print("Not Rotation")
# elif s2 in (s1 + s1):
#     print("Yes")
# else:
#     print("No")