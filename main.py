# 10
# 9
# 7

alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letter_pair_dict = {}
letter_dict = {}
for i, letter in enumerate(alphabet):
    letter_dict[letter] = 0
    for j, letter_pair in enumerate(alphabet[i::]):
        if not(letter == letter_pair):
            letter_pair_dict[letter+letter_pair] = 0

# print(letter_pair_dict)


# print(letter_pair_dict)
f = open("google-10000-english/google-10000-english.txt", "r")
for word in f:
    word = word.rstrip('\n')
    for i, l in enumerate(word):
        letter_dict[l] += 1

        if not(i == (len(word)-1)):
            if not(word[i] == word[i+1]):
                alpha_i1 = alphabet.index(word[i])
                alpha_i2 = alphabet.index(word[i+1])

                if (alpha_i1 <= alpha_i2):
                    letter_pair_dict[word[i]+word[i+1]] += 1
                else:
                    letter_pair_dict[word[i+1]+word[i]] += 1

print(letter_pair_dict)
sort_letters = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)
# print(sort_letters)

max_key = None
max_value = 0
for key, value in letter_pair_dict.items():
    if (value > max_value):
        max_value = value
        max_key = key 

print(max_key)
print(max_value)

# max_key = None
# max_value = 0
print(sort_letters)
print(sort_letters[9:19])
print(sort_letters[0:9])
print(sort_letters[19:-1])    

