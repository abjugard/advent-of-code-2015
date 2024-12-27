from collections import Counter
from itertools import combinations_with_replacement
from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 15)


def optimise_cookie_recipe(stats, meal_replacement=False):
  best = 0
  for recipe in combinations_with_replacement(stats.keys(), 100):
    cap = dur = fla = tex = cal = 0
    for ingredient, count in Counter(recipe).items():
      i_cap, i_dur, i_fla, i_tex, i_cal = stats[ingredient]
      cap += count * i_cap
      dur += count * i_dur
      fla += count * i_fla
      tex += count * i_tex
      cal += count * i_cal
    if meal_replacement and cal != 500:
      continue
    if any(attr <= 0 for attr in [cap, dur, fla, tex]):
      continue
    best = max(best, cap * dur * fla * tex)
  return best


def parse(line):
  ingredient, rest = line.split(': ')
  return ingredient, [int(stat.split()[1]) for stat in rest.split(', ')]


def main():
  data = get_data(today, parse)
  stats = {ingredient: stat_values for ingredient, stat_values in data}
  print_stars(
    today,
    optimise_cookie_recipe(stats),
    optimise_cookie_recipe(stats, meal_replacement=True)
  )


if __name__ == '__main__':
  timed(main)
