from pyfiglet import Figlet
import random
import time

# How many options each face card will give the next player
FACE_CARD_VALUES = {
    'J': 2,
    'Q': 3,
    'K': 4
}

# Suit representations to their symbols
SUIT_SYMBOLS = {
    'D': '♦',
    'C': '♣',
    'H': '♥',
    'S': '♠'
}

# Seconds for program to sleep when dealing and before a dramatic reveal in game
DEAL_SLEEP = .8
SUSPENSE_SLEEP = 1

# How ranks and suits are represented
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['D', 'C', 'H', 'S']

# Ways people might enter rank and suit names
RANKS_ACCEPTED_INPUT = {
    'ACE': 'A',
    'TWO': '2',
    'THREE': '3',
    'FOUR': '4',
    'FIVE': '5',
    'SIX': '6',
    'SEVEN': '7',
    'EIGHT': '8',
    'NINE': '9',
    'TEN': '10',
    'JACK': 'J',
    'QUEEN': 'Q',
    'KING': 'K',
}
SUITS_ACCEPTED_INPUT = {
    'DIAMONDS': 'D',
    'DIAMOND': 'D',
    'DI': 'D',
    'D': 'D',
    'CLUBS': 'C',
    'CLUB': 'C',
    'CL': 'C',
    'C': 'C',
    'HEARTS': 'H',
    'HEART': 'H',
    'HE': 'H',
    'H': 'H',
    'SPADES': 'S',
    'SPADE': 'S',
    'SP': 'S',
    'S': 'S'
}

def print_big(phrase, font_type='standard'):
    f = Figlet(font=font_type)
    print(f.renderText(phrase))

def welcome():
    clear_window()
    welcome_phrase = 'WELCOME TO HYDR-ACE-TION!!'
    print_big(welcome_phrase)
    time.sleep(DEAL_SLEEP)
    print('Please refer to the README to learn the rules if you haven\'t played before!\n')
    time.sleep(DEAL_SLEEP)

def parse_card_input(inp):
    inp = inp.strip().upper()
    cleaned_suit = ''
    rank = None
    suit = None
    ranks_accepted_input_list = list(RANKS_ACCEPTED_INPUT.keys())
    for r in (ranks_accepted_input_list + RANKS):
        # Look for rank in user input
        if inp.find(r) == 0:
            if r in ranks_accepted_input_list:
                rank = RANKS_ACCEPTED_INPUT[r]
            else:
                rank = r
            words = inp.split()
            # Look for suit in user input
            if len(words) == 1:
                # Input contains just one word, just check back of word for a suit
                cleaned_suit = inp[len(r):]
            else:
                # With multiple words, just check the last word for suit
                cleaned_suit = words[-1]
        if cleaned_suit in SUITS_ACCEPTED_INPUT:
            suit = SUITS_ACCEPTED_INPUT[cleaned_suit]
    return rank, suit

def get_card_input():
    rank = None
    suit = None
    while True:
        inp = input()
        rank, suit = parse_card_input(inp)
        if suit is not None and rank is not None:
            break
        else:
            print('Please enter a card in the format specified in the README!')
    return (rank, suit)


def get_players():
    num_players = 2
    while True:
        try:
            # User must specify an integer
            num_players = int(input('How many players?\n'))
            if num_players >= 2 and num_players <= 8:
                break
            else:
                print('There needs to be between 2 and 8 players.')
        except:
            print('Enter an integer between 2 and 8.')
    players = []
    # Get player names
    for i in range(num_players):
        while True:
            player = input('What is player {}\'s name?\n'.format(i + 1))
            if player in players:
                print('Choose a different name from other players!')
            elif len(player) < 1:
                print('Player\'s name must be at least one character long!')
            else:
                break
        players.append(player)
    return players

def create_full_deck():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append((rank, suit))
    return deck

# Returns the random card dealt and the remaining deck
def deal_random_card(avail_cards):
    if len(avail_cards) < 1:
        return (), avail_cards
    rand = random.randint(0, len(avail_cards) - 1)
    rand_card = avail_cards[rand]
    del avail_cards[rand]
    return rand_card, avail_cards

def show_cards(cards):
    space = ' '
    num_per_row = 4
    top, rank_top, padding_top, suit, padding_bottom, rank_bottom, bottom = [''], [''], [''], [''], [''], [''], ['']
    for i in range(len(cards)):
        # Fill in cards in a row
        top[-1] += '┌───────┐' + space
        rank_top[-1] += '| {:<2}    |'.format(cards[i][0]) + space
        padding_top[-1] += '|       |' + space
        suit[-1] += '|   {}   |'.format(SUIT_SYMBOLS[cards[i][1]]) + space
        padding_bottom[-1] += '|       |' + space
        rank_bottom[-1] += '|    {:>2} |'.format(cards[i][0]) + space
        bottom[-1] += '└───────┘' + space
        if (i+1) % num_per_row == 0 and i != len(cards) - 1:
            # Make a new row of cards
            top.append('')
            rank_top.append('')
            padding_top.append('')
            suit.append('')
            padding_bottom.append('')
            rank_bottom.append('')
            bottom.append('')
    if len(cards) > 0:
        # Print all rows
        for i in range(len(top)):
            print(top[i])
            print(rank_top[i])
            print(padding_top[i])
            print(suit[i])
            print(padding_bottom[i])
            print(rank_bottom[i])
            print(bottom[i])

def get_face_card_choice(avail_cards, face_card_rank, player, players):
    num = FACE_CARD_VALUES[face_card_rank]
    prev_player = players[players.index(player) - 1]
    choices = []
    for i in range(num):
        # Gather options
        rand_card, avail_cards = deal_random_card(avail_cards)
        choices.append(rand_card)
    print('Thanks to {} for getting a face card [{}] last turn! {}, pick one card from the following:'.format(prev_player, face_card_rank, player))
    time.sleep(DEAL_SLEEP)
    show_cards(choices)
    print('Enter your choice:')
    while True:
        card_choice = get_card_input()
        if card_choice in choices:
            # Append unchosen cards back to avail_cards
            for c in choices:
                if c != card_choice:
                    avail_cards.append(c)
            return card_choice
        print('That\'s not listed above! Try again.')


def sort_by_rank(hand):
    def sort_by_rank_helper(card):
        rank = card[0]
        return RANKS.index(rank)
    hand.sort(key=sort_by_rank_helper)

def get_drinker(player, players):
    drinker = 0
    while True:
        drinker = input('Who would you like to hydrate?\n')
        if drinker in players:
            return drinker
        print('Please enter a player\'s name with correct spelling and caps! Other players\' names are:', )
        for p in players:
            if player != p:
                print(p)

def handle_hydrate(player, hand, players):
    last_card = hand[-1]
    # Check if ace
    if last_card[0] == 'A':
        print_hydrate_message(player, players, 'GOT AN ACE!', 'TAKE ONE DRINK!', [])
    # Check if the last card creates a new pair, which means 1 drink for 1 pair or
    # two drinks if 2 pairs
    last_card_rank = last_card[0]
    same_rank = 0
    same_rank_cards = []
    for card in hand:
        if card[0] == last_card_rank:
            same_rank_cards.append(card)
            same_rank += 1
    if same_rank == 2:
        #TODO: show the double or quad
        print_hydrate_message(player, players, 'GOT A DOUBLE!', 'TAKE ONE DRINK!', same_rank_cards)
    if same_rank == 4:
        print_hydrate_message(player, players, 'GOT A QUAD!', 'TAKE TWO DRINKS!', same_rank_cards)
        show_cards(same_rank_cards)


def print_hydrate_message(player, players, alert_msg, drink_msg, same_rank_cards):
    time.sleep(SUSPENSE_SLEEP)
    print_big('{} {}'.format(player, alert_msg), font_type='slant')
    show_cards(same_rank_cards)
    drinker = get_drinker(player, players)
    print_big('{} - {}'.format(drinker, drink_msg))

def clear_window():
    # print ANSI sequence to clear screen
    print('\033[H\033[J')

def end():
    time.sleep(SUSPENSE_SLEEP)
    clear_window()
    print_big('NO MORE CARDS - THANKS FOR PLAYING!')
    input('Press Enter to terminate.')

def play_game():
    welcome()
    players = get_players()
    num_players = len(players)
    curr_deck = create_full_deck()
    iter = 0
    present_options = False
    face_card_rank = 1
    hands = {}
    input('Press Enter to start the game!')
    while len(curr_deck) > 1:
        clear_window()
        curr_player = players[iter % num_players]
        # This is curr_player's turn!
        print_big('{}\'s turn!'.format(curr_player))
        if curr_player in hands:
            print('{}, your current hand looks like:'.format(curr_player))
            show_cards(hands[curr_player])
        else:
            print('{}, your current hand is empty.'.format(curr_player))
        time.sleep(DEAL_SLEEP)
        card_taken = ()
        if present_options and len(curr_deck) < FACE_CARD_VALUES[face_card_rank]:
            # Out of cards because last player drew face card
            break
        elif not present_options:
            # Last player did not draw face card, give one card as normal
            rand_card, deck = deal_random_card(curr_deck)
            card_taken = rand_card
            print('This card was drawn and added to your hand:'.format(curr_player))
        elif present_options:
            # Last player drew a face card, so current player gets options
            card_taken = get_face_card_choice(curr_deck, face_card_rank, curr_player, players)
            print('Your chosen card below has been added to your hand.'.format(curr_player))
        show_cards([card_taken])
        if curr_player in hands:
            hands[curr_player].append(card_taken)
        else:
            hands[curr_player] = [card_taken]
        handle_hydrate(curr_player, hands[curr_player], players)
        sort_by_rank(hands[curr_player])
        if card_taken[0] in FACE_CARD_VALUES:
            print('Yep, that\'s a face card! Next player will get {} choices.'.format(FACE_CARD_VALUES[card_taken[0]]))
            present_options = True # Indicate that the next player should get options
            face_card_rank = card_taken[0] # Indicates what options next player should get
        else:
            present_options = False
            face_card_rank = 1
        iter += 1
        time.sleep(DEAL_SLEEP)
        input('Press Enter to continue!')
    end()

if __name__ == '__main__':
    play_game()
