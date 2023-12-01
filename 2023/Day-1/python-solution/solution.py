import re

def get_calibration_sum(list):
    final_total_1 = 0
    final_total_2 = 0

    for line in list.split("\n"):
        digits_1 = []
        digits_2 = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits_1.append(c)
                digits_2.append(c)
            for d, val in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
                if line[i:].startswith(val):
                    digits_2.append(str(d+1))
        final_total_1 += int(digits_1[0] + digits_1[len(digits_1)-1])
        final_total_2 += int(digits_2[0] + digits_2[len(digits_2)-1])
    print("Final Total 1: " + str(final_total_1))
    print("Final Total 2: " + str(final_total_2))
    return final_total_2

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

    return get_calibration_sum(file_contents)

main()