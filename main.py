import sys

Import pygam

def run_game():
  #This will initalize the game and create a screen object
  pygame.init()
  screen = pygame.display.set_mode((1200, 800))
  pygame.display.set_caption("Alien Invasion")
  
  #Start of the main loop for the game
  while True:
  
    #Watches for keyboard and mouse events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
        
    # Make the most recently drawn screen visible
    pygame.display.flip()
    
run_game()
