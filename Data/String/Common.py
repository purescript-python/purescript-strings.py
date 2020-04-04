def _localeCompareImpl(lt, eq, gt, s1, s2):
    # TODO: write correct localeCompare

    # var result = s1.localeCompare(s2);
    # return result < 0 ? lt : result > 0 ? gt : eq;
    if s1 == s2:
        return eq
    if s1 < s2:
        return lt
    if s1 > s2:
        return gt


def _localeCompare(lt):
    return lambda eq: lambda gt: lambda s1: lambda s2: _localeCompareImpl(
        lt, eq, gt, s1, s2
    )


def replace(s1):
    return lambda s2: lambda s3: s3.replace(s1, s2, 1)


def replaceAll(s1):
    return lambda s2: lambda s3: s3.replace(s1, s2)


def split(sep):
    return lambda s: s.split(sep)


def toLower(s):
    return s.lower()


def toUpper(s):
    return s.upper()


def trim(s):
    return s.strip()


def joinWith(s):
    return lambda xs: s.join(xs)
