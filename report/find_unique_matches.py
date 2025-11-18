"""Reads files and reports unique appearances of regular expression matches for each file,
i.e. matches that do not appear in any ohter file."""

from dataclasses import dataclass
from argparse import ArgumentParser
import re



def main():
    """Returns True if there is at least one unique match."""

    parser = ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="the files in which discrepencies will be found")
    parser.add_argument("-e", "--expressions", nargs = "+", required=True, help="the regular expressions that will be used to fild items. They must correspond one-to-one with the files.")

    args = Arguments(**vars(parser.parse_args()))

    if len(args.expressions) != len(args.files):
        raise ValueError(f"Found {len(args.expressions)} regular expression(s) but {len(args.files)} file(s). There must be exactly one regular expression per file.")

    patterns = list(map(re.compile, args.expressions))
    for pattern in patterns:
        if pattern.groups != 1:
            raise ValueError("The regex must have exactly one match group.")
        
    no_unique = True


    match_sets: list[set[str]] = []
    for file, pattern in zip(args.files, patterns):
        with open(file) as f:
            match_sets.append(set(map(str, pattern.findall(f.read()))))
    for i, (file, match_set) in enumerate(zip(args.files, match_sets)):
        others = set[str].union(*match_sets[:i], *match_sets[i+1:])
        unique_sets = match_set - others
        if len(unique_sets) > 0:
            print(file)
            for unique_match in unique_sets:
                print(f"{"":>4}{unique_match}")
                no_unique = False


    return no_unique

    
                


@dataclass
class Arguments:
    files: list[str]
    expressions: list[str]


if __name__ == "__main__":

    try:
        if main():
            exit(0)
        else:
            exit(1)
    except ValueError as e:
        print(e)
        exit(1)