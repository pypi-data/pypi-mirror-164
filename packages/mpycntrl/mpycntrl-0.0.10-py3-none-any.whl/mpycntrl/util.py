import hashlib


def get_file_hash_256(fnam, blk_size=256):
    hm = hashlib.sha256()
    with open(fnam, "rb") as f:
        while True:
            buf = f.read(blk_size)
            if len(buf) == 0:
                break
            hm.update(buf)
    digest = hm.hexdigest()
    return digest
