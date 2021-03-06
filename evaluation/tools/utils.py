#!/usr/bin/env python

# print in colors
def print_red(skk): print("\033[91m {}\033[00m" .format(skk)) 
def print_green(skk): print("\033[92m {}\033[00m" .format(skk)) 
def print_yellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def print_lightpurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def print_purple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def print_cyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def print_lightgray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def print_black(skk): print("\033[98m {}\033[00m" .format(skk))

# Get items from a dictionary
def get_items(dict_object):
    for key in dict_object:
        yield key, dict_object[key]
