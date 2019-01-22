import csv

# Approach 1: Creating all possible matches + assigning match strength factor 'k'

data = {}  # assuming data format is 'kerberos, can_help list, need_help list'
matches = {}  # dict mapping kerb to list of possible matches, ordered by factor k

def strength(can_help1, need_help1, can_help2, need_help2):
    '''
    :param can_help1: set of classes kerb1 can help w/
    :param need_help1: set of classes kerb1 needs help w/
    :param can_help2: set of classes kerb2 can help w/
    :param need_help2: set of classes kerb2 needs help w/
    :return: integer between 0 and 1 indicating strength of match between kerb1 and kerb2
    '''
    x = len(can_help1.intersection(need_help2))/len(can_help1.union(need_help2))
    y = len(need_help1.intersection(can_help2))/len(need_help1.union(can_help2))
    range = abs(x-y)  # accounts for spread

    return (x+y)/2*(1-range)

with open('user_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in range(1, len(csv_reader)):  # creating user data dict
        data[row[0]] = (set(row[1]), set(row[2]))

    for user in data:  # create dict of possible matches
        for poss in data:
            if user != poss:
                k = strength(user[0], user[1], poss[0], poss[1])
                if k > 0.5:  # check if k is strong enough
                    try:  # see if user has been seen already
                        matches[user].append((k, poss))
                    except IndexError:
                        matches[user] = [(k, poss)]

    for user in matches:  # sort each of the results
        matches[user].sort()

    print(matches)
