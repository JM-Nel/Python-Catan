import random
from data_structures import plots, roads,

def correct_road_connected_to_plot(plot, player_colour):
    '''Check that the correct road is connected to the given plot where player wants to build a house'''
    for connected_road in plots[plot]['connected_roads']:
        if roads[connected_road]['built'] == player_colour:
            return True
    return False

def correct_road_connected_to_road(road, player_colour):
    '''Check that correct road is connected to spot where player wants to build road.'''
    for connected_road in roads[road]['connected_roads']:
        if roads[connected_road]['built'] == player_colour:
            return True
    return False

def no_house_nearby(plot):
    for connected_plot in plots[plot]['connected_plots']:
        if not (plots[connected_plot]['house'] == None and plots[connected_plot]['city'] == None):
            return False
    return True

def not_build_through_other_player_house(road, player_colour):
    for connected_road in road[road]['connected_roads']:
        if roads[connected_road]['built'] == player_colour:
            true_connected_road = connected_road
            break
    for plot_connected_to_root_road in roads[true_connected_road]['connected_plots']:
        for plot_connected_to_proposed_road in roads[road]['connected_plots']:
            if plot_connected_to_proposed_road == plot_connected_to_root_road:
                check_plot = plot_connected_to_proposed_road
                break

    if plots[check_plot]['house'] == player_colour or plots[check_plot]['house'] == None or plots[check_plot]['city'] == player_colour or plots[check_plot]['city'] == None:
        return True
    else:
        return False

def can_build_road_here(road, player_colour):
    if roads[road]['built'] == None and not_build_through_other_player_house(road, player_colour) and correct_road_connected_to_road(road, player_colour):
        return True
    else:
        return False

def can_build_house_here(plot, player_colour):
    plots[plot]['house'] == None and plots[plot]['city'] == None and correct_road_connected_to_plot(plot, player_colour) and no_house_nearby(plot)
