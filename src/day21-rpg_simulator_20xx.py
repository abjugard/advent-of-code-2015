from itertools import combinations
from santas_little_helpers import day, get_data, timed

today = day(2015, 21)

              # Item       Cost Damage Armor
weapon_shop = {'Dagger':      (8, 4, 0),
               'Shortsword': (10, 5, 0),
               'Warhammer':  (25, 6, 0),
               'Longsword':  (40, 7, 0),
               'Greataxe':   (74, 8, 0)}
armour_shop = {'None':        (0, 0, 0),
               'Leather':    (13, 0, 1),
               'Chainmail':  (31, 0, 2),
               'Splintmail': (53, 0, 3),
               'Bandedmail': (75, 0, 4),
               'Platemail': (102, 0, 5)}
ring_shop =   {'None1':       (0, 0, 0),
               'None2':       (0, 0, 0),
               'Damage +1':  (25, 1, 0),
               'Damage +2':  (50, 2, 0),
               'Damage +3': (100, 3, 0),
               'Defense +1': (20, 0, 1),
               'Defense +2': (40, 0, 2),
               'Defense +3': (80, 0, 3)}


def buy_items():
  for weapon_name, (w_cost, w_dmg, _) in weapon_shop.items():
    for armour_name, (a_cost, _, a_armour) in armour_shop.items():
      for rings in combinations(ring_shop.keys(), 2):
        cost = w_cost + a_cost
        dmg = w_dmg
        armour = a_armour
        for ring in rings:
          r_cost, r_dmg, r_armour = ring_shop[ring]
          cost += r_cost
          dmg += r_dmg
          armour += r_armour
        yield cost, dmg, armour, (weapon_name, armour_name, *rings)


def fight(p_dmg, p_armour, b_hp, b_dmg, b_armour):
  player_hp = 100
  while player_hp > 0 and b_hp > 0:
    b_hp -= p_dmg - b_armour
    if b_hp <= 0:
      return True
    player_hp -= b_dmg - p_armour
  return False


def simulate_battle(boss):
  wins = set()
  losses = set()
  for cost, dmg, armour, names in buy_items():
    result = fight(dmg, armour, *boss)
    if result:
      wins.add(cost)
    else:
      losses.add(cost)
  return min(wins), max(losses)


def main():
  boss = tuple(get_data(today, [('split', ': '), ('elem', 1), ('func', int)]))
  star1, star2 = simulate_battle(boss)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 2 = {star2}')


if __name__ == '__main__':
  timed(main)
