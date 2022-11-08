# Import the pygame Module that is used for graphics in the game
import pygame

# Import the Random module used to generate random enemy ship positions
import random

# Import the Math Module used along with the Random
import math

# Import the Mixer for sounds from Pygame Module
from pygame import mixer

# Import the Button from the Menu Module
from menu import Button

# Import the OS Module
import os

#Import the Ceil from the math Module
from math import ceil



# Call the Init Function of Pygame
pygame.init()

# Call  the Init Function of Mixer imported from pygame
mixer.init()

# Load Background music to be played in the game
mixer.music.load('Corazon.mp3')

# Play it over and over from the beginning
mixer.music.play(-1)

# Create an instance of the Game Screen where all the action will take place
gameScreen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# Give the screen a title
pygame.display.set_caption('Space Shooter by Steve Shema')

# Load the Icon of the game and Load it on the gameScreen
ico = pygame.image.load('spaceShooter_icon.png')
pygame.display.set_icon(ico)

# Additionally load the background Image of the Game
backGround = pygame.image.load('bgImage.jpg')
# NB: I blit the background Image to the gameScreen later on

# load the Space ship Picture
myShip = pygame.image.load('spaceship.png')

# A list that is used to hold the entire collection of aliens
alienimg=[]

# Another list containing the list xCordinate positions of the alien
alienX=[]

# List containing yCordinate positions of the alien
alienY=[]

#Info Object
infoObject = pygame.display.Info()


#height and width of the game
current_width = infoObject.current_w
current_height = infoObject.current_h

# Return to menu button
return_to_Menu = Button("Return To Main Menu", 450, 45, ((infoObject.current_w / 2) - 250,
                                                         (infoObject.current_h / 2) - 10), "#07da63", 6)

# Game clock
clock = pygame.time.Clock()
FPS = 140

# List holding the values for the propagation and movement of the aliens on the user's Screen but along the x-axis
alienspeedX=[]

# List holding the values for the propagation and movement of the aliens on the user's Screen but along the y-axis
alienspeedY=[]

# Set the initial number of aliens that show up to be maybe 6
alienCount = 10
# NB: You could increase this number if you wanted to but I do not recommend it
# However, if you wanna decrease it that would be fine

# Create a for loop that goes until the alienCount and keeps generating more and more aliens at diff. positions
# on the screen
for x in range(alienCount):

    '''
    The way this works is that for each iteration of the loop, we create an alien with an image, x and y positon
    obtained through the random module, and The speed along xAxis and YAxis 
    '''

    # Append this new alien image to the list of alien images
    alienimg.append(pygame.image.load('alien(1).png'))
    # generate a new xCordinate and append it to the list
    alienX.append(random.randint(0,736))
    # Generate a new yCordinate and append it to the list
    alienY.append(random.randint(30,150))
    # Then set the propagation of the alien along the xAxis
    alienspeedX.append(-1)
    # Set the propagation of the alien along the yAxis
    alienspeedY.append(40)

# Set the inital score to zero at the start of the game
score = 0

# Read the highest score from an External File
f = open("highest_score")
# Get the Score
highestScore = f.read()
# Close the file handle
f.close()

# Configuration for the bullet

# Load the bullet image
bulletimg = pygame.image.load('bullet.png')
# Extra config parameters
check = False
#  x and y cordinates of the spaceship
bulletX = 386
bulletY = 490

# The Initial Co-ordinates specifying the location of the User's spaceship
xCord = 370
yCord = 480

'''
Later on I use changeCordX and changeCordY to manipulate how these locations change depending on the event
triggered 
'''

# variables for storing the change in the X and Y cordinates
xCordChange = 0
yCordChange = 0

# Create a variable that will be used to control the opening and closing of the window
screenState = True

# Set the font to be displayed on the gameScreen
font = pygame.font.SysFont('Arial', 32, 'bold')

# Function to Display game text and configuration for its positioning
def score_text():
    img = font.render(f'Score:{score}', True, 'white')
    gameScreen.blit(img, (10, 20))
    highScore = font.render(f'Highest Score: {highestScore}', True, 'white')
    gameScreen.blit(highScore, (current_width-320, current_height-750))

# Instance of the SysFont that will be used to display the gameover Text
font_gameover = pygame.font.SysFont('Arial',64,'bold')

# Function to control when the its gameOver and you have to display the gameOver text
def gameover():
    img_gameover = font_gameover.render('GAME OVER', True, 'white')
    gameScreen.blit(img_gameover, ((current_width/2)-210, (current_height/2)- 90))
    # Return to Menu Button after you've been hit by an alien
    # Draw the start Game Button on the screen
    return_to_Menu.draw(gameScreen)
    # If the current Score is higher than the Highest Score
    if score > int(highestScore):
        # Re-write everything in the highest_score file to the current score
        fh = open("highest_score", "w")
        fh.write(str(score))
        fh.close()
#######ENtering the mainLoop will update the Screen continuously

# Function is invoked only if the Return to Menu Button is clicked
def returnToMenu():
    # If the Button has been clicked return to menu
    if return_to_Menu.user_clicked:
        pygame.quit()
        os.system("python main.py")

# Get the dimensions for the width
bg_height = backGround.get_height()
tiles = (ceil(infoObject.current_h / bg_height)) + 1

# Add a scroll
scroll = 0

print(tiles)


# Equivalent of mainloop in Pygame
while screenState:
    clock.tick(FPS)

    #For loop to blit a dynamic background
    for i in range(0, tiles):
        #Add the background Image to the screen
        gameScreen.blit(backGround, (0, i*bg_height+scroll))

    #Scroll the background
    scroll -= 2

    # Check for the scroll being greater than the height
    if abs(scroll) > bg_height:
        scroll = 0

    #Get all events happening in the window
    for a in pygame.event.get():
        #If the event is closing the window
        if a.type == pygame.QUIT:
            #Close the window by changing the screenState variable to false
            screenState = False
        #Check for when a key on the keyboard is pressed
        if a.type == pygame.KEYDOWN:

            #If the left arrow key is pressed
            if a.key == pygame.K_LEFT:
                # Decrease the current position by 1 unit of width
                xCordChange -= 3

            #If the right arrow key is pressed
            if a.key == pygame.K_RIGHT:
                # Increase the current position by 1
                xCordChange += 3

            # If the up key is pressed
            if a.key == pygame.K_UP:

                #Decrease the y Cordinate by unit of height
                yCordChange -= 1

            # If the up key is pressed
            if a.key == pygame.K_DOWN:
               # Increase the y Cordinate by 1 unit of height
               yCordChange += 1

            #If the Spacebar is pressed
            if a.key == pygame.K_SPACE:

                if check is False:
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    check = True
                    bulletX = xCord+16

        # Check for when the key is released to know when to stop movement of the ship
        if a.type == pygame.KEYUP:

            # If whatever key was being pressed is released, stop the change in the x-cordinate and y-Cordinate
            xCordChange = 0

    #Then add whatever is left of the change in the X and Y cordinates to the actual values and yCordinate
    xCord += xCordChange

    # To stop the ship from exceeding the boundaries of the gameScreen we set a couple of conditions
    # If the XCordinate is less than the starting position of the Screen
    if xCord<=0:
        # Stop at the Start position of the Screen
        xCord=0

    # Else if the xCord exceeds the width of the screen, but because the spaceship is 64px,
    # we subtract that from the width of the screen to make sure it doesn't go beyond the screen width
    elif xCord >= (current_width-64):
        # Set it to the Screen Width
        xCord = current_width-64

    #Loop through the initial number of aliens
    for i in range(alienCount):
        #
        if alienY[i] > 421:
            for j in range(alienCount):
                alienY[j] = 2000
            gameover()
            break

        #Modify the actual position of the alien depending on the propagation of the alien
        alienX[i]+=alienspeedX[i]

        #if the alien's position
        if alienX[i]<=0:
            alienspeedX[i]=2.5
            alienY[i]+=alienspeedY[i]
        if alienX[i]>=current_width-64:
            alienspeedX[i]=-2.5
            alienY[i]+=alienspeedY[i]

        distance = math.sqrt(math.pow(bulletX - alienX[i], 2) + math.pow(bulletY - alienY[i], 2))
        if distance < 27:
            explosion= mixer.Sound('mixkit-trailer-screaming-people-annihilation-351.wav')
            explosion.play()
            bulletY = 480
            check = False
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(30, 150)
            score += 1
        gameScreen.blit(alienimg[i], (alienX[i], alienY[i]))
        gameScreen.blit(alienimg[i], (alienX[i], alienY[i]))
    if bulletY<=0:
        bulletY=490
        check=False
    if check:
        gameScreen.blit(bulletimg, (bulletX, bulletY))
        bulletY-=5







    #Blit the spaceship onto the screen eachtime before you update
    gameScreen.blit(myShip, (xCord, yCord))

    #Display the score on the screen
    score_text()
    return_to_Menu.check_for_click()
    returnToMenu()


    #Update the display on each iteration.
    pygame.display.update()