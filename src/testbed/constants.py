"""
Constants required by this testbed.
"""

from __future__ import annotations

import enum
import pathlib
import typing

if typing.TYPE_CHECKING:
    from octoprobe.lib_tentacle import Tentacle

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent
DIRECTORY_REPO = DIRECTORY_OF_THIS_FILE.parent.parent
print(DIRECTORY_REPO / "pytest.ini")
assert (DIRECTORY_REPO / "pytest.ini").is_file()
DIRECTORY_DOWNLOADS = DIRECTORY_REPO / "downloads"
DIRECTORY_TESTRESULTS = DIRECTORY_REPO / "testresults"
DIRECTORY_GIT_CACHE = DIRECTORY_REPO / "git_cache"


class TentacleType(enum.StrEnum):
    TENTACLE_MCU = enum.auto()
    TENTACLE_DEVICE_POTPOURRY = enum.auto()
    TENTACLE_DAQ_SALEAE = enum.auto()

    def get_tentacles_for_type(
        self,
        tentacles: list[Tentacle],
        required_futs: list[EnumFut],
    ) -> list[Tentacle]:
        """
        Select all tentacles which correspond to this
        TentacleType and list[EnumFut].
        """

        def has_required_futs(t: Tentacle) -> bool:
            if t.tentacle_spec.tentacle_type == self:
                for required_fut in required_futs:
                    if required_fut in t.tentacle_spec.futs:
                        return True
            return False

        return [t for t in tentacles if has_required_futs(t)]


class EnumFut(enum.StrEnum):
    FUT_MCU_ONLY = enum.auto()
    """
    Do not provide a empty list, use FUT_MCU_ONLY instead!
    """
    FUT_I2C = enum.auto()
    FUT_UART = enum.auto()
    FUT_ONEWIRE = enum.auto()
    FUT_TIMER = enum.auto()
