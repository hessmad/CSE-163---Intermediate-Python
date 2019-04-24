def funky_sum(a, b, mix):
    """
    Returns a mixture between a and b.

    If mix is 0, returns a. If mix is 1, returns b. Otherwise returns a linear
    interpolation between them. If mix is outside the range of 0 and 1, it is
    capped at those numbers.
    """
    if mix < 0:
        return a
    elif mix > 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def count_divisible_digits(n, m):
    '''
    Returns number of digits in one integer that are divisible by another
    '''
    count = 0
    n = abs(n)
    if m == 0:
        return count
    else:
        while n > 0:
            digit = n % 10
            if digit % m == 0:
                count = count + 1
            n = n // 10
        return count


def is_relatively_prime(n, m):
    '''
    Returns True or False whether or not two numbers share 1 as their greatest
    common denominator
    '''
    if n == 1 or m == 1:
        return True
    elif n != 0 and m != 0:
        if n == m:
            return False
        elif n % 2 == 0 and m % 2 == 0:
            return False
        elif n % 3 == 0 and m % 3 == 0:
            return False
        else:
            return True
    else:
        return True


def travel(direction, x, y):
    '''
    Returns new coordinate given a string of directions and a starting point
    '''
    direction = direction.lower()
    y_new = y
    x_new = x
    for i in direction:
        if i.isalpha():
            if i == "n":
                y_new += 1
            elif i == "s":
                y_new -= 1
            elif i == "e":
                x_new += 1
            elif i == "w":
                x_new -= 1
    result = "(" + str(x_new) + ", " + str(y_new) + ")"
    return result


def swip_swap(source, c1, c2):
    '''
    Returns a string with swapped occurances of given characters
    '''
    s = list(source)
    for i in range(len(s)):
        if s[i] == c1:
            s[i] = c2
        elif s[i] == c2:
            s[i] = c1
    return ''.join(s)


def compress(source):
    '''
    Returns a string that is compressed so that each letter is followed by the
    total number that letter occurs in a row in the given string
    '''
    s = ''
    if len(source) > 0:
        count = 1
        last = source[0]
        for i in range(1, len(source) + 1):
            if i == len(source):
                s = s + last + str(count)
            elif source[i] == last:
                count += 1
            else:
                s = s + last + str(count)
                count = 1
                last = source[i]
    return s


def longest_line_length(file_name):
    '''
    Takes a file and returns the length of the longest line in the file
    '''
    with open(file_name) as file:
        lines = file.readlines()
        max_length = 0
        for line in lines:
            if len(line) > max_length:
                max_length = len(line)
        if max_length == 0:
            return None
        else:
            return max_length


def longest_word(file_name):
    '''
    Takes a file and returns the longest word and the line it first occurs on
    '''
    with open(file_name) as file:
        lines = file.readlines()
        max_word = ''
        max_line = 0
        line_num = 0
        for line in lines:
            line_num += 1
            words = line.split()
            for word in words:
                if len(word) > len(max_word):
                    max_word = word
                    max_line = line_num
        if max_line == 0:
            return None
        else:
            result = str(max_line) + ": " + max_word
            return result


def mode_digit(n):
    '''
    Returns the digit with the greatest number of occurances in a given integer
    '''
    max_count = 0
    max_digit = 0
    n = str(abs(n))
    for i in n:
        temp = int(n)
        count = 0
        while temp > 0:
            digit = temp % 10
            if str(digit) == i:
                count += 1
            temp = temp // 10
        if count == max_count:
            max_digit = max(max_digit, int(i))
        elif count > max_count:
            max_count = count
            max_digit = int(i)
    return max_digit
