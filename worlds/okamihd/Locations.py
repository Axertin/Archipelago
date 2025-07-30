from BaseClasses import Region, Location, ItemClassification
from .Rules import apply_event_or_location_rules
from .Types import LocData, OkamiLocation, OkamiItem, resolve_option_callable, EventData
from typing import Dict, TYPE_CHECKING
from .RegionsData import r100, r122, r101, r102, r103, r104, rf01, rf02, rf03, rf04,rf07,rf08,r108

if TYPE_CHECKING:
    from . import OkamiWorld


def get_location_names():
    #FIXME: Inaccurate count due to events that can get transformed in locations.
    location_names = {}
    for region_key, region_locations in okami_locations.items():
        for location_name, location_data in region_locations.items():
            location_names[location_name] = location_data.id

    return location_names


def create_region_locations(reg: Region, world: "OkamiWorld"):
    if reg.name in okami_locations:
        for (location_name, location_data) in okami_locations[reg.name].items():
            # if location_data.praise_sanity  <= world.options.PraiseSanity:
            create_location(location_name,location_data,reg,world)

def create_location(location_name:str,location_data:EventData | LocData,reg:Region, world:"OkamiWorld"):
    location = OkamiLocation(world.player, location_name, location_data.id, reg)
    # Set location
    progress_type = resolve_option_callable(location_data.progress_type, world)
    location.progress_type = progress_type
    apply_event_or_location_rules(location, location_name, location_data, world)
    reg.locations.append(location)


def create_region_events(reg: Region, world: "OkamiWorld"):
    if reg.name in okami_events:
        for (event_name, event_data) in okami_events[reg.name].items():

            precollected_item_event_state=resolve_option_callable(event_data.precollected,world)

            is_event_item_state = resolve_option_callable(event_data.is_event_item, world)

            if not precollected_item_event_state and not is_event_item_state:
                # It's a true event, we need to create it as such.
                if event_data.override_event_item_name:
                    event_location = create_event(event_name, event_data.override_event_item_name,event_data.override_item_id, reg, event_data,
                                                  world)
                else:
                    event_location = create_event(event_name, event_name, event_data.override_item_id, reg, event_data, world)
                event_location.show_in_spoiler = False
            elif is_event_item_state:
                create_location(event_name, event_data, reg, world)


def create_event(location_name: str, item_name: str, code:int|None, region: Region, data: LocData, world: "OkamiWorld") -> Location:
    event = OkamiLocation(world.player, location_name, None, region)
    apply_event_or_location_rules(event, location_name, data, world)
    region.locations.append(event)
    #FIXME: Add an option to give an id to the placed item
    event.place_locked_item(OkamiItem(item_name, ItemClassification.progression, code, world.player))
    return event


def get_total_locations(world: "OkamiWorld") -> int:
    return len(get_location_names().keys())


def is_location_valid(world: "OkamiWorld", location: str) -> bool:
    # used to mark locations as invalid when they're not in the seed bc of settings
    # data = location_table.get(location) or event_locs.get(location)

    return True


okami_locations = {
    **r100.locations,
    **r122.locations,
    **r101.locations,
    **r102.locations,
    **r103.locations,
    **r104.locations,
    **rf01.locations,
    **rf02.locations,
    **rf03.locations,
    **rf04.locations,
    **rf07.locations,
    **rf08.locations,
    **r108.locations
}

okami_events = {
    **r100.events,
    **r122.events,
    **r101.events,
    **r102.events,
    **r103.events,
    **r104.events,
    **rf01.events,
    **rf02.events,
    **rf03.events,
    **rf04.events,
    **rf07.events,
    **rf08.events,
    **r108.events
}
