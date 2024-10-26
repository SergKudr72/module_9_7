def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        summa = sum(args)
        counter = 0
        for i in range(1, summa // 2 + 1):
            if summa % i == 0:
                counter += 1
        if counter >= 0:
            print('Простое')
        else:
            print('Составноe')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
