from warnings import filterwarnings

filterwarnings("ignore")

while True:
    print '''------------------------------------------------


 ___________________________________
|                                   |
|  Welcome to 99999999 in 1 games!  |
|      (actually only 2 in 1)       |
|                                   |
| GAMES:                            |
|                                   |
| 1: Minesweeper                    |
| 2: Connect Four                   |
| 3: Exit                           |
|___________________________________|
'''
    a = raw_input("Enter the game you want to play:")
    print '\n------------------------------------------------'
    if a == '1':
        import mines
    elif a == '2':
        import connect_four
    elif a == '3':
        print 'Goodbye!'
        exit()
    else:
        print 'Invalid choice.'
