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