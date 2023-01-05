n = int(input())
for _ in range(n):
    words = input().split(" ")
    for word in reversed(words):
        print(word)