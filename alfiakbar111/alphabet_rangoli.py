import string  

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    res = []
    for i in range(size):
        s = '-'.join(alphabet[i:n])
        res.append((s[::-1]+s[1:]).center(4*size-3,'-'))
    print('\n'.join(res[:0:-1]+res))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)