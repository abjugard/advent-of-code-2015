from santas_little_helpers import day, get_data, timed

today = day(2015, 7)


def process(op, inps):
  if op == 'NOP':
    return inps[0]
  elif op == 'NOT':
    return ~inps[0] & 0xffff
  elif op == 'AND':
    return inps[0] & inps[1]
  elif op == 'OR':
    return inps[0] | inps[1]
  elif op == 'RSHIFT':
    return inps[0] >> inps[1]
  elif op == 'LSHIFT':
    return inps[0] << inps[1]


def calculate_a(inputs, operations):
  while 'a' not in inputs:
    for op, operands, out in operations:
      if out in inputs:
        continue
      if all(inp in inputs for inp in operands if isinstance(inp, str)):
        inps = [inp if isinstance(inp, int) else inputs[inp] for inp in operands]
        inputs[out] = process(op, inps)
  return inputs['a']


def parse_data(data):
  inputs, operations = {}, []
  for line in data:
    line, out = line.split(' -> ')
    tokens = line.split()
    if len(tokens) == 1:
      operand = tokens[0]
      if operand[-1].isdigit():
        inputs[out] = int(operand)
      else:
        operations.append(('NOP', (operand,), out))
    elif len(tokens) == 2:
      op, operand = tokens
      operations.append((op, (operand,), out))
    elif len(tokens) == 3:
      l, op, r = tokens
      if l.isdigit(): l = int(l)
      if r.isdigit(): r = int(r)
      operations.append((op, (l, r), out))
  return inputs, operations


def main():
  inputs, operations = parse_data(get_data(today))
  star1 = calculate_a(inputs.copy(), operations.copy())
  print(f'{today} star 1 = {star1}')
  inputs['b'] = star1
  print(f'{today} star 1 = {calculate_a(inputs, operations)}')


if __name__ == '__main__':
  timed(main)
