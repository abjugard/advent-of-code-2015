from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 2)


def calculate_wrapping_paper(data):
  area = 0
  for l, w, h in data:
    sides = [l*w, w*h, h*l]
    area += sum(2*side for side in sides) + min(sides)
  return area


def calculate_ribbon(data):
  ribbon = 0
  for l, w, h in data:
    sides = [2*(l+w), 2*(w+h), 2*(h+l)]
    ribbon += min(sides) + l*w*h
  return ribbon


def parse(line):
  return tuple(map(int, line.split('x')))


def main():
  data = list(get_data(today, parse))
  print_stars(
    today,
    calculate_wrapping_paper(data),
    calculate_ribbon(data)
  )


if __name__ == '__main__':
  timed(main)
