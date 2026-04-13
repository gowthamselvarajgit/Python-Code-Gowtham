import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']


word_list = ["dog", "cat", "cow", "fish", "bird", "rat"]

lives = 6

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

#Randomly choosed word
chosen_word = random.choice(word_list)
print(chosen_word)

#create placeholder
placeholder = ""
len_of_chosen_word = len(chosen_word)
for position in range (len_of_chosen_word):
    placeholder = placeholder + "_ "
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    
    print(f"********************{lives}/6 LIVES LEFT*******************")
    #Got the letter from the user and made itto lowercase
    guess = input("Guess a letter: ").lower()
    
    #Check guessed character is in the chosen word
    display = ""
    
    #check the are guessing the letter they have already guessed
    if guess in correct_letters:
        print(f"You have already guessed this letter {guess}")
        
    else:
        for char in chosen_word:
            if char == guess:
                display += char
                correct_letters.append(char)
            elif char in correct_letters:
                display += char
            else:
                 display += "_"
            
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life")
            lives -= 1
            if lives == 0:
                game_over = True
                print(f"********************IT WAS {chosen_word} YOU LOSE!********************")
        
        if "_" not in display:
            game_over = True
            print("********************YOU WIN!********************")
            
        print(display)
        print(stages[lives])
    

        


    

