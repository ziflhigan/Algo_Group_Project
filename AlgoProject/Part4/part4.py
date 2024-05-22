text1 = ""
text2 = ""
different_words = []

# Read contents from text1.txt
with open("text1.txt", "r") as file:
    text1 = file.read()

# Read contents from text2.txt
with open("text2.txt", "r") as file:
    text2 = file.read()

# store the words in text1.txt in a list
words1 = text1.split()
words2 = text2.split()

# Compare the number of words in text1.txt and text2.txt
if len(words1) == len(words2):
    print("The number of words in both letters is the same.")

i=1;
for word1, word2, in zip(words1, words2):
    if word1 != word2:
        different_words.append((word1, word2))
        print("Discrepancy #" + str(i) + ": " + word1 + " -> " + word2)
        i += 1


        