<!--
SPDX-FileCopyrightText: 2021 Jeff Epler

SPDX-License-Identifier: MIT
-->


# chap-backend-replay

A proof-of-concept backend plug-in for chap.

## Installation

If you installed chap with pip, then run `pip install chap-backend-replay`.

If you installed chap with pipx, then run `pipx inject chap chap-backend-replay`.

## Use

`chap --backend replay -B session:/full/path/to/existing-chap-session.json tui`

There are additional back-end parameters, use `chap --backend replay --help` to list them.
