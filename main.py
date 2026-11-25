#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters -- entry program.

Writes one Wi-Fi network name, 32 characters or fewer, to
/output/entry.txt. The name is a joke that implies a whole story in
the few words a passer-by sees in a phone's network list.

How it picks: a shortlist of hand-written candidates, each scored
0-2 on the judge's own rubric, most important first -- the joke
lands on the first read, it implies a whole story (a situation, a
character, something that happened), it is fresh (no stock Wi-Fi
joke), it is tight (every character earns its place). Highest total
wins; ties break toward the shorter name, then the earlier candidate,
so the choice is deterministic. The winner is then checked against
the gate (1-32 characters, not only white space) before it is
written, with no trailing newline, so the file holds exactly the
name and nothing else.

The winner: a proposal answered not with words but with a changed
Wi-Fi password. Two people, one question, one quiet revenge -- the
whole break-up is in the password box.
"""

import os

# (name, joke, story, freshness, tightness) -- scores are my own
# judgement against the judge's rubric, 0-2 each.
CANDIDATES = [
    # Proposal, rejection, revenge -- all in the password box.
    ("He Proposed, I Changed Password", 2, 2, 2, 2),
    # Dark parallel: the router and the marriage died together.
    ("Router Died, So Did the Marriage", 2, 2, 1, 2),
    # A mum, a router, and a haunting nobody else can see.
    ("Mom Thinks the Router Is Haunted", 1, 2, 2, 1),
    # Childhood punishment, told by the kid who lived it.
    ("Dad Unplugged It, Grounding Me", 1, 2, 2, 2),
    # An ongoing password war with an ex, still going.
    ("Ex Changed the Password, Again", 1, 1, 1, 2),
]


def score(candidate):
    _name, joke, story, freshness, tightness = candidate
    return joke + story + freshness + tightness


def pick(candidates):
    best = None
    best_key = None
    for index, candidate in enumerate(candidates):
        name = candidate[0].strip()
        if not (1 <= len(name) <= 32) or not name.strip():
            raise SystemExit(f"candidate fails the gate: {name!r}")
        # Higher score wins; shorter name wins ties; earlier wins the rest.
        key = (score(candidate), -len(name), -index)
        if best_key is None or key > best_key:
            best, best_key = name, key
    return best


def main() -> None:
    text = pick(CANDIDATES)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt: {text!r}")


if __name__ == "__main__":
    main()
