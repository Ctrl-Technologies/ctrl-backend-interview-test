from one_start.test_one import *

"""
Question, look in the one_start directory for challenges in test_one 

"""

if __name__ == "__main__":
    # First test
    assert combine_two_lists_parallel() == [
        (1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F')
    ]

    # Second Test
    test_set = ['were', 'would', 'i', 'upon', 'eyes', 'and', 'in', 'so', 'to']
    assert set(return_matches_in_list_parallel()) == set(test_set)

    #thirds test
    count_shakespeare()

    #Fourth Test
    test_list = [x for x in range(0, 784)]
    compare_infinite = infinite_loop()
    assert compare_infinite[99] == test_list[99]
    assert compare_infinite[1] == test_list[1]

