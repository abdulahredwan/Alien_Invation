class Settings():
    """A class to store all settings for alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color =(230, 230, 230)

        #Ship settingsq
        self.ship_speed_factor =1.5

        #Bullet settings
        self.bullet_speed_factor =3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =60, 60, 60
        self.bullets_allowed =3

        #Alien serrings
        self.alien_speed_factor = 1
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right: -1 represent left
        self.fleet_direction = 1
