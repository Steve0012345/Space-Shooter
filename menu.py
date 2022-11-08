# import the pygame Module
import pygame

# Import exit from the sys module
from sys import exit


# The menu class which contains all code for running the menu
class Menu(object):
    # Constructor Function
    def __init__(self, rand_object):
        self.gameObject = rand_object
        # Fetch the di/mensions of the window
        self.width = self.gameObject.infoObject.current_w
        self.height = self.gameObject.infoObject.current_h
        # Variable for controlling the opening and Closing of the menu
        self.runMenu = True
        # Start game Button version of the button
        self.startGame_button = Button("Start Game", 300, 40, (self.width/2, (self.height/2)+30), "#07da63", 6)
        # Credits Button version of the button
        self.credits_button = Button("Credits", 300, 40, (self.width/2, (self.height/2)+80), "#818589", 6)
        # Quit Game Button version of the button
        self.quitGame_button = Button("Quit Game", 300, 40, (self.width / 2, (self.height / 2)+130), "#DC143C", 6)

    # Function to blit the menu onto the mainScreen
    def blit_screen(self):
        # Blit the background onto the screen once more
        self.gameObject.mockup_screen.blit(self.gameObject.bgImage, (0, 0))
        # Update Screen
        pygame.display.update()
        # Reset all keyboard flags
        self.gameObject.reset_events()


# The class for the Main Menu
class MainMenu(Menu):
    # Constructor method
    def __init__(self, rand_object):
        Menu.__init__(self, rand_object)

    # Function to display the menu
    def display_menu(self):
        self.runMenu = True
        # Enter the mainloop
        while self.runMenu:
            # Check for input on every iteration
            self.check_input()
            # Blit the background onto the screen once more
            self.gameObject.mockup_screen.blit(self.gameObject.bgImage, (0, 0))
            # Draw the title of the menu as text
            self.gameObject.draw_text("Space Shooter by Steve Shema", 20, self.width / 2, self.height/2 - 20)
            # Draw the start Game Button on the screen
            self.startGame_button.draw(self.gameObject.mockup_screen)
            # Draw the Credits Button on the screen
            self.credits_button.draw(self.gameObject.mockup_screen)
            # Draw the Quit Game Button on the screen
            self.quitGame_button.draw(self.gameObject.mockup_screen)
            # Blit all this to the Screen
            self.blit_screen()

    # Check for user input
    def check_input(self):
        # If the start game button is clicked
        if self.startGame_button.user_clicked:
            # Change the self.Run Menu to false
            self.runMenu = False


# Button class
class Button(object):
    # Constructor Method
    def __init__(self, text, width, height, pos, hover_color, elevation):
        # Elevation of the button
        self.elevation = elevation
        # Dynamic variable used when hovering over the button with the mouse
        self.dynamic_elevation = elevation
        # Hover color of the Button
        self.hover_color = hover_color
        # Create a mechanism to also keep the original Y position of the button
        self.original_yCordinate = pos[1]
        # Variable to keep the state of pressing of the button
        self.pressed = False
        # Click variable
        self.user_clicked = False

        # The top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = "#0492C2"

        # The bottom Rectangle
        self.bottom_rect = pygame.Rect(pos, (width, self.elevation))
        self.bottom_color = "#E81E63"

        # Font Configuration
        # Set the font Type to be used
        self.fontType = pygame.font.get_default_font()

        # Create text with the default font type of pygame as specified before and give it the size passed
        font = pygame.font.Font(self.fontType, 15)
        # Text Surface
        self.text_surf = font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    # Draw the Rectangle On the Screen
    def draw(self, screen):
        # Implementation of the Elevation Logic
        self.top_rect.y = self.original_yCordinate - self.dynamic_elevation
        # Once again Align the text to the center of the button
        self.text_rect.center = self.top_rect.center

        # Define the positioning of the bottom rectangle
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        # Draw the Bottom Rectangle
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        # Assign the appropriate parameters to the rectangle
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        # Check for the click event
        self.check_for_click()

    # Function to handle the clicking of the button
    def check_for_click(self):
        # Pygame provides us with a mechanism for getting the mouse position
        mouse_position = pygame.mouse.get_pos()
        # Detect for mouse clicks or other collisions with the rectangle
        if self.top_rect.collidepoint(mouse_position):
            # If the mouse hovers over the button
            self.top_color = self.hover_color
            # Check for which mouse button was pressed
            if pygame.mouse.get_pressed()[0]:
                # Set the elevation to zero
                self.dynamic_elevation = 0
                # Set the pressed to True
                self.pressed = True
            # When the player stops pressing the button
            else:
                # Set the elevation back to normal
                self.dynamic_elevation = self.elevation
                # If the user had already clicked the Left Mouse Button
                if self.pressed:
                    self.user_clicked = True
                    # set the self.pressed back to false
                    self.pressed = False
        # If the Mouse is no longer hovering over the button
        else:
            # Set the elevation back to normal
            self.dynamic_elevation = self.elevation
            # Return the button to its original Color
            self.top_color = "#0492C2"
