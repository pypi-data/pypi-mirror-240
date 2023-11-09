# SPDX-FileCopyrightText: 2023 Jeff Epler <jepler@gmail.com>
#
# SPDX-License-Identifier: MIT

import asyncio
import functools
import os
import random
from dataclasses import dataclass

import click

from ..session import (  # pylint: disable=relative-beyond-top-level
    Assistant,
    Session,
    User,
)


def ipartition(s, sep=" "):
    rest = s
    while rest:
        first, opt_sep, rest = rest.partition(sep)
        yield (first, opt_sep)


class Replay:
    @dataclass
    class Parameters:
        session: str = None
        """Complete path to an existing session file"""
        delay_mu: float = 0.035
        """Average delay between tokens"""
        delay_sigma: float = 0.02
        """Standard deviation of token delay"""

    def __init__(self):
        self.parameters = self.Parameters()

    @property
    @functools.lru_cache()
    def _session(self):
        if self.parameters.session is None:
            raise click.BadParameter(
                "Must specify -B session:/full/path/to/existing_session.json"
            )
        session_file = os.path.expanduser(self.parameters.session)
        with open(session_file, "r", encoding="utf-8") as f:
            return Session.from_json(f.read())

    @property
    @functools.lru_cache()
    def _assistant_responses(self):
        return [
            message for message in self._session.session if message.role == "assistant"
        ]

    @property
    def system_message(self):
        num_assistant_responses = len(self._assistant_responses)
        return (
            f"Replay of {self.parameters.session} with {num_assistant_responses} responses. "
            f"The original session system message was:\n\n{self._session.session[0].content}"
        )

    async def aask(self, session, query):
        data = self.ask(session, query)
        for word, opt_sep in ipartition(data):
            yield word + opt_sep
            await asyncio.sleep(
                random.gauss(self.parameters.delay_mu, self.parameters.delay_sigma)
            )

    def ask(
        self, session, query, *, max_query_size=5, timeout=60
    ):  # pylint: disable=unused-argument
        if self._assistant_responses:
            idx = sum(
                1 for message in session.session if message.role == "assistant"
            ) % len(self._assistant_responses)

            new_content = self._assistant_responses[idx].content
        else:
            new_content = "(No assistant responses in session)"
        session.session.extend([User(query), Assistant(new_content)])
        return new_content


def factory():
    """Replay an existing session file. Useful for testing."""
    return Replay()
