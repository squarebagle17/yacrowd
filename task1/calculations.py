def humidifier_calc(input_str):
    """ Function to calculate the remaining volume of water """

    """data preparation"""
    # the count of top-ups
    first_newline_index = input_str.find("\n")
    N = int(input_str[:first_newline_index])

    # top-ups list of pairs (T_i, V_i)
    top_ups = [tuple(map(int, pair.split())) for pair in input_str[(first_newline_index + 1):].splitlines()]

    """calculation"""
    # index of the previous top-up; -1 means there was no top-ups yet
    j = -1
    # volume of the water in specific moment of time
    V = 0

    for i in range(N):
        if j != -1:
            time_between_top_ups = top_ups[i][0] - top_ups[j][0]
            water_after_lack = V - time_between_top_ups if V - time_between_top_ups >= 0 else 0
            V = water_after_lack + top_ups[i][1]
        else:
            V = top_ups[i][1]
        j = i

    return str(V)
