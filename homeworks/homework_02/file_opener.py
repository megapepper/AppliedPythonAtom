#!/usr/bin/env python
import os.path


def _open_as_utf16(filepath: str):
    fh = None
    if not os.path.isfile(filepath):
        return None
    try:
        fh = open(filepath, 'r', encoding='utf16')
        str = fh.read(32)
    except UnicodeError:
        fh.close()
        return None
    fh.seek(0)
    return fh


def _open_as_utf8(filepath: str):
    fh = None
    if not os.path.isfile(filepath):
        return None
    try:
        fh = open(filepath, 'r', encoding='utf8')
        str = fh.read(32)
    except UnicodeError:
        fh.close()
        return None
    fh.seek(0)
    return fh


def _open_as_cp1251(filepath: str):
    fh = None
    if not os.path.isfile(filepath):
        return None
    fh = open(filepath, 'r', encoding='cp1251')
    return fh


def detect_and_open(filepath: str):
    fh = None
    fh = _open_as_utf16(filepath)
    if fh is not None:
        return fh
    fh = _open_as_utf8(filepath)
    if fh is not None:
        return fh
    fh = _open_as_cp1251(filepath)
    return fh
