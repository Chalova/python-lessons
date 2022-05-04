def sum_final_cards(final_cards):
    print(f"final_cards {final_cards}")
    print(sum(final_cards))
    for i in range(0, len(final_cards)):
        print(i)
        if final_cards[i] == 11:
            print(f"FIIIND")
            if sum(final_cards) > 21:
                print(f"FIIIND")
                final_cards[i] = 1
    print(f"final_cards {final_cards}")
    return print(sum(final_cards))

final_cards = [11, 12, 3]

sum_final_cards(final_cards)