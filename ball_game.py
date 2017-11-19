import pygame
import functions as func
import csv_func
from settings import Settings
from button import Button
from score_stats import ScoreStats
from scoreboard import Scoreboard
from playerstats import Playerstats
from teams import Team


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    bstats_settings = Settings()
    screen = pygame.display.set_mode(
        (bstats_settings.screen_width, bstats_settings.screen_height)
    )
    pygame.display.set_caption("Basketball Scoring")

    # Create an instance to store game statistics.
    stats = ScoreStats(bstats_settings)

    # Create a scoreboard object
    sb = Scoreboard(bstats_settings, screen, stats)

    # Make the play button
    play_button = Button(bstats_settings, screen, "Play")

    # Open Player List CSV, and get players from file in a dictionary
    playerdict = csv_func.read_playersCSV(bstats_settings)

    # List of team objects
    teams = [
        Team(bstats_settings, 'A', -1, 'Home'),
        Team(bstats_settings, 'B', -2, 'Away')
    ]

    # Populate teamlist of team object with correct player
    for team in teams:
        for player in playerdict.values():
            if player.team == team.team:
                team.teamlist.append(player)

    # bstats_settings.get_playerdict(playerdict)

    # Make the stats buttons for players and put it in a dictionary, buttons
    buttons = func.make_stats_buttons(bstats_settings, teams, screen)

    # Create player stats class object
    pstats = Playerstats(bstats_settings, screen, teams)

    # Make a player
    # player = players.Player('Lorelei', 5)

    # Start the main loop for the game.
    while True:

        func.check_events(stats, buttons, playerdict, play_button,
                          bstats_settings, teams)

        func.update_screen(stats, bstats_settings, screen, play_button,
                           buttons, playerdict, sb, pstats, teams)


run_game()
