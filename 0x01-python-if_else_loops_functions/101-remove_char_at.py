#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str):
        str.replace(str[n], '')
