import hashlib


def str_md5(s):
    return hashlib.md5(s.encode(encoding='UTF-8')).hexdigest()


def file_md5(f):
    m = hashlib.md5()
    m.update(f.read())
    return m.hexdigest()
