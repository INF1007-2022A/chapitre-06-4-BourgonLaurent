#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary: dict[int, str]) -> set[int]:
    return {k for k in dictionary.keys() if k % 2 == 0}


def join_dictionaries(dictionaries: list[dict[int, str]]) -> dict[int, str]:
    return {k: v for d in dictionaries for k, v in d.items()}


def dictionary_from_lists(keys: list[str], values: list[str]) -> dict[str, str]:
    return dict(zip(keys, values))


def get_greatest_values(dictionnary: dict[str, int], num_values: int):
    rev_sorted_values = sorted(dictionnary.values(), reverse=True)
    return rev_sorted_values[:num_values]


def get_sum_values_from_key(dictionnaries, key):
    return 0


if __name__ == "__main__":
    yeet = {
        69: "Yeet",
        420: "YeEt",
        9000: "YEET",
    }
    print(get_even_keys(yeet))
    print()

    yeet = {
        69: "Yeet",
        420: "YeEt",
        9000: "YEET",
    }
    doot = {0xBEEF: "doot", 0xDEAD: "DOOT", 0xBABE: "dOoT"}
    print(join_dictionaries([yeet, doot]))
    print()

    doh = ["D'OH!", "d'oh", "DOH!"]
    nice = ["NICE!", "nice", "nIcE", "NAIIIIICE!"]
    print(dictionary_from_lists(doh, nice))
    print()

    nums = {"nice": 69, "nice bro": 69420, "AGH!": 9000, "dude": 420, "git gud": 1337}
    print(get_greatest_values(nums, 1))
    print(get_greatest_values(nums, 3))
    print()

    bro1 = {"money": 12, "problems": 14, "trivago": 1}
    bro2 = {"money": 56, "problems": 406}
    bro3 = {"money": 1, "chichis": 1, "power-level": 9000}
    print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
    print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
    print()
