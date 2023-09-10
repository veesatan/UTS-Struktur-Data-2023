def rearrange_even_odd(arr):
    if not arr:
        return []
    
    # pisahkan bilangan genap dan ganjil
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 != 0]

    # penggabungan hasil genap lalu ganjil 
    return even + odd

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rearrange_even_odd(input_list))