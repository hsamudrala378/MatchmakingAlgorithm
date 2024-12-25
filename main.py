from fastapi import FastAPI, HTTPException
from Apps.models import UserProfile, CompatibilityResult
from Apps.matching.algorithm import calculate_compatibility
from typing import List

import json

app = FastAPI()

# Load mock data
with open("mock_data/users.json", "r") as f:
    users = {user["id"]: UserProfile(**user) for user in json.load(f)}

@app.get("/")
async def root():
    return {"message": "Welcome to the Dating App Matchmaking API"}

@app.post("/api/v1/match/{user_id}", response_model=List[CompatibilityResult])
async def generate_matches(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    user = users[user_id]
    matches = []
    for other_id, other_user in users.items():
        if other_id == user_id:
            continue
        if user.interested_in != other_user.gender:
            continue
        match_data = calculate_compatibility(user, other_user)
        matches.append({
            "user1_id": user_id,
            "user2_id": other_id,
            **match_data
        })
    return sorted(matches, key=lambda x: x["compatibility_score"], reverse=True)

@app.get("/api/v1/compatibility/{user_id1}/{user_id2}", response_model=CompatibilityResult)
async def check_compatibility(user_id1: str, user_id2: str):
    if user_id1 not in users or user_id2 not in users:
        raise HTTPException(status_code=404, detail="User not found")

    user1 = users[user_id1]
    user2 = users[user_id2]
    match_data = calculate_compatibility(user1, user2)
    return {"user1_id": user_id1, "user2_id": user_id2, **match_data}
