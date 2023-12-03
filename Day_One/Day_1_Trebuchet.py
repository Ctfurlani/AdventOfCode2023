'''
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, 
                                two, three, four, five, six, seven, eight, and nine also count as valid "digits".
Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
'''
import re
DIGITS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def read_input(filepath) -> list:
    result = []
    with open(filepath) as file:
        result = [line for line in file]
    
    return result

def sum_calibration(data) -> int:
    sum = 0
    for number in data:
        numbers_map = {}
        #search number with string and save in map if found
        for i, digit in enumerate(DIGITS):
            # all indexes where we can find digit
            indexes = [m.start() for m in re.finditer(digit, number)]
            # add to map
            for index in indexes:
                numbers_map[index] = i + 1
                
        for i, char in enumerate(number):
            if char.isdigit():
                numbers_map[i] = int(char)

        numbers_list = sorted(numbers_map)
        min = str(numbers_map[numbers_list[0]])
        max = str(numbers_map[numbers_list[-1]])

        sum += int(min + max)
    return sum

def test_input():
    data = read_input('./Day_One/test_dayOne.txt')
    print(sum_calibration(data))


if __name__ == '__main__':
    print('Day One')
    data = read_input('./Day_One/day1Input.txt')
    print(sum_calibration(data))