def _unsafeCodePointAt0(fallback):
    def ap(s):
        return ord(s[0])

    return ap


def _codePointAtImpl(fallback, just, nothing, unsafeCodePointAt0, index, s):
    length = len(s)
    if index < 0 or index >= length:
        return nothing
    else:
        return just(unsafeCodePointAt0(s[index]))


def _codePointAt(fallback):
    return lambda just: lambda nothing: lambda unsafeCodePointAt0: lambda index: lambda s: _codePointAtImpl(
        fallback, just, nothing, unsafeCodePointAt0, index, s
    )


def _codePrefixImpl(fallback, unsafeCodePointAt0, pred, s):
    cpCount = 0
    for x in s:
        cp = unsafeCodePointAt0(x)
        if not pred(cp):
            return cpCount
        else:
            cpCount += 1
    return cpCount


def _fromCodePointArray(singleton):
    def ap(cps):
        return "".join(map(_singleton, cps))

    return ap


def _singleton(fallback):
    return chr


def _take(fallback):
    def ap(n):
        return lambda s: s[:n]

    return ap


def _toCodePointArray(fallback):
    def ap(unsafeCodePointAt0):
        return lambda s: list(map(unsafeCodePointAt0, s))

    return ap


def _countPrefix(fallback):
    def unsafeCodePointAt0_(unsafeCodePointAt0):
        def pred_(pred):
            def str_(s):
                count = 0
                for x in s:
                    if not pred(x):
                        return count
                    else:
                        count += 1

            return str_

        return pred_

    return unsafeCodePointAt0_
