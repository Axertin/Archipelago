from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames
from ..Rules import gale_shrine_access
from ..Types import EventData, ExitData, LocData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.KUSA_VILLAGE: [ExitData('Enter Blockhead cave', RegionNames.KUSA_VILLAGE_BLOCKHEAD,
                                        has_events=['Kusa Village - Defeat Blockhead']),
                               ExitData("Enter Mr Bamboo's house", RegionNames.BAMBOO_HOUSE),
                               ExitData("Enter Kusa Village Inn", RegionNames.KUSA_INN),
                               ExitData("Enter Gale Shrine", RegionNames.GALE_SHRINE_ENTRANCE)]
}
events = {
    RegionNames.KUSA_VILLAGE: {
        "Kusa Village - Defeat Blockhead": EventData(precollected=lambda o: o.RemoveBlockHead),
        "Kusa Village - Save Rei": EventData(id=128, cherry_bomb_level=1,
                                             is_event_item=lambda o: o.CanineRewards != 0,
                                             progress_type=lambda
                                                 o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                             else LocationProgressType.DEFAULT, event_item_name="Save Rei"),
        "Kusa Village - Save Shin": EventData(id=129, required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM],
                                              is_event_item=lambda o: o.CanineRewards != 0,
                                              progress_type=lambda
                                                  o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                              else LocationProgressType.DEFAULT, event_item_name="Save Shin"),
        "Kusa Village - Save Chi": EventData(id=130, power_slash_level=1,
                                             is_event_item=lambda o: o.CanineRewards != 0,
                                             progress_type=lambda
                                                 o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                             else LocationProgressType.DEFAULT, event_item_name="Save Chi"),
        "Kusa Village - Save Ko": EventData(id=131, required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE],
                                            is_event_item=lambda o: o.CanineRewards != 0,
                                            progress_type=lambda
                                                o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                            else LocationProgressType.DEFAULT, event_item_name="Save Ko"),
        # Should we add more conditions to get this one ?
        "Kusa Village - Save Tei": EventData(id=132, mandatory_enemies=[OkamiEnemies.TEI],
                                             is_event_item=lambda o: o.CanineRewards != 0,
                                             progress_type=lambda
                                                 o: LocationProgressType.EXCLUDED if o.CanineRewards == 2
                                             else LocationProgressType.DEFAULT, event_item_name="Save Tei")
    }
}
locations = {
    RegionNames.KUSA_VILLAGE: {
        "Kusa Village - Chest on rafters after banners": LocData(967595,
                                                                 required_brush_techniques=[BrushTechniques.GALESTROM,
                                                                                            BrushTechniques.GREENSPROUT_VINE]),
        "Kusa Village - Chest on rafters before banners": LocData(967626,
                                                                  required_brush_techniques=[
                                                                      BrushTechniques.GREENSPROUT_VINE]),
        "Kusa Village - Stray Bead Chest on rafters after banners": LocData(967627,
                                                                            required_brush_techniques=[
                                                                                BrushTechniques.GALESTROM,
                                                                                BrushTechniques.GREENSPROUT_VINE]),
        "Kusa Village - Buried Chest near Fuse's house": LocData(967637, type=LocationType.BURIED_CHEST),
        "Kusa Village - Buried Chest near Gale Shrine Ledge": LocData(967642, type=LocationType.BURIED_CHEST),
        "Kusa Village - Underwater Chest near Fuse's house right": LocData(967654, type=LocationType.UNDERWATER_CHEST),
        "Kusa Village - Underwater Chest near Fuse's house left": LocData(967655, type=LocationType.UNDERWATER_CHEST)
    },
    RegionNames.KUSA_INN: {
        "Kusa Village - Daruma inside Inn": LocData(967652, type=LocationType.DARUMA)
    },
    RegionNames.KUSA_VILLAGE_BLOCKHEAD: {
        "Kusa Village - Chest inside Blockhead Cave": LocData(967594)
    },
    RegionNames.BAMBOO_HOUSE: {
        "Kusa Village - Buried Chest inside Mr Bamboo's house": LocData(967631, type=LocationType.BURIED_CHEST)
    }
}
