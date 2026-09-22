import streamlit as st

from calculator import calculate


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Interactive Calculator",
    page_icon="🧮",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🧮 Interactive Calculator")

st.caption(
    "A simple scientific calculator built with Python and Streamlit"
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "expression" not in st.session_state:
    st.session_state.expression = ""

if "history" not in st.session_state:
    st.session_state.history = []


# --------------------------------------------------
# Display
# --------------------------------------------------

st.text_input(
    "Expression",
    key="expression",
    placeholder="Example: 10 + 5 * 2"
)


# --------------------------------------------------
# Number Buttons
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", use_container_width=True):
        st.session_state.expression += "7"

with col2:
    if st.button("8", use_container_width=True):
        st.session_state.expression += "8"

with col3:
    if st.button("9", use_container_width=True):
        st.session_state.expression += "9"

with col4:
    if st.button("÷", use_container_width=True):
        st.session_state.expression += "/"


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4", use_container_width=True):
        st.session_state.expression += "4"

with col2:
    if st.button("5", use_container_width=True):
        st.session_state.expression += "5"

with col3:
    if st.button("6", use_container_width=True):
        st.session_state.expression += "6"

with col4:
    if st.button("×", use_container_width=True):
        st.session_state.expression += "*"


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1", use_container_width=True):
        st.session_state.expression += "1"

with col2:
    if st.button("2", use_container_width=True):
        st.session_state.expression += "2"

with col3:
    if st.button("3", use_container_width=True):
        st.session_state.expression += "3"

with col4:
    if st.button("-", use_container_width=True):
        st.session_state.expression += "-"


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("0", use_container_width=True):
        st.session_state.expression += "0"

with col2:
    if st.button(".", use_container_width=True):
        st.session_state.expression += "."

with col3:
    if st.button("(", use_container_width=True):
        st.session_state.expression += "("

with col4:
    if st.button(")", use_container_width=True):
        st.session_state.expression += ")"


# --------------------------------------------------
# Control Buttons
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("Clear", use_container_width=True):

        st.session_state.expression = ""

        st.rerun()


with col2:

    if st.button("⌫ Backspace", use_container_width=True):

        st.session_state.expression = (
            st.session_state.expression[:-1]
        )

        st.rerun()


with col3:

    if st.button("=", use_container_width=True):

        result, error = calculate(
            st.session_state.expression
        )

        if error:

            st.error(error)

        else:

            calculation = (
                f"{st.session_state.expression} = {result}"
            )

            st.session_state.history.append(calculation)

            st.session_state.expression = str(result)

            st.rerun()


# --------------------------------------------------
# Scientific Functions
# --------------------------------------------------

st.subheader("Scientific Functions")


col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("√", use_container_width=True):

        st.session_state.expression += "sqrt("

with col2:

    if st.button("sin", use_container_width=True):

        st.session_state.expression += "sin("

with col3:

    if st.button("cos", use_container_width=True):

        st.session_state.expression += "cos("

with col4:

    if st.button("tan", use_container_width=True):

        st.session_state.expression += "tan("


col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("log", use_container_width=True):

        st.session_state.expression += "log("

with col2:

    if st.button("ln", use_container_width=True):

        st.session_state.expression += "ln("

with col3:

    if st.button("π", use_container_width=True):

        st.session_state.expression += "pi"

with col4:

    if st.button("e", use_container_width=True):

        st.session_state.expression += "e"


# --------------------------------------------------
# History
# --------------------------------------------------

st.subheader("Calculation History")


if st.session_state.history:

    for calculation in reversed(
        st.session_state.history
    ):

        st.write(calculation)


    if st.button("Clear History"):

        st.session_state.history = []

        st.rerun()

else:

    st.info("No calculations yet.")
