#! /usr/bin/env python
print "Welcome to UsoroOS Test Sync App"
choice = raw_input('Do you want to (S)end or (R)eceive? ').lower()
sendChoice = ['s', 'send']
receiveChoice = ['r', 'receive']


def choicefunction():
    if choice in sendChoice:
        import usoroserver
    elif choice in receiveChoice:
        import usoroclient
    else:
        print "Invalid input, exiting"
        exit(1)
    return 1


c = choicefunction()



