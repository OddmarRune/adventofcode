"""Advent of Code, 2023, Day 7"""

ORDER_CARD = {'A':'23','K':'22','Q':'21','J':'10',
              'T':'19','9':'18','8':'17','7':'16',
              '6':'15','5':'14','4':'13','3':'12','2':'11'}
RANK_TO_STR = "012345"

def rank(hand):
    """ Evaluate hand """
    c = 0
    sorted_hand = sorted(hand)
    j = 1 if sorted_hand[0]=='J' else 0
    my_rank = [1-j,0,0,0,0]
    for i in range(len(sorted_hand)-1):
        if sorted_hand[i+1] == 'J':
            j += 1
            continue
        if sorted_hand[i+1] == sorted_hand[i]:
            my_rank[c] += 1
        else:
            c += 1
            my_rank[c] += 1
    my_rank_sorted = sorted(my_rank, reverse=True)
    my_rank_sorted[0] += j        
    sorted_rank = ''.join([RANK_TO_STR[r] for r in my_rank_sorted])+\
        ''.join([ORDER_CARD[card] for card in hand])
    return int(sorted_rank)

def main():
    """ Solution to part 2 """
    with open("input.txt", encoding="UTF-8") as file:
        table = []
        for line in file.readlines():
            if line:
                hand, bid = line.strip().split(" ")
                table.append((hand,rank(hand),bid))
        sorted_table = sorted(table, key=lambda hand: hand[1], reverse=False)
        total = 0
        for r,table_line in enumerate(sorted_table):
            # print(r+1, table_line[0], table_line[2], table_line[1])
            total += (r+1)*int(table_line[2])
        print(f"Total winnings : {total}")

if __name__ == "__main__":
    main()
