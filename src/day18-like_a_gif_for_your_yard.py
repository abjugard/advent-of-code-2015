from santas_little_helpers import day, get_data, timed, print_stars
from santas_little_utils import build_dict_map, neighbours

today = day(2015, 18)


def simulate_game_of_life(map_data, lit_corners=False):
  def ensure_lit_corners():
    for c in [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]:
      the_map[c] = True
  the_map, (w, h) = map_data
  t = 0
  while t < 100:
    if lit_corners:
      ensure_lit_corners()
    next_map = the_map.copy()
    for p in the_map:
      ns = sum(the_map[np] for np in neighbours(p, diagonals=True, borders=the_map))
      if the_map[p]:
        next_map[p] = ns in [2, 3]
      else:
        next_map[p] = ns == 3
    the_map = next_map
    t += 1
  if lit_corners:
    ensure_lit_corners()
  return sum(the_map.values())


def main():
  map_data = build_dict_map(get_data(today), conv_func=lambda c, p: c == '#')
  print_stars(
    today,
    simulate_game_of_life(map_data),
    simulate_game_of_life(map_data, lit_corners=True)
  )


if __name__ == '__main__':
  timed(main)
