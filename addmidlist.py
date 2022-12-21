arr = [2,54,23,19,56,30,48,23]
mid = len(arr)//2
final = []

for i in range(mid):
    new_arr = arr[i] + arr[mid+i]
    final.append(new_arr)
print(final)