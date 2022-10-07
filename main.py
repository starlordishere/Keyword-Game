import random 
import time
from os import system, name
  
health= 100 #health of the character
gold = 50 # total wealth of the character
guns = 0 # no. of items in bagpack

print("""The Orb is much more important than you realize. I wonder how many other players are caught up in this game? Things may be about to get quite fascinating..."
―Taneleer Tivan""") #beginning sentence to start the game

  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def name(): # name function, starting function

  name = input("What is your name \n\t ***") #input player name
  print(f"Hello {name.title()}, welcome to the quest to find the Orb. You have been selected by our own Yandu Udonta. He is the Centaurian leader of an exiled faction of the Ravagers.")
  time.sleep(1)
  print("You will be reffered as Starlord from now onwards.")
  time.sleep(10) #pause the next statement by 7 seconds
  clear() #calling clear 

  xandar() # calling the function xandar

def xandar(): #xandar function- Xandar is a planet
  
  

  global heath, gold, backpack #global variables
  print("Starlord, You are sent to Xandar by Yandu to form a team to get the Orb from the planet name Morag.")
  time.sleep(1)
  print("Thousands of years   ago, Morag was the home of an advanced and flourishing civilization, that was wiped out by a global warming catastrophe.")    
  time.sleep(1)
  print("Sometime prior to their demise, the inhabitants of Morag built a temple to guard the Orb.")
  time.sleep(1)
  print(f"You have {guns} guns with you currently. Your heath status is {health} and gold status is {gold}")
  time.sleep(1)
  print("Starlord, Gamora is coming toward you.She is one of the best pilot in the galaxy.") 
  time.sleep(1)
  print("If you want to add her in your team to get the orb, you will have to answer her few questions.")
  time.sleep(1)
  print('Gamora is ready to ask you question.')
  time.sleep(1)
  answer=input('Are you ready to answer? (yes/no) :')
  clear() #ask the player to input yes or no
  score=0 # variable to store total score of a player
  heal= 0 #variable that changes everytime player enters wrong infomation
   
  if answer.lower()=='yes': #check if user input yes
      answer=input('Gamora: What is my father name\n \t ---')
      if answer.lower()=='thanos': #checks if the user input is same as thanos
          score += 1 #score increase by 1
          print('correct')
      else:
        print("Wrong, you've been stabbed by sword. Your health decresed by 20%.")
        heal = heal -20
   
      answer=input('Gamora: What is my sister name?\n \t ---')
      if answer.lower()=='nebula':
          score += 1
          print('correct')
      else:
        print("Wrong, you've been stabbed by sword. Your health decresed by 20%.")
        heal = heal -20
   
      answer=input('Gamora: What is my home planet name?\n\t ---')
      if answer.lower()=='zen-whoberi':
          score += 1
          print('correct')
      else:
        print("Wrong, you've been stabbed by sword. Your health decresed by 20%.")
        heal = heal -20

      if score == 3: #if total score i 3, then only player wins. So is this condition
        print("Congratulation, Gamora is in your team and she will help you to get the orb. She has the co-ordinates of Morag.                 All you need now is a Spaceship. ")
        time.sleep(7)
        clear() #clear the screen
        melano() # player win, so called function melano()
      else:
        print("Unfortunately, you are not serious and underestimited her.")
        time.sleep(1)
        print(f"She is mad at you. You are bleeding. Bleeding is illegal in Xandar. Your health level is {health + heal}  So, you're taken to a high facility prison.")
        
        time.sleep(10)
        prison() #player lost so called function prison()
    
  else:
    print(f"Unfortunately, you are not serious and underestimited her. She is mad at you. She stabs you. You're now bleeding. Bleeding is illegal in Xandar.So, you're taken to a high facility prison.")
    time.sleep(10)
    prison() #player input no which is similar to losing agaist Gamora, So player is sent to prison
    
          
def prison(): #function prison
  
  global heath, gold, backpack #global variables
  clear()
  print("You are in one of the highly guarded prision in the galaxy.")
  time.sleep(1)
  print("To get out from the prison, it is almost impossible. But, it looks like Rocket Raccon is here as well.") 
  time.sleep(1)
  print("He has escaped 22 prision facilities. He can help you break this prison and go back to Morag on his ship.")
  time.sleep(1)
  print("For him to do the prision break, he needs a prosthectic leg from one of the one of the prisoner named Taserface. ")
  time.sleep(1)
  print("Rocket Racoon said that the prosthectic leg is one of the most important tool in breaking out of the prison.")
  time.sleep(1)
  print("You will need to play Hangman game with Taserface. If you win, he will give you his leg.")
  fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya'] #lis of fruits for hangman game
  superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'thanos', 'Kang', 'deadpool', 'Ironman', 'sandman', 'moonknight']
  userGuesslist = [] #for user guess list
  userGuesses = [] #for user guesses
  playGame = True
  category = ""
  continueGame = "Y"
  
  time.sleep(1)
  print("The objective of the game is to guess the secret word chosen by the Taserface.")
  time.sleep(1)
  print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
  time.sleep(2)
  print("Let the fun begin!")
  time.sleep(1)
  
  while True:
      #Choosing the Secret word
      while True:
          if category.upper() == 'S':
              secretWord = random.choice(superHeroes)
              break
          elif category.upper() == 'F':
              secretWord = random.choice(fruits)
              break
          else:
            category = input("Please select a valid categary: F for Fruits / S for Super-Heroes; X to exit")
  
          if category.upper() == 'X':
              clear()
              print("Looks like, you donot want to get out of prison.")
              playGame = False
              finish() 
              break
  
      if playGame:
          secretWordList = list(secretWord)
          attempts = (len(secretWord) + 2)
  
          #Utility function to print User Guess List
          def printGuessedLetter():
              print("Your Secret word is: " + ''.join(userGuesslist))
  
  
          #Adding blank lines to userGuesslist to create the blank secret word
          for n in secretWordList:
              userGuesslist.append('_')
          printGuessedLetter()
  
          print("The number of allowed guesses for this word is:", attempts)
  
  
          #starting the game
          while True:
  
              print("Guess a letter:")
              letter = input()
  
              if letter in userGuesses:
                  print("You already guessed this letter, try something else.")
  
              else:
                  attempts -= 1
                  userGuesses.append(letter)
                  if letter in secretWordList:
                      print("Nice guess!")
                      if attempts > 0:
                          print("You have ", attempts, 'guess left!')
                      for i in range(len(secretWordList)):
                          if letter == secretWordList[i]:
                              letterIndex = i
                              userGuesslist[letterIndex] = letter.upper()
                      printGuessedLetter()
  
                  else:
                      print("Oops! Try again.")
                      if attempts > 0:
                          print("You have ", attempts, 'guess left!')
                      printGuessedLetter()
  
  
              #Win/loss logic for the game
              joinedList = ''.join(userGuesslist)
              if joinedList.upper() == secretWord.upper():
                  print("Congratulations! You won Starlord. Rocket Racon can now break you out of prison and take you to Morag")
                  morag()
              elif attempts == 0:
                  print("Too many Guesses!, Sorry better luck next time.")
                  print("The secret word was: "+ secretWord.upper())
                  print("You lose, if will never leave the prison. You will die here Strarlord!!")
                  finish()
                
  
          
      else:
          break


def melano(): #function melano for the ship Melano
  print("Your only way to Morag is through the spaceship Melano. You will have to buy Melano from the collector.")
  time.sleep(1)
  print("Problem is collector do not like to sell anything to ravegers like you.")
  time.sleep(1)
  print("One thing you can do is play 'Rock, Paper and Scissor' with him. \nIf you win him, you will get the Melano. \n If you lose, you will be locked as one of the item in Collector's vault. \n If the game is tie, you're still going to be in Collector's vault. ")
  time.sleep(2)
  print("Are you ready. There is no turnig back now:")
  computerwins = 0 
  playerwins = 0
  ties = 0
  end = 0
  for i in range(5): #play rock paper scissor 5 times against the Collector
  
      choices = ["rock",
                 "paper",
                 "scissors"]
  
      userChoice = input("Rock, Paper, Scissors\n---")
  
      computerChoice = (random.choice(choices))
      print(computerChoice)
  
      if userChoice == computerChoice: #if both choose same
          time.sleep(0.5)
          print("Tie!\n")
          ties += 1
          end += 1
  
      elif userChoice == "rock": #condition if player choose rock
          if computerChoice == "paper": #and computer choose paper
              time.sleep(0.5)
              print("Computer Win!\n")
              computerwins +=1
              end += 1
  
          else:
              time.sleep(0.5)
              print("Player win!\n")
              playerwins += 1
              end += 1
  
      elif userChoice == "paper":
          if computerChoice == "rock":
              time.sleep(0.5)
              print("Player win!\n")
              playerwins += 1
              end += 1
  
          else:
              time.sleep(0.5)
              print("Computer win!\n")
              computerwins += 1
              end += 1
  
      elif userChoice == "scissors":
          if computerChoice == "rock":
              time.sleep(0.5)
              print("Computer win!\n")
              computerwins += 1
              end += 1
  
          else:
              time.sleep(0.5)
              print("Player win!\n")
              playerwins += 1
              end += 1
  
      else:
              choices.append("end")
              print("\nGreat game!\n")
              break
  print("Total score for Collector: ", computerwins, "wins!")
  print("Total score for Starlord: ", playerwins, "wins!")
  print("Total ties: ", ties, "ties!")
  if playerwins > computerwins: #check if player wins against computer
    print("Congratulation, Melano is all yours. Good luck on your quest Starlord.")
    time.sleep(3)
    clear()
    morag() #calling the function morag
  else:
    print("You lose Starlord. You're now the property of Collector.")
  time.sleep(3)
  finish() #go to the function finish()
              
def morag(): #function morag
  global gold, health, guns
  print()
  print("Welcome to Morag")
  time.sleep(1)
  print("You are not the only one looking for Orb. 'Ronan the Acusser' also is in search of Orb.")
  time.sleep(1)
  print("Starlord, your father 'Ego the Living Planet' can help you defeat 'Ronan the Acusser'.") 
  time.sleep(1)
  print("Problem is you are not worthy enough in your father's eyes.")
  time.sleep(1)
  print("You can win his worthiness if can solve these following 10 question in 10 seconds. \n Are you ready Starlord. This is your only chance.")
  time.sleep(1)
  points = 0
  
  choice = input("Press enter to continue:") #ask player to enter to continue
  start_time = time.time() 
  
  for value in range(10): #for number in range 1 to 10
      num1 = random.randint(1,10)
      num2 = random.randint(1,10)
  
      choice = int(input(f"What is {num1} + {num2}? ")) 
      if choice == num1 + num2: #if the user input is same as num1 + num 2
          print("You got it right!")
          points += 1
      else:
          print("Sorry, that is not right")
  
  elasped_time = time.time() - start_time
  
  print("Your score is",points,"out of 10")
  if elasped_time > 15 or points < 5:
      print("You ran out of time and finished in",elasped_time,"seconds")
      time.sleep(1)
      print("You lose! Ronan will kill you and use the Orb to decimate Xandar.")
      time.sleep(1)
      print(f"Ronan took your {gold}gold units and your health is now {health-health}.")
      time.sleep(10)
      clear() #clear screen
      finish() #calling the function finish()
    
  else:
      print("You finished with a score of",points,"in",elasped_time,"seconds!")
      time.sleep(1)
      print("You win!, You prove your worthiness. Your father helped you to kill Ronan.")
      time.sleep(1)
      print("You may now enter into the Temple of Morag.")
      time.sleep(3)
      clear()
      temple()# calling the function temple()
      

    

 
def temple(): #function temple
  
  print("There are two doors.One door leads to the orb, other lead to the voidness of time.Please select the door carefully")
  time.sleep(1)
  choice =input(print("Please select the door. [1] or [2].")) #ask player to input 1 or 2
  if choice == '1': # for choice 1
    time.sleep(2)
    orb() #call function orb()
    
    
  if choice == '2': #for choice 2
    print("You entered the timeless void. You cannot return back from here.")
    time.sleep(2)
    finish() #call function finish()
  else: #if player input anything else
    print("Enter valid option")
    temple() #go back to start of the function
  
  
  

def finish(): # function if player lose and game over
  print("Game is over")
  time.sleep(1)
  print("You are not worthy to be a member of Ravegers.")

def orb(): #function for the orb
  global gold, guns #global variables
  print("Congraulation, you found the orb.")
  time.sleep(1)
  print("Yandu Odanta is very proud of you. Now everyone will know your name as 'THE LEGENDARY OUTLAW THE STARLORD'")
  time.sleep(1)
  print(f"He gave you 5,000 gold units. Your total gold is now {gold + 5000} unit. He has also given you a new Kree Design Machine GUn. Your bag has now {guns +1} items.") 

name() #calling the name function