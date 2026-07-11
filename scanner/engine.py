from scanner.new_pairs import get_new_pairs

from scanner.filter import filter_tokens

def scan():

    pairs = get_new_pairs()

    good = filter_tokens(pairs)

    return good
