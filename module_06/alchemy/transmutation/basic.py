from alchemy.elements import create_fire, create_earth


def lead_to_gold():
    fire_res = create_fire()
    return f"Lead transmuted to gold using {fire_res}"


def stone_to_gem():
    earth_res = create_earth()
    return f"Stone transmuted to gem using {earth_res}"
