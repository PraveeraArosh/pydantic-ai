from pydantic import BaseModel, Field
from typing import List, Optional

from nutrition_info import NutritionalInfo

class RecipeAnalysis(BaseModel):
    """Complete recipe analysis with structured data"""
    difficulty_level: str = Field(description="Easy, Medium, or Hard")
    prep_time_minutes: int = Field(description="Preparation time in minutes")
    cook_time_minutes: int = Field(description="Cooking time in minutes")
    servings: int = Field(description="Number of servings")
    cuisine_type: str = Field(description="Type of cuisine (e.g., Italian, Asian, etc.)")
    dietary_tags: List[str] = Field(description="Diet tags like vegetarian, gluten-free, etc.")
    nutrition: NutritionalInfo = Field(description="Nutritional information")
    missing_ingredients: List[str] = Field(description="Common ingredients that might be missing")
    cooking_tips: List[str] = Field(description="Helpful cooking tips for this recipe")
    healthiness_score: int = Field(description="Health score from 1-10 (10 being healthiest)")