def get_possible_games(record): 
    bag_max= {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    possible_games_sum = 0;
    
    for game in record.split("\n"):
        game = game.split(":")
        game_ID = int(game[0].split()[1])
        rounds = game[1].split(";")
        for round in rounds:
            cubes = round.split(",")
            for cube in cubes:
                if int(cube.split()[0]) > bag_max[cube.split()[1]]: break
            else: continue
            break
        else: possible_games_sum += game_ID
    return possible_games_sum

def get_min_cubes(record):
    sum_of_powers = 0
    color_count = {}

    for game in record.split("\n"):
        for color in ["red", "green", "blue"]:
            color_count[color] = [0,0] # [current count][max count]
        game = game.split(":")
        rounds = game[1].split(";")
        power = 1
        for round in rounds:
            for color in ["red", "green", "blue"]:
                color_count[color][0] = 0 # Setting all current to 0
            cubes = round.split(",")
            for cube in cubes:
                color_count[cube.split()[1]][0] += int(cube.split()[0])
            for color in color_count:
                if color_count[color][0] > color_count[color][1]:
                    color_count[color][1] = color_count[color][0]
        for count in color_count.values():
            power *= count[1]
        sum_of_powers += power
    return sum_of_powers

def main():
    file_contents = ""
    file_path = "../input.txt"
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"The file '{file_path}' could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(str(get_possible_games(file_contents)))
    print(str(get_min_cubes(file_contents)))

main()