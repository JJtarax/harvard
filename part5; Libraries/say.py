'''import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])'''
import sys

from sayings import hello

if len(sys.agrv) == 2:
    hello(sys.agrv[1])