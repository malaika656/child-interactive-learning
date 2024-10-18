import streamlit as st

# Title of the app
st.title("Kids Learning App")

# Sections of the app
section = st.sidebar.selectbox("Choose a section", ["Learn Colors", "Learn Shapes", "Simple Math", "Fun Facts"])

# Learn Colors Section
if section == "Learn Colors":
    st.header("Learn Colors")
    colors = {
        "Red": "#FF0000",
        "Blue": "#0000FF",
        "Green": "#008000",
        "Yellow": "#FFFF00",
        "Purple": "#800080"
    }
    
    color_name = st.selectbox("Pick a color", list(colors.keys()))
    st.write(f"**{color_name}** looks like this:")
    st.markdown(f"<div style='background-color:{colors[color_name]}; width:100%; height:100px;'></div>", unsafe_allow_html=True)

# Learn Shapes Section
elif section == "Learn Shapes":
    st.header("Learn Shapes")
    shape = st.selectbox("Pick a shape", ["Circle", "Square", "Triangle", "Rectangle"])
    
    if shape == "Circle":
        st.markdown("<div style='border-radius:50%; background-color:blue; width:100px; height:100px;'></div>", unsafe_allow_html=True)
    elif shape == "Square":
        st.markdown("<div style='background-color:green; width:100px; height:100px;'></div>", unsafe_allow_html=True)
    elif shape == "Triangle":
        st.markdown(
            "<div style='width: 0; height: 0; border-left: 50px solid transparent; border-right: 50px solid transparent; border-bottom: 100px solid red;'></div>",
            unsafe_allow_html=True,
        )
    elif shape == "Rectangle":
        st.markdown("<div style='background-color:orange; width:150px; height:100px;'></div>", unsafe_allow_html=True)

# Simple Math Section
elif section == "Simple Math":
    st.header("Simple Math Practice")
    
    num1 = st.number_input("Enter the first number", min_value=0, max_value=100, value=0, step=1)
    num2 = st.number_input("Enter the second number", min_value=0, max_value=100, value=0, step=1)
    operation = st.selectbox("Pick an operation", ["Add", "Subtract", "Multiply"])
    
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    
    st.write(f"The result of {operation.lower()}ing {num1} and {num2} is: **{result}**")

# Fun Facts Section
elif section == "Fun Facts":
    st.header("Fun Facts for Kids")
    
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey that are over 3000 years old and still safe to eat!",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts and blue blood.",
        "A day on Venus is longer than a year on Venus.",
        "Dolphins sleep with one eye open!"
    ]
    
    st.write("Did you know?")
    st.write(st.selectbox("Pick a fun fact!", facts))

# Deploy by running: streamlit run app.py
