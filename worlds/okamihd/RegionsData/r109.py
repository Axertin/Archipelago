from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames
from ..Rules import gale_shrine_access
from ..Types import EventData, ExitData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.SASA_SANCTUARY_ENTRANCE: [
        ExitData("Sasa Sanctuary Gate", RegionNames.SASA_SANCTUARY, has_events=["Taka Pass - Save Chun"])],
    RegionNames.SASA_SANCTUARY: [ExitData("To Bamboo Grove", RegionNames.SASA_SANCTUARY_BAMBOO,
                                          has_events=["Sasa Sanctuary - Open Bamboo grove Door"])]
}
events = {
    RegionNames.SASA_SANCTUARY: {
        "Sasa Sanctuary - Dig with Mr. Bamboo.": EventData(type=LocationType.DIGGING_MINIGAME_EARLY),
        "Sasa Sanctuary - Open Bamboo grove Door": EventData(required_brush_techniques=[BrushTechniques.WATERSPROUT])
    },
    RegionNames.SASA_SANCTUARY_BAMBOO: {
        "Sasa Sanctuary - Save Take": EventData(power_slash_level=1),
        "Sasa Sanctuary - Get Orb from Take": EventData(id=144, mandatory_enemies=[OkamiEnemies.TAKE],
                                                        is_event_item=lambda o: o.CanineRewards != 0,
                                                        progress_type=lambda
                                                            o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                                        else LocationProgressType.DEFAULT,
                                                        event_item_name="Duty Orb",
                                                        required_items_events=["Sasa Sanctuary - Save Take"])
    }
}
locations = {
    RegionNames.SASA_SANCTUARY_ENTRANCE: {
        "Sasa Sanctuary - Buried Chest near Entrance": LocData(967880, type=LocationType.BURIED_CHEST)
    },
    RegionNames.SASA_SANCTUARY: {
        "Sasa Sanctuary - 4th West side chest near Papa Jamba": LocData(967840, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 2nd West side chest near Papa Jamba": LocData(967841, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 5th East side chest near Papa Jamba": LocData(967842, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 3rd East side chest near Papa Jamba": LocData(967843, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 1st East side chest near Papa Jamba": LocData(967844, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 4th East side chest near Papa Jamba": LocData(967860, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 2nd East side chest near Papa Jamba": LocData(967861, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 5th West side chest near Papa Jamba": LocData(967862, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 3rd West side chest near Papa Jamba": LocData(967863, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - 1st West side chest near Papa Jamba": LocData(967864, type=LocationType.NORMAL_CHEST),
        "Sasa Sanctuary - Buried Chest near hot springs": LocData(967881, type=LocationType.BURIED_CHEST),
        "Sasa Sanctuary - Nuregami": LocData(200013, type=LocationType.CONSTELLATION),  # bit 13
        "Sasa Sanctuary - Daruma Doll": LocData(967883, type=LocationType.DARUMA)
    },
    RegionNames.SASA_SANCTUARY_BAMBOO: {
        "Sasa Sanctuary - Buried Chest in bamboo grove stairs": LocData(967882, type=LocationType.BURIED_CHEST),
        "Sasa Sanctuary - Left side Buried Chest in bamboo grove back": LocData(967886, type=LocationType.BURIED_CHEST),
        "Sasa Sanctuary - Right side Buried Chest in bamboo grove back": LocData(967885, type=LocationType.BURIED_CHEST),
    }
}
