import time
import json
import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie

st.title("Jay Hind Driving School, Surli.")
# st.beta_set_page_config(page_title='Jay Hind Driving School, Surli.', page_icon = logo3.png)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

user_menu = st.sidebar.radio("पर्याय निवडा", ["मुख्यपृष्ठ", "प्रतिमा", "उपलब्ध सेवा", "संपर्क"])
if user_menu == "मुख्यपृष्ठ" :
    st.image("logo3.jpg", width=300)
    st.markdown("<h1><bold><center>JAY HIND DRIVING SCHOOL, SURLI<center><bold><h1>", True)
    st.markdown("<hr><hr>", True)

    with st.spinner('Wait for it...'):
        time.sleep(1)
    url = requests.get(
        "https://lottie.host/279919ed-8b0c-4423-a41b-17b4cee6191c/zYnJKHsjRG.json")
    url_json = dict()

    if url.status_code == 200:
        url_json = url.json()
    else:
        st.image("img2.jpg", width=300)

    st_lottie(url_json)
    st.warning("जय हिंद ड्रायव्हिंग स्कूलमध्ये स्वप्नांच्या गाडीला गती मिळवा !!! ")

    st.markdown("<hr><hr>", True)
    st.image("book.jpg", width=300)
elif user_menu=="प्रतिमा" :
    st.title("प्रतिमा")

    st.image("car1.jpg", width=300)
    time.sleep(2)

    st.image("img1.jpg", width=300)
    time.sleep(2)

    st.image("img2.jpg", width=300)
    time.sleep(2)

    st.image("img3.jpg", width=300)
    time.sleep(2)

    st.image("img4.jpg",width=300)
elif user_menu=="उपलब्ध सेवा":
    st.title("उपलब्ध सेवा")
    st.success("We Offer Best Services To You !!!")

    st.info(":white_medium_square:4-Wheeler Training")
    st.image("4wheel.webp", width=300)

    st.info(":white_medium_square:2-Wheeler Training")
    st.image("2wheel.webp", width=300)

    st.info(":white_medium_square: Lisence Services")
    st.image("lisence.jpg", width=300)

elif user_menu=="संपर्क":
    st.title("संपर्क")

    st.success(" ")
    st.header("Srikant Sutar (Ex. Army)")
    st.subheader(":phone: +91 9929878257")
    st.subheader(":phone: +91 8107819649")

    st.success(" ")
    st.subheader(":round_pushpin: At.P Surli, Tal.Koregaon, Dist.Satara, 415511.")

    st.markdown("""
        <a href='https://maps.app.goo.gl/6TFN1uhta3qvf7Mg8' target='_blank' style='text-decoration: none;'>
            🗺️ Open in Google Maps
        </a>
        """, unsafe_allow_html=True)

    st.success(" ")
    facebook_logo_url = "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"

    st.markdown(f"""
        <h2>
            <img src="{facebook_logo_url}" alt="Facebook" style="width:30px;height:30px;margin-right:10px;">
            <a href=""
        </h2>
    """, unsafe_allow_html=True)
    instagram_link = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"

    st.markdown(f"""
            <h2>
                <img src="{instagram_link}" alt="Instagram" style="width:30px;height:30px;margin-right:10px;">
                <a href=""
            </h2>
        """, unsafe_allow_html=True)

