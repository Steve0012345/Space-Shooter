# Import external classes
import gameMockup

# Create instance of gameMockup
mockup = gameMockup.GameMockup()

# Second mainloop loop to control the flow of the game
while mockup.runningState:
    # Set isPlaying to True
    mockup.isPlaying = True
    # Run the mainloop in the Mockup File
    mockup.main_loop()
