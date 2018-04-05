#! /usr/bin/env python
print "Welcome to UsoroOS Test Sync App"
sendChoice = ['s', 'send']
receiveChoice = ['r', 'receive']


def choicefunction():
    while 1:
        choice = raw_input('Do you want to (S)end or (R)eceive? ').lower()
        if choice in sendChoice:
            import usoroserver
            break
        elif choice in receiveChoice:
            import usoroclient
            break
        else:
            print "Invalid input."

choicefunction()
