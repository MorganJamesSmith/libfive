"""
Python bindings to the libfive CAD kernel

DO NOT EDIT BY HAND!
This file is automatically generated from libfive/stdlib/stdlib.h

It was last generated on 2021-03-05 17:20:52 by user mattkeeter

This is libfive.stdlib.text
"""

from libfive.ffi import libfive_tree, tfloat, tvec2, tvec3, stdlib
from libfive.shape import Shape

import ctypes

stdlib.text.argtypes = [ctypes.c_char_p, tvec2]
stdlib.text.restype = libfive_tree
def text(txt, pos=(0, 0)):
    """ Returns the given text, rendered in a custom f-rep font
        (with a character height of 1)
    """
    args = [txt.encode('utf-8'), list([Shape.wrap(i) for i in pos])]
    return Shape(stdlib.text(
        args[0],
        tvec2(*[a.ptr for a in args[1]])))
