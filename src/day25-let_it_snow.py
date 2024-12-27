import re
from santas_little_helpers import day, get_data, timed

today = day(2015, 25)
parse_re = re.compile(r'row (\d+), column (\d+)')


def break_copy_protection(row, col):
  r, c, code = 1, 1, 20151125
  while True:
    if r == row and c == col:
      return code
    r -= 1
    c += 1
    if r == 0:
      r, c = c, 1
    code *= 252533
    code %= 33554393


def parse(line):
  row, column = parse_re.search(line).groups()
  return int(row), int(column)


def main():
  row, col = next(get_data(today, parse, groups=False))
  print(f'{today} star 1 = {break_copy_protection(row, col)}')


if __name__ == '__main__':
  timed(main)
