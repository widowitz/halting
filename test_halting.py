import halting


def test_make_selection():
    # random selection #1:
    data = [34, 56, 18, 20, 36, 35, 47]
    x = halting.make_selection(data)
    assert x == 47, 'Wrong selection' 
    # random selection #2:
    data = [288, 10, 12, 1400, 20]
    x = halting.make_selection(data)
    assert x == 1400, 'Wrong selection' 
    # random selection #3:
    data = [34, 18, 20, 36, 35, 7]
    x = halting.make_selection(data)
    assert x == 36, 'Wrong selection' 
    # random selection #4:
    data = [5, 4, 3, 2, 1]
    x = halting.make_selection(data)
    assert x == 1, 'Wrong selection' 
    # random selection #5:
    data = [100, 101, 1000, 1020, 30]
    x = halting.make_selection(data)
    assert x == 1000, 'Wrong selection' 
    # just three elements:
    data = [1, 2, 3]
    x = halting.make_selection(data)
    assert x == 2, 'Wrong selection' 
    # just three elements:
    data = [1, 2, 3]
    x = halting.make_selection(data)
    assert x == 2, 'Wrong selection' 
    # just three elements:
    data = [3, 2, 1]
    x = halting.make_selection(data)
    assert x == 1, 'Wrong selection' 
    # just three elements:
    data = [2, 3, 1]
    x = halting.make_selection(data)
    assert x == 3, 'Wrong selection' 










if __name__ == "__main__":
    print('Starting tests...')
    test_make_selection()
    print('All tests completed')
















