from email.headerregistry import Group
import pygame

from pygame.sprite import Group
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

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

    #Make the play Button
    play_button = Button(ai_settings, screen, "Play")
    #Create an instance to store game statisitc
    stats =GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
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
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,bullets, play_button)
        
        #Redraw the screen during each pass through the loop

        
run_game()