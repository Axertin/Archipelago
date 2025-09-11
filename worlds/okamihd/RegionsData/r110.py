from typing import TYPE_CHECKING

from ..Enums.BrushTechniques import BrushTechniques
from ..Enums.LocationType import LocationType
from ..Enums.RegionNames import RegionNames
from ..Types import ExitData, LocData, EventData

if TYPE_CHECKING:
    from .. import OkamiWorld

exits = {
    RegionNames.MOON_CAVE_BROKEN_STAIRS: [ExitData("Jump into the hole", RegionNames.MOON_CAVE_UNDERGROUND_ENTRANCE)],
    RegionNames.MOON_CAVE_UNDERGROUND_ENTRANCE: [ExitData("To Calcified Cavern", RegionNames.CALCIFIED_CAVERN)],
    RegionNames.MOON_CAVE: [ExitData("Enter 1F Locked Cave", RegionNames.MOON_CAVE_1F_LOCKED_CAVE,
                                     has_events=["Moon Cave - Free Yokai Chef from soup"]),
                            ExitData("Moon Cave - Take lift to B2F", RegionNames.MOON_CAVE_B2F_LIFT,
                                     has_events=["Moon Cave - Main room disturb lift"])],
    RegionNames.MOON_CAVE_1F_LOCKED_CAVE: [ExitData("To 1F locked cave back", RegionNames.MOON_CAVE_1F_LOCKED_CAVE_BACK,
                                                    has_events=['Moon Cave - 1F Locked Cave open eye door']),
                                           ExitData("To 2F geyser rafters", RegionNames.MOON_CAVE_2F_GEYSER_RAFTER,
                                                    has_events=["Moon Cave - 1F Locked Cave geyser"])],
    RegionNames.MOON_CAVE_2F_GEYSER_RAFTER: [
        ExitData("To 2F main", RegionNames.MOON_CAVE_2F, has_events=["Moon cave - 2F rafter's geyser"])],
    RegionNames.MOON_CAVE_2F: [ExitData("Moon Cave - Fall Down 2F bridge", RegionNames.MOON_CAVE_B1F_LAKE)],
    RegionNames.MOON_CAVE_B1F_LAKE: [ExitData("Moon Cave - Climb to under lift", RegionNames.MOON_CAVE_B1F_UNDER_LIFT,
                                              has_events=["Moon Cave - B1F Lake geyser"])],
    RegionNames.MOON_CAVE_B1F_UNDER_LIFT: [ExitData("Moon Cave - Climb to main room", RegionNames.MOON_CAVE,
                                                    has_events=["Moon Cave - B1F under lift geyser"])],

    RegionNames.MOON_CAVE_B2F_LIFT: [ExitData("Moon Cave - Enter Frozen Statue room",RegionNames.MOON_CAVE_B2F_FROZEN_STATUE,has_events=["Moon Cave - B2F oepn eyes door"])],
    RegionNames.MOON_CAVE_B2F_FROZEN_STATUE:[ExitData("Moon Cave - To B2F lift back", RegionNames.MOON_CAVE_B2F_OTHER_LIFT, has_events=["Moon Cave - B2F melt Ice block to other lift"])],
    RegionNames.MOON_CAVE_B2F_OTHER_LIFT:[ExitData("Moon Cave - to B2F room beihnd bombable wall",RegionNames.MOON_CAVE_B2F_BOMBABLE, has_events=["Moon Cave - B2F Explode wall behind lift"]),
                                          ExitData("Moon Cave - Take lift back to kitchen",RegionNames.MOON_CAVE_KITCHEN_BACK)]

}
events = {
    RegionNames.MOON_CAVE: {
        "Moon Cave - Free Yokai Chef from soup": EventData(
            required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Moon Cave - Main room geyser": EventData(required_brush_techniques=[BrushTechniques.WATERSPROUT],
                                                  required_items_events=["Moon Cave - Get Ogre Liver"]),
        "Moon Cave - Main room disturb lift": EventData(power_slash_level=1,
                                                        required_items_events=["Moon Cave - B1F Open lift hatch"])
    },
    RegionNames.MOON_CAVE_1F_LOCKED_CAVE: {
        "Moon Cave - Cross 1F Locked Cave": EventData(required_brush_techniques=[BrushTechniques.GREENSPROUT_VINE]),
        "Moon Cave - 1F Locked Cave Blow up wall": EventData(cherry_bomb_level=1),
        "Moon Cave - 1F Locked Cave open eye door": EventData(power_slash_level=1, required_items_events=[
            "Moon Cave - Cross 1F Locked Cave"]),
        # Does this require Ogre Liver ?
        "Moon Cave - 1F Locked Cave geyser": EventData(required_brush_techniques=[BrushTechniques.WATERSPROUT]),
    },
    RegionNames.MOON_CAVE_1F_LOCKED_CAVE_BACK: {
        "Moon Cave - Mandatory Ogre Encounter": EventData(mandatory_enemies=[]),
        "Moon Cave - Get Ogre Liver": EventData(event_item_name="Ogre Liver")
    },
    RegionNames.MOON_CAVE_2F_GEYSER_RAFTER: {
        "Moon cave - 2F rafter's geyser": EventData(required_brush_techniques=[BrushTechniques.WATERSPROUT])
    },
    RegionNames.MOON_CAVE_B1F_LAKE: {
        # FIXME: Fill ennemies
        "Moon Cave - B1F Lake cursed Torii": EventData(mandatory_enemies=[]),
        "Moon Cave - B1F Lake open valve": EventData(required_brush_techniques=[BrushTechniques.WATERSPROUT]),
        "Moon Cave - B1F Lake geyser": EventData(required_brush_techniques=[BrushTechniques.WATERSPROUT],
                                                 required_items_events=["Moon Cave - B1F Lake open valve"]),
    },
    RegionNames.MOON_CAVE_B1F_UNDER_LIFT: {
        "Moon Cave - B1F Open lift hatch": EventData(power_slash_level=1),
        "Moon Cave - B1F under lift geyser": EventData(required_brush_techniques=[BrushTechniques.WATERSPROUT])
    },
    RegionNames.MOON_CAVE_B2F_LIFT:{
        "Moon Cave - B2F oepn eyes door":EventData(power_slash_level=1)
    },
    RegionNames.MOON_CAVE_B2F_FROZEN_STATUE:{
        "Moon Cave - B2F Defeat Ice Lips": EventData(mandatory_enemies=[]),
        "Moon Cave - B2F Melt Ice block to other lift": EventData(required_brush_techniques=[BrushTechniques.INFERNO])
    },
    RegionNames.MOON_CAVE_B2F_OTHER_LIFT:{
        "Moon Cave - B2F Melt Ice Block behind lift" : EventData(required_brush_techniques=[BrushTechniques.INFERNO]),
        "Moon Cave - B2F Explode wall behind lift" : EventData(cherry_bomb_level=1,required_items_events=["Moon Cave - B2F Melt Ice Block behind lift"])
    },
    RegionNames.MOON_CAVE_KITCHEN_BACK:{
        "Moon Cave - 1F Cursed Door in kitchen back": EventData(mandatory_enemies=[]),
        "Moon Cave - Get Ice Lips":EventData(required_items_events=["Moon Cave - 1F Cursed Door in kitchen back"]),
        #TODO: Can be done from the other way too;
        "Moon Cave - Melt Ice in the kitchen": EventData(required_brush_techniques=[BrushTechniques.INFERNO])
    }

}
locations = {
    RegionNames.MOON_CAVE: {
        "Moon Cave - 1F Chest on ledge in the kitchen": LocData(175)
    },
    RegionNames.MOON_CAVE_1F_LOCKED_CAVE: {
        "Moon Cave - 1F locked cave Treasure bud behind bombable wall": LocData(176, type=LocationType.TREASURE_BUD)
    },
    RegionNames.MOON_CAVE_B2F_LIFT:{
        "Moon Cave - B2F Chest on ledge near eyes door" : LocData(178)
    },
    RegionNames.MOON_CAVE_B2F_FROZEN_STATUE:{
        "Moon Cave - Moegami":LocData(177, type=LocationType.CONSTELLATION)
    },
    RegionNames.MOON_CAVE_B2F_BOMBABLE:{
        "Moon Cave - B2F Chest behind bombable wall":LocData(178)
    }
}
