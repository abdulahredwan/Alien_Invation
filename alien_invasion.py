from email.headerregistry import Group
import pygame

from pygame.sprite import Group
from game_stats import GameStats

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf



def run_game():
    #Initialize pygame, settings, and screen object

    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion BY@abd_red080")

    #Create an instance to store game statisitc
    stats =GameStats(ai_settings)
    #Make a ship
    ship = Ship(ai_settings, screen)

    #Make a group to store bullet in
    bullets =Group()
    aliens = Group()
    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)   
    alien = Alien(ai_settings, screen)
    #Start the main loop for the game

    while True: 

        #Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
        #Redraw the screen during each pass through the loop

        
run_game()