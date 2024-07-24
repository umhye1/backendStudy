#Rock-Scissor-Paper

while True :
    print("player 1 : 주먹, 가위, 보 중 고르세요")
    player1 = str(input())

    if player1 != "보" and player1 != "주먹" and player1 != "가위":
        print("다시 입력하세요")
        break

    print("player 2 : 주먹, 가위, 보 중 고르세요")
    player2 = str(input())

    if player2 != "보" and player2 != "주먹" and player2 != "가위":
        print("다시 입력하세요")
        break

    elif player1 == player2:
        print("비겼습니다")
        break

    elif player1 == "주먹" :
        if player2 == "가위":
            print("player1 승리")
            break
        else :
            print("player2 승리")
            break

    elif player1 == "가위" :
        if player2 == "주먹" :
            print("player2 승리")
            break
        else :
            print("player1 승리")
            break

    elif player1 == "보" :
        if player2 == "주먹":
            print("player1 승리")
            break
        else :
            print("player2 승리")
            break
    
    


