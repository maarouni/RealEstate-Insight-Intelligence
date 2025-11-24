import streamlit as st
import os
from dotenv import load_dotenv

# ✅ Must come before any st.* calls
#st.set_page_config(
    #page_title="main",
    #layout="centered",
    #initial_sidebar_state="collapsed"
#)

# ❌ Hide sidebar nav via CSS fallback (works in most cases)

st.markdown("""
    <style>
        /* Hide the default sidebar nav (e.g. 'main', page list) */
        [data-testid="stSidebarNav"] {
            display: none;
        }

        /* Style visible sidebar links (when shown after login) */
        section[data-testid="stSidebar"] ul li a {
            font-size: 1.1rem !important;
            color: white !important;
            font-weight: 600 !important;
        }
    </style>
""", unsafe_allow_html=True)

#st.markdown("""
    #<style>
        #[data-testid="stSidebarNav"] {display: none;}
    #</style>
#""", unsafe_allow_html=True)


# ---------------------
# 🔐 Password Protection
# ---------------------
load_dotenv()
APP_PASSWORD = os.getenv("APP_PASSWORD", "SmartInvest1!")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Password prompt
if not st.session_state.authenticated:
    st.title("🏠 Real Estate Deal Evaluator")
    password = st.text_input("🔒 Please enter access password", type="password")
    if password == APP_PASSWORD:
        st.session_state.authenticated = True
        st.rerun()
    elif password:
        st.error("❌ Incorrect password. Please try again.")
    st.stop()

# ---------------------
# 🏡 Hub Page UI
# ---------------------

#st.set_page_config(page_title="🏡 Real Estate Evaluator Hub", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <h1 style='text-align: center;'>🏡 Real Estate Investment Evaluator</h1>
    <p style='text-align: center;'>Analyze single properties or compare two side-by-side with AI-enhanced metrics and cash flow projections.</p>
""", unsafe_allow_html=True)

# 👇 Option Cards for Navigation
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Single Property Evaluator")
    st.write("Evaluate one property's cash flow, ROI, and more.")
    if st.button("Go to Single Evaluator", key="single_btn"):
        st.switch_page("pages/1_Main_Single_Property.py")

with col2:
    st.subheader("📊 Dual Property Comparison Evaluator")
    st.write("Compare two investment opportunities side-by-side.")
    if st.button("Go to Dual Comparison", key="dual_btn"):
        st.switch_page("pages/2_Main_Dual_Property.py")

st.markdown("""
    <hr style="margin-top: 2rem; margin-bottom: 1rem;">
    <div style='text-align: center; font-size: 0.9em;'>
        🔐 Protected by access password | 📄 PDF + Email Export | 🤖 AI Verdict
    </div>
""", unsafe_allow_html=True)
