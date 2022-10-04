import random
l=["rock","scissor","paper"]

while True:
    ucount=0
    ccount=0
    uc=int(input('''
    game start....
    1 play | yes
    2 No | exit
    '''))
    if uc==1:
            for i in range(1,6):
                userinput=int(input('''
    1 rock
    2 scissor
    3 paper        
                '''))
                if userinput==1:
                    uchoice="rock"
                elif userinput==2:
                    uchoice="scissor"
                elif userinput==3:
                    uchoice="paper"
                cchoice=random.choice(l)
                print(uchoice)
                print(cchoice)
                if uchoice==cchoice:
                    print("computer value ",cchoice)
                    print("user choice ",uchoice)
                    print("game draw")
                    ucount+=1
                    ccount+=1
                elif (uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
                    print("computer value ", cchoice)
                    print("user choice ", uchoice)
                    print("you win")
                    ucount+=1
                else:
                    print("computer value ", cchoice)
                    print("user choice ", uchoice)
                    print("computer win")
                    ccount+=1
            if ucount==ccount:
                print("final game draw...")
                print("user score",ucount)
                print("computer score",ccount)
            elif ucount>ccount:
                print("finally you won game...")
                print("user score",ucount)
                print("computer score",ccount)
            else:
                print("finally computer won game...")
                print("user score",ucount)
                print("computer score",ccount)
    else:
        break
