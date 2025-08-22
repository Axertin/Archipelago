from typing import TYPE_CHECKING

from ..Enums.RegionNames import RegionNames
from ..Types import ExitData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits={
    RegionNames.MOON_CAVE_BROKEN_STAIRS:[ExitData("Jump into the hole",RegionNames.MOON_CAVE_UNDERGROUND_ENTRANCE)],
    RegionNames.MOON_CAVE_UNDERGROUND_ENTRANCE:[ExitData("To Calcified Cavern",RegionNames.CALCIFIED_CAVERN)]
}
events={

}
locations={

}