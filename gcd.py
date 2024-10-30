# 유클리드 호제법
# 두 자연수 a, b에 대해 (a>b) a를 b로 나눈 나머지를 r이라 하자.
# 이때 a, b의 최대 공약수는 b,r의 최대 공약수와 같다

def gcd(a,b) :
    if a % b ==0:
        return b
    return gcd(b, a%b)

print(gcd(192, 162))