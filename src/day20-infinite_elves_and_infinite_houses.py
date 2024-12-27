from collections import defaultdict
from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 20)
MAX_ELVES = 790_000 # Crank this number for other inputs


def find_house_index(target, elf_limit=MAX_ELVES, elf_efficiency=10):
  houses = defaultdict(int)
  for elf in range(1, target):
    for house in range(elf, min(elf * elf_limit, MAX_ELVES), elf):
      houses[house] += elf * elf_efficiency
    if houses[elf] >= target:
      return elf


def main():
  data = next(get_data(today, int))
  print_stars(
    today,
    find_house_index(data),
    find_house_index(data, elf_limit=50, elf_efficiency=11)
  )


if __name__ == '__main__':
  timed(main)
