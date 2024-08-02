n= int(input())

count =0

array = [500,100,50,10]

#해당 화폐로 거슬러 줄 수 있는 동전의 개수
for coin in array :
    count += n // coin
    n %= coin

print(count)