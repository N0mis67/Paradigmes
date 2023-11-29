def check(word):
    if word == 3:
        return True
    
    return False

word = ['chat', 'chien', 'canard', 'oi']

even_num_iterator = filter(check, word)

even_num = list(even_num_iterator)

print(even_num)