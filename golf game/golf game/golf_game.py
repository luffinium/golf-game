class Golf:
    results = ' '
    def __init__(player, currentHole, currentScore, currentPar):
        player.currentHole = currentHole
        player.currentScore = currentScore
        player.currentPar = currentPar 
        
    def evaluate(player, currentScore):
        if player.currentScore > player.currentPar :
            results = "Over Par"
        elif player.currentScore < player.currentPar:
            results = "Under Par"
        else:
            results = "At Par"          
        return results
    
    def evaluateAndDisplayScore(player, enterHole, currentScore):
        print("You scored", player.evaluate(currentScore), "on hole #",enterHole,"with a par of",player.currentPar)

def main():

    enterHole = int(input("Enter the hole number: "))
    currentScore = int(input("Enter your score: "))
    if enterHole == 1:
        hole1 = Golf(1, currentScore , 3)
        hole1.evaluateAndDisplayScore(enterHole, currentScore)
    elif enterHole == 2:
        hole1 = Golf(2, currentScore , 4)
        hole1.evaluateAndDisplayScore(enterHole, currentScore)
    else :
        hole1 = Golf(3, currentScore , 5)
        hole1.evaluateAndDisplayScore(enterHole, currentScore)

if __name__ == '__main__':
    main()