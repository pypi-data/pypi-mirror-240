# ruff: noqa: D100, D101, D102, D103, D104, D107
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypedDict

from redux import BaseAction, InitializationActionError


class IconState(TypedDict):
    symbol: str
    color: str
    priority: int


class StatusIconsState(TypedDict):
    icons: list[IconState]


@dataclass
class IconRegistrationActionPayload:
    icon: str
    color: str = 'white'
    priority: int = 0


@dataclass
class IconRegistrationAction(BaseAction):
    payload: IconRegistrationActionPayload
    type: Literal['REGISTER_ICON'] = 'REGISTER_ICON'


IconAction = IconRegistrationAction


def reducer(state: StatusIconsState | None, action: IconAction) -> StatusIconsState:
    if state is None:
        if action.type == 'INIT':
            return {'icons': []}
        raise InitializationActionError
    if action.type == 'REGISTER_ICON':
        return {
            **state,
            'icons': sorted(
                [
                    *state['icons'],
                    IconState(
                        symbol=action.payload.icon,
                        color=action.payload.color,
                        priority=action.payload.priority,
                    ),
                ],
                key=lambda entry: entry['priority'],
            ),
        }
    return state
