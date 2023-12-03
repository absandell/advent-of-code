def partlist_parser(partlist):
    lines = partlist.split('\n')

    # Parse symbols and gears
    symbols = set()
    symbol_loc = set()
    gear_loc = set()
    for y, i in enumerate(lines):
        for x, k in enumerate(i):
            if k != '.' and not(k.isnumeric()):
                symbols.add(k)
                symbol_loc.add((x,y))
                if k == "*": 
                    gear_loc.add((x,y))

    # Parse part IDs
    ids = []
    part_of_num = False
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not(part_of_num) and (char == "." or char in symbols): # Ignore Symbols
                continue
            elif not(part_of_num) and char.isnumeric(): # Beginning of an ID
                part_of_num = True
                num_start = x
                current_num = char
            elif part_of_num and (char == "." or char in symbols):  # End of an ID
                part_of_num = False
                num_end = x-1
                ids.append((int(current_num), num_start, num_end, y))
                current_num = ""
            elif part_of_num and char.isnumeric(): # 
                current_num += char
                if x == (len(lines[0])-1): # At end of row
                    part_of_num = False
                    num_end = x
                    ids.append((int(current_num), num_start, num_end, y))
                    current_num = ""

    print("ID Sum: " + str(get_id_sum(ids, symbol_loc)))
    print("Gear Sum: " + str(get_gear_sum(ids, gear_loc)))
    return 0

def get_id_sum(ids, symbol_loc):
    sum = 0
    for number, num_start, num_end, y in ids:
        border_loc = set()
        for y in range(y-1, y+2):
            for x in range(num_start-1, num_end+2): border_loc.add((x,y))
        intersection = symbol_loc & border_loc
        if len(intersection) > 0: sum += number
    return sum

def get_gear_sum(ids, gear_loc):
    sum = 0
    for gx, gy in gear_loc:
        gear_border = set()
        gear_ids = []
        for x in range(gx-1, gx+2):
            for y in range (gy-1, gy+2): gear_border.add((x, y))
        for number, num_start, num_end, y in ids:
            if (num_start, y) in gear_border or (num_end, y) in gear_border: gear_ids.append(number)
        if len(gear_ids) == 2: sum += (gear_ids[0] * gear_ids[1])
    return sum

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

    partlist_parser(file_contents)
main()