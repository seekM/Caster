from dragonfly import Function, Choice

from castervoice.lib import control, alphanumeric
from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R


class Alphabet(MergeRule):
    pronunciation = CCRMerger.CORE[0]

    mapping = {
        "[<big>] <letter>":
            R(Function(alphanumeric.letters2, extra={"big", "letter"}),
              rdescript="Core: Spell"),
    }
    extras = [
        #alphanumeric.get_alphabet_choice("letter"),
        Choice("letter", {
            "arch"    : "a",
            "brov"    : "b",
            "char"    : "c",
            "delta"   : "d",
            "echo"    : "e",
            "foxy"    : "f",
            "goof"    : "g",
            "hotel"   : "h",
            "India"   : "i",
            "julia"   : "j",
            "kilo"    : "k",
            "Lima"    : "l",
            "Mike"    : "m",
            "Novakeen": "n",
            "oscar"   : "o",
            "prime"   : "p",
            "Quebec"  : "q",
            "Romeo"   : "r",
            "Sierra"  : "s",
            "tango"   : "t",
            "uniform" : "u",
            "victor"  : "v",
            "whiskey" : "w",
            "x-ray"   : "x",
            "yankee"  : "y",
            "Zulu"    : "z",
        }),
        Choice("big", {
            "big": True,
        }),
    ]
    defaults = {
        "big": False,
    }


control.nexus().merger.add_global_rule(Alphabet())
