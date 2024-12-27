from collections import Counter
from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 1)


def first_visit_to_basement(data):
  floor = 0
  for idx, c in enumerate(data):
    floor += 1 if c == '(' else -1
    if floor < 0:
      return idx + 1


def main():
  data = next(get_data(today))
  counts = Counter(data)
  print_stars(
    today,
    counts["("]-counts[")"],
    first_visit_to_basement(data)
  )

if __name__ == '__main__':
  timed(main)
