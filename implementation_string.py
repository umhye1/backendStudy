# 입력 : 알파벳 대문자와 숫자로만 구성된 문자열
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 모든 숫자를 더한 값을 이어서 출력

data = list(input())
d = list()
count=0

for i in range(len(data)) :
    if (ord(data[i])>64):
        d.append(data[i])

    else:
        count += int(data[i])

d.sort()

# ord()대신 isalpha() 함수 사용: 알파벳 여부를 확인하는 함수
# "".join(d): 리스트의 요소를 하나의 문자열로 이어붙여 출력합니다.
# str(count): 숫자 합계를 문자열로 변환하여 알파벳과 이어서 출력합니다.

print("".join(d) + str(count))