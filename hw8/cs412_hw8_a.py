"""
name: Alex Polivka
This work abides by the JMU honor code.
"""

from collections import defaultdict


def arbitrage(edges):
    cur_dollar = 1.0

    # multiplies each edge by their weight
    for edge in edges:
        cur_dollar = cur_dollar*edges[edge]
    
    # checks if the dollar has increased or decreased
    if cur_dollar > 1.0 or cur_dollar < 1.0:
        print("Arbitrage Detected")
    else:
        print("No Arbitrage Detected")
    pass


def main():
    n = int(input())
    edges = defaultdict()
    # gathers each edge and their weight
    for x in range(n):
        values = input().split()
        edges[(values[0], values[1])] = float(values[2])
    arbitrage(edges)
    

if __name__ == "__main__":
    main()