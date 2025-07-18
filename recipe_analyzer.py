from pydantic_ai import Agent
from recipe_analysis import RecipeAnalysis
from app import initialize_openai_client

class RecipeAnalyzer:
    """Main class for analyzing recipes using Pydantic AI"""
    
    def __init__(self):
        self.agent = Agent(
            model="gpt-3.5-turbo",
            result_type=RecipeAnalysis,
            system_prompt="""
            You are a professional chef and nutritionist. Analyze recipes and provide detailed, 
            accurate information about cooking difficulty, timing, nutrition, and helpful tips.

            Be realistic with your estimates and provide practical advice that home cooks can use.
            For nutritional information, provide reasonable estimates based on typical ingredient portions.
            """,
            client=initialize_openai_client()
        )
    
    async def analyze_recipe(self, recipe_text: str) -> RecipeAnalysis:
        """
        Analyze a recipe and return structured data
        
        Args:
            recipe_text: The recipe text to analyze
            
        Returns:
            RecipeAnalysis: Structured analysis of the recipe
        """
        try:
            result = await self.agent.run(f"Analyze this recipe: {recipe_text}")
            return result.data
        except Exception as e:
            raise Exception(f"Error analyzing recipe: {str(e)}")
    
    def format_analysis(self, analysis: RecipeAnalysis) -> str:
        """Format the analysis for display"""
        return f"""
🍳 RECIPE ANALYSIS
==================

📊 Basic Info:
• Difficulty: {analysis.difficulty_level}
• Prep Time: {analysis.prep_time_minutes} minutes
• Cook Time: {analysis.cook_time_minutes} minutes
• Servings: {analysis.servings}
• Cuisine: {analysis.cuisine_type}
• Health Score: {analysis.healthiness_score}/10

🏷️ Dietary Tags: {', '.join(analysis.dietary_tags)}

📈 Nutrition (per serving):
• Calories: {analysis.nutrition.calories}
• Protein: {analysis.nutrition.protein_g}g
• Carbs: {analysis.nutrition.carbs_g}g
• Fat: {analysis.nutrition.fat_g}g
• Fiber: {analysis.nutrition.fiber_g}g

❓ Might be missing: {', '.join(analysis.missing_ingredients)}

💡 Cooking Tips:
{chr(10).join(f'• {tip}' for tip in analysis.cooking_tips)}
"""