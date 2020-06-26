def right_shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

print([1, 0, 0, 0, 0, 0, 0, 0])
print(right_shift([1, 0, 0, 0, 0, 0, 0, 0],1))
print(right_shift([1, 0, 0, 0, 0, 0, 0, 0],7))
