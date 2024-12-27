import re
from collections import defaultdict
from itertools import pairwise, permutations
from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 13)
parse_re = re.compile(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).')


def score(guests, arrangement):
  count = 0
  for l, r in pairwise(arrangement + (arrangement[0],)):
    count += guests[l][r]
    count += guests[r][l]
  return count


def optimise_seating(guests, additional=None):
  guest_list = list(guests.keys())
  if additional is not None:
    guest_list.extend(additional)
  return max(
    score(guests, arrangement)
    for arrangement in permutations(guest_list)
  )


def parse(line):
  l, op, change, r = parse_re.match(line).groups()
  if op == 'lose':
    change = f'-{change}'
  return l, r, int(change)


def main():
  data = list(get_data(today, parse))
  guests = defaultdict(lambda: defaultdict(int))
  for l, r, change in data:
    guests[l][r] = change
  print_stars(
    today,
    optimise_seating(guests),
    optimise_seating(guests, additional=["Me"])
  )


if __name__ == '__main__':
  timed(main)
