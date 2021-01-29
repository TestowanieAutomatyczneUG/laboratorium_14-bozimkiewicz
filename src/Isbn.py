def isbn(num):
    no_dash_num = num.split('-')
    ready_number = ''.join(no_dash_num)
    if len(ready_number) != 13:
        return 'Length of given number should be 13'
    for i in ready_number:
        if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 'Number should consist of integers only'
    result = 0
    for digit_idx in range(0, len(ready_number)):
        if digit_idx % 2 != 0:
            result += int(ready_number[digit_idx]) * 3
        else:
            result += int(ready_number[digit_idx])
    rest = result % 10
    if rest == 10 or rest == 0:
        return True
    else:
        return False


print(isbn('854-3872-3-380-21'))
print(isbn('3-15298-982-8947'))
print(isbn('3235-29-2389-077'))
print(isbn('14-28-77-2836-723'))
print(isbn('73-954-5629-54-61'))
