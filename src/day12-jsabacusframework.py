import json
from santas_little_helpers import day, get_data, timed

today = day(2015, 12)


def flatten(dictionary, parent_key='', ignore=None):
  items = []
  for key, value in dictionary.items():
    new_key = '.'.join([parent_key, key]) if parent_key else key
    if isinstance(value, dict):
      if ignore is None or ignore not in value.values():
        items.extend(flatten(value, new_key, ignore).items())
    elif isinstance(value, list):
      l_val = {str(idx): val for idx, val in enumerate(value)}
      items.extend(flatten(l_val, new_key, ignore).items())
    else:
      items.append((new_key, value))
  return dict(items)


def sum_numbers(data):
  return sum(
    val
    for val in data.values()
    if isinstance(val, int)
  )


def main():
  data = json.loads(''.join(get_data(today)))
  print(f'{today} star 1 = {sum_numbers(flatten(data))}')
  print(f'{today} star 2 = {sum_numbers(flatten(data, ignore="red"))}')


if __name__ == '__main__':
  timed(main)
