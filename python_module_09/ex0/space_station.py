from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main(id: str,
         name: str,
         size: int,
         power: float,
         oxygen: float,
         last: datetime,
         is_oper: bool = True,
         note: Optional[str] = None) -> None:
    try:
        model = SpaceStation(station_id=id,
                             name=name,
                             crew_size=size,
                             power_level=power,
                             oxygen_level=oxygen,
                             last_maintenance=last,
                             is_operational=is_oper,
                             notes=note)
        print("Valid station created:")
        print(f"ID: {model.station_id}")
        print(f"Name: {model.name}")
        print(f"Crew: {model.crew_size} people")
        print(f"Power: {model.power_level}%")
        print(f"Oxygen: {model.oxygen_level}%")
        if model.is_operational:
            print("Status: Operational")
        else:
            print("Status: not Operational")

    except ValidationError as error:
        print("Expected validation error:")
        for e in error.errors():
            print(e.get('msg'))


if __name__ == "__main__":
    try:
        print("Space Station Data Validation")
        print("=" * 40)
        main("ISS001",
             "International Space Station",
             6,
             85.5,
             92.3,
             "2026-03-08",
             is_oper=True,
             note="Maintenance")
        print(f"\n{'=' * 40}")
        main(
            "ISS001",
            "Space_Station",
            25,
            86.5,
            92.3,
            "2026-03-08",
        )
    except Exception as e:
        print(f"Error: {e}")
