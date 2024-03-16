import streamlit as st
import numpy as np
import json
import pandas as pd
import time
from datetime import time
import datetime
from geopy.geocoders import Nominatim
from PIL import Image
from io import StringIO
import cv2

#initiating geo locatior agent to fetch longitude and latitude
geolocator = Nominatim(user_agent="my_user_agent")


#Basic display functions
st.text("st.text can only write in normal fonts no formatting is available")

st.write("**st.write**: This has all the capabilities of st.text but it can use all the markdown functions, graphs, dataframes and definitions, JSON anything")

st.write("st.code is used to print codes and the syntex is st.code(code,language='python')")

code = '''
def sum(a,b):
    return a+b
'''
st.code(code,language='python')

# Manipulate Dataframe, table, matrix and json

st.dataframe(np.random.randn(50,20), width=100, height=50)
st.table(np.random.randn(50,20))
st.metric("NVIDIA stock", value="988", delta="105.22", delta_color='normal')
st.json(json.load(open("ranodm.json")), expanded= False)

#plotting:

df = pd.DataFrame(np.random.randn(10,2), columns = ["Prices", "Diff"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
# st.pyplot(np.random.randn(10), bins=100)

address = st.text_input(
        "address ",
        key="placeholder"
    )

if address:
    loc = geolocator.geocode(address)
    st.write("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)    
    places = pd.DataFrame({
        "lat" : [float(loc.latitude)] ,
        "lon" : [float(loc.longitude)]
    })
    st.map(places)


#button
pr = st.button("Check time!!") 
if pr == True:
    st.write(time.time())


#Download csv file
df = pd.DataFrame(
    np.random.randn(10 , 2) ,
    columns = ["col1" , "col2"]
)
data = df.to_csv().encode("utf-8")

st.download_button(
    label = "Download this" ,
    data = data ,
    file_name = "new_data_file.csv" ,
    mime = "text/csv"
)

#Download text file
text_contents = "This is some text"
st.download_button("Please download" , text_contents)

#Download image file
file = open("image-3-1.jpg" , "rb")
btn = st.download_button(
    label = "Download the image" ,
    data = file ,
    file_name = "the_house_image.jpg" ,
    mime = "image/jpg"
)

#create checkbox
ck = st.checkbox("I agree" , value = False)
if ck:
    st.write("Agreement reached")

#create radio button
food = st.radio("What would like to eat?" ,
                ("Pizza" , "Burger" , "Chips"))
if food == "Pizza":
    st.write("You ordered Pizza")
elif food == "Burger":
    st.write("You ordered Burger")
elif food == "Chips":
    st.write("You ordered Chips")

#create selectbox
option = st.selectbox("Where do you live?" ,
                      ("Moscow" , "New York" , "Istanbul"))
if option == "Moscow":
    st.write("You wrote Moscow")
elif option == "New York":
    st.write("You wrote New York")
elif option == "Istanbul":
    st.write("You wrote Istanbul")


#input widget
#multi select
option = st.multiselect(
    label = "Which places have you been?" ,
    options = ("Sydney" , "Tokyo" , "New Delhi" , "Paris" , "Cape Town") ,
    default = ("Sydney" , "Paris")
)
st.write(option)

#slider
num = st.slider(
    label = "Your age" ,
    min_value = 18 ,
    max_value = 120 ,
    value = 20 ,
    step = 1
)
st.write(num)

#range
num = st.slider(
    label = "Your age" ,
    min_value = 18 ,
    max_value = 120 ,
    value = (40 , 60) ,
    step = 1
)
st.write(num)

#time slider:
visit_timing = st.slider(
   label = "Your appointment" ,
   value = (time(11 , 30) , time(12 , 45))
)
st.write(visit_timing)

option = st.select_slider(
    label = "Select the best color" ,
    options = ("Violet" , "Indigo" , "Blue" , "Green" , "Yellow" , "Orange" , "Red")
)
st.write(option)

start_color , end_color = st.select_slider(
    label = "Select color range" ,
    options = ("Violet" , "Indigo" , "Blue" , "Green" , "Yellow" , "Orange" , "Red") ,
    value = ("Blue" , "Orange")
)
st.write("From" , start_color , "to" , end_color)

txt = st.text_input(
    label = "Please enter your email" ,
    max_chars = 20 ,
    placeholder = "Email here"
)
st.write(txt)

passw = st.text_input(
    label = "Enter your password" ,
    max_chars = 20 ,
    placeholder = "password here" ,
    type = "password"
)
st.write(passw)

num = st.number_input(
    label = "Enter your weight" ,
    min_value = 40 ,
    max_value = 120 ,
    value = 65 ,
    step = 1
)
st.write(num)

txt = st.text_area(
    label = "Write something" ,
    height = 200 ,
    max_chars = 100 ,
    placeholder = "Write here"
)
st.write(txt)

dat = st.date_input("Enter your birthday" ,
                    value = datetime.date(2023 , 4 , 11))
st.write(dat)

tim = st.time_input("Enter your meal time" , value = datetime.time(14 , 00))
st.write(tim)

fl = st.file_uploader(
    label = "Upload here"
)
if fl:
    st.write(fl.type)
    if "image" in fl.type:
        img = Image.open(fl)
        st.write(np.array(img).shape)
    elif fl.type == "text/plain":
        stringio = StringIO(fl.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)

picture = st.camera_input("Take a pic")
if picture:
    img = Image.open(picture)
    st.write(np.array(img).shape)

color = st.color_picker("Pick a color")
if color:
    st.write("You selected" , color)

#add images
img = Image.open("image-3-1.jpg")
st.image(
    img ,
    caption = "Image of a house" ,
    width = 400 ,
    channels = "RGB"
)

st.write("st.audio(add your audio file path , start_time = 10)")

st.write("st.video(add your video file path here)")


#Layouts using sidebars
choice = st.sidebar.radio(
    label = "Choose the option" ,
    options = ("audio" , "video")
)
if choice == "audio":
    st.audio("India Elections 2024 [ ytmp3x.cc ].mp3")
    st.write("This is audio")
elif choice == "video":
    st.video("swapped.mp4")
    st.write("this is video")

#creating a column view
col1 , col2 = st.columns([1 , 3] , gap = "small")
col1.audio("India Elections 2024 [ ytmp3x.cc ].mp3")
col1.write("This is audio")
col2.video("swapped.mp4")

#creating tab view
tab1 , tab2 = st.tabs(["audio" , "video"])
tab1.audio("India Elections 2024 [ ytmp3x.cc ].mp3")
tab1.write("hi")
tab2.video("swapped.mp4")

#creating a container
exp = st.expander("See pic")
exp.write("Video and image")
exp.image("image-3-1.jpg" , width = 400)

st.write("One")
st.write("Two")
st.write("Three")

#creating a container of elements
cont = st.container()
cont.write("One")
st.write("Two")
cont.write("Three")
st.write("This is last")
cont.write("Last")


#status elements
import time
txt = "% completed"

#add a progress bar
my_bar = st.progress(0 , text = txt)
for pr in range(100):
    time.sleep(0.1)
    my_bar.progress(pr + 1 , text = txt)
#add a spinner
with st.spinner("wait for it..."):
    time.sleep(5)
st.write("wait over")

#add bloons animation
st.balloons()

#add snowflakes animation
st.snow()

#print different error messages 
st.error("This is an error message!!!!!!!!!!!")
st.warning("This is an warning message!!!!!!!!!!!")
st.info("This is an info message!!!!!!!!!!!")
st.success("This is an success message!!!!!!!!!!!")

#print exception messages 
e = RuntimeError("Exp")
st.exception(e)

