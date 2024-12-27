from santas_little_helpers import day, get_data, timed
from santas_little_utils import ints, all_points

today = day(2015, 6)


def set_dumb_lights(instructions):
  grid = {p: False for p in all_points(1000, 1000)}
  for instr, ps in instructions:
    if instr.startswith('turn'):
      changes = {p: ('on' in instr) for p in ps}
    else:
      changes = {p: (not grid[p]) for p in ps}
    grid |= changes
  return sum(grid.values())


def set_dimmable_lights(instructions):
  grid = {p: 0 for p in all_points(1000, 1000)}
  for instr, ps in instructions:
    if instr == 'turn_off':
      for p in ps:
        grid[p] = max(0, grid[p] - 1)
      continue
    for p in ps:
      grid[p] += 1 if instr == 'turn_on' else 2
  return sum(grid.values())


def parse(line):
  line = line.replace('turn ', 'turn_')
  instr, tl, _, br = line.split()
  x_start, y_start = ints(tl, ',')
  x_end, y_end = ints(br, ',')

  points = set()
  for y in range(y_start, y_end+1):
    for x in range(x_start, x_end+1):
      points.add((x, y))
  return instr, points


def main():
  instructions = list(get_data(today, parse))
  print(f'{today} star 1 = {set_dumb_lights(instructions)}')
  print(f'{today} star 1 = {set_dimmable_lights(instructions)}')


if __name__ == '__main__':
  timed(main)
