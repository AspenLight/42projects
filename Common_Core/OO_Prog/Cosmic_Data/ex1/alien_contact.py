from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum
from typing import Self


class ContactType(Enum):
    Radio = "radio"
    Visual = "visual"
    Physical = "physical"
    Telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_recieved: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validator(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if (self.contact_type == ContactType.Physical and
                self.is_verified is False):
            raise TypeError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.Telepathic and
                self.witness_count < 3):
            raise ValueError("Telepathic contact requires"
                             " at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_recieved:
            raise TypeError("Strong signals (>7.0) should"
                            " include recieved messages")
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 1, 5),
        contact_type=ContactType.Radio,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_recieved="Greetings from Zeta Reticuli"
    )
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_recieved}'")
    print("\n======================================")
    try:
        telerror = AlienContact(
            contact_id="AC_1987_023",
            timestamp=datetime(1987, 7, 14),
            contact_type=ContactType.Telepathic,
            location="Paris, France",
            signal_strength=4.3,
            duration_minutes=2,
            witness_count=1,
            message_recieved="Beep Boop",
            is_verified=True
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]['msg'].split(",")[1][1:])
