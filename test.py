def minmax(list):
    max1 = max(list)
    min1 = min(list)
    list.remove(max(list))
    list.remove(min(list))
    return max1, min1, list

l = [0,1,2,5]

print(minmax(l))