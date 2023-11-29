def create_cumul():
    sum_value = 0

    def cumul_sum(value):
        nonlocal sum_value
        sum_value += value
        return sum_value
    

    return cumul_sum


cumul_sum_function = create_cumul()

print(cumul_sum_function(5))
print(cumul_sum_function(3))
print(cumul_sum_function(10))