# in method, index method

array_100 = range(0, 50, 10)
array_100 = list(array_100)
array_100 += range(50, 60)
array_100 += range(60, 100, 10)
if (50 in array_100):
    for i in range(1, 10):
        array_100[array_100.index(50) + i] = f"cincuenta y {i}"
print(array_100)
