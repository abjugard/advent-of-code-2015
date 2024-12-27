from itertools import pairwise
from string import ascii_lowercase
from santas_little_helpers import day, get_data, timed

today = day(2015, 11)


def increment_string(s, alph=ascii_lowercase):
  data, max_idx = list(s), len(alph) - 1
  for i in reversed(range(len(data))):
    if data[i] != alph[max_idx]:
      data[i] = alph[alph.index(data[i]) + 1]
      return ''.join(data)
    data[i] = alph[0]
  return alph[0] + ''.join(data)


def increasing_straight(password):
  return any(
    password[i:i+3] in ascii_lowercase
    for i in range(len(password) - 2)
  )


def not_iol(password):
  return all(c not in 'iol' for c in password)


def has_pairs(password):
  for i, (c, cn) in enumerate(pairwise(password)):
    if c != cn:
      continue
    for c2, c2n in pairwise(password[i+2:]):
      if c != c2 and c2 == c2n:
        return True
  return False


all_rules = [
  increasing_straight,
  not_iol,
  has_pairs,
]


def password_generator(password):
  while True:
    if all(rule(password) for rule in all_rules):
      yield password
    password = increment_string(password)


def main():
  data = next(get_data(today))
  star_gen = password_generator(data)
  print(f'{today} star 1 = {next(star_gen)}')
  print(f'{today} star 2 = {next(star_gen)}')


if __name__ == '__main__':
  timed(main)
