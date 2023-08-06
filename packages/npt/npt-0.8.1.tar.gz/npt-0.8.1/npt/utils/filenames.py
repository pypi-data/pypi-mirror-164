import os

from . import log

def change_extension(filename, new_ext):
    """
    Change file extension
    """
    fn = '.'.join(filename.split('.')[:-1] + [new_ext])
    return fn

def change_dirname(filename, new_dir):
    """
    Change file directory path ("dirname")
    """
    bn = os.path.basename(filename)
    fn = os.path.join(new_dir, bn)
    return fn

def insert_preext(filename, sub_ext):
    """
    Insert a pre-extension before file extension

    E.g:    'file.csv' -> 'file.xyz.csv'
    """
    fs = filename.split('.')
    fs.insert(-1, sub_ext)
    fn = '.'.join(fs)
    return fn
