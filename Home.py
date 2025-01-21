import streamlit as st
from streamlit_calendar import calendar
import datetime
import uuid

#https://bernevents.streamlit.app/                                              #live link
#https://github.com/TastStreamlit/Events/tree/main                              github link
#https://docs.streamlit.io/develop/api-reference                                #streamlit api
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/         #streamlit emoji shortcodes
#https://github.com/im-perativa/streamlit-calendar?tab=readme-ov-file           #calendar package

#TODO:  -Login system so other users cant edit already existing events
#       -Payment system
#       -Inform people (send emails)

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.logo("https://seeklogo.com/images/K/Kanton_Bern-logo-62EAC80617-seeklogo.com.png")

#Init session state
if not st.session_state.get("Calendar", False):
    st.session_state["Calendar"] = str(uuid.uuid4())
if not st.session_state.get("Events", False):
    st.session_state["Events"] = []

# Light/Dark mode toggle button session state
ms = st.session_state
if "themes" not in ms: 
    ms.themes = {"currentTheme": "dark",        
        "light": {"theme.base": "dark",
            #"theme.backgroundColor": "black",
            #"theme.primaryColor": "#c98bdb",
            #"theme.secondaryBackgroundColor": "#5591f5",
            #"theme.textColor": "white",
            "buttonFace": "Dark 🌜"},  #🌑

        "dark":  {"theme.base": "light",
            #"theme.backgroundColor": "white",
            #"theme.primaryColor": "#5591f5",
            #"theme.secondaryBackgroundColor": "#82E1D7",
            #"theme.textColor": "#0a1464",
            "buttonFace": "Light 🌞"}, #🌕
        }
    
# Change theme from/to light/dark
def changeTheme():
    previousTheme = ms.themes["currentTheme"]
    themeDict = ms.themes["light"] if ms.themes["currentTheme"] == "light" else ms.themes["dark"]
    for key, val in themeDict.items(): 
        if key.startswith("theme"): st._config.set_option(key, val)

    if previousTheme == "dark": ms.themes["currentTheme"] = "light"
    elif previousTheme == "light": ms.themes["currentTheme"] = "dark"

with st.sidebar:
    buttonFace = ms.themes["light"]["buttonFace"] if ms.themes["currentTheme"] == "light" else ms.themes["dark"]["buttonFace"]
    st.button(buttonFace, on_click=changeTheme, help="🌓")

#Vars
today = str(datetime.date.today())

mietables = {
    "Boxe": "blue",
    "Rouchmaschine": "red",
    "Rouchmaschine 2": "green"
}

events = []

people = [
    {"id": "a", "title": "Jeff"},
    {"id": "b", "title": "John"},
    {"id": "c", "title": "Both"}
]

calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "resources": people,
    "selectable": "true",
}

calendar_options = {
    **calendar_options,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridDay,dayGridWeek,dayGridMonth",
    },
    "initialDate": today,
    "initialView": "dayGridMonth",
}

#Calendar
state = calendar(
    events=st.session_state["Events"],
    options=calendar_options,
    custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
    """,
    key=st.session_state["Calendar"],
)

#@st.dialog("Miet")
def addEvent(selectionMethod):
    #choice = st.radio("How would you like to be contacted?", ("Email", "Home phone", "Mobile phone"))
    choice = st.selectbox("Weles am bestä? (debug)", ["multiselect", "segmented_control", "pills"])
    st.divider()

    if choice == "multiselect":
        new_mietable = st.multiselect("Equipment", mietables)
    elif choice == "segmented_control":
        new_mietable = st.segmented_control("Equipment", mietables, selection_mode="multi")
    elif choice == "pills":
        new_mietable = st.pills("Equipment", mietables, selection_mode="multi")

    st.info("Selected: " + str(new_mietable))

    t = st.time_input("When?", "now", step=1800)               #datetime.time(8, 45)
    st.write("At", t)

    #if t before today == st.warning("Selected date is in the past")    or st.error
    #else st.info or st.success

    if selectionMethod == "click":
        all_day = True
        start_date = state["dateClick"]["date"]
        end_date = state["dateClick"]["date"]
    elif selectionMethod == "select":
        all_day = True
        start_date = state["select"]["start"]
        end_date = state["select"]["end"]
    
    if st.button("Miet!", use_container_width=True):
        i = 0
        for new_m in new_mietable:
            new_event_desc = {
                "allDay": all_day,     #all day or certain hours
                "title": new_mietable[i],
                "color": mietables[new_m],
                "location": "Bern",
                "start": start_date,
                "end": end_date,
                "resourceId": "a"
            }

            st.session_state["Events"].append(new_event_desc)
            #st.toast(f"{new_mietable[i]} added", icon='😍') #isnt seen because of rerun right after
            i += 1

        st.session_state["Calendar"] = str(uuid.uuid4())
        st.rerun()
        #st.balloons()      #doesnt run after rerun

if "callback" in state.keys():
#if state["callback"] != "eventsSet":
    if state["callback"] == "dateClick":
        addEvent("click")
    elif state["callback"] == "select":
        addEvent("select")

with st.expander("About Equipment", icon="🎧"): #🎵🎶🔈🔉🔊
    st.write("Boxe desc")
    st.image(
            "https://cdn.pixabay.com/photo/2019/11/13/10/17/monkey-banana-4623184_640.jpg",
            caption = "Boxe Image",
            width = 400,
        )
    st.divider()

    st.write("Rouchmaschine desc")
    st.divider()

with st.expander("About Us", icon="🌍"):
    st.write("Uber uns")

#DEBUG
with st.sidebar:
    st.divider()
    st.write("DEBUG")

    st.write("State")
    st.write(state)

    st.write("SESSION_EVENTS " + str(st.session_state["Events"]))

    st.divider()
    st.write("TEST")
    color = st.color_picker("Pick A Color", "#00f900")
