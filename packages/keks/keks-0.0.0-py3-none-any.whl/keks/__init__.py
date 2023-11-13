"""
"""
from typing import NamedTuple, Literal


class VersionInfo(NamedTuple):
    major: int = 0
    minor: int = 0
    micro: int = 0
    releaselevel: Literal['alpha', 'beta', 'candidate', 'final'] = 'final'
    serial: int = 0

    def to_string(self):
        base = f'{self.major}.{self.minor}.{self.micro}'
        level = self.releaselevel

        if level == 'final':
            return base

        if level == 'candidate':
            label = 'rc'
        else:
            label = level[0]

        return f'{base}{label}{self.serial}'


version_info = VersionInfo()


__title__ = 'keks'
__author__ = 'katzensindniedlich'
__version__ = version_info.to_string()
__license__ = 'MIT'
__copyright__ = 'Copyright 2023-present katzensindniedlich'



del NamedTuple, Literal, VersionInfo