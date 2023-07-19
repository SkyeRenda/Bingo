import random

def create_bingo_card():
    bingo_card = []
    numbers_per_column = 5
    min_numbers = [1, 16, 31, 46, 61]
    max_numbers = [15, 30, 45, 60, 75]
    columns = ["B", "I", "N", "G", "O"]

    for column in range(len(columns)):
        column_values = random.sample(range(min_numbers[column], max_numbers[column] + 1), numbers_per_column)
        bingo_card.append(column_values)

    # Insert a free space in the middle of the card
    bingo_card[2][2] = "FREE"

    return bingo_card

def display_bingo_card(card):
    print("B   I   N   G   O")
    for i in range(len(card[0])):
        for j in range(len(card)):
            value = str(card[j][i])
            if value.isdigit():
                value = value.rjust(2)
            print(value, end=" ")
        print()

# Create a Bingo card
bingo_card = create_bingo_card()

# Display the Bingo card
display_bingo_card(bingo_card)
