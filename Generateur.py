def generate_even_numbers(n):
    i = 0
    while i < n:
        yield i * 2
        i += 1

gen = generate_even_numbers(10)

print(next(gen))
print(next(gen))

for num in gen:
    print(num)