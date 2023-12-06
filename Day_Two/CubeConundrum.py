'''
Each game is listed with its ID number (like the 11 in Game 11: ...) 
followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).
The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
What is the sum of the IDs of those games?

--- Part Two ---
As you continue your walk, the Elf poses a second question: in each game 
you played, what is the fewest number of cubes of each color that could 
have been in the bag to make the game possible?

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, the game could have been played with as few as 4 red, 2 
    green, and 6 blue cubes. If any color had even one fewer cube, the 
    game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue
cubes multiplied together. The power of the minimum set of cubes in game 1 
is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up 
these five powers produces the sum 2286.

What is the sum of the power of these sets?

'''

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

def read_input(filepath) -> list:
    result = []
    with open(filepath) as file:
        result = [line for line in file]
    
    return result

def sum_ids(data) -> int:
    result = 0
    
    for line in data:
        #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        lines = str(line).split(':')
        game_str = lines[0].strip()
        game_id = int( game_str[game_str.find(' ')+1:].strip() )
        count_id = True

        ## compute games
        # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        games = lines[1].split(';')
        for game in games:
            #3 blue, 4 red
            cubes_draw = game.strip().split(',')
            for cubes in cubes_draw:
                cubes = cubes.strip()
                if 'red' in cubes:
                    num = int(cubes[:cubes.index(' ')].strip())
                    if num > RED_CUBES:
                        count_id = False
                        break
                if 'green' in cubes:
                    num = int(cubes[:cubes.index(' ')].strip())
                    if num > GREEN_CUBES:
                        count_id = False
                        break
                if 'blue' in cubes:
                    num = int(cubes[:cubes.index(' ')].strip())
                    if num > BLUE_CUBES:
                        count_id = False
                        break
        if count_id:
            result += game_id
            
    return result

def part_two(data) ->int:
    result = 0
    
    for line in data:
        #Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        lines = str(line).split(':')
        game_str = lines[0].strip()
        game_id = int( game_str[game_str.find(' ')+1:].strip() )
        count_id = True

        red = 0
        green = 0
        blue = 0

        ## compute games
        # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        games = lines[1].split(';')
        for game in games:
            #3 blue, 4 red
            cubes_draw = game.strip().split(',')
            for cubes in cubes_draw:
                cubes = cubes.strip()
                if 'red' in cubes:
                    num = int(cubes[:cubes.index(' ')].strip())
                    if num > red:
                        red = num
                if 'green' in cubes:
                    num = int(cubes[:cubes.index(' ')].strip())
                    if num > green:
                        green = num
                if 'blue' in cubes:
                    num = int(cubes[:cubes.index(' ')].strip())
                    if num > blue:
                        blue = num                        
        result += red*green*blue
            
    return result

def test_input():
    data = read_input('./Day_Two/test_dayTwo.txt')
    print(sum_ids(data))

def test_input_part_two():
    data = read_input('./Day_Two/test_dayTwo.txt')
    print(part_two(data))

if __name__ == '__main__':
    print('Day Two')
    data = read_input('./Day_Two/day2Input.txt')
    print(sum_ids(data))
    print(part_two(data))
