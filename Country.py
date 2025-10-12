import streamlit as st
from countryinfo import CountryInfo
st.title("Country info")
Country_name=st.text_input("Enter the Country name : ")
if st.button("Search") and Country_name:
    country=CountryInfo(Country_name)
    st.write("**The capital is :**",country.capital())
    st.write("**The Borders are :**",country.borders())
    st.write("**The Currency is :**",country.currencies())
    st.write("**The Language is :**",country.languages())
