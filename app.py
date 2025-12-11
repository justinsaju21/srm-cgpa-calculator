import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="SRM GPA Calculator",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Premium Design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Container */
    .main .block-container {
        max-width: 900px;
        padding: 1rem 1rem;
    }
    
    /* Header Styling */
    .main-header {
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem 0 0 0;
    }
    .main-header h1 {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -1px;
        line-height: 1.1;
    }
    .main-header .subtitle {
        color: #a0aec0;
        font-size: 0.95rem;
        font-weight: 400;
        margin-top: 0.8rem;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    
    /* Table Header */
    .table-header {
        display: grid;
        grid-template-columns: 80px 1fr 1fr;
        gap: 1.5rem;
        padding: 1.2rem 2rem;
        background: rgba(102, 126, 234, 0.08);
        border-radius: 14px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(102, 126, 234, 0.25);
    }
    .table-header div {
        color: #b8c5d6;
        font-weight: 600;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    /* Course Row Spacing */
    .row-widget.stHorizontal {
        margin-bottom: 1rem !important;
    }
    
    /* Input Styling */
    div[data-baseweb="select"] > div, .stNumberInput input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: 10px !important;
        color: white !important;
    }
    
    div[data-baseweb="select"] > div:hover, .stNumberInput input:hover {
        border-color: #667eea !important;
    }
    
    /* Fix Selectbox Text Color & Dropdown */
    div[data-baseweb="select"] span {
        color: white !important;
    }
    div[data-baseweb="menu"] {
        background-color: #1a1a2e !important;
        border: 1px solid rgba(102, 126, 234, 0.3) !important;
    }
    div[data-baseweb="menu"] div {
        color: white !important;
    }
    div[data-baseweb="menu"] div:hover {
        background-color: rgba(102, 126, 234, 0.2) !important;
    }
    
    /* Remove padding issues that hide text */
    .stNumberInput input {
        padding: 0.5rem !important;
    }
    
    /* Course Number */
    .course-number {
        color: #667eea;
        font-weight: 700;
        font-size: 1.3rem;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
        padding-top: 0.5rem;
    }
    
    /* Button Styling */
    .stButton > button {
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        padding: 0.9rem 2rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: none !important;
        min-height: 52px !important;
        width: 100% !important;
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.5) !important;
    }
    
    .stButton > button[kind="secondary"] {
        background: rgba(239, 68, 68, 0.12) !important;
        color: #ef4444 !important;
        border: 1.5px solid rgba(239, 68, 68, 0.35) !important;
    }
    .stButton > button[kind="secondary"]:hover {
        background: rgba(239, 68, 68, 0.2) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(239, 68, 68, 0.25) !important;
    }
    
    /* Control Buttons (Add/Remove) */
    div[data-testid="column"] .stButton > button:not([kind="primary"]):not([kind="secondary"]) {
        background: rgba(102, 126, 234, 0.12) !important;
        border: 1.5px solid rgba(102, 126, 234, 0.3) !important;
        color: #8b9dc3 !important;
        font-weight: 600 !important;
    }
    div[data-testid="column"] .stButton > button:not([kind="primary"]):not([kind="secondary"]):hover:not(:disabled) {
        background: rgba(102, 126, 234, 0.2) !important;
        border-color: rgba(102, 126, 234, 0.5) !important;
        color: #a8b8d8 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 18px rgba(102, 126, 234, 0.2) !important;
    }
    div[data-testid="column"] .stButton > button:disabled {
        opacity: 0.4 !important;
        cursor: not-allowed !important;
    }
    
    /* Result Card */
    .result-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
        backdrop-filter: blur(10px);
        padding: 3.5rem 2.5rem;
        border-radius: 24px;
        border: 1px solid rgba(102, 126, 234, 0.3);
        text-align: center;
        margin-top: 3rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
        animation: slideUp 0.6s ease-out;
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .result-label {
        color: #a0aec0;
        font-size: 1.05rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 1.5rem;
    }
    
    .gpa-score {
        font-size: 5.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
        margin: 1.5rem 0;
    }
    
    .gpa-bar-container {
        width: 100%;
        height: 14px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 12px;
        overflow: hidden;
        margin-top: 2.5rem;
    }
    .gpa-bar {
        height: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        transition: width 1s ease-out;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.5);
    }
    
    /* Spacing Utilities */
    .spacer-small {
        height: 1.5rem;
    }
    .spacer-medium {
        height: 2.5rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 5rem;
        padding-top: 2.5rem;
        border-top: 1px solid rgba(102, 126, 234, 0.2);
        color: #718096;
        font-size: 0.9rem;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.4), transparent);
        margin: 2.5rem 0;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Grade Points Mapping
GRADE_POINTS = {
    "O": 10.0,
    "A+": 9.0,
    "A": 8.0,
    "B+": 7.0,
    "B": 6.0,
    "C": 5.5,
    "W": 0.0,
    "F": 0.0,
    "Ab": 0.0,
    "I": 0.0,
    "*": 0.0
}

def calculate_gpa(courses):
    """Calculate GPA from course data"""
    total_points = 0
    total_credits = 0
    
    for course in courses:
        credits = course['credits'] if course['credits'] is not None else 0
        grade_val = GRADE_POINTS.get(course['grade'], 0.0)
        
        total_points += credits * grade_val
        total_credits += credits
        
    return total_points / total_credits if total_credits > 0 else 0.0

def main():
    # Header
    st.markdown("""
        <div class="main-header">
            <h1>SRM GPA Calculator</h1>
            <div class="subtitle">CALCULATE YOUR GRADE POINT AVERAGE</div>
        </div>
    """, unsafe_allow_html=True)

    # Initialize Session State
    if 'num_courses' not in st.session_state:
        st.session_state.num_courses = 1
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False
    if 'calculated_gpa' not in st.session_state:
        st.session_state.calculated_gpa = 0.0

    # Table Header
    st.markdown("""
        <div class="table-header">
            <div>#</div>
            <div>Credits</div>
            <div>Grade</div>
        </div>
    """, unsafe_allow_html=True)

    # Course Input Rows
    courses_data = []
    for i in range(st.session_state.num_courses):
        col1, col2, col3 = st.columns([0.8, 2, 2])
        
        with col1:
            st.markdown(f'<div class="course-number">{i+1}</div>', unsafe_allow_html=True)
        
        with col2:
            credits = st.number_input(
                f"Credits {i+1}", 
                min_value=0,
                max_value=10,
                value=0,
                step=1,
                key=f"credit_{i}",
                label_visibility="collapsed"
            )
        
        with col3:
            grade = st.selectbox(
                f"Grade {i+1}", 
                options=list(GRADE_POINTS.keys()),
                key=f"grade_{i}",
                label_visibility="collapsed"
            )
        
        courses_data.append({'credits': credits, 'grade': grade})

    st.markdown("<div class='spacer-medium'></div>", unsafe_allow_html=True)

    # Past Semesters Section (CGPA) - MOVED HERE
    with st.expander("📚 Add Past Semesters (For CGPA)", expanded=st.session_state.get('include_cgpa', False)):
        st.checkbox("Include in Calculation", key='include_cgpa')
        
        if st.session_state.include_cgpa:
            if 'past_semesters' not in st.session_state:
                st.session_state.past_semesters = [{'credits': 0, 'sgpa': 0.0}]
            
            p_cols_header = st.columns([1, 1, 0.2])
            p_cols_header[0].caption("CREDITS")
            p_cols_header[1].caption("SGPA")
            
            for i, p_sem in enumerate(st.session_state.past_semesters):
                pc1, pc2, pc3 = st.columns([1, 1, 0.2])
                with pc1:
                    st.session_state.past_semesters[i]['credits'] = st.number_input(
                        f"p_cred_{i}", min_value=0, value=p_sem['credits'], key=f"p_c_{i}", label_visibility="collapsed"
                    )
                with pc2:
                    st.session_state.past_semesters[i]['sgpa'] = st.number_input(
                        f"p_sgpa_{i}", min_value=0.0, max_value=10.0, value=float(p_sem['sgpa']), step=0.01, key=f"p_s_{i}", label_visibility="collapsed"
                    )
                with pc3:
                    if len(st.session_state.past_semesters) > 1:
                        if st.button("🗑️", key=f"del_p_{i}"):
                            st.session_state.past_semesters.pop(i)
                            st.rerun()
            
            if st.button("➕ Add Semester"):
                st.session_state.past_semesters.append({'credits': 0, 'sgpa': 0.0})
                st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    # Add/Remove Course Controls (Keeping this one above as per original flow, but ensuring spacing)
    # Actually wait, the Add/Remove Course controls are for the current semester courses.
    # The user wants the Calculate button at the very bottom.
    
    # Calculate & Reset Buttons
    col_calc, col_reset = st.columns(2)
    
    with col_calc:
        if st.button("🎯 Calculate GPA", type="primary", use_container_width=True):
            sgpa = calculate_gpa(courses_data)
            st.session_state.calculated_gpa = sgpa
            st.session_state.show_result = True
            
            # CGPA Calculation
            if st.session_state.get('include_cgpa', False):
                total_past_points = 0
                total_past_credits = 0
                for sem in st.session_state.past_semesters:
                    total_past_points += sem['sgpa'] * sem['credits']
                    total_past_credits += sem['credits']
                
                # Current Sem details
                current_sem_credits = sum(c['credits'] for c in courses_data)
                current_sem_points = sgpa * current_sem_credits
                
                total_credits = total_past_credits + current_sem_credits
                
                if total_credits > 0:
                    cgpa = (total_past_points + current_sem_points) / total_credits
                    st.session_state.calculated_cgpa = cgpa
            
            st.rerun()
    
    with col_reset:
        if st.button("🔄 Reset", type="secondary", use_container_width=True):
            st.session_state.num_courses = 1
            st.session_state.past_semesters = [{'credits': 0, 'sgpa': 0.0}]
            st.session_state.show_result = False
            st.session_state.calculated_gpa = 0.0
            st.session_state.calculated_cgpa = 0.0
            st.rerun()

    # Display Result
    if st.session_state.show_result:
        gpa = st.session_state.calculated_gpa
        percentage = min(gpa * 10, 100)
        
        # Determine what to show
        show_cgpa = st.session_state.get('include_cgpa', False) and 'calculated_cgpa' in st.session_state
        
        # Build HTML content
        cgpa_html = ""
        if show_cgpa:
            cgpa_val = st.session_state.calculated_cgpa
            cgpa_html = f"""
                <hr style="opacity: 0.3; margin: 2rem 0;">
                <div style="margin-top: 1rem;">
                    <div class="result-label" style="font-size: 0.9rem; opacity: 0.8;">Cumulative GPA (CGPA)</div>
                    <div class="gpa-score" style="font-size: 3.5rem; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                        {cgpa_val:.2f}
                    </div>
                </div>
            """
        
        st.markdown(f"""
            <div class="result-card">
                <div class="result-label">Semester GPA (SGPA)</div>
                <div class="gpa-score">{gpa:.2f}</div>
                <div class="gpa-bar-container">
                    <div class="gpa-bar" style="width: {percentage}%"></div>
                </div>
                {cgpa_html}
            </div>
        """, unsafe_allow_html=True)

    # Footer
    current_year = datetime.now().year
    st.markdown(f"""
        <div class="footer">
            <p>Created by Streamlit with ❤️ by Justin</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
