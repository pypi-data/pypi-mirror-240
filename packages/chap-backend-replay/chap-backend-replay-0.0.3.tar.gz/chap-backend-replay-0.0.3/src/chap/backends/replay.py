# SPDX-FileCopyrightText: 2023 Jeff Epler <jepler@gmail.com>
#
# SPDX-License-Identifier: MIT

import asyncio
import os
import random
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, AsyncGenerator, Callable, Iterable, TypeVar

import click

from ..core import Backend  # pylint: disable=relative-beyond-top-level
from ..session import (  # pylint: disable=relative-beyond-top-level
    Assistant,
    Session,
    User,
    session_from_file,
)

if TYPE_CHECKING:
    F = TypeVar("F", bound=Callable[..., Any])

    def cached(f: F) -> F:
        return f

else:
    from functools import lru_cache

    def cached(f):
        return lru_cache()(f)


def ipartition(s: str, sep: str = " ") -> Iterable[tuple[str, str]]:
    rest = s
    while rest:
        first, opt_sep, rest = rest.partition(sep)
        yield (first, opt_sep)


class Replay:
    @dataclass
    class Parameters:
        session: str | None = None
        """Complete path to an existing session file"""
        delay_mu: float = 0.035
        """Average delay between tokens"""
        delay_sigma: float = 0.02
        """Standard deviation of token delay"""

    def __init__(self) -> None:
        self.parameters = self.Parameters()

    @property
    @cached
    def _session(self) -> Session:
        if self.parameters.session is None:
            raise click.BadParameter(
                "Must specify -B session:/full/path/to/existing_session.json"
            )
        session_file = os.path.expanduser(self.parameters.session)
        return session_from_file(session_file)

    @property
    @cached
    def _assistant_responses(self) -> Session:
        return [message for message in self._session if message.role == "assistant"]

    @property
    def system_message(self) -> str:
        num_assistant_responses = len(self._assistant_responses)
        return (
            f"Replay of {self.parameters.session} with {num_assistant_responses} responses. "
            f"The original session system message was:\n\n{self._session[0].content}"
        )

    @system_message.setter
    def system_message(self, value: str) -> None:
        raise AttributeError("Read-only attribute 'system_message'")

    async def aask(self, session: Session, query: str) -> AsyncGenerator[str, None]:
        data = self.ask(session, query)
        for word, opt_sep in ipartition(data):
            yield word + opt_sep
            await asyncio.sleep(
                random.gauss(self.parameters.delay_mu, self.parameters.delay_sigma)
            )

    def ask(
        self, session: Session, query: str
    ) -> str:  # pylint: disable=unused-argument
        if self._assistant_responses:
            idx = sum(1 for message in session if message.role == "assistant") % len(
                self._assistant_responses
            )

            new_content = self._assistant_responses[idx].content
        else:
            new_content = "(No assistant responses in session)"
        session.extend([User(query), Assistant(new_content)])
        return new_content


def factory() -> Backend:
    """Replay an existing session file. Useful for testing."""
    return Replay()
