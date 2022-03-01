l = [2, 4, 6, 8]

for i in l:
    assert i % 2 == 0 # verify if every number is even

l2 = [2, 3, 4, 6, 8]

for i in l2:
    assert i % 2 == 0 # raise AssertionError because 3 is not an even number
