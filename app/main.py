import streamlit as st
from chains.cpt_explainer import CPTExplainer
import os

st.set_page_config(
    page_title="CPT AI Code Assistant",
    layout="centered",
    page_icon="💡"
)

st.markdown("""
# 💡 CPT AI Code Assistant
Explain **CPT medical codes** in plain language for patients and non-medical professionals.
""")

# Debug: Show if API key is found (remove in production)
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    st.error("❌ OPENAI_API_KEY environment variable not set! Please set it before running.")
    st.stop()  # Stop further execution

with st.form("cpt_form"):
    cpt_code = st.text_input("CPT Code", placeholder="e.g., 99213")
    short_description = st.text_area("Short Description", placeholder="Brief description of the procedure")
    submitted = st.form_submit_button("Find")

if submitted:
    # Input validation
    if not cpt_code.strip():
        st.warning("⚠️ CPT Code cannot be empty.")
    elif not short_description.strip():
        st.warning("⚠️ Short Description cannot be empty.")
    else:
        # Try calling GPT explainer
        try:
            explainer = CPTExplainer()
        except Exception as e:
            st.error(f"❌ Failed to initialize CPT Explainer: {e}")
        else:
            with st.spinner("Generating explanation using GPT..."):
                try:
                    explanation = explainer.explain(cpt_code.strip(), short_description.strip())
                    if explanation:
                        st.success("Explanation:")
                        st.markdown(f"""
                        <div style="
                            background-color: #f0f2f6;
                            padding: 1rem;
                            border-radius: 0.5rem;
                            font-size: 1.1rem;
                            color: #111;
                        ">
                            {explanation}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.warning("⚠️ GPT returned no explanation. Try different input.")
                except Exception as e:
                    st.error(f"❌ Error during explanation generation: {e}")
