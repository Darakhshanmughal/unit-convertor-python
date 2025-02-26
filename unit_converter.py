import streamlit as st
import pint

# Initialize the unit registry
ureg = pint.UnitRegistry()

def convert_units(value, from_unit, to_unit):
    try:
        # Special handling for temperature conversion
        if "celsius" in from_unit.lower() or "fahrenheit" in from_unit.lower():
            result = ureg.Quantity(value, ureg(from_unit)).to(ureg(to_unit))
        else:
            result = (value * ureg(from_unit)).to(to_unit)
            
        return f"{result.magnitude:.4f} {result.units}"
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Google Unit Converter")
st.write("Convert units like length, weight, temperature, and more!")

# User Inputs
value = st.number_input("Enter value:", min_value=0.0, value=1.0, step=0.1)
from_unit = st.text_input("From unit (e.g., meter, kg, Celsius):").strip()
to_unit = st.text_input("To unit (e.g., feet, pounds, Fahrenheit):").strip()

if st.button("Convert"):
    if from_unit and to_unit:
        result = convert_units(value, from_unit, to_unit)
        st.success(f"Converted Value: {result}")
    else:
        st.error("Please enter both units for conversion.")
