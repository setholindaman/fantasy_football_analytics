
playerList = ['Hopkins', 'Kupp', 'Wents', 'Carson', 'Mack', 'Kelce',
              'Murray', 'Breida', 'Robinson', 'Davis', 'Edmonds', 'Kirk',
              'Prater', 'MIN']

qbList = ['Wentz']
wrList = ['Hopkins', 'Kupp', 'Robinson', 'Kirk', 'Davis']
rbList = ['Carson', 'Mack', 'Breida', 'Edmonds', 'Murray']
teList = ['Kelce']
kList = ['Prater']
dList = ['MIN']


def get_starting_lineup():
    qb = input(f'Choose a QB...{qbList} ')
    rb1 = input(f'Choose a RB1...{rbList} ')
    rbList.remove(rb1)
    rb2 = input(f'Choose a RB2...{rbList} ')
    rbList.remove(rb2)
    wr1 = input(f'Choose a WR1...{wrList} ')
    wrList.remove(wr1)
    wr2 = input(f'Choose a WR2...{wrList} ')
    wrList.remove(wr2)
    te = input(f'Choose a TE...{teList} ')
    teList.remove(te)
    flex = input(f'Choose a FLEX...{rbList}{wrList}{teList} ')
    k = input(f'Choose a K...{kList} ')
    d = input(f'Choose a DEF...{dList} ')

    startingLineup = [qb, rb1, rb2, wr1, wr2, te, flex, k, d]
    print(f'''
    Your starting lineup: 
    QB: {qb}
    RB1: {rb1}
    RB2: {rb2}
    WR1: {wr1}
    WR2: {wr2}
    TE: {te}
    FLEX: {flex}
    K: {k}
    DEF: {d}
    ''')
    return startingLineup


get_starting_lineup()
