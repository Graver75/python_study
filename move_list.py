def shift_list_for(arr, n):
    for i in range(n):
        arr.insert(0, arr.pop(len(arr) - 1))
    return arr


print('Moving lists')
arr = list(input('Enter list: ').split())
shift = int(input('Enter value for move: ')) % len(arr)
print('Your new list: ', shift_list_for(arr, shift))