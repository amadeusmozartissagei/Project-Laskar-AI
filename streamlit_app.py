import sys
import os

# Add dashboard directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'dashboard'))

# Import and run the dashboard
from dashboard.dashboard import *

# This file serves as an alternative entry point for Streamlit Cloud
# You can set this as the main file path: streamlit_app.py 