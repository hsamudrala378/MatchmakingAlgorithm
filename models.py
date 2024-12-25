from pydantic import BaseModel
from typing import List, Optional

class UserProfile(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    interested_in: str
    location: str
    hobbies: List[str]
    interests: List[str]
    occupation: str
    education_level: str
    personality_traits: List[str]

class CompatibilityResult(BaseModel):
    user1_id: str
    user2_id: str
    compatibility_score: float
    common_interests: Optional[List[str]] = None
    common_hobbies: Optional[List[str]] = None
