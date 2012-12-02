#!/usr/bin/env python
#
#   eliz_curse.py - A random elizebethian curse generator. Its fun try it.
#

import random

column_1 = ["artless", "bawdy", "belubbering", "bootless", "churlish",
            "cockered", "clouted", "craven", "currish", "dankish",
            "dissembling", "droning", "errant", "fawning", "fobbing",
            "froward", "frothy", "gleeking", "goatish", "gorbellied",
            "impertinent", "infectious", "jarring", "loggerheaded", 
            "lumpish", "mammering", "mangled", "mewling", "paunchy",
            "pribbling", "puking", "puny", "quailing", "rank", "reeky",
            "rougish", "ruttish", "saucy", "spleeny", "spongy", "surly",
            "tottering", "unmuzzled", "vain", "venomed", "villainous",
            "warped", "wayward", "weedy", "yeasty"]

column_2 = ["base-court", "bat-fowling", "beef-witted", "beetle-headed",
            "boil-brained", "clapper-clawed", "clay-brained", "common-kissing",
            "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted",
            "dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed",
            "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen",
            "fool-born", "full-gorged", "guts-griping", "half-faced",
            "hasty-witted", "hedge-born", "hell-hated", "idle-headed",
            "ill-breeding", "ill-nurtured", "knotty-pated", "milk-liverd",
            "motley-minded", "onion-eyed", "plume-plucked", "pottle-deep",
            "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing",
            "rump-fed", "shard-borne", "sheep-biting", "spur-galled",
            "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted",
            "unchin-snouted", "weather-bitten"]

column_3 = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig",
            "bugbear", "bum-baily", "canker-blossom", "clack-dish", "clotpole",
            "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon",
            "flax-wench", "flirt-gill", "foot-licker", "fustilarian", "giglet",
            "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast",
            "hugger-mugger", "jolthead", "lewdster", "lout", "maggot-pie",
            "malt-worm", "mammet", "measle", "minnow", "miscreant",
            "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut",
            "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet",
            "varlot", "vassal", "whey-face", "wagtail"]

print "Thou %s %s %s" % (random.choice(column_1),
                         random.choice(column_2),
                         random.choice(column_3))
