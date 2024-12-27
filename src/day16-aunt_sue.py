from santas_little_helpers import day, get_data, timed

today = day(2015, 16)
sue_criteria = {
  'children': 3,
  'cats': 7,
  'samoyeds': 2,
  'pomeranians': 3,
  'akitas': 0,
  'vizslas': 0,
  'goldfish': 5,
  'trees': 3,
  'cars': 2,
  'perfumes': 1,
}


def analyse_data_points(data, ranges=False):
  for sue, data_points in data:
    for key, value in sue_criteria.items():
      if key not in data_points:
        continue
      if ranges and key in ['cats', 'trees']:
        if data_points[key] <= value:
          break
      elif ranges and key in ['pomeranians', 'goldfish']:
        if data_points[key] >= value:
          break
      elif data_points[key] != value:
        break
    else:
      return sue
  return None


def parse(line):
  sue, raw_data = line.split(": ", 1)
  data = dict()
  for data_point in raw_data.split(', '):
    key, value = data_point.split(': ')
    data[key] = int(value)
  return sue.split()[1], data


def main():
  data = list(get_data(today, parse))
  print(f'{today} star 1 = {analyse_data_points(data)}')
  print(f'{today} star 2 = {analyse_data_points(data, ranges=True)}')


if __name__ == '__main__':
  timed(main)
