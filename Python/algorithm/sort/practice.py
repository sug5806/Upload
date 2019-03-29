def gen():
    print('gen start')
    data1 = yield 2
    print(f'gen[1] : {data1}')
    data2 = yield 1
    print(f'gen[2] : {data2}')
    return 'done'

g = gen()

first = g.send(None)
print(first)
