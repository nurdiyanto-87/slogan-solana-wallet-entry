#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent entry.

Writes one original one-line slogan for a Solana wallet agent to
/output/entry.txt. Pure Python standard library only.

Slogan (v2, revised from v1):
    Solana in your pocket: a wallet agent that turns 'I wish' into 'done'
    before your coffee cools.

Revision reasoning: v1's "with a wallet agent" softened the opening and
cost a word. The colon turns the first clause into a setup and the second
into the payoff — "Solana in your pocket" (the promise) : "a wallet agent
that turns 'I wish' into 'done'" (the mechanism). One word shorter, same
fresh pocket-and-coffee image, sharper beat on the 'I wish' / 'done'
contrast.

Why this line: it names the wallet agent outright (criterion 1), swaps the
stock crypto imagery (keys, moons, bags) for a fresh, everyday image — a
wallet in your pocket and coffee still cooling (criterion 2) — and the
promise is plain on one read: say what you want, the agent does it, fast
(criterion 3). The 'I wish' / 'done' contrast gives it a repeatable rhythm
(criterion 4), and it promises nothing a wallet agent cannot do: it acts
on your instructions on Solana, nothing more (criterion 5).
"""

import os

SLOGAN = "Solana in your pocket: a wallet agent that turns 'I wish' into 'done' before your coffee cools."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SLOGAN)


if __name__ == "__main__":
    main()
