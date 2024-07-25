# Python station project 1: Mad Libs for GSL-12
# Mad Libs is a game with a basic story template that has blank spaces which 
# need to be filled by the user. The user inputs words without knowing the story.

# The task:
# Write a program on Python that does the following:
# 1. Allows the user to pick one of the templates
# 2. Asks the user to input words. “Type number”, for example
# 3. Generate a story afterwards and shows it to the user
# Make sure your program follows these 3 conditions. You will have to use the 
# “random” library, and the only functions you’ll be able to use will be 
# print() and input().

# I have used the functions while, for, if - else statements, etc. Hope
# this is ot a big deal :)

import random

timeMeasure = ['second', 'minute', 'hour', 'day', 'week', 'month', 'year', 
               'decade', 'century'] # possible time measures
a = random.randint(0,8) # generating a random number to choose from time measure for the stories

print('''Please, choose one of the templates by inserting 1 or 2: 
  1 Unbelievable story
  2 Camping''') # requesting the user to choose among two stories
  
option = input() # storing the story choice in the variable option

# Checking if the input is correct. If it's not, waiting for a correct input
while option not in ('1', '2'):
    print('''Wrong input, number 1,2 or 3 expected.''')
    option = input()

print('''We will need some additional info to create the story of your choice. 
      Please, be patient and follow the instructions.''')

# List of inputs from the user depending on the chosen option for the story. 
if option == '1':
    request = ['Input your favourite food:', 'Input your name:', 'Input an adjective', 
                'Input a name of an animal:', 'Input a verb in a past tense:', 
                'Input another verb in a past tense:', 'Input a noun', 
                'Please, insert your gender. "M" for make and "F" for female.']
elif option == '2':
    request = ['Input Person Name: ', 'Input noun: ', 'Input adjective (feeling): ', 
            'Input verb: ', 'Input adjective (feeling): ', 'Input an animal: ', 
            'Input a verb: ', 'Input a color: ', 'Input a verb + ing: ', 
            'Input a adverb + ly: ', 'Input a number: ', 'Input a color: ', 
            'Input a animal: ', 'Input a number: ', 'Input a silly word: ', 
            'Input a noun again: ']

# Creating a variable to store the length of the list for a chosen story
requestLength = len(request)
# Creating an empty list 'answerStored' which has the size of the list 'request'
answerStored = ['']*requestLength

# Storing answers in 'answerStored'
i = 0
for item in request:
    print(item)
    answerStored[i] = input()
    i += 1

    
if option == '1': # checking if an Unbelievable story was chosen. 
    pronoun = 'she' # storing the pronouns in a separate variable
    objPronoun = 'her ' # storing the pronouns in a separate variable
    article = 'a' # storing the indefinite article in a separate variable
    
    # Checking if the input gender is male or female and redefining the pronouns accordingly
    if answerStored[requestLength-1] in ('M','m','male'):
        pronoun = 'he'
        objPronoun = 'his '
    
    # Checking if the article needs to be 'a' or 'an' and changing its value, if necessary
    if answerStored[3][0] in ('a','e','o','i'):
        article = 'an'

    # Printing out the story for template 1 with the stored answers in answerStored
    print("\n It was " + answerStored[0] + " day at Tumo, and " + answerStored[1] + 
          " was super  " + answerStored[2]  + " for lunch. But when " + pronoun + 
          " went outside to eat, " + article +" " + answerStored[3]  + " stole " + objPronoun + 
          answerStored[0] + "! " + answerStored[1] + " chased the  " + answerStored[3]  
          + " all over Tumo. And " + pronoun   + " " + answerStored[4] + ",  " 
          + answerStored[5] + ", and ran through the playground. Then " + pronoun 
          + " tripped on her " +  answerStored[6] + " and the " + answerStored[3] 
          + " escaped! Luckily, " +  answerStored[1] + "'s friends were willing to share their " 
          +  answerStored[0] + ". " + answerStored[1] + " would stay full for a whole " 
          + timeMeasure[a] + '.')

else: # If not Unbelievable story was chosen, then a story on Camping is generated (option == '2')

    # Checking if the indefinit article needs to be 'a' or 'an' and changing its value, if necessary
    if answerStored[5][0] in ('a','e','o','i'):
        answerStored[5] = 'n ' + answerStored[5]
    else:
        answerStored[5] = ' ' + answerStored[9]
    
    
    # Printing out the story for template 2 with the stored answers in answerStored
    print("\n This weekend I am going camping with " + answerStored[0] + 
          ". I packed my lantern, sleeping bag, and " + answerStored[1]+". I am so " 
          + answerStored[2] + " to " +answerStored[3] + " in a tent. I am " 
      + answerStored[4] + " we might see a" + answerStored[5] + 
      ", I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and "
      + answerStored[6] +". I have heard that the "+answerStored[7]+" lake is great for "
      + answerStored[8] +". Then we will " + answerStored[9] + " hike through the forest for " 
      + answerStored[10] + " " + timeMeasure[a] + ". If I see a " + answerStored[11] 
      + " " + answerStored[12] + " while hiking, I am going to bring it home as a pet! t night we will tell " 
      + answerStored[13] +" "+ answerStored[14] +" stories and roast " + answerStored[15] + 
      " around the campfire!!!")

print("\n\n Hope you enjoyed this little game.")