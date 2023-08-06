# This file is placed in the Public Domain.
# pylint: disable=E1101,E0611,C0116,C0413,C0411,W0406,W0613,W0105


"utility"


import json
import pathlib
import time
import _thread


def cdir(path):
    if os.path.exists(path):
        return
    if path.split(os.sep)[-1].count(":") == 2:
        path = os.path.dirname(path)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


def fntime(daystr):
    daystr = daystr.replace("_", ":")
    datestr = " ".join(daystr.split(os.sep)[-2:])
    datestr = datestr.split(".")[0]
    return time.mktime(time.strptime(datestr, "%Y-%m-%d %H:%M:%S"))


def locked(lock):

    def lockeddec(func, *args, **kwargs):
        def lockedfunc(*args, **kwargs):
            lock.acquire()
            res = None
            try:
                res = func(*args, **kwargs)
            finally:
                lock.release()
            return res

        lockeddec.__wrapped__ = func
        return lockedfunc

    return lockeddec


def spl(txt):
    try:
        res = txt.split(",")
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]



def listfiles(workdir):
    path = os.path.join(workdir, "store")
    if not os.path.exists(path):
        return []
    return sorted(os.listdir(path))


"object"


import copy as copying
import datetime
import os
import uuid


def __dir__():
    return (
            'Class',
            'Db',
            'Default',
            'Object',
            'ObjectDecoder',
            'ObjectEncoder',
            'Wd',
            'cdir',
            'clear',
            'copy',
            'edit',
            'find',
            'fntime',
            'get',
            'items',
            'keys',
            'last',
            'load',
            'locked',
            'pop',
            'popitem',
            'prt',
            'register',
            'save',
            'search',
            'setdefault',
            'spl',
            'update',
            'values'
           )


class Wd:

    workdir = ".botlib"


class Object:

    "object"

    __slots__ = (
        "__dict__",
        "__otype__",
        "__stp__",
        "__deleted__"
    )


    def __init__(self):
        object.__init__(self)
        self.__otype__ = str(type(self)).split()[-1][1:-2]
        self.__stp__ = os.path.join(
            self.__otype__,
            str(uuid.uuid4()),
            os.sep.join(str(datetime.datetime.now()).split()),
        )

    def __delitem__(self, key):
        if key in self:
            del self.__dict__[key]

    def __getitem__(self, key):
        return self.__dict__[key]

    def __getstate__(self):
        return self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __str__(self):
        return str(self.__dict__)


def clear(oobj):
    oobj.__dict__ = {}


def copy(oobj):
    return copying.copy(oobj)


def get(oobj, key, default=None):
    return oobj.__dict__.get(key, default)


def items(oobj):
    try:
        return oobj.__dict__.items()
    except AttributeError:
        return oobj.items()

def keys(oobj):
    try:
        return oobj.__dict__.keys()
    except (AttributeError, TypeError):
        return oobj.keys()


def pop(oobj, key, default=None):
    try:
        return oobj[key]
    except KeyError as ex:
        if default:
            return default
        raise KeyError from ex


def popitem(oobj):
    key = keys(oobj)
    if key:
        value = oobj[key]
        del oobj[key]
        return (key, value)
    raise KeyError


def register(oobj, key, value):
    setattr(oobj, key, value)


def setdefault(oobj, key, default=None):
    if key not in oobj:
        oobj[key] = default
    return oobj[key]


def update(oobj, data):
    try:
        oobj.__dict__.update(vars(data))
    except TypeError:
        oobj.__dict__.update(data)
    return oobj


def values(oobj):
    try:
        return oobj.__dict__.values()
    except TypeError:
        return oobj.values()


"default"


class Default(Object):

    def __getattr__(self, key):
        return self.__dict__.get(key, "")


"json"


class ObjectDecoder(json.JSONDecoder):

    def decode(self, s, _w=None):
        value = json.loads(s)
        oobj = Object()
        update(oobj, value)
        return oobj


class ObjectEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, dict):
            return o.items()
        if isinstance(o, Object):
            return vars(o)
        if isinstance(o, list):
            return iter(o)
        if isinstance(o,
                      (type(str), type(True), type(False),
                       type(int), type(float))):
            return o
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)


def dump(oobj, opath):
    if opath.split(os.sep)[-1].count(":") == 2:
        dirpath = os.path.dirname(opath)
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)
    with open(opath, "w", encoding="utf-8") as ofile:
        json.dump(
            oobj.__dict__, ofile, cls=ObjectEncoder, indent=4, sort_keys=True
        )
    return oobj.__stp__


def dumps(oobj):
    return json.dumps(oobj, cls=ObjectEncoder)


def load(oobj, opath):
    splitted = opath.split(os.sep)
    stp = os.sep.join(splitted[-4:])
    lpath = os.path.join(Wd.workdir, "store", stp)
    if os.path.exists(lpath):
        with open(lpath, "r", encoding="utf-8") as ofile:
            res = json.load(ofile, cls=ObjectDecoder)
            update(oobj, res)
    oobj.__stp__ = stp


def loads(name):
    return json.loads(name, cls=ObjectDecoder)


def save(oobj, stime=None):
    prv = os.sep.join(oobj.__stp__.split(os.sep)[:2])
    oobj.__stp__ = os.path.join(
                                prv,
                                os.sep.join(str(datetime.datetime.now()).split())
                               )
    opath = os.path.join(Wd.workdir, "store", oobj.__stp__)
    dump(oobj, opath)
    os.chmod(opath, 0o444)
    return oobj.__stp__


"database"


dblock = _thread.allocate_lock()


class Class():

    cls = {}

    @staticmethod
    def add(clz):
        Class.cls["%s.%s" % (clz.__module__, clz.__name__)] =  clz

    @staticmethod
    def full(name):
        name = name.lower()
        res = []
        for cln in Class.cls:
            if cln.split(".")[-1].lower() == name:
                res.append(cln)
        return res

    @staticmethod
    def get(name):
        return Class.cls.get(name, None)

    @staticmethod
    def remove(name):
        del Class.cls[name]


class Db(Object):

    names = Object()

    @staticmethod
    def all(otype, timed=None):
        result = []
        for fnm in fns(otype, timed):
            oobj = hook(fnm)
            if "__deleted__" in oobj and oobj.__deleted__:
                continue
            result.append((fnm, oobj))
        if not result:
            return []
        return result

    @staticmethod
    def find(otype, selector=None, index=None, timed=None):
        if selector is None:
            selector = {}
        _nr = -1
        result = []
        for fnm in fns(otype, timed):
            oobj = hook(fnm)
            if selector and not search(oobj, selector):
                continue
            if "__deleted__" in oobj and oobj.__deleted__:
                continue
            _nr += 1
            if index is not None and _nr != index:
                continue
            result.append((fnm, oobj))
        return result

    @staticmethod
    def lastmatch(otype, selector=None, index=None, timed=None):
        dbs = Db()
        res = sorted(dbs.find(otype, selector, index, timed),
                     key=lambda x: fntime(x[0]))
        if res:
            return res[-1]
        return (None, None)

    @staticmethod
    def lasttype(otype):
        fnn = fns(otype)
        if fnn:
            return hook(fnn[-1])
        return None

    @staticmethod
    def lastfn(otype):
        fnm = fns(otype)
        if fnm:
            fnn = fnm[-1]
            return (fnn, hook(fnn))
        return (None, None)

    @staticmethod
    def remove(otype, selector=None):
        has = []
        for _fn, oobj in Db.find(otype, selector or {}):
            oobj.__deleted__ = True
            has.append(oobj)
        for oobj in has:
            save(oobj)
        return has

    @staticmethod
    def types():
        path = os.path.join(Wd.workdir, "store")
        if not os.path.exists(path):
            return []
        return sorted(os.listdir(path))




@locked(dblock)
def fns(name, timed=None):
    if not name:
        return []
    path = os.path.join(Wd.workdir, "store", name) + os.sep
    if not os.path.exists(path):
        return []
    res = []
    dpath = ""
    for rootdir, dirs, _files in os.walk(path, topdown=False):
        if dirs:
            dpath = sorted(dirs)[-1]
            if dpath.count("-") == 2:
                ddd = os.path.join(rootdir, dpath)
                fls = sorted(os.listdir(ddd))
                if fls:
                    opath = os.path.join(ddd, fls[-1])
                    if (
                        timed
                        and "from" in timed
                        and timed["from"]
                        and fntime(opath) < timed["from"]
                    ):
                        continue
                    if timed and timed.to and fntime(opath) > timed.to:
                        continue
                    res.append(opath)
    return sorted(res, key=fntime)


@locked(dblock)
def hook(hfn):
    if hfn.count(os.sep) > 3:
        oname = hfn.split(os.sep)[-4:]
    else:
        oname = hfn.split(os.sep)
    cname = oname[0]
    cls = Class.get(cname)
    if cls:
        oobj = cls()
    else:
        oobj = Object()
    fnm = os.sep.join(oname)
    load(oobj, fnm)
    return oobj


def find(name, selector=None, index=None, timed=None, names=None):
    dbs = Db()
    if not names:
        names = Class.full(name)
    for nme in names:
        for fnm, oobj in dbs.find(nme, selector, index, timed):
            yield fnm, oobj


def last(oobj):
    dbs = Db()
    path, _obj = dbs.lastfn(oobj.__otype__)
    if _obj:
        update(oobj, _obj)
    if path:
        splitted = path.split(os.sep)
        stp = os.sep.join(splitted[-4:])
        return stp
    return None


Class.add(Object)


"functions"


def edit(oobj, setter):
    for key, value in items(setter):
        register(oobj, key, value)


def matchkey(oobj, key, default=None):
    res = None
    for key2 in keys(oobj):
        if key.lower() in key2.lower():
            res = key2
            break
    return res


def prt(oobj, args="", skip="_", empty=False, plain=False, **kwargs):
    keyz = list(keys(oobj))
    res = []
    if args:
        try:
            keyz = args.split(",")
        except (TypeError, ValueError):
            pass
    for key in keyz:
        try:
            skips = skip.split(",")
            if key in skips or key.startswith("_"):
                continue
        except (TypeError, ValueError):
            pass
        value = getattr(oobj, key, None)
        if not value and not empty:
            continue
        if " object at " in str(value):
            continue
        txt = ""
        if plain:
            txt = str(value)
        elif isinstance(value, str) and len(value.split()) >= 2:
            txt = '%s="%s"' % (key, value)
        else:
            txt = '%s=%s' % (key, value)
        res.append(txt)
    return " ".join(res)


def search(oobj, selector):
    res = False
    for key, value in items(selector):
        val = get(oobj, key)
        if value in str(val):
            res = True
            break
    return res
