test = {"input": {"cards": [13, 11, 10, 7,
                            4, 3, 1, 0], "query": 7}, "output": 3}

tests = [
    # TEST CASE #1
    {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3},

    # TEST CASE #2
    # Query occcurs in the middle
    {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1}, "output": 6},

    # TEST CASE #3
    # Query is the first element
    {"input": {"cards": [4, 2, 1, -1], "query": 4}, "output": 0},

    # TEST CASE #4
    # Query is the last element
    {"input": {"cards": [3, -1, -9, -127], "query": -127}, "output": 3},

    # TEST CASE #5
    # Cards contains just one element, query
    {"input": {"cards": [6], "query": 6}, "output": 0},

    # TEST CASE #6
    # card does not contain query
    {"input": {"cards": [9, 7, 5, 2, -9], "query": 4}, "output": -1},

    # TEST CASE #7
    # cards is empty
    {"input": {"cards": [], "query": 7}, "output": -1},

    # TEST CASE #8
    # number can repeat in cards
    {"input": {"cards": [8, 8, 6, 6, 6, 6, 6, 3, 2,
                         2, 2, 0, 0, 0], "query": 3}, "output": 7},
    # TEST CASE #9
    # query occurs can repeat in cards
    {"input": {"cards": [8, 8, 6, 6, 6, 6, 6, 6, 3,
                         2, 2, 2, 0, 0, 0], "query": 6}, "output": 2},
]


large_test = {"input": {"cards": list(
    range(10000000, 0, -1)), "query": 2}, "output": 9999998}
