from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.RegionNames import RegionNames
from ..Types import ExitData, LocData, EventData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.CURSED_SHINSHU_FIELD: [ExitData("Cursed Shinshu field - To Cursed Hana Valley", RegionNames.CURSED_HANA_VALLEY),
                                       ExitData("Shinshu field restoration",RegionNames.SHINSHU_FIELD,has_events=["Shinshu Field - Restore Guardian Sapling"])],

}
events = {
    RegionNames.CURSED_SHINSHU_FIELD: {
        "Shinshu Field - Restore Guardian Sapling": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM],precollected=lambda o:o.BloomGuardianSaplings)
    },
}
locations = {
}

# Shop locations (shopId=18): 300000 + 18*1000 + slot = 318000 + slot
# These are added separately and conditionally created based on RandomizeShops option
shop_locations = {
    RegionNames.SHINSHU_FIELD: {
        "Shinshu Field - Shop Slot 1": LocData(318000, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 2": LocData(318001, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 3": LocData(318002, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 4": LocData(318003, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 5": LocData(318004, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 6": LocData(318005, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 7": LocData(318006, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 8": LocData(318007, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 9": LocData(318008, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 10": LocData(318009, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 11": LocData(318010, type=LocationType.SHOP),
        "Shinshu Field - Shop Slot 12": LocData(318011, type=LocationType.SHOP),
    }
}
