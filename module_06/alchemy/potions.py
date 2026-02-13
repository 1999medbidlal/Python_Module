from .elements import create_fire, create_water, create_earth, create_air


def healing_potion():
    fire_res = create_fire()
    water_res = create_water()
    return f"Healing potion brewed with {fire_res} and {water_res}"


def strength_potion():
    earth_res = create_earth()
    fire_res = create_fire()
    return f"Strength potion brewed with {earth_res} and {fire_res}"


def invisibility_potion():
    air_res = create_air()
    water_res = create_water()
    return f"Invisibility potion brewed with {air_res} and {water_res}"


def wisdom_potion():
    fire_res = create_fire()
    water_res = create_water()
    earth_res = create_earth()
    air_res = create_air()
    return ("Wisdom potion brewed with all elements: "
            f"{fire_res} {water_res} {earth_res} {air_res}")
