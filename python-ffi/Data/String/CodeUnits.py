def fromCharArray(a):
    return "".join(a)


def toCharArray(s):
    return s.split("")


def singleton(c):
    return c


def _charAt(just):
    return (
        lambda nothing: lambda i: lambda s: just(s[i])
        if i >= 0 and i < len(s)
        else nothing
    )


def _toChar(just):
    return lambda nothing: lambda s: just(s) if len(s) == 1 else nothing


length = len


def countPrefix(p):
    def ap(s):
        i = 0
        while i < len(s) and p(s[i]):
            i += 1
        return i

    return ap


def _indexOfImpl(just, nothing, x, s):
    i = s.find(x)
    return nothing if i == -1 else just(i)


def _indexOf(just):
    return lambda nothing: lambda x: lambda s: _indexOfImpl(just, nothing, x, s)


def _indexOfStartingAtImpl(just, nothing, x, startAt, s):
    if startAt < 0 or startAt > len(s):
        return nothing
    i = s.find(x, startAt)
    return nothing if i == -1 else just(i)


def _lastIndexOfImpl(just, nothing, x, s: str):
    i = s.rfind(x)
    return nothing if i == -1 else just(i)


def _lastIndexOf(just):
    return lambda nothing: lambda x: lambda s: _lastIndexOfImpl(just, nothing, x, s)


def _lastIndexOfStartAtImpl(just, nothing, x, startAt, s):
    if startAt < 0 or startAt > len(s):
        return nothing
    i = s.rfind(x, startAt)
    return nothing if i == -1 else just(i)


def _lastIndexOfStartingAt(just):
    return lambda nothing: lambda x: lambda startAt: lambda s: _lastIndexOfStartAtImpl(
        just, nothing, x, startAt, s
    )


def take(n: int):
    return lambda s: s[:n]

def drop(n: int):
    return lambda s: s[n:]


def _slice(b):
    return lambda e: lambda s: s[b:e]


def splitAt(i):
    return lambda s: {"before": s[:i], "after": s[i:]}
