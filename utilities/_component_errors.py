"""_component_errors.py

Definitions for (simple) errors generated while running EPSA calculations
"""
# Nonlocal imports
from dataclasses import dataclass
from enum import Enum

class ComponentNoteLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    CRITICAL = 4


@dataclass
class ComponentNote:
    note_level: ComponentNoteLevel # Note level. Intention is to be used when generating reports. User can select the level of information to generate.
    note: str # Note