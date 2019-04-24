import math

import hw1


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If expected or recieved are floats,
    will do an approximate check.
    """
    # You don't need to understand how this function works
    # just look at its documentation!
    if type(expected) == 'float' or type(received) == 'float':
        match = math.isclose(expected, received)
    else:
        match = expected == received

    assert match, f'Failed: Expected {expected}, but received {received}'


def test_funky_sum():
    """
    Tests the function funky_sum
    """
    print('Testing funky_sum')

    # Notice that we have to start the function calls with "hw1." since
    # they live in another file

    # Cases from the made up "spec" for this problem
    assert_equals(1, hw1.funky_sum(1, 2, 0))
    assert_equals(2, hw1.funky_sum(1, 2, 1))
    assert_equals(1.5, hw1.funky_sum(1, 2, 0.5))
    assert_equals(1.33, hw1.funky_sum(1, 2, 0.33))

    # edge cases to test the 0 check
    assert_equals(1, hw1.funky_sum(1, 2, -1))
    assert_equals(1, hw1.funky_sum(1, 2, -0.1))
    assert_equals(1.01, hw1.funky_sum(1, 2, 0.01))

    # edge cases to test the 1 check
    assert_equals(2, hw1.funky_sum(1, 2, 2))
    assert_equals(2, hw1.funky_sum(1, 2, 2.1))
    assert_equals(1.99, hw1.funky_sum(1, 2, 0.99))


def test_count_divisible_digits():
    """
    Tests the function count_divisible_digits
    """
    print('Testing count_divisible_digits')

    # Cases given to test this problem
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))

    # Additional cases to check the 0 check
    assert_equals(0, hw1.count_divisible_digits(0, 0))
    assert_equals(2, hw1.count_divisible_digits(-579300, 2))


def test_is_relatively_prime():
    print('Testing is_relatively_prime')

    # Cases given to test this problem
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(4, 24))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))

    # Additional case to check 1 check
    assert_equals(True, hw1.is_relatively_prime(1, 35))

    # Additional case to check 2 check
    assert_equals(False, hw1.is_relatively_prime(6, 54))


def test_travel():
    """
    Tests the function travel
    """
    print('Testing travel')

    # Case given to test this problem
    assert_equals('(-1, 4)', hw1.travel('NW!ewnW', 1, 2))

    # Additional cases to test this problem
    assert_equals('(3, 5)', hw1.travel('!!WNEwssw.', 5, 6))
    assert_equals('(0, 0)', hw1.travel(('eNN@'), -1, -2))


def test_swip_swap():
    """
    Tests the function swip_swap
    """
    print('Testing swip_swap')

    # Cases given to test this problem
    assert_equals('offbar', hw1.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw1.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw1.swip_swap('foobar', 'z', 'c'))

    # Additional cases to test this problem
    assert_equals('nesnitg', hw1.swip_swap('testing', 't', 'n'))
    assert_equals('nap', hw1.swip_swap('nap', 'f', 'g'))


def test_compress():
    """
    Tests the function compress
    """
    print('Testing compress')

    # Cases given to test this problem
    assert_equals('c1o17l1k1a1n1g1a1r1o2',
                  hw1.compress('cooooooooooooooooolkangaroo'))
    assert_equals('a3', hw1.compress('aaa'))
    assert_equals('', hw1.compress(''))

    # Additional cases to test this problem
    assert_equals('a1p2l1e1', hw1.compress('apple'))
    assert_equals('g1o6d1a1w1g4s3', hw1.compress('goooooodawggggsss'))


def test_longest_line_length():
    """
    Tests the function longest_line_length
    """
    print('Testing longest_line_length')

    # Case given to test this problem
    assert_equals(13, hw1.longest_line_length('poem.txt'))

    # Additional case to test empty file check
    assert_equals(None, hw1.longest_line_length('test1.txt'))

    # Additional case to test basic function
    assert_equals(18, hw1.longest_line_length('test2.txt'))


def test_longest_word():
    """
    Tests the function longest_word
    """
    print('Testing longest_word')

    # Case given to test this problem
    assert_equals('3: shells', hw1.longest_word('poem.txt'))

    # Additional case to test empty file check
    assert_equals(None, hw1.longest_word('test1.txt'))

    # Additional case to test multiple same length words
    assert_equals('1: fish', hw1.longest_word('test2.txt'))


def test_mode_digit():
    """
    Tests the function mode_digit
    """
    print('Testing mode_digit')

    # Cases given to test this problem
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))

    # Additional cases to test numbers with same digit occurance numbers
    assert_equals(3, hw1.mode_digit(-333000221))
    assert_equals(4, hw1.mode_digit(440011))


def main():
    test_funky_sum()
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_swip_swap()
    test_compress()
    test_longest_line_length()
    test_longest_word()
    test_mode_digit()


if __name__ == '__main__':
    main()
