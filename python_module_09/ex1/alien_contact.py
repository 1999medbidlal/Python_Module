from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def model_checks(self):
        if not self.contact_id[:2] == ("AC"):
            raise ValueError("Contact ID must start with AC")
        if self.contact_type is ContactType.physical:
            if not self.is_verified:
                raise ValueError(
                    "physical contact requires reports must be verified")
        if self.contact_type is ContactType.telepathic:
            if not self.witness_count >= 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError("should include received messages")
        return self


def main(id: str,
         time: datetime,
         location: str,
         contact_type: ContactType,
         signal: float,
         duration: int,
         witness: int,
         message: Optional[str] = None,
         verified: bool = False) -> None:
    try:
        contact = AlienContact(contact_id=id,
                               timestamp=time,
                               location=location,
                               contact_type=contact_type,
                               signal_strength=signal,
                               duration_minutes=duration,
                               witness_count=witness,
                               message_received=message,
                               is_verified=verified)
        print("Valid Contact created:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.name}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error.get('msg')[13:])


if __name__ == "__main__":
    try:
        print("Alien Contact Log Validation")
        print('=' * 40)
        main("AC_2024_001",
             "2026-08-12",
             " Area 51, Nevada",
             ContactType.radio,
             8.5,
             45,
             5,
             message='Greetings from Zeta Reticuli',
             verified=True)
        print(f"\n{'=' * 40}")
        main("AC_2024_001",
             "2026-08-12",
             " Area 51, Nevada",
             ContactType.telepathic,
             8.5,
             45,
             2,
             message='Greetings from Zeta Reticuli',
             verified=True)
    except Exception as e:
        print(f"Error: {e}")
