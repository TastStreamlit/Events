import streamlit as st
from streamlit_calendar import calendar
import uuid

st.set_page_config(
    page_title='Home',
    page_icon='🏠',
    layout='centered',
    initial_sidebar_state='collapsed',
)


colors = ["blue", "red", "green"]

#events = [
#    {
#        "title": "Event 1",
#        "color": colors[2],
#        "location": "LA",
#        "start": "2024-08-30",
#        "end": "2024-09-02",
#        "resourceId": "b",
#    }
#]

mietables = ["Boxe", "Rouchmaschine"]

mietablesColors = [
    {mietables[0]: "red"},
    {mietables[1]: "blue"},
]

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
    "initialDate": "2024-08-01",
    "initialView": "dayGridMonth",
}
if not st.session_state.get("Calendar", False):
    st.session_state["Calendar"] = str(uuid.uuid4())
if not st.session_state.get("Events", False):
    st.session_state["Events"] = [{}]

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

event_to_add = {
    "title": "Event 7",
    "color": "#FF4B4B",
    "location": "SF",
    "start": "2024-09-01",
    "end": "2024-09-07",
    "resourceId": "a"
}

@st.dialog("Miet")
def addEvent():
    new_event = st.multiselect("What to miet", mietables)
    #st.write(new_event)


    if st.button("Miet!"):
        #st.write("new event selected")

        new_event_desc = {
            "title": new_event,
            "color": "#FF4B4B",
            "location": "SF",
            "start": (state["dateClick"]["date"]),
            "end": (state["dateClick"]["date"]),
            "resourceId": "a"
        }

        st.session_state["Events"].append(new_event_desc)

        st.session_state["Calendar"] = str(uuid.uuid4())
        st.rerun()

if state["callback"] == "dateClick":
    addEvent()

#if user clicks on a date
#if state["callback"] == "dateClick":
#    #st.write(state["dateClick"]["date"])
#
#    new_event = st.multiselect("What to miet", mietables)
#    st.write(new_event)
#
#    if new_event != []:
#        st.write("new event selected")
#
#        new_event_desc = {
#            "title": new_event,
#            "color": "#FF4B4B",
#            "location": "SF",
#            "start": (state["dateClick"]["date"]),
#            "end": (state["dateClick"]["date"]),
#            "resourceId": "a"
#        }
#
#        st.session_state["Events"].append(new_event_desc)
#
#        st.session_state["Calendar"] = str(uuid.uuid4())
#        st.rerun()


#To DEBUG
with st.sidebar:
    st.write("State")
    st.write(state)

    st.write("SESSION_EVENTS " + str(st.session_state["Events"]))
