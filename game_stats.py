class GameStats():
    """Track statics for alien inavation"""

    def __init__(self, ai_settings):
        """Initialize statics"""
        self.ai_settings =ai_settings
        self.reset_stats()
        #Start game in active state
        self.game_active =False

    def reset_stats(self):
        """Initialize statisc tha can chage during the game"""
        self.ship_left =self.ai_settings.ship_limit
        
        #Start alien Invation in an active state
        self.game_active = True
        self.score =0