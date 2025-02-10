import streamlit as st
import json

# Initialize session state
if 'categories' not in st.session_state:
    st.session_state.categories = {}
if 'total_points' not in st.session_state:
    st.session_state.total_points = 0

# Function to save categories to a JSON file
def save_categories(categories):
    with open('categories.json', 'w') as f:
        json.dump(categories, f)

# Function to load categories from a JSON file
def load_categories():
    try:
        with open('categories.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Load existing categories
st.session_state.categories = load_categories()

# Set page configuration
st.set_page_config(page_title="Kid's Achievement Tracker", page_icon="🏆", layout="wide")

# Custom CSS for styling
custom_css = """
<style>
    .stApp {
        background-color: #f0f8ff; /* Light blue background */
        font-family: 'Arial', sans-serif;
        color: #333; /* Dark text color */
    }
    .stTitle {
        text-align: center;
        color: #1e90ff; /* Dodger blue */
    }
    .stHeader {
        text-align: center;
        color: #ff6347; /* Tomato */
    }
    .stButton > button {
        background-color: #32cd32; /* Lime green */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #2e8b57; /* Sea green */
    }
    .total-points {
        text-align: center;
        color: #ff6347; /* Tomato */
        font-size: 36px;
        margin-top: 20px;
    }
    .category-button {
        display: inline-block;
        margin: 10px;
    }
    .sidebar-title {
        text-align: center;
        color: #1e90ff; /* Dodger blue */
    }
    .sidebar-input {
        margin-bottom: 10px;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar for adding/editing categories
with st.sidebar:
    st.markdown("<h2 class='sidebar-title'>Manage Categories</h2>", unsafe_allow_html=True)
    category_name = st.text_input("Category Name", key="category_name_input", placeholder="Enter category name", on_change=None, args=None, kwargs=None, help=None, type="default", label_visibility="visible")
    category_points = st.number_input("Points", min_value=0, step=1, key="category_points_input", help="Enter points for the category")
    
    if st.button("Add/Edit Category"):
        if category_name:
            st.session_state.categories[category_name] = category_points
            save_categories(st.session_state.categories)
            st.success(f"Category '{category_name}' added/updated with {category_points} points.")
        else:
            st.error("Please enter a category name.")

# Main content area for tracking achievements
st.markdown("<h1 class='stTitle'>Kid's Achievement Tracker 🏆</h1>", unsafe_allow_html=True)

# Display current total points prominently
total_points_display = st.empty()  # Create an empty slot for the total points display
total_points_display.markdown(
    f"<div class='total-points'>Total Points for the Week: <strong>{st.session_state.total_points}</strong></div>",
    unsafe_allow_html=True
)

# Display categories and allow marking achievements
st.markdown("<h2 class='stHeader'>Categories</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

for i, (category, points) in enumerate(st.session_state.categories.items()):
    if i % 2 == 0:
        with col1:
            if st.button(f"Mark '{category}' Completed ({points} points)", key=f"button_{category}", use_container_width=True):
                st.session_state.total_points += points
                st.success(f"'{category}' completed! Added {points} points. Total Points: {st.session_state.total_points}")
                # Update the total points display immediately
                total_points_display.markdown(
                    f"<div class='total-points'>Total Points for the Week: <strong>{st.session_state.total_points}</strong></div>",
                    unsafe_allow_html=True
                )
    else:
        with col2:
            if st.button(f"Mark '{category}' Completed ({points} points)", key=f"button_{category}", use_container_width=True):
                st.session_state.total_points += points
                st.success(f"'{category}' completed! Added {points} points. Total Points: {st.session_state.total_points}")
                # Update the total points display immediately
                total_points_display.markdown(
                    f"<div class='total-points'>Total Points for the Week: <strong>{st.session_state.total_points}</strong></div>",
                    unsafe_allow_html=True
                )

# Button to reset total points for the week
st.markdown("<h2 class='stHeader'>Actions</h2>", unsafe_allow_html=True)
if st.button("Reset Total Points for the Week", use_container_width=True):
    st.session_state.total_points = 0
    st.success("Total points reset to 0.")
    # Update the total points display immediately
    total_points_display.markdown(
        f"<div class='total-points'>Total Points for the Week: <strong>{st.session_state.total_points}</strong></div>",
        unsafe_allow_html=True
    )