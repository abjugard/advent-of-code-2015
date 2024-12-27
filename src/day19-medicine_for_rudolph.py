from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 19)


def distinct_molecules(replacements, molecule):
  seen = set()
  for l, r in replacements:
    for i in range(len(molecule)):
      if molecule[i:].startswith(l):
        seen.add(molecule[:i] + r + molecule[i+len(l):])
  return len(seen)


def steps_to_make(replacements, molecule):
  initial_replacements = replacements.copy()
  steps, curr = 0, molecule
  while curr != 'e':
    try:
      replacement = max(replacements, key=lambda x: len(x[1]))
    except:
      replacements = initial_replacements.copy()
      replacement = max(replacements, key=lambda x: len(x[1]))
    l, r = replacement
    n_molecule = curr.replace(r, l, 1)
    if curr != n_molecule:
      steps += 1
    else:
      replacements.remove(replacement)
    curr = n_molecule
  return steps


def main():
  replacements, molecule = list(get_data(today, groups=True))
  replacements = [line.split(' => ') for line in replacements]
  molecule = next(molecule)
  print_stars(
    today,
    distinct_molecules(replacements, molecule),
    steps_to_make(replacements, molecule)
  )


if __name__ == '__main__':
  timed(main)
