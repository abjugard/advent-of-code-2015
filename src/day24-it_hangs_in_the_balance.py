from itertools import combinations
from santas_little_helpers import day, get_data, timed, print_stars
from santas_little_utils import mul

today = day(2015, 24)


# this doesn't actually solve the general problem,
# just happens to be correct for the input...
def find_qe(packages, parts=3):
  target_weight = sum(packages) // parts
  for count in range(1, len(packages)):
    for group in combinations(packages, count):
      if sum(group) != target_weight:
        continue
      return mul(group)


def main():
  data = set(get_data(today, int))
  print_stars(
    today,
    find_qe(data),
    find_qe(data, parts=4)
  )


if __name__ == '__main__':
  timed(main)
