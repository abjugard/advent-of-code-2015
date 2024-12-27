from collections import defaultdict
from itertools import combinations
from santas_little_helpers import day, get_data, timed

today = day(2015, 17)


def fill_containers(data):
  count = defaultdict(int)
  for n in range(len(data)):
    for x in combinations(data, n):
      if sum(x) == 150:
        count[n] += 1
  return sum(count.values()), count[min(count.keys())]


def main():
  data = list(get_data(today, int))
  star1, star2 = fill_containers(data)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')


if __name__ == '__main__':
  timed(main)
