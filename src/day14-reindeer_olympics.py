import re
from collections import defaultdict
from santas_little_helpers import day, get_data, timed
from santas_little_utils import ints

today = day(2015, 14)
reindeer_re = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')


def get_distance(velocity, duration, rest_period, t):
  full = duration * (t // (duration + rest_period))
  partial = min([duration, (t % (duration + rest_period))])
  return velocity * (full + partial)


def simulate_race(reindeer):
  distances = dict()
  points = defaultdict(int)
  for t in range(1, 2504):
    for name, *vals in reindeer:
      distances[name] = get_distance(*vals, t)
    for name, *_ in reindeer:
      if distances[name] == max(distances.values()):
        points[name] += 1
  return max(distances.values()), max(points.values())


def parse(line):
  name, *vals = reindeer_re.match(line).groups()
  return name, *ints(vals)


def main():
  data = list(get_data(today, parse))
  star1, star2 = simulate_race(data)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')


if __name__ == '__main__':
  timed(main)
