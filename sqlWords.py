#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $Id$

import sys
import optparse


SQLWORDS = (
    "INSERT", "DELETE", "SELECT", "UPDATE",
    "WHERE", "JOIN", "ON", "BEWTEEN", "AND",
    "OR", "VALUE", "VALUES", "INTO", "FROM",
)


def shiftSqlWords(line):
    words = line.split()
    tmpLine = []
    blankSpace = " "

    for word in words:
        tmpWord = word
        if word.upper() in SQLWORDS:
            tmpWord = word.upper()

        tmpLine.append(tmpWord)

    return blankSpace.join(tmpLine)


def run(options, args):
    input_file = args[0]
    fp = open(input_file, "r")

    for line in fp.readlines():
        print shiftSqlWords(line)


if __name__ == "__main__":
    usage = "usage: %prog INPUT_FILE"

    option_list = ()
    option_default = {}

    parser = optparse.OptionParser(usage=usage, option_list=option_list)
    parser.set_defaults(**option_default)
    options, args = parser.parse_args()

    if len(args) < 1:
        parser.error("must specify the input file path")
        sys.exit(-1)

    run(options, args)
    sys.exit(0)
