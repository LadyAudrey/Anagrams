# Write a program to create dictionary of English anagrams and then test user input against it

# Using a python file of word lists to create the dictionary
##with open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Adulting\\Coding\\MIT600\\bookwork\\miniwords.txt", encoding="utf-8",) as file:
##
##    allText = file.read()
##    # a list in the program to call words from
##    vocab = list(map(str, allText.split()))

with open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\Adulting\\Coding\\MIT600\\bookwork\\miniwords.txt",
          encoding="utf-8", ) as file:
    allText = file.read()
    # a list in the program to call words from
    highvocab = list(map(str, allText.split()))
    vocab = [x.lower() for x in highvocab]
anagram_dict = {}
stripped_word = ('')
sorted_input = ('')

# Go through the list and create a dictionary with keys (set of sorted letters)
# and values that are anagrams
for n in vocab:
    # to create a key that's ordered letters of all anagrams.
    sorted_word = sorted(n)
    # the key I was getting had a lot of ' and , so using join to strip out the letters only
    stripped_word = "".join(sorted_word)

    # code to test if sorted_word or the OG word is in the dictionary, add if not
    if stripped_word not in anagram_dict.keys():
        anagram_dict[stripped_word] = [n]
    if stripped_word in anagram_dict.keys():
        if [n] in anagram_dict.values():
            continue
        else:
            anagram_dict[stripped_word] += [n]

### print(anagram_dict.keys())
### print(anagram_dict)

print("Let's find all the anagrams of chosen words")
test = input("What word would you like to know the anagrams of?\n")

# Making sure the word is an English word and then finding the key of the word
if test in vocab:
    for n in test:
        sorted_input = sorted(test)
        stripped_input = "".join(sorted_input)
        if stripped_input in anagram_dict:
            print(f"{test} has the anagrams of")
            print(anagram_dict[stripped_input])
            break

# Rejecting the word as non-english
if test not in vocab:
    print("I'm sorry, that is a not a legal word. Would you like to try another?")