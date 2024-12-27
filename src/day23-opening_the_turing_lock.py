from collections import defaultdict
from santas_little_helpers import day, get_data, timed, print_stars

today = day(2015, 23)


def run_vm(program, a=0):
  pc = 0
  registers = defaultdict(int)
  registers['a'] = a
  while pc < len(program):
    instr, operands = program[pc]
    if instr == 'hlf':
      register, *_ = operands
      registers[register] //= 2
    elif instr == 'tpl':
      register, *_ = operands
      registers[register] *= 3
    elif instr == 'inc':
      register, *_ = operands
      registers[register] += 1
    elif instr == 'jmp':
      offset, *_ = operands
      pc += offset - 1
    elif instr == 'jie':
      register, offset = operands
      if registers[register] % 2 == 0:
        pc += offset - 1
    elif instr == 'jio':
      register, offset = operands
      if registers[register] == 1:
        pc += offset - 1
    pc += 1
  return registers['b']


def parse(line):
  instr = line[:3]
  return instr, tuple(
    int(v) if v[-1].isnumeric() else v
    for v in line[4:].split(', ')
  )


def main():
  program = list(get_data(today, parse))
  print_stars(
    today,
    run_vm(program),
    run_vm(program, a=1)
  )


if __name__ == '__main__':
  timed(main)
