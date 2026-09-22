import streamlit as st
from calculator import calculate

st.set_page_config(
    page_title="Interactive Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Interactive Calculator")


# -----------------------------
# Session State
# -----------------------------

if "expression_input" not in st.session_state:
    st.session_state.expression_input = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "error" not in st.session_state:
    st.session_state.error = ""


# -----------------------------
# Functions
# -----------------------------

def add(value):
    st.session_state.expression_input += value
    st.session_state.error = ""


def clear():
    st.session_state.expression_input = ""
    st.session_state.error = ""


def backspace():
    st.session_state.expression_input = (
        st.session_state.expression_input[:-1]
    )
    st.session_state.error = ""


def do_calculate():
    expression = st.session_state.expression_input

    if not expression:
        return

    result, error = calculate(expression)

    if error:
        st.session_state.error = error
        return

    st.session_state.history.append(
        f"{expression} = {result}"
    )

    st.session_state.expression_input = str(result)
    st.session_state.error = ""


# -----------------------------
# Expression Input
# -----------------------------
# Pressing ENTER inside this form submits the form.

with st.form("calculator_form"):

    st.text_input(
        "Expression",
        key="expression_input",
        placeholder="Example: 10 + 5 * 2"
    )

    submitted = st.form_submit_button(
        "Enter / =",
        use_container_width=True
    )

    if submitted:
        do_calculate()


# -----------------------------
# Error
# -----------------------------

if st.session_state.error:
    st.error(st.session_state.error)


# -----------------------------
# Calculator Buttons
# -----------------------------

# Row 1
cols = st.columns(4)

with cols[0]:
    st.button("7", on_click=add, args=("7",),
              use_container_width=True)

with cols[1]:
    st.button("8", on_click=add, args=("8",),
              use_container_width=True)

with cols[2]:
    st.button("9", on_click=add, args=("9",),
              use_container_width=True)

with cols[3]:
    st.button("/", on_click=add, args=("/ ",),
              use_container_width=True)


# Row 2
cols = st.columns(4)

with cols[0]:
    st.button("4", on_click=add, args=("4",),
              use_container_width=True)

with cols[1]:
    st.button("5", on_click=add, args=("5",),
              use_container_width=True)

with cols[2]:
    st.button("6", on_click=add, args=("6",),
              use_container_width=True)

with cols[3]:
    st.button("*", on_click=add, args=("*",),
              use_container_width=True)


# Row 3
cols = st.columns(4)

with cols[0]:
    st.button("1", on_click=add, args=("1",),
              use_container_width=True)

with cols[1]:
    st.button("2", on_click=add, args=("2",),
              use_container_width=True)

with cols[2]:
    st.button("3", on_click=add, args=("3",),
              use_container_width=True)

with cols[3]:
    st.button("-", on_click=add, args=("-",),
              use_container_width=True)


# Row 4
cols = st.columns(4)

with cols[0]:
    st.button("0", on_click=add, args=("0",),
              use_container_width=True)

with cols[1]:
    st.button(".", on_click=add, args=(".",),
              use_container_width=True)

with cols[2]:
    st.button("+", on_click=add, args=("+",),
              use_container_width=True)

with cols[3]:
    st.button("=", on_click=do_calculate,
              use_container_width=True)


# -----------------------------
# Control Buttons
# -----------------------------

cols = st.columns(2)

with cols[0]:
    st.button(
        "Clear",
        on_click=clear,
        use_container_width=True
    )

with cols[1]:
    st.button(
        "⌫ Backspace",
        on_click=backspace,
        use_container_width=True
    )


# -----------------------------
# History
# -----------------------------

if st.session_state.history:

    st.divider()
    st.subheader("History")

    for item in reversed(st.session_state.history):
        st.write(item)
