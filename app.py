import streamlit as st
import pandas as pd
from collections import Counter
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Top Skills App", page_icon="📊", layout="wide")

# Custom CSS to improve the UI
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .sidebar .sidebar-content {
        background: #ffffff
    }
    .Widget>label {
        color: #31333F;
        font-weight: bold;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #0066cc;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #0052a3;
    }
</style>
""", unsafe_allow_html=True)


# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("job_and_skills.csv")


# Process the data to get top skills for a job position
def get_top_skills(job_title, df, top_n=10):
    job_data = df[df['job_title'].str.contains(job_title, case=False, na=False)]
    all_skills = []
    for skills in job_data['job_skills'].dropna():
        all_skills.extend(skills.split(", "))
    skill_counts = Counter(all_skills)
    top_skills = skill_counts.most_common(top_n)
    return top_skills


# Create a bar chart for skills
def create_skills_chart(skills):
    skills, counts = zip(*skills)
    # Reverse the order of skills and counts to put the top skill at the top
    skills = skills[::-1]
    counts = counts[::-1]

    fig = go.Figure(go.Bar(
        x=counts,
        y=skills,
        orientation='h',
        marker_color='rgba(0, 102, 204, 0.8)',
        text=counts,
        textposition='auto',
    ))
    fig.update_layout(
        title="Top Skills Distribution",
        xaxis_title="Number of Job Postings",
        yaxis_title="Skills",
        height=500,
        margin=dict(l=0, r=0, t=30, b=0),
    )
    return fig


# Streamlit app
def main():
    st.title("📊 Top Skills Analyzer")
    st.write(
        "Discover the most in-demand skills for various job positions based on LinkedIn data. "
        "Enter a job title and select the number of top skills to display."
    )

    # Load the data
    df = load_data()

    # Create two columns for layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🔍 Search Parameters")
        # Input for job position
        job_position = st.text_input("Enter a job position:", placeholder="e.g., Data Scientist, Software Engineer")

        # Slider for selecting top N skills
        top_n = st.slider("Number of top skills to display:", min_value=5, max_value=50, value=10, step=5)

        if st.button("Analyze Skills"):
            if job_position:
                # Get top N skills
                skills = get_top_skills(job_position, df, top_n)
                if skills:
                    with col2:
                        st.subheader(f"🎯 Top {top_n} Skills for '{job_position}'")
                        # Create and display the bar chart
                        fig = create_skills_chart(skills)
                        st.plotly_chart(fig, use_container_width=True)

                        # Display skills as a formatted list
                        st.subheader("Detailed Skill List:")
                        for i, (skill, count) in enumerate(skills, 1):
                            st.write(f"{i}. **{skill}** (Mentioned in {count} job postings)")
                else:
                    st.warning("⚠️ No matching jobs found. Try a different job title.")
            else:
                st.warning("⚠️ Please enter a job position.")

    # Add some information about the data source
    st.sidebar.header("ℹ️ About")
    st.sidebar.info(
        "This app analyzes job postings data to identify the most frequently "
        "mentioned skills for specific job positions. The data is sourced from "
        "LinkedIn job listings."
    )

    # Add a footer
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0066cc;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        Developed with ❤️ by Khaidhir | Data Source: 1.3M Linkedin Jobs & Skills (2024)
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()