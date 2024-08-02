# n이 100억이 이상의 큰 수가 되는 경우를 가정했을 때도 빠르게 동작하려면, n이 k의 배수가 되도록 효율적으로 한번에 빼는 방식으로 소스코드 작성 가능

n,k = map(int,input().split())
result =0 

#(n==k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기

while True:
    # n%k==0이 될때까지 1씩 빼야하는데 걍 한번에 빼려고 아래와 같이 짠 것
    target = (n//k)*k
    result += (n-target)
    n = target

    if n<k :
        break
    result+=1
    n//=k

result +=(n-1)
print(result)