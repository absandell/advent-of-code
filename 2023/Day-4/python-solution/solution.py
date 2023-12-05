def get_winning_numbers(scratchcards):
    final_sum = 0
    
    for scratchcard in scratchcards.split('\n'):
        card_part = scratchcard.split(":")
        winning_numbers = card_part[1].split("|")[0]
        possible_numbers = card_part[1].split("|")[1]

        winning_number_set = {}
        for winning_number in winning_numbers.split():
            winning_number_set[winning_number] = 0
        
        for possible_number in possible_numbers.split():
            if winning_number_set.get(possible_number, None) is not None: 
                winning_number_set[possible_number] += 1
            else: continue
        
        card_sum = 0
        for number in winning_number_set:
            if winning_number_set.get(number, None) is not None:
                if winning_number_set.get(number, None) > 0:
                    if card_sum == 0:
                        card_sum += 1
                    elif card_sum > 0:
                        card_sum *= 2
                else: continue
            else: continue

        final_sum += card_sum
    print(final_sum)
    return final_sum

def get_count_cards(scratchcards):
    final_sum = 0

    extra_cards = {}
    
    for scratchcard in scratchcards.split('\n'):
        card_part = scratchcard.split(":")
        card_num = int(card_part[0].split()[1])
        winning_numbers = card_part[1].split("|")[0]
        possible_numbers = card_part[1].split("|")[1]

        num_matched = 0
        winning_number_set = {}
        for winning_number in winning_numbers.split():
            winning_number_set[winning_number] = 0
        
        for possible_number in possible_numbers.split():
            if possible_number in winning_number_set:
                winning_number_set[possible_number] += 1 
                num_matched += 1
        
        
        print("\nGame: ", card_num, "- Initial num matched is ", num_matched)
        temp = card_num
        if extra_cards.get(temp, None) is not None:
            if num_matched > 0:
                print("Had", extra_cards[card_num-1], "matches here")
                num_matched +=  (num_matched * extra_cards[card_num])
                print("Total matches after multiplying is ", num_matched)
        
        final_sum += num_matched + 1
        print("Final Sum Here: ", final_sum)

        for i in range (num_matched):
            temp2 = card_num + i
            extra_cards[temp2] = extra_cards.get(temp2, 0) + 1

    print(final_sum)
    return final_sum


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

    get_winning_numbers(file_contents)
    get_count_cards(file_contents)
main()


# Add part 1 to has