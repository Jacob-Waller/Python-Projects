import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

  #Initalize pygame, settings and screen object
  pygame.init()

  ai_settings = Settings()
  screen = pygame.display.set_mode(
      (ai_settings.screen_width, ai_settings.screen_height))
  

  pygame.display.set_caption("Alien Invasion")

  # Make a shnip
  ship = Ship(screen)

  # Set the background color
  bg_color = (230, 230, 230)
  
  #Start of the main loop for the game
  while True:
  
    #Watches for keyboard and mouse events
    gf.check_events(ship)
    ship.update()
    gf.update_screen(ai_settings, screen, ship)
    
run_game()
