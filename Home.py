import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime
import uuid

#https://bernevents.streamlit.app/                                              #live link
#https://github.com/TastStreamlit/Events/tree/main                              #github link
#https://docs.streamlit.io/develop/api-reference                                #streamlit api
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/         #streamlit emoji shortcodes
#https://github.com/im-perativa/streamlit-calendar?tab=readme-ov-file           #calendar package
#https://cdn.jsdelivr.net/npm/fullcalendar@5.10.1/locales-all.js                #locale (go to de (nr. 17)) or just go here: https://github.com/fullcalendar/fullcalendar/blob/3e4ce4c2fcee749eb459c59013f70b3cbd3e5a51/packages/core/src/locales/de.ts#L31

#TODO:  
#       -Logo/Branding (colors)
#       -Prices (with breakdown like delivery fees)
#       -Login system so other users cant edit already existing events & faster future bookings
#       -Secure payment system & insurance? Data protection
#       -Inform people (send emails)
#       -Reviews       st.feedback("stars") or st.feedback("thumbs") or st.feedback("faces")
#       -Include an option for delivery/pick-up of rented equipment?
#       -Provide customer support and FAQs?
#       -Contact form? Phone number? Email?
#       -Terms of service?
#       -Testing

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.logo("https://seeklogo.com/images/K/Kanton_Bern-logo-62EAC80617-seeklogo.com.png")

testEvents = [
    {
        "title": "Event 1",
        "color": "#FF6C6C",
        "start": "2023-07-03",
        "end": "2023-07-05",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "color": "#FFBD45",
        "start": "2023-07-01",
        "end": "2023-07-10",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "color": "#FF4B4B",
        "start": "2023-07-20",
        "end": "2023-07-20",
        "resourceId": "c",
    },
    {
        "title": "Event 4",
        "color": "#FF6C6C",
        "start": "2023-07-23",
        "end": "2023-07-25",
        "resourceId": "d",
    },
    {
        "title": "Event 5",
        "color": "#FFBD45",
        "start": "2023-07-29",
        "end": "2023-07-30",
        "resourceId": "e",
    },
    {
        "title": "Event 6",
        "color": "#FF4B4B",
        "start": "2023-07-28",
        "end": "2023-07-20",
        "resourceId": "f",
    },
    {
        "title": "Event 7",
        "color": "#FF4B4B",
        "start": "2023-07-01T08:30:00",
        "end": "2023-07-01T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 8",
        "color": "#3D9DF3",
        "start": "2023-07-01T07:30:00",
        "end": "2023-07-01T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 9",
        "color": "#3DD56D",
        "start": "2023-07-02T10:40:00",
        "end": "2023-07-02T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 10",
        "color": "#FF4B4B",
        "start": "2023-07-15T08:30:00",
        "end": "2023-07-15T10:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 11",
        "color": "#3DD56D",
        "start": "2023-07-15T07:30:00",
        "end": "2023-07-15T10:30:00",
        "resourceId": "e",
    },
    {
        "title": "Event 12",
        "color": "#3D9DF3",
        "start": "2023-07-21T10:40:00",
        "end": "2023-07-21T12:30:00",
        "resourceId": "f",
    },
    {
        "title": "Event 13",
        "color": "#FF4B4B",
        "start": "2023-07-17T08:30:00",
        "end": "2023-07-17T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 14",
        "color": "#3D9DF3",
        "start": "2023-07-17T09:30:00",
        "end": "2023-07-17T11:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 15",
        "color": "#3DD56D",
        "start": "2023-07-17T10:30:00",
        "end": "2023-07-17T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 16",
        "color": "#FF6C6C",
        "start": "2023-07-17T13:30:00",
        "end": "2023-07-17T14:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 17",
        "color": "#FFBD45",
        "start": "2023-07-17T15:30:00",
        "end": "2023-07-17T16:30:00",
        "resourceId": "e",
    },
]

#Init session state
if not st.session_state.get("Calendar", False): st.session_state["Calendar"] = str(uuid.uuid4())
if not st.session_state.get("Events", False):
    #st.session_state["Events"] = []    #set to empty
    st.session_state["Events"] = testEvents

#Light/Dark mode toggle button session state
ms = st.session_state
if "themes" not in st.session_state: 
    st.session_state.themes = {"currentTheme": "dark",        
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
    
#Change theme from/to light/dark
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

def refreshCalendar():
    st.session_state["Calendar"] = str(uuid.uuid4())

def days_past(date_string1, date_string2, date_format="%Y-%m-%d"):
    #Strip time and timezone information by splitting on "T" and selecting only the date part
    date_string1 = date_string1.split("T")[0]  #Remove time portion if it exists
    date_string2 = date_string2.split("T")[0]  #Remove time portion if it exists

    #Convert the input date strings to datetime objects, set time to midnight
    given_date1 = datetime.strptime(date_string1, date_format).replace(hour=0, minute=0, second=0, microsecond=0)
    given_date2 = datetime.strptime(date_string2, date_format).replace(hour=0, minute=0, second=0, microsecond=0)

    #Calculate the difference in days
    delta = given_date2 - given_date1
    return delta.days

#---------------------------------------------------------Vars------------------------------------------------------------
today = str(datetime.today())  #set to today
#today = "2023-07-01"

mietables = {
    "Lautsprecher 1 (25.-/Tag)": "red",
    "Lautsprecher 2 (25.-/Tag)": "orange",
    "Subwoofer (50.-/Tag)": "turquoise",
    "Mischpult (0.-/Tag)": "pink",
    "Näbumaschine (0.-/Tag)": "blue",
    "Lichteffekte (0.-/Tag)": "green",
    "Mikrofon (0.-/Tag)": "purple",
    "Gorilla Bag (25.-/Tag)": "grey",
}
costs = [25, 25, 50, 0, 0, 0, 0, 25]

mietables_cost = []
for key, cost in zip(mietables.keys(), costs):
    mietables_cost.append((key, cost))
mietables_cost_dict = dict(mietables_cost)  #Convert mietables_cost to a dictionary for faster lookup

calendar_resources = []
for key in mietables.keys():
    calendar_resources.append({"id": key, "title": key})

modes = {
    "daygrid": "Kalender (Tag/Woche/Monat)",
    "timegrid": "Wochenansicht (Zeit)",
    "timeline": "Zeitleiste (Tag/Woche/Monat)",
    "resource-daygrid": "Equipment (Tag)",
    "resource-timegrid": "Equipment (Zeit)",
    "resource-timeline": "Equipment (Zeitleiste)",
    "list": "Liste (Monat)",
    "multimonth": "Jahr",
}
#Create a list of tuples (key, value) for the selectbox options
mode_options = [(key, value) for key, value in modes.items()]

#Selectbox displaying the values, but returning the corresponding key
#with st.sidebar:
selected_option = st.selectbox(
    "Kalender Ansicht:",
    mode_options,  #The options list contains tuples (key, value)
    format_func=lambda x: x[1],  #Display the value in the selectbox
    on_change=lambda: refreshCalendar()  #Callback function when selection changes
)

#mode = "daygrid"    #default
mode = selected_option[0]

events = []

button_options = {  #"list": "Liste",
    "buttonText": {
        "today": "Heute",
        "day": "Tag",
        "week": "Woche",
        "month": "Monat",
    },
    "buttonHints": {
        "prev": "Vorheriger",
        "next": "Nächster",
        "today": "Heute",
        "day": "Tag",
        "week": "Woche",
        "month": "Monat",
    },
}

calendar_options = {
    "editable": "true",         #false      #This determines if the events can be dragged and resized
    "navLinks": "false",
    "resources": calendar_resources,
    "selectable": "true",
    "initialDate": today,       #set todays date
    "firstDay": 1,              #start on monday
    "locale": "de",             #german/deutsch
    "navLinkHint": 'Zum $0',
    "allDayText": "Ganzer Tag",
    **button_options
}

header_toolbar = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
}

if "resource" in mode:
    if mode == "resource-daygrid":
        calendar_options = {
            **calendar_options,
            "initialView": "resourceDayGridDay",
            "resourceGroupField": "title",
        }
    elif mode == "resource-timeline":
        calendar_options = {
            **calendar_options,
            "initialView": "resourceTimelineDay",
            "resourceGroupField": "title",
        }
    elif mode == "resource-timegrid":
        calendar_options = {
            **calendar_options,
            **header_toolbar,
            "initialView": "resourceTimeGridDay",
            "resourceGroupField": "title",
        }
else:
    if mode == "daygrid":
        calendar_options = {
            **calendar_options,
            **header_toolbar,
            "initialView": "dayGridMonth",
        }
    elif mode == "timegrid":
        calendar_options = {
            **calendar_options,
            "initialView": "timeGridWeek",
        }
    elif mode == "timeline":
        calendar_options = {
            **calendar_options,
            **header_toolbar,
            "initialView": "timelineMonth",
        }
    elif mode == "list":
        calendar_options = {
            **calendar_options,
            "initialView": "listMonth",
        }
    elif mode == "multimonth":
        calendar_options = {
            **calendar_options,
            "initialView": "multiMonthYear",
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
            font-size: 1rem;
        }
        .fc-today-button, .fc-next-button, .fc-prev-button, .fc-dayGridDay-button, .fc-dayGridWeek-button, .fc-dayGridMonth-button, .fc-resourceTimelineDay-button, .fc-resourceTimelineWeek-button, .fc-resourceTimelineMonth-button {
            font-size: 12px;
        }
    """,
    key=st.session_state["Calendar"],
)

def contains_time(date_string):
    return 'T' in date_string or ':' in date_string or '+' in date_string #Check for the presence of 'T' or ':' (indicates time or timezone)

def formatDate(dateString):
    date_obj = datetime.strptime(dateString, "%Y-%m-%dT%H:%M:%S%z") if contains_time(dateString) else datetime.strptime(dateString, "%Y-%m-%d") #Convert string to datetime object

    #Format the datetime object to your desired format
    formatted_date = date_obj.strftime("%d.%m.%Y")
    formatted_date_with_time = date_obj.strftime("%H:%M")
    return formatted_date, formatted_date_with_time

@st.dialog("Event")
def showEvent():
    eventTitle = state["eventClick"]["event"]["title"]

    eventStart = state["eventClick"]["event"]["start"]
    formattedEventStart, formattedEventStartTime = formatDate(eventStart)
    startTimeFix = ''
    endTimeFix = ''

    if contains_time(eventStart): startTimeFix = f"um {formattedEventStartTime}"

    if "end" in state["eventClick"]["event"]:
        eventEnd = state["eventClick"]["event"]["end"]
        formattedEventEnd, formattedEventEndTime = formatDate(eventEnd)

        startFix = "vom"
        endFix = f"bis {formattedEventEnd}"

        if contains_time(eventEnd): endTimeFix = f"um {formattedEventEndTime}"
    else:
        startFix = "am"
        endFix = ''

    st.write(f"{eventTitle} {startFix} {formattedEventStart} {startTimeFix} {endFix} {endTimeFix}")

@st.dialog("Miet")
def addEvent(selectionMethod):
    choice = st.selectbox("Weles am bestä? (FEEDBACK BITTE)", ["multiselect", "segmented_control", "pills"])

    if choice == "multiselect": new_mietable = st.multiselect("Equipment", mietables)
    elif choice == "segmented_control": new_mietable = st.segmented_control("Equipment", mietables, selection_mode="multi")
    elif choice == "pills": new_mietable = st.pills("Equipment", mietables, selection_mode="multi")

    #st.info("Selected: " + str(new_mietable))

    #t = st.time_input("When?", "now", step=1800)               #datetime.time(8, 45)
    #st.write("Um", t)

    #Check if date in the past
    #if t before today == st.warning("Selected date is in the past")    or st.error

    if selectionMethod == "click":
        all_day = True
        start_date = state["dateClick"]["date"]
        end_date = state["dateClick"]["date"]
    elif selectionMethod == "select":
        all_day = False
        start_date = state["select"]["start"]
        end_date = state["select"]["end"]

    if (mode == "daygrid" or mode == "timeline" or mode == "resource-daygrid" or mode == "multimonth"): all_day = True

    totalcost = 0
    for m in new_mietable:
        #Access the cost from the dictionary
        totalcost += mietables_cost_dict.get(m, None)

    cost_col1, cost_col2 = st.columns(2)
    with cost_col1:
        st.info(f"Kosten/Tag = {totalcost}.-")
    with cost_col2:
        if selectionMethod == "click": st.info(f"Kosten total =  {totalcost * 1}.-")
        else: st.info(f"Kosten total =  {totalcost * days_past(start_date, end_date)}.-")

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
                "resourceId": new_mietable[i]
            }

            st.session_state["Events"].append(new_event_desc)
            #st.toast(f"{new_mietable[i]} added", icon='😍') #isnt seen because of rerun right after
            i += 1

        refreshCalendar()
        st.rerun()

if "callback" in state.keys():
#if state["callback"] != "eventsSet":
    if state["callback"] == "dateClick": addEvent("click")
    elif state["callback"] == "select": addEvent("select")
    elif state["callback"] == "eventClick": showEvent()
    elif state["callback"] == "eventChange": print("Called after an event has been modified in some way.")            #https://fullcalendar.io/docs/eventChange
    elif state["callback"] == "eventsSet": print("Called after event data is initialized OR changed in any way.")   #https://fullcalendar.io/docs/eventsSet

with st.expander("Über das Equipment", icon="🎧"): #🎵🎶🔈🔉🔊
    containerBorder = True
    containerDivider = True
    
    with st.container(border=containerBorder):
        st.subheader('Lautsprecher', divider=containerDivider) 
        st.write("""2x Turbosound IX12""")
        st.image("https://cdn.pixabay.com/photo/2019/11/13/10/17/monkey-banana-4623184_640.jpg",
            caption = "Lautsprecher caption",
            use_container_width = True,
            #width = 400,
        )

        st.write("Review")
        col1, col2, col3 = st.columns(3)
        with col1: st.feedback("stars")
        with col2: st.feedback("faces")
        with col3: st.feedback("thumbs")
    
    with st.container(border=containerBorder):
        st.subheader('Subwoofer', divider=containerDivider) 
        st.write("""Turbosound IP15B""")

    with st.container(border=containerBorder):
        st.subheader('Näbumaschine', divider=containerDivider) 
        st.write("""Näbumaschine BeamZ I1500W
- Fernbedienigskabu 3m
- Stromkabu T13 – C13             
- Fluid: BeamZ Super-Density Blue 5L
    """)

    with st.container(border=containerBorder):
        st.subheader('Lichteffekte', divider=containerDivider) 
        st.write("""Derby - Cameo Superfly XS
- Fernbedienig
- Stromkabu T13 – C13
- Bedienigsaleitig
- 2x LED Spots
- 2x Party Liechtli
    """)
        
    with st.container(border=containerBorder):
        st.subheader('Mikrofon', divider=containerDivider) 
        st.write("""Mikrofon Shure BG 1.1 mit Hülle""")
    
    with st.container(border=containerBorder):
        st.subheader('Mischpult', divider=containerDivider) 
        st.write("""Behringer Xenyx Q502USB""")

with st.expander("Über Us", icon="🌍"):
    st.write("hei mir vermiete boxe und equipment, damit o du chasch choschtegünschtig di event ufd bei steue")

with st.expander("FAQ", icon="🛠️"):
    st.write("FAQ: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

#DEBUG
with st.sidebar:
    st.divider()
    st.write("---DEBUG---")

    st.write("Calendar state:")
    st.write(state)

    st.write("Session events:")
    st.write(st.session_state["Events"])

    st.divider()
    st.write("---TEST---")
    colorpicker = st.color_picker("Pick A Color", "#00f900")
