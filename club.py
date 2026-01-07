from pyscript import document

def display(event=None):

    club_details = { # The Club Details can be found here!
        "robotics": {
            "name": "Robotics Club",
            "desc": "The Robotics Club focuses on programming, coding, and robotics.",
            "time": "Friday, 3:45 PM",
            "loc": "Computer Lab",
            "teacher": "Mr. Balajadia (super cool)",
            "num": "20"
        },
        "comm": {
            "name": "Communication Arts Club",
            "desc": "The Comm. Arts Club can help in bringing out your inner public speaker.",
            "time": "Monday, 4:00 PM",
            "loc": "Room 416",
            "teacher": "Mr. Alegrid",
            "num": "15"
        },
        "choir": {
            "name": "Glee Club",
            "desc": "The Glee Club can help hone your singing skills.",
            "time": "Tuesday and Thursday, 3:00 PM",
            "loc": "Music Room, 6th Floor",
            "teacher": "Ms. Aguirre",
            "num": "25"
        },
        "cocc": {
            "name": "Cadet Officer Candidate Course",
            "desc": "The Cadet Officer Candidate Course will help you develop your leadership skills.",
            "time": "Monday, 3:00 PM",
            "loc": "411, Teatro Maximo, or Quadrangle",
            "teacher": "Mr. Santos",
            "num": "10"
        },
         "sci": {
            "name": "Science Club",
            "desc": "The Science Club focuses on bringing out that inner scientist in you!",
            "time": "Friday, 4:00 PM",
            "loc": "Science Lab",
            "teacher": "Ms. Galang",
            "num": "22"
        },
         "rainbow": {
            "name": "Rainbow Catering",
            "desc": "The Rainbow Catering Club focuses on serving the younger kids in their parties.",
            "time": "Tuesday, 2:00 PM",
            "loc": "TLE Lab",
            "teacher": "Ms. Sarmiento",
            "num": "30"
        },

    }

    workingoptions = {"robotics", "comm", "choir", "cocc", "sci", "rainbow"} # This is to filter out the "Click Here" option and so it wont crash

    selection = document.querySelector("#clubSelector").value #this is the line of code that checks the selected option in the dropdown

    if selection in workingoptions: #this checks if the option that is selected is within the workingoptions, and if it does work,
        info = club_details[selection]

        details_list = [
            f"Description: {info['desc']}",
            f"Meeting Time: {info['time']}",
            f"Location: {info['loc']}",
            f"Club Moderator: {info['teacher']}",
            f"Number of Members: {info['num']}"
        ] #then the code will eventually start and run

        document.querySelector("#displayTitle").innerText = info["name"]
        document.querySelector("#displayContent").innerText = "\n".join(details_list) # This makes it so taht not everythng is in a straight line when the results pop up
        
        document.querySelector("#clubInfoDisplay").style.display = "block"