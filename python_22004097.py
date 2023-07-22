#importing a library named random
import random

# When the function " MasterGameDetail() " is call than the print detail will display
def MasterGameDetail():
       print('---------------------------------------------')
       print('-------- A Master Mind Computer Game --------') 
       print('---------------------------------------------')
       print('Welcome', name, "!", 'Thank you for joining ! Hope you enjoy our Master Mind Computer Game.')
       print('Enter the selection that you want')
       viewMainMenu() #Call a function "viewMainMenu()"

# When the function " viewMainMenu() " is call than the print detail will display
def viewMainMenu():
       print('---------------------------------------------')
       print('---------------- Main Menu ------------------')
       print('---------------------------------------------')
       print('[1] A Master Mind Computer Game Instruction. ')
       print('[2] Start the Game. ')
       print('---------------------------------------------')

# When the function " selection1() " is call than the print detail will display
def selection1():
       print('------------------------------------------------------------------')
       print('-------- A Master Mind Computer Game Instruction -----------------')
       print('------------------------------------------------------------------')
       print('The 4 fruits in the list such as apple, orange, banana, durian') 
       print('1. The computer will automatically generate four fruits from a list of possible fruits (it should be possible for the computer to select the same fruit more than once random)')
       print('   For example the computer may choose apple, apple, orange, and banana.')
       print('2. Only complete word e.g. "apple" is allowed to represent the fruit. No numbers or shorthand characters are allowed to be used to represent the fruit.')
       print('3. The Player need to guess fruits position. What is the color in the first, second, third, and the fourth position? ')
       print('4. After guessing palyer should enter their choice of four fruits from the same list the computer used. For instance, may choose apple, orange, banana, and banana. ')
       print('5. After the user has made their selection, the program will display how many fruits player got right in the correct position and how many fruits player got right but in the wrong position. ')
       print('   For example: it should display the message:   ')
       print('       Correct fruits in the correct place: 1    ')
       print('       Correct fruits but in the wrong place: 1. ')
       print('6. The Player may continues guessing until player correctly enter the four fruits in the order')
       print('7. At the end of the game, the computer will display a message and tell how many guesses player took.')
       print('------------------------------------------------------------------')

       #Confirm Message to player ask understand instruction or not
       understand = input("Do you understand? [yes/no]: ")

       #Check the player input and display the message to player
       if (understand.lower() == "yes"):
              print("Thanks for response")
              print("Hope you understand better about this Master Mind Computer Game.")
              print("If you have better understand now. You can enter selection 2 to start game otherwise enter selection 1 view instruction again.")

       elif (understand.lower() == "no"):
              selection1() #Call a function "selection1()"
       else:
              print("Invalid Input")
              print("Please enter correct selection [yes] or [no]. ") 
              print("Now, Back to Main Menu...")
              
           

#Computer create a random fruits list.
def randomlist(fruitsinlist, result): 
    for x in range(4):
        randomposition = random.randint(0,3)
        result.append(fruitsinlist[randomposition])
    
    
    


contineLoop = "Yes"

#If the contineLoop is equal to "Yes" or "yes" than the program run.
while contineLoop == "Yes" or contineLoop == "yes":
    name = ""
    while name == "":
        name = input("Enter your name: ")
        while name != "":
            MasterGameDetail()
            selection = input("Enter your selection 1 or 2: ")
            contineLoop = "No"
            
            #Check the player selection and display the message to player 
            if selection == "1":
                selection1() #Call the function "selection()"
                

            elif selection == "2":
                 fruits = ["apple", "orange", "banana", "durian"] #A fruits list
                 randomfruits = [] #A list of random fruits
                 randomlist(fruits, randomfruits)
                 
                 print("Answer:" ,randomfruits)

                 count = 0 #counter
                 correctposition = 0  #counter for correctposition
                 wrongposition   = 0  #counter for wrongposition
                 while correctposition < 4:
                        correctposition = 0 #counter for correctposition
                        wrongposition   = 0 #counter for wrongposition
                        userguess = [] #A list of player enter fruits
                        count = count + 1 #increment

                        for i in range(4):
                               #loops indefinately until input correctly
                               while True: 

                                      #Ask player enter the fruits. After player enter the fruits, computer will convert the input to the lowercase. 
                                      value = input(" Enter the fruits " + str(i+1) + " : ").lower()

                                      #Check the player enter fruits inside the fruits list or not.
                                      if (value == "apple" or value == "orange" or value == "banana" or value == "durian"):
                                             userguess.append(value)
                                             break #will end the loop
                                      else:
                                             print("Invalid Value")
                        print("You guessing fruits:")
                        print(userguess)
                        wrong = [] 
                        
                        #Check how many correct fruits in the correct place
                        for i in range(4):
                               if randomfruits[i] == userguess[i]:
                                      correctposition = correctposition + 1 #increment
                               else:
                                      wrong.append(userguess[i])
                     
                        #Check how many correct fruits in the wrong place
                        for y in range(0, len(wrong)):
                               if (randomfruits.count(wrong[y]) >= userguess.count(wrong[y])):
                                      wrongposition = wrongposition + 1 #increment
                                      
                        #If 4 fruit in the correct place than display message to player 
                        if correctposition == 4:
                               print("Congratulations", name , "you win!")
                               
                        #Display message to player. Let player know
                        #How many fruits they got right position
                        #How many fruits they got right but wrong position
                        #How many guesses they took
                        print("Correct fruits in the correct place:", correctposition)
                        print("Correct fruits in the wrong place:", wrongposition)
                        print(" You had guesses" , count, "times.")
                        

                           

                 break #will end the loop
            else:
                print("ERROR: Invalid Input!")
                print("Please enter correct selection [1] or [2]. ")
              
               
                
            
        else:
            print("Empty Input ! ", "Please enter your name")
            contineLoop = "Yes"

          
