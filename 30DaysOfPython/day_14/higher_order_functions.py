def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f,lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers,[1,2,3,4,5])
print(result)