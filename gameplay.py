import time
from random import randint
from data_structures import plots, roads, dev_cards, players, colours, hexes, resource_tiles, numbers, hexes_sorted

#Internal functions - These will not change when GUI is created

def correct_road_connected_to_plot(plot, player_no):
    '''Check that the correct road is connected to the given plot where player wants to build a house'''
    for connected_road in plots[plot]['connected_roads']:
        if roads[connected_road]['built'] == player_no:
            return True
    return False

def correct_road_connected_to_road(road, player_no):
    '''Check that correct road is connected to spot where player wants to build road.'''
    for connected_road in roads[road]['connected_roads']:
        if roads[connected_road]['built'] == player_no:
            return True
    return False

def no_house_nearby(plot):
    for connected_plot in plots[plot]['connected_plots']:
        if not (plots[connected_plot]['house'] == None and plots[connected_plot]['city'] == None):
            return False
    return True

def not_build_through_other_player_house(road, player_no):
    for connected_road in road[road]['connected_roads']:
        if roads[connected_road]['built'] == player_no:
            true_connected_road = connected_road
            break
    for plot_connected_to_root_road in roads[true_connected_road]['connected_plots']:
        for plot_connected_to_proposed_road in roads[road]['connected_plots']:
            if plot_connected_to_proposed_road == plot_connected_to_root_road:
                check_plot = plot_connected_to_proposed_road
                break

    if plots[check_plot]['house'] == player_no or plots[check_plot]['house'] == None or plots[check_plot]['city'] == player_no or plots[check_plot]['city'] == None:
        return True
    else:
        return False

def can_build_road_here(road, player_no):
    if roads[road]['built'] == None and not_build_through_other_player_house(road, player_no) and correct_road_connected_to_road(road, player_no):
        return True
    else:
        return False

def can_build_house_here(plot, player_no):
    return plots[plot]['house'] == None and plots[plot]['city'] == None and correct_road_connected_to_plot(plot, player_no) and no_house_nearby(plot)

def roll_2_dice():
    return randint(1, 6) + randint(1, 6)

def roll_1_di():
    return randint(1, 6)

def player_to_play(round_counter, no_of_players):
    player = round_counter % no_of_players
    if player is 0:
        return str(no_of_players)
    else:
        return str(round_counter % no_of_players)

def check_house_connected_to_road(player, road):
    for settlement in roads[road]['connected_plots']:
        if plots[settlement]['house'] == player:
            return True
    return False



# Command line catan - Will rewrite these for the GUI

def print_scores():
    print "Player scores are as follows: "
    for player in players:
        print '%s : %s' % (players[player]['name'], players[player]['score'])


def initial_setup():

    global no_of_players
    while 1:
        try:

            no_of_players = int(raw_input('How many players will play? '))
            assert no_of_players >= 2 and no_of_players <= 4
            break
        except:
            print 'Please enter an integer between 2 and 4'

    #remove player not playing in player
    for playa in range(1, 5):
        if playa > no_of_players:
            players.pop(str(playa))

    for i in range(1, no_of_players + 1):
        players[str(i)]['name'] = raw_input('Please enter the name for player %s ' % i)
        print '%s, available colours are: ' % players[str(i)]['name']
        for x in colours:
            print x
        while 1:
            try:
                colour_selected = raw_input('Please select a colour ')
                assert colour_selected in colours
                players[str(i)]['colour'] = colour_selected
                colours.remove(colour_selected)
                break
            except:
                print 'Selected colour is not one of the available colours. \nColours currently available: '
                for x in colours:
                    print x

    print 'Players and colours are as follows:'
    for player in players:
            print players[player]['name'], " - ", players[player]['colour']

    time.sleep(2)

    #Populate the board
    for hex in hexes:
        hexes[hex]['resource'] = resource_tiles.pop((randint(0, len(resource_tiles) - 1)))
        if hexes[hex]['resource'] != 'desert':
            hexes[hex]['number'] = numbers.pop((randint(0, len(numbers) - 1)))

    print 'The board has been populated as follows: '
    for hex in hexes_sorted:
        print '%s - resource is %s, number is %s' % (hex, hexes[hex]['resource'], hexes[hex]['number'])

    time.sleep(2)

    #Checking who begins

    print "dice roll to see who's to begin the placing"
    peoples_to_roll = []
    for player in players:
        peoples_to_roll.append(player)

    while 1:
        rolled_by_players = {}
        rolls = []

        for player in peoples_to_roll:
            roll = roll_1_di()
            print '%s rolled a %s' % (players[player]['name'], roll)
            rolled_by_players[player] = roll
            rolls.append(roll)

        best_roll = max(rolls)
        peoples_to_roll = []
        for roller in rolled_by_players:
            if rolled_by_players[roller] == best_roll:
                peoples_to_roll.append(roller)

        if len(peoples_to_roll) == 1:
            break
        else:
            print "There's a tie"
            for person in peoples_to_roll:
                print ' ' + players[person]['name']
            print "Needs to roll again"

    best_roller = peoples_to_roll[0]
    print '%s had the highest roll with %s, and will begin' % (players[best_roller]['name'], best_roll)
    round_counter = int(best_roller)
    players_placing = []
    counter = int(best_roller)
    for i in players:
        players_placing.append(player_to_play(counter, no_of_players))
        counter += 1

    #do the initial settlement and road placement

    #house placement part

    for placement_way in [1, -1]:
        for player_to_place in players_placing[::placement_way]:
            while 1:
                house_placement = raw_input('%s, please make your house placement ' % players[player_to_place]['name'])
                try:
                    assert plots[house_placement]['house'] == None
                    assert no_house_nearby(house_placement)
                    break
                except AssertionError:
                    print "You can't built here, please try again."

            # Do road placements
            while 1:
                try:
                    print '%s, please make your road placement. \n Options are: ' % players[player_to_place]['name']
                    for road in plots[house_placement]['connected_roads']:
                        print ' ' + road
                    road_placement = raw_input('%s, please select one of these roads ' % players[player_to_place]['name'])
                    assert road_placement in plots[house_placement]['connected_roads']
                    break
                except AssertionError:
                    print 'Selected road is not one of the available options '

            plots[house_placement]['house'] = player_to_place
            roads[road_placement]['built'] = player_to_place
            print '%s Made a placement at plot no %s and a road placement at road %s ' % (players[player_to_place]['name'], house_placement, road_placement)

            if placement_way == -1:
                for tile in hexes:
                    if hexes[tile]['resource'] == 'desert':
                        continue
                    if house_placement in hexes[tile]['plots']:
                        players[player_to_place]['resources'][hexes[tile]['resource']] += 1
                        print "%s received 1 %s" % (players[player_to_place]['name'], hexes[tile]['resource'])

    for player in players:
        players[player]['score'] += 2

    print_scores()
    return round_counter





initial_setup()