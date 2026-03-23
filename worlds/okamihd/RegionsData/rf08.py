from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames
from ..Types import EventData, ExitData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits={
    RegionNames.TAKA_PASS:[ExitData("Kusa Village Entrance",RegionNames.KUSA_VILLAGE),
                           ExitData("Sasa Sanctuary Entrance",RegionNames.SASA_SANCTUARY_ENTRANCE)]

}
events={
    RegionNames.TAKA_PASS:{
        "Taka Pass - Save Chun" : EventData(cherry_bomb_level=1,mandatory_enemies=[OkamiEnemies.CUTTERS])
    }
}

locations = {
    RegionNames.TAKA_PASS:{
        "Taka Pass - Chest under leaf pile near Guardian Sapling" : LocData(99, type=LocationType.BURIED_UNDER_LEAF_PILE,required_items_events=["Taka pass - Restore Bridge to Guardian Sapling"]),
        "Taka Pass - Chest on top of big rock above ledge": LocData(1885088,required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Taka Pass - Chest under leaf pile after cave": LocData(101,type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near cave west": LocData(102, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near Ultimate Origin mirror": LocData(103, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest on top of Gutters' House":LocData(1885089,required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Taka Pass - Chest across banners": LocData(1885091, required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE, BrushTechniques.GALESTROM]),
        "Taka Pass - Buried chest near Gutters' house":LocData(106,type=LocationType.BURIED_CHEST),
        "Taka Pass - Buried chest near mermaid spring": LocData(107, type=LocationType.BURIED_CHEST),
        "Taka Pass - Buried chest near tea house": LocData(108, type=LocationType.BURIED_CHEST),
        "Taka Pass - Buried chest near treasure hunter": LocData(109, type=LocationType.BURIED_CHEST),
        #Find a better name
        "Taka Pass - Buried under leaf pile near city checkpoint exit": LocData(110, type=LocationType.BURIED_UNDER_LEAF_PILE),
        #Find out which house
        "Taka Pass - Chest under leaf pile behind house": LocData(111, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near mermaid spring": LocData(112, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near city checkpoint exit #2": LocData(113, type=LocationType.BURIED_UNDER_LEAF_PILE),
        "Taka Pass - Chest under leaf pile near moles gang": LocData(114,type=LocationType.BURIED_UNDER_LEAF_PILE),
    }

}

# Shop locations (shopId=19): 300000 + 19*1000 + slot = 319000 + slot
# These are added separately and conditionally created based on RandomizeShops option
shop_locations = {
    RegionNames.TAKA_PASS: {
        "Taka Pass - Shop Slot 1": LocData(319000, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 2": LocData(319001, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 3": LocData(319002, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 4": LocData(319003, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 5": LocData(319004, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 6": LocData(319005, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 7": LocData(319006, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 8": LocData(319007, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 9": LocData(319008, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 10": LocData(319009, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 11": LocData(319010, type=LocationType.SHOP),
        "Taka Pass - Shop Slot 12": LocData(319011, type=LocationType.SHOP),
    }
}
