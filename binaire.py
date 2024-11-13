def binaire(N):
    if N == 0:
        return []
    return binaire(N//2)+[N % 2]


print(binaire(16))
