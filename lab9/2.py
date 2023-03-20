def get_info():

    # List of team names
    info_list = ['Python', 'Java', 'SQL', 'JS']

    # Tuple of team countries
    info_tuple = ('DB', 'ML', 'Backend', 'Frontend')

    # Dictionary of team managers
    info_dict = {
        'DB': 'SQL',
        'ML': 'Python',
        'Java': 'Backend',
        'JS': 'Frontend'
    }

    return info_list, info_tuple, info_dict

info_list, info_tuple, info_dict = get_info()
print(info_list) # Output: ['Barcelona', 'Real Madrid', 'Manchester United', 'Liverpool']
print(info_tuple) # Output: ('Spain', 'Spain', 'England', 'England')
print(info_dict) #
