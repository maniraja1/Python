def prinfol(path):
    import os

    for f in os.listdir(path):
        fpath = os.path.join(path,f)
        if os.path.isdir(fpath):
            print(fpath, os.path.isdir(fpath))
            prinfol(fpath)
        else:
            print("     ",os.path.join(path,f),os.path.isdir(f))


prinfol('/var/log')