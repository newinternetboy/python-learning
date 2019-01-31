def quick_sort(arr):
    ARRAY_LENGHT = len(arr)
    if(ARRAY_LENGHT <=1):
        return arr
    else:
        PRIVOT = arr[0]
        LESSER = [element for element in arr if element < PRIVOT]
        GREATER = [element for element in arr if element > PRIVOT]
        arr = quick_sort(LESSER) + [PRIVOT] + quick_sort(GREATER)
        return arr

user_input=input("please input number splite by comma\n").split(',')
user_input_int = [int(element) for element in user_input]
sorted_arr = quick_sort(user_input_int)
print(sorted_arr)