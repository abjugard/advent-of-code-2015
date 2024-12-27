from math import inf as infinity
from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 22)


def fight(boss, hard_mode=False):
  def fight_rec(hp, mana, b_hp, shield_t=0, poison_t=0, recharge_t=0, player_turn=False):
    n_shield_t =   max(0, shield_t   - 1)
    n_poison_t =   max(0, poison_t   - 1)
    n_recharge_t = max(0, recharge_t - 1)

    if poison_t:
      b_hp -= 3
    if recharge_t:
      mana += 101

    if b_hp <= 0:
      return 0

    if player_turn:
      if mana < 53:
        return infinity
      if hard_mode:
        hp -= 1
      costs = []
      if mana >= 53:
        costs.append(53 + fight_rec(hp, mana-53, b_hp-4, n_shield_t, n_poison_t, n_recharge_t))
      if mana >= 73:
        costs.append(73 + fight_rec(hp+2, mana-73, b_hp-2, n_shield_t, n_poison_t, n_recharge_t))
      if mana >= 113 and n_shield_t == 0:
        costs.append(113 + fight_rec(hp, mana-113, b_hp, 6, n_poison_t, n_recharge_t))
      if mana >= 173 and n_poison_t == 0:
        costs.append(173 + fight_rec(hp, mana-173, b_hp, n_shield_t, 6, n_recharge_t))
      if mana >= 229 and n_recharge_t == 0:
        costs.append(229 + fight_rec(hp, mana-229, b_hp, n_shield_t, n_poison_t, 5))
      return min(costs)
    else:
      p_armor = 0 if shield_t == 0 else 7
      hp -= max(1, b_dmg - p_armor)
      if hp <= 0:
        return infinity
      return fight_rec(hp, mana, b_hp, n_shield_t, n_poison_t, n_recharge_t, True)

  b_hp_initial, b_dmg = boss
  return fight_rec(50, 500, b_hp_initial, player_turn=True)


def main():
  boss = tuple(get_data(today, [('split', ': '), ('elem', 1), ('func', int)]))
  print_stars(
    today,
    fight(boss),
    fight(boss, hard_mode=True)
  )


if __name__ == '__main__':
  timed(main)
