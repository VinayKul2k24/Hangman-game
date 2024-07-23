import random
print("Let's Start Game")
lives = 6
words = ['apple','beautiful','happy','sad']
choosen_word = random.choice(words)
#print(choosen_word)
blank = []
for i in range(len(choosen_word)) : # 0 1 2 3 4 5 #apple
  blank += '_'
print(blank)
game_over = False
while not game_over:
  guessed_letter = input("guess a letter : ").lower() #p_ _pp_ _
  for position in range(len(choosen_word)): #0 1 2 3 4
      letter = choosen_word[position]
      if letter==guessed_letter :
        blank[position] = guessed_letter
  print(blank)
  if(guessed_letter not in choosen_word):
     lives-=1
     if lives == 6:
      print("________      ")
      print("|      |      ")
      print("|             ")
      print("|             ")
      print("|             ")
      print("|             ")
     elif lives == 5:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|             ")
      print("|             ")
      print("|             ")
     elif lives == 4:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /       ")
      print("|             ")
      print("|             ")
     elif lives == 3:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /|      ")
      print("|             ")
      print("|             ")
     elif lives == 2:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /|\     ")
      print("|             ")
      print("|             ")
     elif lives == 1:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /|\     ")
      print("|     /       ")
      print("|             ")
     else:
      print("________      ")
      print("|      |      ")
      print("|      0      ")
      print("|     /|\     ")
      print("|     / \     ")
      print("|             ")
     if lives == 0:
      game_over = True
      print("you lose !!")
     if '_' not in blank:
      game_over = True
      print("you win")
