"""
Authors: Alex Polivka and Devon Boldt
This work abides by the JMU Honor Code

"""
def main():
    vertices = int(input())
    dict = {}
    
    for line in range(vertices):
        line = input().split()
        dict[line[0]] = line[1:]

    query = input().split()
    is_np = True

    for edge in query:
        for check in query:
            if check in dict[edge]:
                is_np = False
    print(str(is_np).upper())     


if __name__ == "__main__":
    main()