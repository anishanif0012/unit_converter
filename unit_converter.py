import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(white);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3)"
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    st.Button>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: black;
        font-size: 18px:
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    st.Button>Button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and decsription
st.markdown("<h1> Unit Convertor using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

#sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", min_value=0.0, value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Kilometers", "Meters", "Centimeters", "Millimeters", "Micrometers", "Nanometers", "Feet", "Miles", "Yards", "Inches", "Nautical Miles"])
    with col2:
        to_unit = st.selectbox("To", ["Kilometers", "Meters", "Centimeters", "Millimeters", "Micrometers", "Nanometers", "Feet", "Miles", "Yards", "Inches", "Nautical Miles"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Micrograms", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Micrograms", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#conversion logic
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Kilometers": 1000,
        "Meters": 1,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Micrometers": 0.000001,
        "Nanometers": 0.000000001,
        "Feet": 0.3048,
        "Miles": 1609.34,
        "Yards": 0.9144,
        "Inches": 0.0254,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Milligrams": 0.000001,
        "Micrograms": 0.000000001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" :
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value

#button for conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by Anis Hanif</div>", unsafe_allow_html=True)
        
        


            
