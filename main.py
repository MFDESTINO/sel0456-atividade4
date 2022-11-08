#!/usr/bin/env python3
import re


def fib(n):  #fibonacci recursivo
    if n > 1:
        return (fib(n-1) + fib(n-2))
    return n

def fact(n): #fatorial recursivo
    if n > 1:
        return n * fact(n-1)
    return 1

def output_line(n, x, y): #calcula os valores e gera a linha no formato desejado
    return 'Linha {}: Fib({})={} Fact({})={}\n'.format(n, x, fib(x), y, fact(y))

def generate_output_file(input_fname, output_fname):
    with open(input_fname, 'r') as finput:
        lines = finput.readlines() #le as linhas do arquivo de entrada
    exp = re.compile('([0-9]+)[,\ ]([0-9]+)') #regex para pegar os dois valores separados por virgula ou espaco
    with open(output_fname, 'w') as f:
        for i, line in enumerate(lines):
            m = exp.match(line)
            if m: #se a linha estiver no formato desejado, havera match
                x, y = [int(x) for x in m.groups()] #pega os dois valores e transforma em int
                f.write(output_line(i, x, y)) #escreve a linha no formato desejado


if __name__ == '__main__':
    generate_output_file('input.dat', 'output.dat')
