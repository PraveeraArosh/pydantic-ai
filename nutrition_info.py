from pydantic import BaseModel, Field

class NutritionalInfo(BaseModel):
    """Nutritional information per serving"""
    calories: int = Field(description="Estimated calories per serving")
    protein_g: float = Field(description="Protein content in grams")
    carbs_g: float = Field(description="Carbohydrate content in grams")
    fat_g: float = Field(description="Fat content in grams")
    fiber_g: float = Field(description="Fiber content in grams")