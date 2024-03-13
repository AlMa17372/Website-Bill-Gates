import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Website", page_icon=":skull:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding=load_lottieurl("https://lottie.host/0149fc50-a45f-48cc-bd23-eb0cd81e8906/6sT7I8mFfn.json")
img_lottie_animation = ("https://cisoclub.ru/wp-content/uploads/mrsmajor3-exe-novyj-strashnyj-virus-kak-ego-udalit-virusologiya-ot-undermind-youtube-thumbnail.jpg")
img_lottie_animation0 = ("https://i.ytimg.com/vi/Qgu7CAMkjv4/maxresdefault.jpg")
img_lottie_animation1 = ("https://img.youtube.com/vi/w4XFYlTPg8Q/sddefault.jpg")

with st.container():
    st.subheader("Hello, I am Bill Gates :wave:")
    st.title("A creator of Microsoft")
    st.write("I will help you with your Microsoft issues")
    st.write("[Learn more >](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my job I do:
            - Nothing
            - Procrastinating
            - Sleeping
            - Gambling
            
            If this sounds interesting to you apply to our job here

            Also you can install these deadly viruses for fun
            """
        )
        st.write("[Apply](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

with st.container():
    st.write("---")
    st.header("Deadly Viruses")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("MrsMajor3.exe")
        st.write(
            """
            Instant damage to all files and change of wallpaper
            Bloody screen with scary music
            Uneasy to delete
            """
        )
        st.markdown("[Download](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation0)
    with text_column:
        st.subheader("Scorpion Virus V3")
        st.write(
            """
            Animation of TV issues and red skull
            Text saying that your computer is dead
            Unable to open your computer again
            """
        )
        st.markdown("[Download](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation1)
    with text_column:
        st.subheader("VStorageBoost.exe")
        st.write(
            """
            Slowly corrupts your computer
            Later it becomes extremely epileptic
            Shows up a threatening message upon restarting your computer
            Sends your IP to the owner
            """
        )
        st.markdown("[Download](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

with st.container():
    st.write("---")
    st.header("Contact me if your microsoft account got hijacked")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/bill.gates@email.com" method="POST">
     <input type = "hidden" name = "_captcha" value = "false">
     <input type="text" name="name" placeholder = "Your name here" required>
     <input type="email" name="email" placeholder = "Your email here" required>
     <textarea name = "message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()