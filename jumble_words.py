# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:51:17 2019

@author: vignesh
"""
import random
def choose():
    words=['rainbow','computer','programing','player','water']
    pick=random.choice(words)
    return pick
def jumble(words):
       jumble="".join(random.sample(words,len(words)))
       return jumble
def thank(p1n,p2n,p1,p2):
       print(p1n,'your score is: ',p1)
       print(p2n,'your score is: ',p2)
       print("thank you")
       print('have a nice day')
def play():
    p1name=input("player 1 enter your name\n")
    p2name=input("player 2 enter your name\n")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer task
        picked_words=choose()
        #createquestion
        qn=jumble(picked_words)
        print(qn)
        #player 1
        if (turn%2==0):
            print(p1name,'your turn')
            ans=input('what is on my mind')
            if ans==picked_words:
                pp1=pp1+1
                print('your score is:',pp1)
            else:
                print('better luck next time:',picked_words)
                c=input('press 1 to continue and 0 to quit :')
                if(c==0):
                    thank(p1name,p2name,pp1,pp2)
                    break
                #player2
                else:         
                  print(p2name,'your turn')
            ans=input('what is on my mind')
            if ans==picked_words:
                pp2=pp2+1
                print('your score is:',pp2)
            else:
                print('better luck next time:',picked_words)
                c=input('press 1 to continue and 0 to quit :')
                if(c==0):
                    thank(p1name,p2name,pp1,pp2)
                    break
                turn=turn+1
                
play()