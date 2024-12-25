from typing import Dict
from Apps.models import UserProfile


def calculate_compatibility(user1: UserProfile, user2: UserProfile) -> Dict:
    # Calculate compatibility based on common interests, hobbies, and traits
    common_interests = list(set(user1.interests) & set(user2.interests))
    common_hobbies = list(set(user1.hobbies) & set(user2.hobbies))
    common_traits = list(set(user1.personality_traits) & set(user2.personality_traits))

    score = (
        len(common_interests) * 0.4 +
        len(common_hobbies) * 0.4 +
        len(common_traits) * 0.2
    )
    return {
        "compatibility_score": round(score, 2),
        "common_interests": common_interests,
        "common_hobbies": common_hobbies
    }
