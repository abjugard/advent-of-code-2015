from santas_little_classes import Origo, Heading
from santas_little_helpers import day, get_data, timed

today = day(2015, 3)


def santa_only(data):
  p = Origo
  visited = { p.t }
  for x in data:
    p = p.next(Heading(x))
    visited.add(p.t)
  return len(visited)


def santa_and_robo(data):
  p = Origo
  p_r = Origo
  visited = { p.t }
  gen = iter(data)
  while True:
    d_santa = next(gen, None)
    if d_santa is None:
      break
    p = p.next(Heading(d_santa))
    visited.add(p.t)
    d_robo = next(gen, None)
    if d_robo is None:
      break
    p_r = p_r.next(Heading(d_robo))
    visited.add(p_r.t)
  return len(visited)


def main():
  data = next(get_data(today))
  print(f'{today} star 1 = {santa_only(data)}')
  print(f'{today} star 1 = {santa_and_robo(data)}')


if __name__ == '__main__':
  timed(main)
