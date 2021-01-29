"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

class MultiApp:
 
    def __init__(self):
        self.apps = []

    # Add a new application.
    def add_app(self, title, func):
 
        self.apps.append({
            "title": title, # title of the app. Appears in the dropdown in the sidebar.
            "function": func  # render this app.
        })

    def run(self):
        app = st.sidebar.radio(
        #app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
