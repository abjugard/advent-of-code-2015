from collections import defaultdict
from itertools import pairwise, permutations
from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 9)


def parse(line):
  l, _, r, *_, dist = line.split()
  return l, r, int(dist)


def main():
  distance = defaultdict(dict)
  for l, r, dist in get_data(today, parse):
    distance[l][r] = dist
    distance[r][l] = dist
  path_lengths = [
    sum(distance[l][r] for l, r in pairwise(path))
    for path in permutations(distance.keys())
  ]
  print_stars(
    today,
    min(path_lengths),
    max(path_lengths)
  )


if __name__ == '__main__':
  timed(main)
