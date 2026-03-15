from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_mode(self):
        if not self.mission_id[:1] == "M":
            raise ValueError("mission ID must start with M")
        valid = False
        for member in self.crew:
            if member.rank in [Rank.commander, Rank.captain]:
                valid = True
        if not valid:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        if self.duration_days > 365:
            total = 0
            experience = 0
            for member in self.crew:
                total += 1
                if member.years_experience >= 5:
                    experience += 1
            res = experience / total * 100
            if res < 50:
                raise ValueError("need 50'%' experienced crew (5+ years)")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("need All crew members must be active")
        return self


def crew_management(id: str,
                    name: str,
                    rank: Rank,
                    age: int,
                    speciale: str,
                    years: int,
                    active=True) -> CrewMember:

    crew_member = CrewMember(member_id=id,
                             name=name,
                             rank=rank,
                             age=age,
                             specialization=speciale,
                             years_experience=years,
                             is_active=active)
    return crew_member


def mission_management(id: str,
                       name: str,
                       destination: str,
                       launch_date: datetime,
                       duration_days: int,
                       crew_list: list[CrewMember],
                       budget_millions: float,
                       status: str = 'planned') -> None:

    try:
        mission = SpaceMission(mission_id=id,
                               mission_name=name,
                               destination=destination,
                               launch_date=launch_date,
                               duration_days=duration_days,
                               crew=crew_list,
                               mission_status=status,
                               budget_millions=budget_millions)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        len = 0
        for member in mission.crew:
            len += 1
        print(f"Crew size: {len}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")
    except ValidationError as e:
        for error in e.errors():
            print("Expected validation error:")
            print(error.get('msg')[13:])


if __name__ == "__main__":
    try:
        crew1 = crew_management("CR001", "Sarah Connor", Rank.commander, 40,
                                "Mission Command", 20, True)
        crew2 = crew_management("CR002", "John Smith", Rank.lieutenant, 35,
                                "Navigation", 25, True)
        crew3 = crew_management("CR003", "Alice Johnson", Rank.officer, 50,
                                "Engineering", 15, True)
        crew_total = [crew1, crew2, crew3]
        print("Space Mission Crew Validation")
        print('=' * 40)
        mission1 = mission_management("M2024_MARS",
                                      "Mars Colony Establishment", "Mars",
                                      "2015-03-18", 900, crew_total, 2500.0)
        print(f"\n{'=' * 40}")
        crew_total2 = [crew2, crew3]
        mission2 = mission_management("M2026_MARS",
                                      "Jupiter Colony Establishment",
                                      "Jupiter", "2015-03-18", 1500,
                                      crew_total2, 2960.0)
    except Exception as e:
        print(f"Error: {e}")
