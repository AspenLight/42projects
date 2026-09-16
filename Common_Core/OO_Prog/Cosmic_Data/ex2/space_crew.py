from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum
from typing import Self


class Rank(Enum):
    Cadet = "cadet"
    Officer = "officer"
    Lieutenant = "lieutenant"
    Captain = "captain"
    Commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validator(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        if not any(member.rank in [Rank.Commander, Rank.Captain]
                   for member in self.crew):
            raise ValueError("Mission must have at least"
                             " on Commander or Captain")
        if (self.duration_days > 365 and
                (len([0 for member in self.crew if
                      member.years_experience >= 5]) / len(self.crew) < 0.5)):
            raise ValueError("Long missions (> 365 days) need 50%%"
                             " experienced crew (5+ years)")
        if any(member.is_active is False for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("======================================")
    sarah = CrewMember(
        member_id="SC-Comm1",
        name="Sarah Connor",
        rank=Rank.Commander,
        age=40,
        specialization="Mission Command",
        years_experience=10
    )
    john = CrewMember(
        member_id="JS-Lieu1",
        name="John Smith",
        rank=Rank.Lieutenant,
        age=43,
        specialization="Navigation",
        years_experience=6
    )
    alice = CrewMember(
        member_id="AJ-Offi1",
        name="Alice Johnson",
        rank=Rank.Officer,
        age=33,
        specialization="Engineering",
        years_experience=4
    )
    mission = SpaceMission(
        mission_name="Mars Colony Establishment",
        mission_id="M2024_MARS",
        destination="Mars",
        duration_days=900,
        budget_millions=2500,
        crew=[sarah, john, alice],
        launch_date=datetime(2024, 6, 13)
    )
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value})"
              f" - {member.specialization}")
    print("\n======================================")
    try:
        misserror = SpaceMission(
            mission_name="Solo Moon Mission",
            mission_id="M2306_MOON",
            destination="Moon",
            duration_days=45,
            budget_millions=5,
            crew=[alice],
            launch_date=datetime(2306, 4, 2)
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]['msg'].split(",")[1][1:])
