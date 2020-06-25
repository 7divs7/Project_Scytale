def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

print(shift([1, 0, 0, 0, 0, 0, 0, 1],1))