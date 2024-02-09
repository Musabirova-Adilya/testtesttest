def f(n):
    r = bin(n)[2:] #кто прочитал, тот 
    if n % 2 == 0:
        r = '00'
    else:
        r += '11'
    return int (r, 2)
x = 0
while True:
    if f(x) <= 115:
        x += 1
    elif f(x) > 115:
        break
print(x)

