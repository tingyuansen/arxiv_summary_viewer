import streamlit as st
import pandas as pd
from pathlib import Path

# Read the CSV file
@st.cache_data
def load_data():
    csv_path = Path(__file__).parent / "arxiv_summaries.csv"
    return pd.read_csv(csv_path)

def main():
    st.set_page_config(
        page_title="ArXiv Summary Viewer",
        page_icon="📚",
        layout="wide"
    )

    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main {
            padding: 0rem 1rem;
        }
        .stExpander {
            background-color: #f0f2f6;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        .paper-title {
            color: #1f77b4;
            font-size: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar for paper selection
    with st.sidebar:
        st.title("📚 Paper Selection")
        df = load_data()
        selected_paper = st.selectbox(
            "Choose a paper",
            options=df['arxiv_id'].tolist(),
            format_func=lambda x: f"{x}: {df[df['arxiv_id'] == x]['title'].iloc[0]}"
        )

    if selected_paper:
        paper_data = df[df['arxiv_id'] == selected_paper].iloc[0]
        
        # Main content area
        st.markdown(f"<h1 class='paper-title'>{paper_data['title']}</h1>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"**Authors:** {paper_data['author']}")
        with col2:
            st.markdown(f"**ArXiv ID:** [{paper_data['arxiv_id']}](https://arxiv.org/abs/{paper_data['arxiv_id']})")
        
        st.divider()

        # Sections in tabs
        tab_names = ['Background', 'Motivation', 'Methodology', 
                    'Results', 'Interpretation', 'Implication']
        tabs = st.tabs(tab_names)
        
        for tab, section in zip(tabs, [name.lower() for name in tab_names]):
            with tab:
                st.markdown(f"### {section.title()}")
                st.write(paper_data[section])

if __name__ == "__main__":
    main()