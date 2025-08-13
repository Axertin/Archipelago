from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnnemies import OkamiEnnemies
from ..Enums.RegionNames import RegionNames
from ..Rules import gale_shrine_access
from ..Types import EventData, ExitData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.SASA_SANCTUARY_ENTRANCE:[ExitData("Sasa Sanctuary Gate",RegionNames.SASA_SANCTUARY,has_events=["Taka Pass - Save Chun"])]
}
events = {
}
locations = {

}
