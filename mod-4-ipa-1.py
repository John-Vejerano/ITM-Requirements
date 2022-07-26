'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    following_list1 = social_graph[from_member]["following"]
    following_list2 = social_graph[to_member]["following"]
    relationship = ""
    if to_member in following_list1:
        if from_member in following_list2:
            relationship +="friends" 
        else:
            relationship +="follower"
    elif from_member in following_list2:
            relationship +="followed by"
    else:
        relationship +="no relationship"
    return relationship


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    horizontal = range(len(board))
    vertical = [i for i in zip(*board)]
    diagonal1 = [board[i][i] for i,v in enumerate(board)]
    diagonal2 = [board[2-i][i] for i,v in enumerate(board)]
    winner = ""

    for i in horizontal:
    
        if all([s =="X" for s in board[i]]) == True:
            winner += "X"
        
        elif all([s =="O" for s in board[i]]) == True:
            winner += "O"
        
        if all([s =="X" for s in vertical[i]]) == True:
            winner +="X"
        
        elif all([s =="O" for s in vertical[i]]) == True:
            winner += "O"
        
    if all(s == "X" for s in diagonal1) == True:
        winner += "X"
        
    elif all(s == "O" for s in diagonal1) == True:
        winner +="O"
        
    elif all(s == "X" for s in diagonal2) == True:
        winner +="X"
        
    elif all(s == "O" for s in diagonal2) == True:
        winner +="O"
    
    if winner == "":
        winner += "NO WINNER"
        
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    keys = [i for i in route_map.keys()]

    for i in range(len(keys)):
        if keys[i][1] == second_stop:
            second_key = keys[i]
        if keys[i][0] == first_stop:
            first_key = keys[i]

    index_first = keys.index(first_key)
    index_second = keys.index(second_key)
    travel_time_values = []

    if first_stop == second_stop:
        total_travel_time = 0
    elif index_first == index_second:
        total_travel_time = route_map[keys[index_first]]["travel_time_mins"]    
    elif index_first < index_second:
        for i in range(index_first,index_second+1):
            travel_time_values.append(route_map[keys[i]]["travel_time_mins"])
        total_travel_time = sum(travel_time_values)
    elif index_first > index_second:
        if index_first == len(keys)-1:
            travel_time_values.append(route_map[keys[index_first]]["travel_time_mins"])
            for i in range(0, index_second+1):
                travel_time_values.append(route_map[keys[i]]["travel_time_mins"])
            total_travel_time = sum(travel_time_values)
        else:
            for i in range(index_first, len(keys)):
                travel_time_values.append(route_map[keys[i]]["travel_time_mins"])
            for i in range(0, index_second+1):
                travel_time_values.append(route_map[keys[i]]["travel_time_mins"])
            total_travel_time = sum(travel_time_values)
            
    return total_travel_time 
