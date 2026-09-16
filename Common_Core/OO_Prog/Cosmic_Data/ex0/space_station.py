from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("======================================")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 1, 1)
        )
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    if station.is_operational is True:
        print("Status: Operational")
    else:
        print("Status: Not Operational")
    print("\n======================================")
    try:
        errorstation = SpaceStation(
            station_id="3RR0R",
            name="Invalid Space Station",
            crew_size=50,
            power_level=20.3,
            oxygen_level=1.3,
            is_operational=False,
            last_maintenance=datetime(1787, 12, 12)
            )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]['msg'])
