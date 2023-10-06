#This code is a madlibs generator. A story with replaceble words. The user is going to tell the program the words that he want in the story
#1 story with those words.
#story in an external file.

#ChatGPT story import
with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

#access to the caracters
for i, char in enumerate(story): #enumerate, posicion and character
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)

with open("lastStory.txt", "w") as new:
    new.write(story)