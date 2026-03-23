from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.OkamiEnemies import OkamiEnemies
from ..Enums.RegionNames import RegionNames
from ..Types import ExitData, LocData, EventData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.TSUTA_RUINS_1F_MAIN_PART: [
        ExitData("Tsuta Ruins - Push the glass ball", RegionNames.TSUTA_RUINS_MUSHROOMS,
                 has_events=["Tsuta Ruins - Mandatory Single Ogre Fight"]
                 ),
        ExitData("Tsuta Ruins - Left side door", RegionNames.TSUTA_RUINS_LEFT_SIDE,
                 has_events=["Tsuta Ruins - Defeat Blockhead"]),
        ExitData("Tsuta Ruins - Enter Inner Statue", RegionNames.TSUTA_RUINS_CENTRAL_STATUE,
                 has_events=["Tsuta Ruins - Destroy Poison Pots"])
    ],
    RegionNames.TSUTA_RUINS_MUSHROOMS: [
        ExitData("Tsuta Ruins - Cross flimsy bridge to left side", RegionNames.TSUTA_RUINS_LEFT_SIDE,
                 has_events=["Tsuta Ruins - Blow up weakened wall above Mushrooms"])
    ],
    RegionNames.TSUTA_RUINS_LEFT_SIDE: [
        ExitData("Tsuta Ruins - Cross the repaired Bridge", RegionNames.TSUTA_RUINS_DEVIL_GATES,
                 has_events=["Tsuta Ruins - Restore Bridge to Devil Gates' room"])
    ],
    RegionNames.TSUTA_RUINS_CENTRAL_STATUE: [
        ExitData("Tsuta Ruins - Enter the spider queen's lair", RegionNames.TSUTA_RUINS_SPIDER,
                 has_events=["Tsuta Ruins - Open the top of the statue"])
    ]
}
events = {
    RegionNames.TSUTA_RUINS_1F_MAIN_PART: {
        "Tsuta Ruins - Mandatory Single Ogre Fight": EventData(mandatory_enemies=[OkamiEnemies.BUD_OGRE])
    },
    RegionNames.TSUTA_RUINS_MUSHROOMS: {
        "Tsuta Ruins - Mandatory Double Ogre Fight": EventData(mandatory_enemies=[OkamiEnemies.BUD_OGRE]),
        "Tsuta Ruins - Grow the Mushrooms": EventData(required_brush_techniques=[BrushTechniques.SUNRISE],
                                                      required_items_events=[
                                                          "Tsuta Ruins - Mandatory Double Ogre Fight"]),
        "Tsuta Ruins - Blow up weakened wall above Mushrooms": EventData(cherry_bomb_level=1, required_items_events=[
            "Tsuta Ruins - Grow the Mushrooms"])
    },
    RegionNames.TSUTA_RUINS_LEFT_SIDE: {
        # Maybe add a check that Celestial Brush is unlocked to do this, i'm not sure this matters a lot
        "Tsuta Ruins - Defeat Blockhead": EventData(precollected=lambda o:o.RemoveBlockHead),
        "Tsuta Ruins - Open Lockjaw with Exorcising Arrow": EventData(
            required_items_events=["Tsuta Ruins - Defeat Blockhead"]),
        "Tsuta Ruins - Restore Bridge to Devil Gates' room": EventData(
            required_items_events=["Tsuta Ruins - Open Lockjaw with Exorcising Arrow"],
            required_brush_techniques=[BrushTechniques.REJUVENATION])
    },
    RegionNames.TSUTA_RUINS_DEVIL_GATES: {
        "Tsuta Ruins - Defeat Devil Gate 1": EventData(
            mandatory_enemies=[OkamiEnemies.GREEN_IMP, OkamiEnemies.DEAD_FISH]),
        "Tsuta Ruins - Defeat Devil Gate 2": EventData(
            mandatory_enemies=[OkamiEnemies.GREEN_IMP, OkamiEnemies.YELLOW_IMP]),
        "Tsuta Ruins - Defeat Devil Gate 3": EventData(
            mandatory_enemies=[OkamiEnemies.RED_IMP, OkamiEnemies.BUD_OGRE]),
        "Tsuta Ruins - Grow Mushrooms in Devil Gates Room": EventData(
            required_items_events=["Tsuta Ruins - Defeat Devil Gate 1", "Tsuta Ruins - Defeat Devil Gate 2",
                                   "Tsuta Ruins - Defeat Devil Gate 3"],
            required_brush_techniques=[BrushTechniques.SUNRISE]),
        "Tsuta Ruins - Destroy Poison Pots": EventData(
            required_items_events=["Tsuta Ruins - Grow Mushrooms in Devil Gates Room"])
    },
    RegionNames.TSUTA_RUINS_CENTRAL_STATUE: {
        "Tsuta Ruins - Bloom every cursed patch inside statue": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_BLOOM]),
        "Tsuta Ruins - Open the top of the statue": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Tsuta Ruins - Defeat the spider queen": EventData(mandatory_enemies=[OkamiEnemies.SPIDER_QUEEN])
    }
}
locations = {
    # Container IDs: 900000 + (0x104 << 8) + spawn_idx = 966560 + spawn_idx
    RegionNames.TSUTA_RUINS_1F_MAIN_PART: {
        "Tsuta Ruins - Freestanding Chest at Entrance": LocData(966577),  # spawn_idx=17, Travel Guide: Enhancing Divinity
        "Tsuta Ruins - Treasure Bud in Entrance Hall Middle": LocData(966568, type=LocationType.TREASURE_BUD),  # spawn_idx=8, Traveler's Charm
        "Tsuta Ruins - Treasure Bud in Entrance Hall Right Side": LocData(966569, type=LocationType.TREASURE_BUD),  # spawn_idx=9, Steel Soul Sake
        "Tsuta Ruins - Chest in Entrance Hall near right side door": LocData(966586),  # spawn_idx=26, Vase
        "Tsuta Ruins - Treasure Bud on 1F rightside path before ledge": LocData(966572, type=LocationType.TREASURE_BUD),  # spawn_idx=12, Steel Fist Sake
        "Tsuta Ruins - Treasure Bud near glass ball": LocData(966560, type=LocationType.TREASURE_BUD),  # spawn_idx=0, Incense Burner
        "Tsuta Ruins - Stray bead chest on 1F rightside path upper part": LocData(966575, required_brush_techniques=[
            BrushTechniques.GREENSPROUT_VINE], type=LocationType.TREASURE_BUD),  # spawn_idx=15, Stray Bead
    },
    RegionNames.TSUTA_RUINS_MUSHROOMS: {
        "Tsuta Ruins - Treasure bud behind logs in Mushrooms room": LocData(966562, power_slash_level=1,
                                                                            type=LocationType.TREASURE_BUD),  # spawn_idx=2, Vengeance Slip
    },
    RegionNames.TSUTA_RUINS_LEFT_SIDE: {
        "Tsuta Ruins - Treasure Bud behind hidden bombable wall on third plaform.": LocData(966561, cherry_bomb_level=1,
                                                                                            type=LocationType.TREASURE_BUD),  # spawn_idx=1, Stray Bead
        "Tsuta Ruins - Treasure Bud behind Lockjaw": LocData(966564, type=LocationType.TREASURE_BUD, required_items_events=[
            "Tsuta Ruins - Open Lockjaw with Exorcising Arrow"]),  # spawn_idx=4, Exorcism Slip S
        "Tsuta Ruins - Left side hidden treasure bud": LocData(966578, required_brush_techniques=[
            BrushTechniques.GREENSPROUT_VINE], type=LocationType.TREASURE_BUD),  # spawn_idx=18, Golden Peach
    },
    RegionNames.TSUTA_RUINS_DEVIL_GATES: {
        "Tsuta Ruins - Treasure Bud near Devil gates": LocData(966583, type=LocationType.TREASURE_BUD),  # spawn_idx=23, Lacquerware Set
        "Tsuta Ruins - Treasure Bud #2 near Devil gates": LocData(966584, type=LocationType.TREASURE_BUD),  # spawn_idx=24, Holy Bone S
        "Tsuta Ruins - Map Chest near poison pots": LocData(966594, required_items_events=[
            "Tsuta Ruins - Grow Mushrooms in Devil Gates Room"]),  # spawn_idx=34, Tsuta Ruins Map
        "Tsuta Ruins - Treasure Bud behind waterfall bombable wall": LocData(966585, required_items_events=[
            "Tsuta Ruins - Destroy Poison Pots"], cherry_bomb_level=1, type=LocationType.TREASURE_BUD),  # spawn_idx=25, Stray Bead
    },
    RegionNames.TSUTA_RUINS_CENTRAL_STATUE: {
        "Tsuta Ruins - Tsutagami": LocData(200019, required_items_events=[
            "Tsuta Ruins - Bloom every cursed patch inside statue"], type=LocationType.CONSTELLATION),  # Brush acquisition (Vine, bit 19)
    },
    RegionNames.TSUTA_RUINS_SPIDER: {
        "Tsuta Ruins - Left Chest before Spider queen": LocData(966581),  # spawn_idx=21, Travel Guide: Godhood Tips
        "Tsuta Ruins - Right Chest before Spider queen": LocData(966582),  # spawn_idx=22, Holy Bone S
        "Tsuta Ruins - Boss reward": LocData(966595, required_items_events=["Tsuta Ruins - Defeat the spider queen"]),  # spawn_idx=35, Bull Horn
    }
}
