import csv

# Approach 1: Creating all possible matches + assigning match strength factor 'k'
#
# To add:
#       - increase match weight if share "rare" classes, maybe use class size as input

data = {}
matches = {}  # dict mapping kerb to list of possible matches, ordered by factor k
kerb_to_name = {}  # dict mapping kerb to corresponding name

def strength(can_help1, need_help1, can_help2, need_help2):
    '''
    :param can_help1: set of classes kerb1 can help w/
    :param need_help1: set of classes kerb1 needs help w/
    :param can_help2: set of classes kerb2 can help w/
    :param need_help2: set of classes kerb2 needs help w/
    :return: tuple of index, range
    '''
    x = len(can_help1.intersection(need_help2))
    y = len(need_help1.intersection(can_help2))
    range = abs(x-y)

    if x == 0 or y == 0:  # help is mutual
        return 0, 0
    return (x+y)/2, range


with open('testdata.csv') as csv_file:  # data format is 'timestamp, name, kerberos, can_help list, need_help list'
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:  # creating user data dict + kerb dict
        data[row[2]] = (set(row[3].split()), set(row[4].split()))  # assuming classes split by spaces
        kerb_to_name[row[2]] = row[1]

    for user in data:  # create dict of possible matches
        for poss in data:
            if user != poss:
                k = strength(data[user][0], data[user][1], data[poss][0], data[poss][1])
                if k[0] > 0:  # check if k is strong enough
                    try:  # see if user has been seen already
                        matches[user].append((k, poss))
                    except KeyError:
                        matches[user] = [(k, poss)]

    for user in matches:  # sort each of the results
        matches[user] = sorted(matches[user], key=lambda s: s[0][0], reverse=True)  # not sure if range is auto sorted

    print(matches)
