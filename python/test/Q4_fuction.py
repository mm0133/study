def all_add_function(para):
    result = 0
    for num in para:
        result += int(num)
    return result

input_numbers = input('더할 수를 여러 개 입력 하시오 > ').split()
total = all_add_function(input_numbers)
print(total)

