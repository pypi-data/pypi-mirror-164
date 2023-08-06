import os
import glob
import json

from .util import get_file_hash_256


def cmd_exe(cmd, info, callb=None):
    print(info, "execute", cmd)
    rc = ""
    with os.popen(cmd) as proc:
        rcl = proc.readline()
        if callb:
            callb("proc-rc:", rcl)
        rc += rcl
    return rc


DEFAULT_SYNC = "mpycntrl_sync.json"


def sync_dev(sync_fnam, timeout=3, blocksize=512, create_folders=True, hash_copy=True):

    with open(sync_fnam) as f:
        cont = f.read()
        conf = json.loads(cont)

    include_pat = conf.get("include", [])
    remove_ext = conf.get("remove_ext", [])
    remove_pat = conf.get("remove", [])

    basepath = os.getcwd()

    path = os.path.expanduser(basepath)
    path = os.path.expandvars(path)
    path = os.path.abspath(path)

    path += os.path.sep

    print()
    print("basedir", path)
    print()

    found = []

    for pattern in include_pat:
        if pattern.startswith("#"):
            continue
        it = glob.iglob(path + pattern, recursive=True)
        found.extend(it)

    remove_pattern = [
        "/**/*" + x for x in filter(lambda x: not x.startswith("#"), remove_ext)
    ]
    remove_pattern.extend(remove_pat)

    for pattern in remove_pattern:
        if pattern.startswith("#"):
            continue
        it = glob.iglob(path + pattern, recursive=True)
        for i in it:
            try:
                found.remove(i)
            except:
                pass

    files = list(map(lambda x: x[len(path) :], found))

    folders = set(
        filter(lambda x: len(x) > 0, map(lambda x: os.path.dirname(x), files))
    )

    if create_folders:
        l = len(folders)
        for i, d in enumerate(folders):
            cmd = f"python3 -m mpycntrl -mkdir '{d}'"
            cmd_exe(cmd, info=f"{i+1}/{l}", callb=print)

    for i, f in enumerate(files):
        l = len(files)

        subcmd = "hashcopy" if hash_copy else "put"

        cmd = f"python3 -m mpycntrl -{subcmd} '{f}' -to {timeout} -bs {blocksize}"
        cmd_exe(cmd, info=f"{i+1}/{l}", callb=print)
