# Display the Tttle of the story
print("~ Tales of the Wild West~")
print("(A Work of Fiction)")
print( )
# Give the reader the story background
print("One rainy day, you decide to hop in your time machine to go on an adventure. Your time machine transports you to the 1880s, and it becomes clear to you that you've ended up in the Wild West.")
print( )

print("You only have two days to explore so you decide to head to town to see what life in the wild west offers!")
print( )

# Display the first multiple choice question to choose if you will talk to the  bartender, the sheriff, or the outlaw
print("You ride your horse into town and see a few places you could stop in to get some information:")
print(" A. The local saloon, where the bartender's waiting to serve you")
print(" B. The sheriff is standing outside the local jail")
print(" C. An outlaw, is loading up his six-shooter in the shadows")

# Have the reader type the letter of who they want to talk to
firstChoice = input("Who will you talk to? Please selection option A through C: ")
print( )

# If they picked the bartender, ask the reader a multiple choice question on what drink the want
if(firstChoice == "A"): 
  print("You walk in into the saloon, and the bartender asks you what you want to drink")
  print(" A. boilermaker")
  print(" B. moonshine")
  print(" C. a beer")
 
# Have the reader type the letter of what drink they want 
  drinkChoice = input("What do you order? Please enter a letter A through C: ")
  print( )

  #If the reader picked the moonshine, display the message that they'll get in a fight and go to jail
  if(drinkChoice == "B"):
    print("You get into fight, then the sheriff hauls you off to jail")
    print("~ The End~")
    print( )

# If the reader picked the beer or boilermaker, display the message that they'll be on their way after
  else:
    print("You finish your drink and continue on your way")
    print("~ The End ~")

# If they picked the sheriff, ask the reader to answer the sheriff's question
if(firstChoice == "B"): 
  print("You ride past the sheriff to say hello and he asks you a questions")
  print("If you had 20 horses, but sold 5, how many would you have left?")
  horseAnswer = input("Enter the number of horses you have left:" )
  horseAnswer = int(horseAnswer)
  print( )
# If they entered the correct answer, display message
  if(horseAnswer == 15):
    print("The sheriff says, 'Boy you're pretty, would you like to be my deputy?' You gladly accept the position.")
    print("~ The End ~")

# If they answer incorrectly, display message telling you to get lost
  else:
    print("The sheriff shakes his head and tells you good luck")
    print("~ The End ~")