from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 8)
escape_chars = '\\"'


def main():
  data = list(get_data(today))
  print_stars(
    today,
    sum(len(l) - len(eval(l)) for l in data),
    sum(sum(l.count(c) for c in escape_chars) + 2 for l in data)
  )


if __name__ == '__main__':
  timed(main)
