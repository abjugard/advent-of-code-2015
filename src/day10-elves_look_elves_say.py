from itertools import groupby
from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 10)


def expand(sequence):
  return ''.join(f'{len(list(cs))}{c}' for c, cs in groupby(sequence))


def look_and_say(sequence, n=40):
  for _ in range(n):
    sequence = expand(sequence)
  return len(sequence)


def main():
  data = next(get_data(today))
  print_stars(
    today,
    look_and_say(data),
    look_and_say(data, n=50)
  )


if __name__ == '__main__':
  timed(main)
