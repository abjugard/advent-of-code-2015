from santas_little_helpers import day, get_data, timed

today = day(2015, 5)
vowels = set('aeiou')
naughty = {'ab', 'cd', 'pq', 'xy'}


def is_nice(word):
  last, repeats, vowel = None, False, ''
  for c in word:
    if c in vowels:
      vowel += c
    if last is not None:
      if f'{last}{c}' in naughty:
        return False
      if last == c:
        repeats = True
    last = c
  return repeats and len(vowel) >= 3


def real_is_nice(word):
  for i in range(len(word)-3):
    token = word[i:i+2]
    if token in word[i+2:]:
      break
  else:
    return False
  for i in range(len(word)-2):
    if word[i] == word[i+2]:
      return True
  return False


def main():
  star1 = star2 = 0
  for word in get_data(today):
    star1 += is_nice(word)
    star2 += real_is_nice(word)
  print(f'{today} star 1 = {star1}')
  print(f'{today} star 1 = {star2}')


if __name__ == '__main__':
  timed(main)
