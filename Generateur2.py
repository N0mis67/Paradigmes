def pair_num(n):
    for i in range(0, n+1, 2):
        yield i

n = 15

gen_num = pair_num(n)

for even_num in gen_num:
    print(even_num)


