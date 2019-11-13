# create list of player dictionaries

qb = [
    {
        'Name': 'Carson Wentz',
        'Position': 'Quarterback',
        'Age': 26,
        'Team': 'PHI',
        'Starter': True,
        'Schedule': {
            'week4': 'at GB',
            'week5': 'NYJ',
            'week6': 'at MIN',
            'week7': 'at DAL',
            'week8': 'at BUF',
            'week9': 'CHI',
            'week10': 'BYE',
            'week11': 'NE',
            'week12': 'SEA',
            'week13': 'at MIA',
            'week14': 'NYG',
            'week15': 'at WAS',
            'week16': 'DAL'
        }
    }
]

carsonWentz = qb[0]
print(f'{carsonWentz["Schedule"]["week4"]}')
# ---------------------------------------------------------------

rb = [
    {
        'Name': 'Chris Carson',
        'Position': 'Runningback',
        'Age': 26,
        'Team': 'Seahawks',
        'Starter': True,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }, {
        'Name': 'Marlon Mack',
        'Position': 'Runningback',
        'Team': 'Colts',
        'Starter': True,
        'Schedule': [
            'OAK',
            'LAR',
            'OAK']
    }, {
        'Name': 'Chris Thompson',
        'Position': 'Runningback',
        'Team': 'Redskins',
        'Starter': False,
        'Schedule': [
            'at NYG',
            'LAR',
            'OAK']
    }, {
        'Name': 'Matt Breida',
        'Position': 'Runningback',
        'Team': '49ers',
        'Starter': False,
        'Schedule': [
            'BYE',
            'LAR',
            'OAK']
    }, {
        'Name': 'Alexander Mattison',
        'Position': 'Runningback',
        'Team': 'Vikings',
        'Starter': False,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }, {
        'Name': 'Wayne Gallman',
        'Position': 'Runningback',
        'Team': 'Giants',
        'Starter': False,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }]

chrisCarson = rb[0]
marlonMack = rb[1]
chrisThompson = rb[2]
mattBreida = rb[3]
alexanderMattison = rb[4]
wayneGallman = rb[5]

# ---------------------------------------------------------------

wr = [
    {
        'Name': 'OBJ',
        'Position': 'Wide Receiver',
        'Team': 'CLE',
        'Starter': True,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }, {
        'Name': 'Cooper Kupp',
        'Position': 'Wide Receiver',
        'Team': 'LAR',
        'Starter': True,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }, {
        'Name': 'Allen Robinson',
        'Position': 'Wide Receiver',
        'Team': 'CHI',
        'Starter': True,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }, {
        'Name': 'Mecole Hardman',
        'Position': 'Wide Receiver',
        'Team': 'KC',
        'Starter': False,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }, {
        'Name': 'Corey Davis',
        'Position': 'Wide Receiver',
        'Team': 'TEN',
        'Starter': False,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }
]

odellBeckhamJr = wr[0]
cooperKupp = wr[1]
allenRobinson = wr[2]
mecoleHardman = wr[3]
coreyDavis = wr[4]

# ---------------------------------------------------------------

te = [
    {
        'Name': 'Travis Kelce',
        'Position': 'Tight End',
        'Team': 'KC',
        'Starter': True,
        'Schedule': [
            'at ARZ',
            'LAR',
            'OAK']
    }
]

travisKelce = te[0]

# ---------------------------------------------------------------

print(f'---------------------------------------------------')
print(f'{chrisCarson["Name"]} is playing {rb[0]["Schedule"][0]} this week.')
print(f'---------------------------------------------------')


# a dictionary can even contain another dictionary
team = {'Team': 'Hooker with a Penis',
        'QB': carsonWentz["Name"],
        'WR1': odellBeckhamJr["Name"],
        'WR2': cooperKupp["Name"]
        }
print(team)

print(f'---------------------------------------------------')
print(f'Team {team["Team"]} is starting ')
print(f'---------------------------------------------------')
