# 계산기

while True :
    print("숫자와 수식을 차례로 입력하세요 (예 : 2 * 3)")
    print("끝내려면 0 0 0 입력")
    num1, operator, num2 = map(str,input().split())

    if num1 == "0" and operator == "0" and num2 == "0":
        break

    num1 = int(num1)
    num2 = int(num2)


    if operator == "+":
        result = num1 + num2
        print("답은",result)

    elif operator == "-":
        result = num1 - num2
        print("답은",result)

    elif operator == "/" :
        result = num1/num2
        print("답은",result)

    elif operator == "*" :
        result = num1 * num2
        print("답은",result)

    elif operator == "//":
        result = num1//num2
        print("답은",result)

    elif operator == "%" :
        result = num1%num2
        print("답은",result)
    
    elif operator == "**":
        result = num1**num2
        print("답은",result)

    else :
        print("연산자를 다시 입력하세요")