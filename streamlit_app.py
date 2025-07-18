import streamlit as st
import asyncio
from app import RecipeAnalyzer, recipe_to_shopping_list, is_healthy_recipe, get_time_category
from recipe_analysis import RecipeAnalysis

# Streamlit app configuration
st.set_page_config(page_title="Recipe Analyzer", page_icon="🍳", layout="wide")

# Title and description
st.title("🍽️ Recipe Analyzer")
st.markdown("Enter your recipe below to get a detailed analysis including difficulty, timing, nutrition, and cooking tips.")

# User input for recipe
recipe_text = st.text_area("Enter Your Recipe", height=300, placeholder="Paste or type your recipe here (include ingredients and instructions)...")

# Analyze button
if st.button("Analyze Recipe"):
    if not recipe_text.strip():
        st.error("Please enter a recipe to analyze.")
    else:
        with st.spinner("🔍 Analyzing recipe..."):
            try:
                # Initialize analyzer
                analyzer = RecipeAnalyzer()

                # Run analysis
                analysis = asyncio.run(analyzer.analyze_recipe(recipe_text))

                # Display formatted results
                st.subheader("Recipe Analysis")
                st.markdown(analyzer.format_analysis(analysis))

                # Additional insights
                st.subheader("Quick Insights")
                st.write(f"- **Difficulty**: This is a {analysis.difficulty_level.lower()} recipe")
                st.write(f"- **Total Time**: {analysis.prep_time_minutes + analysis.cook_time_minutes} minutes")
                st.write(f"- **Calories per Serving**: {analysis.nutrition.calories}")
                st.write(f"- **Meal Category**: {get_time_category(analysis)}")
                st.write(f"- **Healthy?**: {'Yes' if is_healthy_recipe(analysis) else 'No'} (Health Score: {analysis.healthiness_score}/10)")

                # Shopping list
                if analysis.missing_ingredients:
                    st.subheader("Shopping List (Possible Missing Ingredients)")
                    for item in recipe_to_shopping_list(analysis):
                        st.write(item)
                else:
                    st.write("No missing ingredients detected.")

            except Exception as e:
                st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")