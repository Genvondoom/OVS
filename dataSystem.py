from datetime import *

# username, info2, mail, password, level,status



def createUser(info):
    # work on this

    username, matricNo, mail, password, level, status = info
    temp = [matricNo, username, mail, password, level, status]
    return temp



def registerForElection(userid, matricNo, electionId, status):
    # to register users for election
    # user id or matric no, election id, status

    pass


def verifyCandidates():
    # candidates verification
    pass


def verifyVoters():
    # to verify voters
    pass


def addAdmin():
    # to add new administrator
    pass


def removeUserFromElection():
    pass


def removeCandidate():
    pass


def electionResult():
    pass


def getElectionWinners():
    pass


elections = []


def getFirstLetters(string):
    word = string.split()

    result = ""
    temp = []
    for x in word:
        temp.append(x[0])

    return result.join(temp).upper()


def createElection(name, category, sch_dept, startingDate, startingtime, duration):
    # category = dept, faculty, school, busa
    # date format= dd/mm/yy
    # time format = hh/mm
    # duration format hour:min
    time = datetime.strptime(startingtime, "%I:%M%p")
    date = datetime.strptime(startingDate, "%d/%m/%Y").strftime("%d/%m/%Y")
    limit = timedelta(hours=duration)
    # wok on duraton hours and miniutes
    stopTime = time + limit
    stopTime = stopTime.strftime('%I:%M%p')
    status = "active"
    temp = [name, category, sch_dept, date, startingtime, duration, stopTime, status]
    date = datetime.now().strftime("%m%d%y")
    no = 0
    electionId = f"{getFirstLetters(sch_dept)}{date}{no}"
    temp.insert(0, electionId)
    return temp
