# functions.py - the functions called in Ball Game Stats
# Author:       Dan Retonel
# Date:         20 Sept 2017
# Contains all the functions that run within the Ball Game Stats

import sys
import re
import pygame
import csvfunc
from button import Button


def check_keydown_events(event, stats):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        stats.reset_stats()
    elif event.key == pygame.K_e:
        stats.edit_stats()
    # elif event.key == pygame.K_LEFT:
        # something2


def check_keyup_events(event, stats):
    """Respond to key releases"""
    # if event.key == pygame.K_RIGHT:
    #     false something1
    # elif event.key == pygame.K_LEFT:
    #     false something2


def check_play_button(stats, play_button, mouse_x, mouse_y):
    """Start a new game when the user clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.game_active = True


def check_player_buttons(stats, buttons, playerdict, teams,
                         runScore, mouse_x, mouse_y):
    """Check fg button presses and add stat to player."""
    if stats.game_active:
        for key, button in buttons.items():
            button_clicked = button.rect.collidepoint(mouse_x, mouse_y)

            if "_fg" in key and "_fga" not in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.fg_made(stats.editFlag)
                        runScore.update_rs(person, stats.editFlag)
                        stats.statChange = True
                        break

            if "_fga" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.fg_att(stats.editFlag)
                        stats.statChange = True
                        break

            if "_3pt" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.threeP_made(stats.editFlag)
                        runScore.update_rs(person, stats.editFlag)
                        stats.statChange = True
                        break

            if '_3pa' in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.threeP_att(stats.editFlag)
                        stats.statChange = True
                        break

            if '_ft' in key and "fta" not in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.ft_made(stats.editFlag)
                        runScore.update_rs(person, stats.editFlag)
                        stats.statChange = True
                        break

            if '_fta' in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.fta += 1 - (2 * int(stats.editFlag))
                        stats.statChange = True
                        break

            if "_ast" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.ast += 1 - (2 * int(stats.editFlag))
                        stats.statChange = True
                        break

            if "_orb" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.orb += 1 - (2 * int(stats.editFlag))
                        person.update_rb()
                        stats.statChange = True
                        break

            if "_drb" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.drb += 1 - (2 * int(stats.editFlag))
                        person.update_rb()
                        stats.statChange = True
                        break

            if "_stl" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.stl += 1 - (2 * int(stats.editFlag))
                        stats.statChange = True
                        break

            if "_blk" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.blk += 1 - (2 * int(stats.editFlag))
                        stats.statChange = True
                        break

            if "_tov" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.tov += 1 - (2 * int(stats.editFlag))
                        stats.statChange = True
                        break

            if "_pf" in key:
                for person in playerdict.values():
                    if re.match(person.name, key) and button_clicked:
                        person.pf += 1 - (2 * int(stats.editFlag))
                        stats.statChange = True
                        break


def make_stats_buttons(bstats_settings, teams, screen):
    """Make the stats buttons for players and return dict, buttons"""
    buttons = {}

    # Variables for building buttons
    homecount = 0
    awaycount = 0

    for team in teams:
        for player in sorted(team.teamlist, key=lambda player: player.name):
            if player.team == 'Away':
                offset = bstats_settings.screen_width / 2
                awaycount += 1
                i = awaycount
            elif player.team == 'Home':
                offset = 0
                homecount += 1
                i = homecount

            for index, msg in enumerate(player.stats):
                buttons[player.name + '_' + msg] = \
                    Button(bstats_settings, screen, msg, index, i, offset)

    return buttons


def team_results(teams):
    """Fill the proper value of win/loss """

    team1Pts = 0

    for i, team in enumerate(teams):
        if i == 0:
            team1Pts = team.pts
            continue
        if team1Pts > team.pts:
            teams[i-1].win = 1
            team.loss = 1
        else:
            team.win = 1
            teams[i-1].loss = 1


def check_events(stats, buttons, playerdict, play_button, bstats_settings,
                 teams, runScore):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():

        # Event is Quit ? write CSV then close program
        if event.type == pygame.QUIT:
            team_results(teams)
            csvfunc.write_CSV(bstats_settings, teams, runScore)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, stats)
#        elif event.type == pygame.KEYUP:
#            check_keyup_events(event, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
            check_player_buttons(stats, buttons, playerdict, teams,
                                 runScore, mouse_x, mouse_y)


def update_screen(stats, bstats_settings, screen, button,
                  buttons, playerdict, sb, pstats, teams, runScore):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen during each pass through the loop.
    screen.fill(bstats_settings.bg_color)

    if stats.statChange:
        for team in teams:
            team.update_stats()
        stats.statChange = False

    # Update the score
    stats.update_score(teams)

    # Draw the score information.
    sb.prep_home_score()
    sb.prep_away_score()

    # Draw player stats
    # pstats.prep_stats_header()
    # pstats.show_stats()
    pstats.prep_stats()

    runScore.prep_rs()

    # Edit Mode ? Show Edit Mode String
    if stats.editFlag:
        pstats.prep_editmode_str()

    # Draw the stats buttons for players
    for key, value in buttons.items():
        value.draw_button()

    # Make lines
#    bstats_lines.drawHouse(0, bstats_settings.screen_height,\
#        bstats_settings.screen_width,\
#        bstats_settings.screen_height, screen, (0, 0, 0))

#    for i, x in stats.score.items():
#        print(i + ' ' + str(x) + '\n')

#    for i, person in playerdict.items():
#        print(person.name + ' ' + str(person.fg) + ' ' + str(person.threeP)\
#            + ' ' +    str(person.ast) + ' ' + str(person.orb) + ' '\
#            + str(person.drb) + ' ' + str(person.stl) + ' '\
#            + str(person.blk) + ' ' + str(person.tov) + ' '\
#            + str(person.pf))

    # Draw the Play button
    if not stats.game_active:
        button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
