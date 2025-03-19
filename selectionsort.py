# 선택 정렬
# 가장 원시적인 방법. 
# 매번 가장 작은 것을 선택한다는 의미
# 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬이 완료.
# O(N^2)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array)