def rotLeft(a, d):
    assert 1 <= d <= len(a)

    if len(a) == d:
        return a

    return a[d:len(a)] + a[0:d]
