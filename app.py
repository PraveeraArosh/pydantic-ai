import os
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from typing import List, Optional
import asyncio
from dotenv import load_dotenv
from openai import OpenAI

from nutrition_info import NutritionalInfo
from recipe_analysis import RecipeAnalysis

from recipe_analyzer import RecipeAnalyzer

load_dotenv()

def initialize_openai_client():
    """Initialize OpenAI client with API key from environment"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")
    
    return OpenAI(api_key=api_key)

openai_client = initialize_openai_client()


recipe_agent = Agent(
    model="gpt-3.5-turbo",
    result_type=RecipeAnalysis,
    system_prompt="""
    You are a professional chef and nutritionist. Analyze recipes and provide detailed, 
    accurate information about cooking difficulty, timing, nutrition, and helpful tips.

    Be realistic with your estimates and provide practical advice that home cooks can use.
    For nutritional information, provide reasonable estimates based on typical ingredient portions.
    """,
)

async def main():
    # Sample recipe for demonstration
    sample_recipe = """
    Spaghetti Carbonara
    
    Ingredients:
    - 400g spaghetti
    - 200g pancetta or guanciale, diced
    - 4 large eggs
    - 100g Pecorino Romano cheese, grated
    - Black pepper
    - Salt
    
    Instructions:
    1. Cook spaghetti in salted boiling water until al dente
    2. Meanwhile, cook pancetta in a large pan until crispy
    3. In a bowl, whisk eggs with cheese and black pepper
    4. Drain pasta, reserving some pasta water
    5. Add hot pasta to pancetta pan, remove from heat
    6. Quickly stir in egg mixture, adding pasta water as needed
    7. Serve immediately with extra cheese and pepper
    """
    
    # Initialize analyzer
    analyzer = RecipeAnalyzer()
    
    print("🔍 Analyzing recipe...")
    
    try:
        # Analyze the recipe
        analysis = await analyzer.analyze_recipe(sample_recipe)
        
        # Display formatted results
        print(analyzer.format_analysis(analysis))
        
        # You can also access individual fields programmatically
        print(f"\n🎯 Quick Check:")
        print(f"This is a {analysis.difficulty_level.lower()} recipe")
        print(f"Total time: {analysis.prep_time_minutes + analysis.cook_time_minutes} minutes")
        print(f"Calories per serving: {analysis.nutrition.calories}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def recipe_to_shopping_list(analysis: RecipeAnalysis) -> List[str]:
    """Generate a shopping list from missing ingredients"""
    return [f"□ {ingredient}" for ingredient in analysis.missing_ingredients]

def is_healthy_recipe(analysis: RecipeAnalysis) -> bool:
    """Quick health check"""
    return analysis.healthiness_score >= 7

def get_time_category(analysis: RecipeAnalysis) -> str:
    """Categorize recipe by total time"""
    total_time = analysis.prep_time_minutes + analysis.cook_time_minutes
    if total_time <= 30:
        return "Quick meal"
    elif total_time <= 60:
        return "Regular meal"
    else:
        return "Special occasion"
    
if __name__ == "__main__":
    asyncio.run(main())
