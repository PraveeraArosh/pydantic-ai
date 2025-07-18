Recipe Analyzer

A Streamlit-based web application that analyzes recipes, providing detailed insights on difficulty, timing, nutrition, dietary tags, and cooking tips. Powered by OpenAI and Pydantic, with a modular Python backend and containerized using Docker.

Features

Recipe Input: Enter a recipe (ingredients and instructions) via a Streamlit interface.
Analysis: Get structured output including:
Difficulty level (Easy, Medium, Hard)
Prep and cook time
Nutritional information (calories, protein, carbs, fat, fiber)
Cuisine type and dietary tags
Healthiness score (1-10)
Cooking tips and potential missing ingredients
Shopping List: Generate a list of possibly missing ingredients.
Docker Support: Run the app in a container for easy deployment.

File Structure
recipe-analyzer/
├── app.py                  # Core backend logic and RecipeAnalyzer class
├── recipe_analyzer.py      # Recipe analysis wrapper
├── recipe_analysis.py      # Pydantic model for analysis output
├── nutrition_info.py       # Pydantic model for nutritional data
├── streamlit_app.py        # Streamlit front-end
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in version control)
└── README.md               # Project documentation

Prerequisites

Python 3.10+

Docker (for containerized deployment)
OpenAI API key (set in .env)

