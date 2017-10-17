def shift_list_for(arr, n):
    for i in range(n):
        arr.insert(0, arr.pop(len(arr) - 1))
    return arr
def get_list():
    return list(input('Enter list: ').split())

print('Moving lists')
arr = get_list()
try:
    shift = int(input('Enter value for move: ')) % len(arr)
    print('Your new list: ', shift_list_for(arr, shift))
except Exception:
    print('List should be not empty and value for move should be integer!')

