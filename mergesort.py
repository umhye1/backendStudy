# 합병 정렬 merge sort
# 주어진 배열을 더이상 쪼갤 수 없을 때까지 데이터의 크기를 절반으로 계속 나누어 재귀적으로 정렬을 수행하면서 통합하는 정렬 알고리즘
# DIVIDE, CONQUER, COMBINE
# O(NlogN)

def mergesort(array):
    if len(array) <= 1:
        return array
    
    # 배열을 둘로 나눔
    mid = len(array)//2
    left_half = array[:mid]
    right_half = array[mid:]

    # 재귀적으로 두 부분을 정렬
    left_sorted = mergesort(left_half)
    right_sorted = mergesort(right_half)

    # 두 정렬된 배열들을 합침
    return merge(left_sorted,right_sorted)



def merge(left, right):
    sorted_array = []
    i = j = 0

    # 두 배열의 요소들을 비교해 작은 값을 하나씩 넣음
    while i<len(left) and j<len(right) :
        if left[i]< right[j] :  # 작은 것 먼저 넣어야 정렬되기 때문에 left[i]가 right[j] 보다 작을 경우, left[i]를 넣음
            sorted_array.append(left[i])
            i += 1
        else :
            sorted_array.append(right[j])
            j += 1

    # 남은 요소들을 추가
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array



array = [7,5,9,0,3,1,6,2,4,8]
sorted_array = mergesort(array)
print(sorted_array)