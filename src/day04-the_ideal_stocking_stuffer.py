from hashlib import md5
from santas_little_helpers import day, get_data, timed

today = day(2015, 4)
i = 0


def mine_advent_coins(data, zeroes=5):
  global i
  while True:
    res = md5(str.encode(f'{data}{i}')).hexdigest()
    if res.startswith('0'*zeroes):
      return i
    i += 1


def main():
  data = next(get_data(today))
  print(f'{today} star 1 = {mine_advent_coins(data)}')
  print(f'{today} star 1 = {mine_advent_coins(data, zeroes=6)}')


if __name__ == '__main__':
  timed(main)