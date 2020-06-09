import re


def showRegexImpl(r):
    return "" + r


def regexImpl(left):
    raise NotImplementedError("FFI Not implemented. Data.String.Regex.regexImpl")


#   return function (right) {
#     return function (s1) {
#       return function (s2) {
#         try {
#           return right(new RegExp(s1, s2));
#         } catch (e) {
#           return left(e.message);
#         }


def source(r):
    return r["source"]


def flagsImpl(r):
    return {
        "multiline": r["multiline"],
        "ignoreCase": r["ignoreCase"],
        "global": r["global"],
        "sticky": bool(r["sticky"]),
        "unicode": bool(r["unicode"]),
    }


def test(r):
    raise NotImplementedError("FFI Not implemented. Data.String.Regex.test")


#   return function (s) {
#     var lastIndex = r.lastIndex;
#     var result = r.test(s);
#     r.lastIndex = lastIndex;
#     return result;


def _match(just):
    raise NotImplementedError("FFI Not implemented. Data.String.Regex._match")


#   return function (nothing) {
#     return function (r) {
#       return function (s) {
#         var m = s.match(r);
#         if (m == null || m.length === 0) {
#           return nothing;
#         } else {
#           for (var i = 0; i < m.length; i++) {
#             m[i] = m[i] == null ? nothing : just(m[i]);
#           }
#           return just(m);
#         }


def replace(r):
    return lambda s1: lambda s2: s2.replace(s1, 1)


def replaceBy(r):
    raise NotImplementedError("FFI Not implemented. Data.String.Regex.replaceBy")


#   return function (f) {
#     return function (s2) {
#       return s2.replace(r, function (match) {
#         return f(match)(Array.prototype.splice.call(arguments, 1, arguments.length - 3));
#       });


def _searchImpl(just, nothing, r, s):
    m = re.search(r, s)
    if m:
        return just(m.start())
    else:
        return nothing


def _search(just):
    return lambda nothing: lambda r: lambda s: _searchImpl(just, nothing, r, s)


def split(r):
    return lambda s: s.split(r)
