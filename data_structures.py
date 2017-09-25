#This files contains all of the required data structures
#
#Please refer to the "map_to_explain_data_structures" for graphical representation of how data structures work
#
#The following dictionaries are used
#   plots - represent the points where three hexes meet
#         - these are the spots where settlements (houses) can be built
#         - numbered from on to 1 to 54
#
#   roads - lines that connect two plots
#         - possible spaces where roads can be built
#
#   hexes - represent the hexes (tiles) on the board
#
#   players -
#
#
#
#

hexes_sorted = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']

no_of_players = None
round_counter = None

plots = {
    '1': {
        'house': None,
        'city': None,
        'connected_roads': ['1_5', '1_4'],
        'connected_plots': ['5', '4'],
        'harbour': None
    },

    '2': {
        'house': None,
        'city': None,
        'connected_roads': ['2_5', '2_6'],
        'connected_plots': ['5', '6'],
        'harbour': None
    },

    '3': {
        'house': None,
        'city': None,
        'connected_roads': ['3_7', '3_6'],
        'connected_plots': ['7', '6'],
        'harbour': None
    },

    '4': {
        'house': None,
        'city': None,
        'connected_roads': ['1_4', '4_8'],
        'connected_plots': ['1', '8'],
        'harbour': None
    },

    '5': {
        'house': None,
        'city': None,
        'connected_roads': ['1_5', '2_5', '5_9'],
        'connected_plots': ['1', '2', '9'],
        'harbour': None
    },

    '6': {
        'house': None,
        'city': None,
        'connected_roads': ['3_6', '2_6', '6_10'],
        'connected_plots': ['3', '2', '10'],
        'harbour': None
    },

    '7': {
        'house': None,
        'city': None,
        'connected_roads': ['3_7', '7_11'],
        'connected_plots': ['3', '11'],
        'harbour': None
    },

    '8': {
        'house': None,
        'city': None,
        'connected_roads': ['8_12', '8_13', '4_8'],
        'connected_plots': ['12', '13', '4'],
        'harbour': None
    },

    '9': {
        'house': None,
        'city': None,
        'connected_roads': ['5_9', '9_13', '9_14'],
        'connected_plots': ['5', '13', '14'],
        'harbour': None
    },

    '10': {
        'house': None,
        'city': None,
        'connected_roads': ['10_14', '10_15', '6_10'],
        'connected_plots': ['14', '15', '6'],
        'harbour': None
    },

    '11': {
        'house': None,
        'city': None,
        'connected_roads': ['7_11', '11_16', '11_15'],
        'connected_plots': ['7', '16', '15'],
        'harbour': None
    },

    '12': {
        'house': None,
        'city': None,
        'connected_roads': ['8_12', '12_17'],
        'connected_plots': ['8', '17'],
        'harbour': None
    },

    '13': {
        'house': None,
        'city': None,
        'connected_roads': ['8_13', '13_18', '9_13'],
        'connected_plots': ['8', '18', '9'],
        'harbour': None
    },

    '14': {
        'house': None,
        'city': None,
        'connected_roads': ['14_19', '10_14', '9_14'],
        'connected_plots': ['19', '10', '9'],
        'harbour': None
    },

    '15': {
        'house': None,
        'city': None,
        'connected_roads': ['10_15', '15_20', '11_15'],
        'connected_plots': ['10', '20', '11'],
        'harbour': None
    },

    '16': {
        'house': None,
        'city': None,
        'connected_roads': ['16_21', '11_16'],
        'connected_plots': ['21', '11'],
        'harbour': None
    },

    '17': {
        'house': None,
        'city': None,
        'connected_roads': ['17_23', '12_17', '17_22'],
        'connected_plots': ['23', '12', '22'],
        'harbour': None
    },

    '18': {
        'house': None,
        'city': None,
        'connected_roads': ['13_18', '18_24', '18_23'],
        'connected_plots': ['13', '24', '23'],
        'harbour': None
    },

    '19': {
        'house': None,
        'city': None,
        'connected_roads': ['19_24', '19_25', '14_19'],
        'connected_plots': ['24', '25', '14'],
        'harbour': None
    },

    '20': {
        'house': None,
        'city': None,
        'connected_roads': ['20_26', '20_25', '15_20'],
        'connected_plots': ['26', '25', '15'],
        'harbour': None
    },

    '21': {
        'house': None,
        'city': None,
        'connected_roads': ['21_27', '21_26', '16_21'],
        'connected_plots': ['27', '26', '16'],
        'harbour': None
    },

    '22': {
        'house': None,
        'city': None,
        'connected_roads': ['22_28', '17_22'],
        'connected_plots': ['28', '17'],
        'harbour': None
    },

    '23': {
        'house': None,
        'city': None,
        'connected_roads': ['23_29', '17_23', '18_23'],
        'connected_plots': ['29', '17', '18'],
        'harbour': None
    },

    '24': {
        'house': None,
        'city': None,
        'connected_roads': ['19_24', '18_24', '24_30'],
        'connected_plots': ['19', '18', '30'],
        'harbour': None
    },

    '25': {
        'house': None,
        'city': None,
        'connected_roads': ['19_25', '25_31', '20_25'],
        'connected_plots': ['19', '31', '20'],
        'harbour': None
    },

    '26': {
        'house': None,
        'city': None,
        'connected_roads': ['21_26', '20_26', '26_32'],
        'connected_plots': ['21', '20', '32'],
        'harbour': None
    },

    '27': {
        'house': None,
        'city': None,
        'connected_roads': ['21_27', '27_33'],
        'connected_plots': ['21', '33'],
        'harbour': None
    },

    '28': {
        'house': None,
        'city': None,
        'connected_roads': ['28_34', '22_28'],
        'connected_plots': ['34', '22'],
        'harbour': None
    },

    '29': {
        'house': None,
        'city': None,
        'connected_roads': ['23_29', '29_34', '29_35'],
        'connected_plots': ['23', '34', '35'],
        'harbour': None
    },

    '30': {
        'house': None,
        'city': None,
        'connected_roads': ['24_30', '30_35', '30_36'],
        'connected_plots': ['24', '35', '36'],
        'harbour': None
    },

    '31': {
        'house': None,
        'city': None,
        'connected_roads': ['25_31', '31_37', '31_36'],
        'connected_plots': ['25', '37', '36'],
        'harbour': None
    },

    '32': {
        'house': None,
        'city': None,
        'connected_roads': ['32_38', '26_32'],
        'connected_plots': ['38', '26'],
        'harbour': None
    },

    '33': {
        'house': None,
        'city': None,
        'connected_roads': ['27_33', '33_38'],
        'connected_plots': ['27', '38'],
        'harbour': None
    },

    '34': {
        'house': None,
        'city': None,
        'connected_roads': ['28_34', '34_39', '29_34'],
        'connected_plots': ['28', '39', '29'],
        'harbour': None
    },

    '35': {
        'house': None,
        'city': None,
        'connected_roads': ['35_40', '30_35', '29_35'],
        'connected_plots': ['40', '30', '29'],
        'harbour': None
    },

    '36': {
        'house': None,
        'city': None,
        'connected_roads': ['31_36', '30_36', '36_41'],
        'connected_plots': ['31', '30', '41'],
        'harbour': None
    },

    '37': {
        'house': None,
        'city': None,
        'connected_roads': ['37_42', '31_37'],
        'connected_plots': ['42', '31'],
        'harbour': None
    },

    '38': {
        'house': None,
        'city': None,
        'connected_roads': ['32_38', '38_43', '33_38'],
        'connected_plots': ['32', '43', '33'],
        'harbour': None
    },

    '39': {
        'house': None,
        'city': None,
        'connected_roads': ['39_44', '34_39'],
        'connected_plots': ['44', '34'],
        'harbour': None
    },

    '40': {
        'house': None,
        'city': None,
        'connected_roads': ['35_40', '40_44', '40_45'],
        'connected_plots': ['35', '44', '45'],
        'harbour': None
    },

    '41': {
        'house': None,
        'city': None,
        'connected_roads': ['41_45', '41_46', '36_41'],
        'connected_plots': ['45', '46', '36'],
        'harbour': None
    },

    '42': {
        'house': None,
        'city': None,
        'connected_roads': ['37_42', '42_47', '42_46'],
        'connected_plots': ['37', '47', '46'],
        'harbour': None
    },

    '43': {
        'house': None,
        'city': None,
        'connected_roads': ['43_47', '38_43'],
        'connected_plots': ['47', '38'],
        'harbour': None
    },

    '44': {
        'house': None,
        'city': None,
        'connected_roads': ['44_48', '39_44', '40_44'],
        'connected_plots': ['48', '39', '40'],
        'harbour': None
    },

    '45': {
        'house': None,
        'city': None,
        'connected_roads': ['41_45', '40_45', '45_49'],
        'connected_plots': ['41', '40', '49'],
        'harbour': None
    },

    '46': {
        'house': None,
        'city': None,
        'connected_roads': ['46_50', '41_46', '42_46'],
        'connected_plots': ['50', '41', '42'],
        'harbour': None
    },

    '47': {
        'house': None,
        'city': None,
        'connected_roads': ['43_47', '47_51', '42_47'],
        'connected_plots': ['43', '51', '42'],
        'harbour': None
    },

    '48': {
        'house': None,
        'city': None,
        'connected_roads': ['44_48', '48_52'],
        'connected_plots': ['44', '52'],
        'harbour': None
    },

    '49': {
        'house': None,
        'city': None,
        'connected_roads': ['49_52', '49_53', '45_49'],
        'connected_plots': ['52', '53', '45'],
        'harbour': None
    },

    '50': {
        'house': None,
        'city': None,
        'connected_roads': ['46_50', '50_54', '50_53'],
        'connected_plots': ['46', '54', '53'],
        'harbour': None
    },

    '51': {
        'house': None,
        'city': None,
        'connected_roads': ['51_54', '47_51'],
        'connected_plots': ['54', '47'],
        'harbour': None
    },

    '52': {
        'house': None,
        'city': None,
        'connected_roads': ['49_52', '48_52'],
        'connected_plots': ['49', '48'],
        'harbour': None
    },

    '53': {
        'house': None,
        'city': None,
        'connected_roads': ['50_53', '49_53'],
        'connected_plots': ['50', '49'],
        'harbour': None
    },

    '54': {
        'house': None,
        'city': None,
        'connected_roads': ['51_54', '50_54'],
        'connected_plots': ['51', '50'],
        'harbour': None
    }
}

hexes = {
    'A': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['1', '4', '5', '8', '9', '13']},

    'B': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['2', '5', '6', '9', '10', '14']},

    'C': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['3', '6', '7', '10', '11', '15']},

    'D': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['8', '12', '13', '17', '18', '23']},

    'E': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['9', '13', '14', '18', '19', '24']},

    'F': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['10', '14', '15', '19', '20', '25']},

    'G': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['11', '15', '16', '20', '21', '26']},

    'H': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['17', '22', '23', '28', '29', '34']},

    'I': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['18', '23', '24', '29', '30', '35']},

    'J': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['19', '24', '25', '30', '31', '36']},

    'K': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['20', '25', '26', '31', '32', '37']},

    'L': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['21', '26', '27', '32', '33', '38']},

    'M': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['29', '34', '35', '39', '40', '46']},

    'N': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['30', '35', '36', '40', '41', '47']},

    'O': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['31', '36', '37', '41', '42', '48']},

    'P': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['32', '37', '38', '42', '43', '49']},

    'Q': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['40', '44', '45', '48', '49', '52']},

    'R': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['41', '45', '46', '49', '50', '53']},

    'S': {'number': None,
          'resource': None,
          'robber': None,
          'plots': ['42', '46', '47', '50', '51', '54']}}

roads = {
    '1_4': {
        'built': None,
        'connected_roads': ['1_5', '4_8'],
        'connected_plots': ['1', '4']
    },

    '1_5': {
        'built': None,
        'connected_roads': ['1_4', '2_5', '5_9'],
        'connected_plots': ['1', '5']
    },

    '2_5': {
        'built': None,
        'connected_roads': ['2_6', '1_5', '5_9'],
        'connected_plots': ['2', '5']
    },

    '2_6': {
        'built': None,
        'connected_roads': ['2_5', '3_6', '6_10'],
        'connected_plots': ['2', '6']
    },

    '3_6': {
        'built': None,
        'connected_roads': ['3_7', '2_6', '6_10'],
        'connected_plots': ['3', '6']
    },

    '3_7': {
        'built': None,
        'connected_roads': ['3_6', '7_11'],
        'connected_plots': ['3', '7']
    },

    '4_8': {
        'built': None,
        'connected_roads': ['1_4', '8_12', '8_13'],
        'connected_plots': ['4', '8']
    },

    '5_9': {
        'built': None,
        'connected_roads': ['1_5', '2_5', '9_13', '9_14'],
        'connected_plots': ['5', '9']
    },

    '6_10': {
        'built': None,
        'connected_roads': ['3_6', '2_6', '10_14', '10_15'],
        'connected_plots': ['6', '10']
    },

    '7_11': {
        'built': None,
        'connected_roads': ['3_7', '11_16', '11_15'],
        'connected_plots': ['7', '11']
    },

    '8_12': {
        'built': None,
        'connected_roads': ['8_13', '4_8', '12_17'],
        'connected_plots': ['8', '12']
    },

    '8_13': {
        'built': None,
        'connected_roads': ['8_12', '4_8', '13_18', '9_13'],
        'connected_plots': ['8', '13']
    },

    '9_13': {
        'built': None,
        'connected_roads': ['5_9', '9_14', '8_13', '13_18'],
        'connected_plots': ['9', '13']
    },

    '9_14': {
        'built': None,
        'connected_roads': ['5_9', '9_13', '14_19', '10_14'],
        'connected_plots': ['9', '14']
    },

    '10_14': {
        'built': None,
        'connected_roads': ['10_15', '6_10', '14_19', '9_14'],
        'connected_plots': ['10', '14']
    },

    '10_15': {
        'built': None,
        'connected_roads': ['10_14', '6_10', '15_20', '11_15'],
        'connected_plots': ['10', '15']
    },

    '11_15': {
        'built': None,
        'connected_roads': ['7_11', '11_16', '10_15', '15_20'],
        'connected_plots': ['11', '15']
    },

    '11_16': {
        'built': None,
        'connected_roads': ['7_11', '11_15', '16_21'],
        'connected_plots': ['11', '16']
    },

    '12_17': {
        'built': None,
        'connected_roads': ['8_12', '17_23', '17_22'],
        'connected_plots': ['12', '17']
    },

    '13_18': {
        'built': None,
        'connected_roads': ['8_13', '9_13', '18_24', '18_23'],
        'connected_plots': ['13', '18']
    },

    '14_19': {
        'built': None,
        'connected_roads': ['10_14', '9_14', '19_24', '19_25'],
        'connected_plots': ['14', '19']
    },

    '15_20': {
        'built': None,
        'connected_roads': ['10_15', '11_15', '20_26', '20_25'],
        'connected_plots': ['15', '20']
    },

    '16_21': {
        'built': None,
        'connected_roads': ['11_16', '21_27', '21_26'],
        'connected_plots': ['16', '21']
    },

    '17_22': {
        'built': None,
        'connected_roads': ['17_23', '12_17', '22_28'],
        'connected_plots': ['17', '22']
    },

    '17_23': {
        'built': None,
        'connected_roads': ['12_17', '17_22', '23_29', '18_23'],
        'connected_plots': ['17', '23']
    },

    '18_23': {
        'built': None,
        'connected_roads': ['13_18', '18_24', '23_29', '17_23'],
        'connected_plots': ['18', '23']
    },

    '18_24': {
        'built': None,
        'connected_roads': ['13_18', '18_23', '19_24', '24_30'],
        'connected_plots': ['18', '24']
    },

    '19_24': {
        'built': None,
        'connected_roads': ['19_25', '14_19', '18_24', '24_30'],
        'connected_plots': ['19', '24']
    },

    '19_25': {
        'built': None,
        'connected_roads': ['19_24', '14_19', '25_31', '20_25'],
        'connected_plots': ['19', '25']
    },

    '20_25': {
        'built': None,
        'connected_roads': ['20_26', '15_20', '19_25', '25_31'],
        'connected_plots': ['20', '25']
    },

    '20_26': {
        'built': None,
        'connected_roads': ['20_25', '15_20', '21_26', '26_32'],
        'connected_plots': ['20', '26']
    },

    '21_26': {
        'built': None,
        'connected_roads': ['21_27', '16_21', '20_26', '26_32'],
        'connected_plots': ['21', '26']
    },

    '21_27': {
        'built': None,
        'connected_roads': ['21_26', '16_21', '27_33'],
        'connected_plots': ['21', '27']
    },

    '22_28': {
        'built': None,
        'connected_roads': ['17_22', '28_34'],
        'connected_plots': ['22', '28']
    },

    '23_29': {
        'built': None,
        'connected_roads': ['17_23', '18_23', '29_34', '29_35'],
        'connected_plots': ['23', '29']
    },

    '24_30': {
        'built': None,
        'connected_roads': ['19_24', '18_24', '30_35', '30_36'],
        'connected_plots': ['24', '30']
    },

    '25_31': {
        'built': None,
        'connected_roads': ['19_25', '20_25', '31_37', '31_36'],
        'connected_plots': ['25', '31']
    },

    '26_32': {
        'built': None,
        'connected_roads': ['21_26', '20_26', '32_38'],
        'connected_plots': ['26', '32']
    },

    '27_33': {
        'built': None,
        'connected_roads': ['21_27', '33_38'],
        'connected_plots': ['27', '33']
    },

    '28_34': {
        'built': None,
        'connected_roads': ['22_28', '34_39', '29_34'],
        'connected_plots': ['28', '34']
    },

    '29_34': {
        'built': None,
        'connected_roads': ['23_29', '29_35', '28_34', '34_39'],
        'connected_plots': ['29', '34']
    },

    '29_35': {
        'built': None,
        'connected_roads': ['23_29', '29_34', '35_40', '30_35'],
        'connected_plots': ['29', '35']
    },

    '30_35': {
        'built': None,
        'connected_roads': ['24_30', '30_36', '35_40', '29_35'],
        'connected_plots': ['30', '35']
    },

    '30_36': {
        'built': None,
        'connected_roads': ['24_30', '30_35', '31_36', '36_41'],
        'connected_plots': ['30', '36']
    },

    '31_36': {
        'built': None,
        'connected_roads': ['25_31', '31_37', '30_36', '36_41'],
        'connected_plots': ['31', '36']
    },

    '31_37': {
        'built': None,
        'connected_roads': ['25_31', '31_36', '37_42'],
        'connected_plots': ['31', '37']
    },

    '32_38': {
        'built': None,
        'connected_roads': ['26_32', '38_43', '33_38'],
        'connected_plots': ['32', '38']
    },

    '33_38': {
        'built': None,
        'connected_roads': ['27_33', '32_38', '38_43'],
        'connected_plots': ['33', '38']
    },

    '34_39': {
        'built': None,
        'connected_roads': ['28_34', '29_34', '39_44'],
        'connected_plots': ['34', '39']
    },

    '35_40': {
        'built': None,
        'connected_roads': ['30_35', '29_35', '40_44', '40_45'],
        'connected_plots': ['35', '40']
    },

    '36_41': {
        'built': None,
        'connected_roads': ['31_36', '30_36', '41_45', '41_46'],
        'connected_plots': ['36', '41']
    },

    '37_42': {
        'built': None,
        'connected_roads': ['31_37', '42_47', '42_46'],
        'connected_plots': ['37', '42']
    },

    '38_43': {
        'built': None,
        'connected_roads': ['32_38', '33_38', '43_47'],
        'connected_plots': ['38', '43']
    },

    '39_44': {
        'built': None,
        'connected_roads': ['34_39', '44_48', '40_44'],
        'connected_plots': ['39', '44']
    },

    '40_44': {
        'built': None,
        'connected_roads': ['35_40', '40_45', '44_48', '39_44'],
        'connected_plots': ['40', '44']
    },

    '40_45': {
        'built': None,
        'connected_roads': ['35_40', '40_44', '41_45', '45_49'],
        'connected_plots': ['40', '45']
    },

    '41_45': {
        'built': None,
        'connected_roads': ['41_46', '36_41', '40_45', '45_49'],
        'connected_plots': ['41', '45']
    },

    '41_46': {
        'built': None,
        'connected_roads': ['41_45', '36_41', '46_50', '42_46'],
        'connected_plots': ['41', '46']
    },

    '42_46': {
        'built': None,
        'connected_roads': ['37_42', '42_47', '46_50', '41_46'],
        'connected_plots': ['42', '46']
    },

    '42_47': {
        'built': None,
        'connected_roads': ['37_42', '42_46', '43_47', '47_51'],
        'connected_plots': ['42', '47']
    },

    '43_47': {
        'built': None,
        'connected_roads': ['38_43', '47_51', '42_47'],
        'connected_plots': ['43', '47']
    },

    '44_48': {
        'built': None,
        'connected_roads': ['39_44', '40_44', '48_52'],
        'connected_plots': ['44', '48']
    },

    '45_49': {
        'built': None,
        'connected_roads': ['41_45', '40_45', '49_52', '49_53'],
        'connected_plots': ['45', '49']
    },

    '46_50': {
        'built': None,
        'connected_roads': ['41_46', '42_46', '50_54', '50_53'],
        'connected_plots': ['46', '50']
    },

    '47_51': {
        'built': None,
        'connected_roads': ['43_47', '42_47', '51_54'],
        'connected_plots': ['47', '51']
    },

    '48_52': {
        'built': None,
        'connected_roads': ['44_48', '49_52'],
        'connected_plots': ['48', '52']
    },

    '49_52': {
        'built': None,
        'connected_roads': ['49_53', '45_49', '48_52'],
        'connected_plots': ['49', '52']
    },

    '49_53': {
        'built': None,
        'connected_roads': ['49_52', '45_49', '50_53'],
        'connected_plots': ['49', '53']
    },

    '50_54': {
        'built': None,
        'connected_roads': ['46_50', '50_53', '51_54'],
        'connected_plots': ['50', '54']
    },

    '50_53': {
        'built': None,
        'connected_roads': ['46_50', '50_54', '49_53'],
        'connected_plots': ['50', '53']
    },

    '51_54': {
        'built': None,
        'connected_roads': ['47_51', '50_54'],
        'connected_plots': ['51', '54']
    }
}

players = {'1': {
    'colour': None,
    'name': None,
    'Points': 0,
    'unplayed dev cards': [],
    'played dev cards': [],
    'resources': {'wood': 0,
                  'wheat':0,
                  'ore': 0,
                  'brick': 0,
                  'sheep': 0,
                  },

},
    '2': {
        'colour': None,
        'name': None,
        'Points': 0,
        'unplayed dev cards': [],
        'played dev cards': [],
        'resources': {'wood': 0,
                      'wheat':0,
                      'ore': 0,
                      'brick': 0,
                      'sheep': 0,
                      },

    },
    '3': {
        'colour': None,
        'name': None,
        'Points': 0,
        'unplayed dev cards': [],
        'played dev cards': [],
        'resources': {'wood': 0,
                      'wheat':0,
                      'ore': 0,
                      'brick': 0,
                      'sheep': 0,
                      },

    },
    '4': {
        'colour': None,
        'name': None,
        'Points': 0,
        'unplayed dev cards': [],
        'played dev cards': [],
        'resources': {'wood': 0,
                      'wheat':0,
                      'ore': 0,
                      'brick': 0,
                      'sheep': 0,
                      },

    }}

dev_cards = []

def create_dev_cards():
    devies = []
    devies.append(['knight'] * 14)
    devies.append(['victory point'] * 5)
    devies.append(['road builder'] *2)
    devies.append(['year of plenty'] * 2)
    devies.append(['monopoly'] * 2)
    for listie in devies:
        for card in listie:
            dev_cards.append(card)


colours = ['green', 'blue', 'white', 'orange']

resource_tiles = []

def create_resource_hexes():
    tilos = []
    tilos.append(['desert'])
    tilos.append(['ore'] * 3)
    tilos.append(['brick'] * 3)
    tilos.append(['wheat'] * 4)
    tilos.append(['wood'] * 4)
    tilos.append(['sheep'] * 4)
    for tile in tilos:
        for ti in tile:
            resource_tiles.append(ti)

create_dev_cards()
create_resource_hexes()

numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]