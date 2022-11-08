# import the pygame Module
import os


import pygame

# Import the Mixer from the pygame Module
from pygame import mixer

# From menu import the mainMenu
from menu import MainMenu

# From menu also Import the Button
from menu import Button

# From the subprocess import the Popen Func
from subprocess import Popen


# The gameMockup Function to create a virtual instance of the game
class GameMockup(object):
    # Constructor Class
    def __init__(self):
        # Call the init method of pygame
        pygame.init()
        # Call the init method of mixer
        mixer.init()
        # Variables to control the running of the game
        self.runningState = True
        self.isPlaying = False
        # variables used to handle events
        self.UP = False
        self.DOWN = False
        self.START = False
        self.BACK = False
        # Display dimensions configuration
        self.mockup_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Get the dimensions of the window and store them in an object
        self.infoObject = pygame.display.Info()
        # Set the font Type to be used
        self.fontType = pygame.font.get_default_font()
        self.black_bg, self.white_bg = (0, 0, 0), (255, 255, 255)
        self.bgImage = pygame.image.load("menuBG.jpg")
        # Load the music to play
        mixer.music.load("Corazon_Instrumental.mp3")
        # Start playing the music
        mixer.music.play(-1)
        # Instance of the menu
        self.curr_menu = MainMenu(self)
        # Start game Button version of the button
        self.startGame_button = Button("Start Game", 450, 45, ((self.infoObject.current_w / 2) - 537,
                                                               (self.infoObject.current_h/2) - 70), "#07da63", 6)
        # Credits Button version of the button
        self.credits_button = Button("Credits", 450, 45, ((self.infoObject.current_w / 2) - 537,
                                                          (self.infoObject.current_h/2) + 0), "#818589", 6)
        # Credits Button version of the button
        self.quitGame_button = Button("Quit Game", 450, 45, ((self.infoObject.current_w / 2) - 537,
                                                          (self.infoObject.current_h / 2) + 70), "#DC143C", 6)

    # Function with the mainloop
    def main_loop(self):
        # Start the mainloop
        while self.isPlaying:
            # Check for all the events happening
            self.get_events()
            # If the user prompts for the game to be started
            if self.START:
                # Change start to False
                self.isPlaying = False
            # Blit the background Image to the Screen
            self.mockup_screen.blit(self.bgImage, (0, 0))
            # Draw the title of the menu as text
            self.draw_text("Steve Shema's", 50, (self.infoObject.current_w / 2) - 390,
                           (self.infoObject.current_h / 2) - 140, (232, 30, 99))
            self.draw_text("Space Shooter", 50, (self.infoObject.current_w / 2) - 15,
                           (self.infoObject.current_h / 2) - 140, (4, 146, 194))
            # Draw the start Game Button on the screen
            self.startGame_button.draw(self.mockup_screen)
            # Draw the Credits Button on the screen
            self.credits_button.draw(self.mockup_screen)
            # Draw the Quit Game Button on the screen
            self.quitGame_button.draw(self.mockup_screen)
            # Call the run game Function
            self.run_game()

            # Enter the mainloop by calling the update Function
            pygame.display.update()
            # Reset all keys to false
            self.reset_events()

    # Function to check for User Events
    def get_events(self):
        # Fetch all the events happening
        for x in pygame.event.get():
            # If the event is closing the window
            if x.type == pygame.QUIT:
                # Close the window
                self.runningState = False
                self.isPlaying = False
            # If a key is pressed
            if x.type == pygame.KEYDOWN:
                # Check for the key and execute the corresponding action
                if x.key == pygame.K_RETURN:
                    # Set the game to start
                    self.START = True
                if x.key == pygame.K_BACKSPACE:
                    # Set the game to go back one step
                    self.BACK = True
                if x.key == pygame.K_DOWN:
                    # Set the cursor to move down
                    self.DOWN = True
                if x.key == pygame.K_UP:
                    # Set the cursor to move up
                    self.UP = True

    # Function to reset all events after each iteration of the loop
    def reset_events(self):
        # Reset all events to False
        self.DOWN = False
        self.UP = False
        self.BACK = False
        self.START = False

    # Function to run the actual game
    def run_game(self):
        # Run all the functions that execute Upon a condition
        self.quit_game()
        self.credits()
        self.startGame()

    # Function to draw some text on the screen
    def draw_text(self, text, size, x, y, color):
        # Create text with the default font type of pygame as specified before and give it the size passed
        font = pygame.font.Font(self.fontType, size)
        # Render the font
        text_surface = font.render(text, True, color)
        # Get the rectangle holding in which the text is encapsulated
        text_rect = text_surface.get_rect()
        # Position center
        text_rect.center = (x, y)
        # Blit the text to the screen
        self.mockup_screen.blit(text_surface, text_rect)

    # Function that will execute once the quit game button is clicked
    def quit_game(self):
        # If the quit game button is clicked
        if self.quitGame_button.user_clicked:
            pygame.quit()
            exit()
    # Function to display credits
    def credits(self):
        # If the credits button is clicked
        if self.credits_button.user_clicked:
            self.draw_text("This software is the intellectual property of Steve Shema. Any and all rights are reserved under his name.",
                           20, (self.infoObject.current_w / 2) - 40,
                           (self.infoObject.current_h / 2) + 170, (235, 250, 250))

    # Function to start the game
    def startGame(self):
        # If the Start Game button is clicked
        if self.startGame_button.user_clicked:
            # CLose current Window
            pygame.quit()
            os.system('python game.py')


