```python
import streamlit as st

from calculator import calculate


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Interactive Calculator",
    page_icon="🧮",
    layout="centered"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "expression" not in st.session_state:
    st.session_state.expression = ""

if "history" not in st.session_state:
    st.session_state.history = []


# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------

def add_to_expression(value):

    st.session_state.expression += value


def clear_expression():

    st.session_state.expression = ""


def backspace():

    st.session_state.expression = (
        st.session_state.expression[:-1]
    )


def calculate_result():

    expression = st.session_state.expression

    result, error = calculate(expression)

    if error:

        st.session_state.error = error

    else:

        calculation = f"{expression} = {result}"

        st.session_state.history.append(calculation)

        st.session_state.expression = str(result)

        st.session_state.error = ""


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🧮 Interactive Calculator")

st.caption(
    "A simple scientific calculator built with Python and Streamlit"
)


# --------------------------------------------------
# DISPLAY
# --------------------------------------------------

st.text_input(
    "Expression",
    value=st.session_state.expression,
    disabled=False
)


# --------------------------------------------------
# NUMBER BUTTONS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("7", use_container_width=True):
        add_to_expression("7")
        st.rerun()

with col2:

    if st.button("8", use_container_width=True):
        add_to_expression("8")
        st.rerun()

with col3:

    if st.button("9", use_container_width=True):
        add_to_expression("9")
        st.rerun()

with col4:

    if st.button("÷", use_container_width=True):
        add_to_expression("/")
        st.rerun()


col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("4", use_container_width=True):
        add_to_expression("4")
        st.rerun()

with col2:

    if st.button("5", use_container_width=True):
        add_to_expression("5")
        st.rerun()

with col3:

    if st.button("6", use_container_width=True):
        add_to_expression("6")
        st.rerun()

with col4:

    if st.button("×", use_container_width=True):
        add_to_expression("*")
        st.rerun()


col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("1", use_container_width=True):
        add_to_expression("1")
        st.rerun()

with col2:

    if st.button("2", use_container_width=True):
        add_to_expression("2")
        st.rerun()

with col3:

    if st.button("3", use_container_width=True):
        add_to_expression("3")
        st.rerun()

with col4:

    if st.button("-", use_container_width=True):
        add_to_expression("-")
        st.rerun()


col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("0", use_container_width=True):
        add_to_expression("0")
        st.rerun()

with col2:

    if st.button(".", use_container_width=True):
        add_to_expression(".")
        st.rerun()

with col3:

    if st.button("(", use_container_width=True):
        add_to_expression("(")
        st.rerun()

with col4:

    if st.button(")", use_container_width=True):
        add_to_expression(")")
        st.rerun()


# --------------------------------------------------
# CONTROL BUTTONS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("Clear", use_container_width=True):

        clear_expression()

        st.session_state.error = ""

        st.rerun()


with col2:

    if st.button("⌫ Backspace", use_container_width=True):

        backspace()

        st.rerun()


with col3:

    if st.button("=", use_container_width=True):

        calculate_result()

        st.rerun()


# --------------------------------------------------
# ERROR MESSAGE
# --------------------------------------------------

if "error" in st.session_state:

    if st.session_state.error:

        st.error(st.session_state.error)


# --------------------------------------------------
# SCIENTIFIC FUNCTIONS
# --------------------------------------------------

st.subheader("Scientific Functions")


col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("√", use_container_width=True):

        add_to_expression("sqrt(")

        st.rerun()

with col2:

    if st.button("sin", use_container_width=True):

        add_to_expression("sin(")

        st.rerun()

with col3:

    if st.button("cos", use_container_width=True):

        add_to_expression("cos(")

        st.rerun()

with col4:

    if st.button("tan", use_container_width=True):

        add_to_expression("tan(")

        st.rerun()


col1, col2, col3, col4 = st.columns(4)

with col1:

    if st.button("log", use_container_width=True):

        add_to_expression("log(")

        st.rerun()

with col2:

    if st.button("ln", use_container_width=True):

        add_to_expression("ln(")

        st.rerun()

with col3:

    if st.button("π", use_container_width=True):

        add_to_expression("pi")

        st.rerun()

with col4:

    if st.button("e", use_container_width=True):

        add_to_expression("e")

        st.rerun()


# --------------------------------------------------
# HISTORY
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
```
