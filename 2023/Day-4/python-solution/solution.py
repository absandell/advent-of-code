def get_winning_numbers(scratchcards):
    cards = []
    final_sum = 0
    
    for line in scratchcards.splitlines():
        card = line.replace(':', '|').split('|')
        winning_numbers = set(card[1].split())
        possible_numbers = set(card[2].split())
        card = [winning_numbers, possible_numbers]
        cards.append(card)
    
    for c, card in enumerate(cards):
        winning_numbers, possible_numbers = card
        matches = winning_numbers & possible_numbers
        num_matches = len(matches)
        if num_matches == 0: continue
        elif num_matches > 0:
            card_sum = 0
            for i in range(num_matches):
                if card_sum == 0:
                    card_sum += 1
                elif card_sum > 0:
                    card_sum *= 2
            final_sum += card_sum
    return final_sum

def get_count_cards(scratchcards):
    cards = []
    
    for line in scratchcards.splitlines():
        card = line.replace(':', '|').split('|')
        winning_numbers = set(card[1].split())
        possible_numbers = set(card[2].split())
        card = [1, winning_numbers, possible_numbers]
        cards.append(card)

    for c, card in enumerate(cards):
        count, winning_numbers, possible_numbers = card
        matches = winning_numbers & possible_numbers
        num_matches = len(matches)
        if num_matches == 0: continue
        elif num_matches > 0:
            for num_extra in range(c+1, c+1+num_matches):
                cards[num_extra][0] += count
    return get_num_cards(cards)

def get_num_cards(cards):
    final_sum = 0
    for card in cards:
        final_sum += card[0]
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

    print(get_winning_numbers(file_contents))
    print(get_count_cards(file_contents))
main()


# Add part 1 to has