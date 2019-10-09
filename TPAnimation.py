#################################################
# Term Project
# Your andrewID: rmahtab
# Your section: O

# This Animation file controls all of the visual aspects of the project
# and no mathematical calculations are made here
#################################################

from tkinter import *
from TPAnalytics import *

#################################################
# NHL Playoff Bracket Predictor
#################################################

# Object-Oriented Programming with Animation
class PlayoffTeam(object):
    
    def __init__(self, name, division, seed):
        # PlayoffTeam object has three properties: name, division, and seed
        self.name = name
        self.division = division
        self.seed = seed
    
    def __repr__(self):
        return "The " + self.name + " are the " + str(self.seed) + \
        " seed in the " + self.division + " division."
    
    def __eq__(self, other):
        return isinstance(other, PlayoffTeam) and (self.name == other.name)
    
    def __hash__(self):
        return hash(self.name)
    
    def drawPath(self, canvas, width, height, color):
        # Length of round line
        rl = width//11
        # Height of round line
        rh = height//9
        
        # Draw single brackets path based on division and seed
        if self.division == "Central":
            if self.seed == 1:
                canvas.create_line(rl, rh, 2*rl, rh, fill = color)
                canvas.create_line(2*rl, rh, 2*rl, 1.5*rh, fill = color)
                canvas.create_line(2*rl, 1.5*rh, 3*rl, 1.5*rh, fill = color)
                canvas.create_line(3*rl, 1.5*rh, 3*rl, 2.5*rh, fill = color)
                canvas.create_line(3*rl, 2.5*rh, 4*rl, 2.5*rh, fill = color)
                canvas.create_line(4*rl, 2.5*rh, 4*rl, 4.5*rh, fill = color)
                canvas.create_line(4*rl, 4.5*rh, 5*rl, 4.5*rh, fill = color)
            elif self.seed == 4:
                canvas.create_line(rl, 2*rh, 2*rl, 2*rh, fill = color)
                canvas.create_line(2*rl, 2*rh, 2*rl, 1.5*rh, fill = color)
                canvas.create_line(2*rl, 1.5*rh, 3*rl, 1.5*rh, fill = color)
                canvas.create_line(3*rl, 1.5*rh, 3*rl, 2.5*rh, fill = color)
                canvas.create_line(3*rl, 2.5*rh, 4*rl, 2.5*rh, fill = color)
                canvas.create_line(4*rl, 2.5*rh, 4*rl, 4.5*rh, fill = color)
                canvas.create_line(4*rl, 4.5*rh, 5*rl, 4.5*rh, fill = color)
            elif self.seed == 2:
                canvas.create_line(rl, 3*rh, 2*rl, 3*rh, fill = color)
                canvas.create_line(2*rl, 3*rh, 2*rl, 3.5*rh, fill = color)
                canvas.create_line(2*rl, 3.5*rh, 3*rl, 3.5*rh, fill = color)
                canvas.create_line(3*rl, 3.5*rh, 3*rl, 2.5*rh, fill = color)
                canvas.create_line(3*rl, 2.5*rh, 4*rl, 2.5*rh, fill = color)
                canvas.create_line(4*rl, 2.5*rh, 4*rl, 4.5*rh, fill = color)
                canvas.create_line(4*rl, 4.5*rh, 5*rl, 4.5*rh, fill = color)
            elif self.seed == 3:
                canvas.create_line(rl, 4*rh, 2*rl, 4*rh, fill = color)
                canvas.create_line(2*rl, 4*rh, 2*rl, 3.5*rh, fill = color)
                canvas.create_line(2*rl, 3.5*rh, 3*rl, 3.5*rh, fill = color)
                canvas.create_line(3*rl, 3.5*rh, 3*rl, 2.5*rh, fill = color)
                canvas.create_line(3*rl, 2.5*rh, 4*rl, 2.5*rh, fill = color)
                canvas.create_line(4*rl, 2.5*rh, 4*rl, 4.5*rh, fill = color)
                canvas.create_line(4*rl, 4.5*rh, 5*rl, 4.5*rh, fill = color)
        elif self.division == "Pacific":
            if self.seed == 1:
                canvas.create_line(rl, 5*rh, 2*rl, 5*rh, fill = color)
                canvas.create_line(2*rl, 5*rh, 2*rl, 5.5*rh, fill = color)
                canvas.create_line(2*rl, 5.5*rh, 3*rl, 5.5*rh, fill = color)
                canvas.create_line(3*rl, 5.5*rh, 3*rl, 6.5*rh, fill = color)
                canvas.create_line(3*rl, 6.5*rh, 4*rl, 6.5*rh, fill = color)
                canvas.create_line(4*rl, 6.5*rh, 4*rl, 4.5*rh, fill = color)
                canvas.create_line(4*rl, 4.5*rh, 5*rl, 4.5*rh, fill = color)
            elif self.seed == 4:
                canvas.create_line(rl, 6*rh, 2*rl, 6*rh, fill = color)
                canvas.create_line(2*rl, 6*rh, 2*rl, 5.5*rh, fill = color)
                canvas.create_line(2*rl, 5.5*rh, 3*rl, 5.5*rh, fill = color)
                canvas.create_line(3*rl, 5.5*rh, 3*rl, 6.5*rh, fill = color)
                canvas.create_line(3*rl, 6.5*rh, 4*rl, 6.5*rh, fill = color)
                canvas.create_line(4*rl, 6.5*rh, 4*rl, 4.5*rh, fill = color)
                canvas.create_line(4*rl, 4.5*rh, 5*rl, 4.5*rh, fill = color)
            elif self.seed == 2:
                canvas.create_line(rl, 7*rh, 2*rl, 7*rh, fill = color)
                canvas.create_line(2*rl, 7*rh, 2*rl, 7.5*rh, fill = color)
                canvas.create_line(2*rl, 7.5*rh, 3*rl, 7.5*rh, fill = color)
                canvas.create_line(3*rl, 7.5*rh, 3*rl, 6.5*rh, fill = color)
                canvas.create_line(3*rl, 6.5*rh, 4*rl, 6.5*rh, fill = color)
                canvas.create_line(4*rl, 6.5*rh, 4*rl, 4.5*rh, fill = color)
                canvas.create_line(4*rl, 4.5*rh, 5*rl, 4.5*rh, fill = color)
            elif self.seed == 3:
                canvas.create_line(rl, 8*rh, 2*rl, 8*rh, fill = color)
                canvas.create_line(2*rl, 8*rh, 2*rl, 7.5*rh, fill = color)
                canvas.create_line(2*rl, 7.5*rh, 3*rl, 7.5*rh, fill = color)
                canvas.create_line(3*rl, 7.5*rh, 3*rl, 6.5*rh, fill = color)
                canvas.create_line(3*rl, 6.5*rh, 4*rl, 6.5*rh, fill = color)
                canvas.create_line(4*rl, 6.5*rh, 4*rl, 4.5*rh, fill = color)
                canvas.create_line(4*rl, 4.5*rh, 5*rl, 4.5*rh, fill = color)
        elif self.division == "Atlantic":
            if self.seed == 1:
                canvas.create_line(10*rl, rh, 9*rl, rh, fill = color)
                canvas.create_line(9*rl, rh, 9*rl, 1.5*rh, fill = color)
                canvas.create_line(9*rl, 1.5*rh, 8*rl, 1.5*rh, fill = color)
                canvas.create_line(8*rl, 1.5*rh, 8*rl, 2.5*rh, fill = color)
                canvas.create_line(8*rl, 2.5*rh, 7*rl, 2.5*rh, fill = color)
                canvas.create_line(7*rl, 2.5*rh, 7*rl, 4.5*rh, fill = color)
                canvas.create_line(7*rl, 4.5*rh, 6*rl, 4.5*rh, fill = color)
            elif self.seed == 4:
                canvas.create_line(10*rl, 2*rh, 9*rl, 2*rh, fill = color)
                canvas.create_line(9*rl, 2*rh, 9*rl, 1.5*rh, fill = color)
                canvas.create_line(9*rl, 1.5*rh, 8*rl, 1.5*rh, fill = color)
                canvas.create_line(8*rl, 1.5*rh, 8*rl, 2.5*rh, fill = color)
                canvas.create_line(8*rl, 2.5*rh, 7*rl, 2.5*rh, fill = color)
                canvas.create_line(7*rl, 2.5*rh, 7*rl, 4.5*rh, fill = color)
                canvas.create_line(7*rl, 4.5*rh, 6*rl, 4.5*rh, fill = color)
            elif self.seed == 2:
                canvas.create_line(10*rl, 3*rh, 9*rl, 3*rh, fill = color)
                canvas.create_line(9*rl, 3*rh, 9*rl, 3.5*rh, fill = color)
                canvas.create_line(9*rl, 3.5*rh, 8*rl, 3.5*rh, fill = color)
                canvas.create_line(8*rl, 3.5*rh, 8*rl, 2.5*rh, fill = color)
                canvas.create_line(8*rl, 2.5*rh, 7*rl, 2.5*rh, fill = color)
                canvas.create_line(7*rl, 2.5*rh, 7*rl, 4.5*rh, fill = color)
                canvas.create_line(7*rl, 4.5*rh, 6*rl, 4.5*rh, fill = color)
            elif self.seed == 3:
                canvas.create_line(10*rl, 4*rh, 9*rl, 4*rh, fill = color)
                canvas.create_line(9*rl, 4*rh, 9*rl, 3.5*rh, fill = color)
                canvas.create_line(9*rl, 3.5*rh, 8*rl, 3.5*rh, fill = color)
                canvas.create_line(8*rl, 3.5*rh, 8*rl, 2.5*rh, fill = color)
                canvas.create_line(8*rl, 2.5*rh, 7*rl, 2.5*rh, fill = color)
                canvas.create_line(7*rl, 2.5*rh, 7*rl, 4.5*rh, fill = color)
                canvas.create_line(7*rl, 4.5*rh, 6*rl, 4.5*rh, fill = color)
        elif self.division == "Metropolitan":
            if self.seed == 1:
                canvas.create_line(10*rl, 5*rh, 9*rl, 5*rh, fill = color)
                canvas.create_line(9*rl, 5*rh, 9*rl, 5.5*rh, fill = color)
                canvas.create_line(9*rl, 5.5*rh, 8*rl, 5.5*rh, fill = color)
                canvas.create_line(8*rl, 5.5*rh, 8*rl, 6.5*rh, fill = color)
                canvas.create_line(8*rl, 6.5*rh, 7*rl, 6.5*rh, fill = color)
                canvas.create_line(7*rl, 6.5*rh, 7*rl, 4.5*rh, fill = color)
                canvas.create_line(7*rl, 4.5*rh, 6*rl, 4.5*rh, fill = color)
            elif self.seed == 4:
                canvas.create_line(10*rl, 6*rh, 9*rl, 6*rh, fill = color)
                canvas.create_line(9*rl, 6*rh, 9*rl, 5.5*rh, fill = color)
                canvas.create_line(9*rl, 5.5*rh, 8*rl, 5.5*rh, fill = color)
                canvas.create_line(8*rl, 5.5*rh, 8*rl, 6.5*rh, fill = color)
                canvas.create_line(8*rl, 6.5*rh, 7*rl, 6.5*rh, fill = color)
                canvas.create_line(7*rl, 6.5*rh, 7*rl, 4.5*rh, fill = color)
                canvas.create_line(7*rl, 4.5*rh, 6*rl, 4.5*rh, fill = color)
            elif self.seed == 2:
                canvas.create_line(10*rl, 7*rh, 9*rl, 7*rh, fill = color)
                canvas.create_line(9*rl, 7*rh, 9*rl, 7.5*rh, fill = color)
                canvas.create_line(9*rl, 7.5*rh, 8*rl, 7.5*rh, fill = color)
                canvas.create_line(8*rl, 7.5*rh, 8*rl, 6.5*rh, fill = color)
                canvas.create_line(8*rl, 6.5*rh, 7*rl, 6.5*rh, fill = color)
                canvas.create_line(7*rl, 6.5*rh, 7*rl, 4.5*rh, fill = color)
                canvas.create_line(7*rl, 4.5*rh, 6*rl, 4.5*rh, fill = color)
            elif self.seed == 3:
                canvas.create_line(10*rl, 8*rh, 9*rl, 8*rh, fill = color)
                canvas.create_line(9*rl, 8*rh, 9*rl, 7.5*rh, fill = color)
                canvas.create_line(9*rl, 7.5*rh, 8*rl, 7.5*rh, fill = color)
                canvas.create_line(8*rl, 7.5*rh, 8*rl, 6.5*rh, fill = color)
                canvas.create_line(8*rl, 6.5*rh, 7*rl, 6.5*rh, fill = color)
                canvas.create_line(7*rl, 6.5*rh, 7*rl, 4.5*rh, fill = color)
                canvas.create_line(7*rl, 4.5*rh, 6*rl, 4.5*rh, fill = color)
    
    def highlightWinningPath(self, canvas, width, height, color):
        # Redraws bracket path in a different color
        self.drawPath(canvas, width, height, color)

# Core Animation
#################################################

def init(data):
    # List to store teams that user selects
    data.teams = []
    data.validTeams = True
    
    # Width of round line
    data.rl = data.width//11
    # Height of round line
    data.rh = data.height//9
    
    # Mouse click variables
    data.clickX = 0
    data.clickY = 0
    
    # Game mode variable
    data.mode = "home"

### Mode Dispatcher: Mode dispatcher adapted from 15-112 website (CITATION))

def keyPressed(event, data):
    if data.mode == "home":
        homeKeyPressed(event, data)
    elif data.mode == "bracket entry":
        bracketEntryKeyPressed(event, data)
    elif data.mode == "bracket":
        bracketKeyPressed(event, data)
    elif data.mode == "h2h entry":
        h2hEntryKeyPressed(event, data)
    elif data.mode == "h2h":
        h2hKeyPressed(event, data)
    elif data.mode == "error":
        errorKeyPressed(event, data)

def mousePressed(event, data):
    if data.mode == "home":
        homeMousePressed(event, data)
    elif data.mode == "bracket entry":
        bracketEntryMousePressed(event, data)
    elif data.mode == "bracket":
        bracketMousePressed(event, data)
    elif data.mode == "h2h entry":
        h2hEntryMousePressed(event, data)
    elif data.mode == "h2h":
        h2hMousePressed(event, data)
    elif data.mode == "error":
        errorMousePressed(event, data)

def redrawAll(canvas, data):
    if data.mode == "home":
        homeRedrawAll(canvas, data)
    elif data.mode == "bracket entry":
        bracketEntryRedrawAll(canvas, data)
    elif data.mode == "bracket":
        bracketRedrawAll(canvas, data)
        highlight(canvas, data)
    elif data.mode == "h2h entry":
        h2hEntryRedrawAll(canvas, data)
    elif data.mode == "h2h":
        h2hRedrawAll(canvas, data)
    elif data.mode == "error":
        errorRedrawAll(canvas, data)

### Home Page

def homeKeyPressed(event, data):
    # Movement between pages
    if event.keysym == "p":
        data.mode = "bracket entry"
    elif event.keysym == "h":
        data.mode = "h2h entry"

def homeMousePressed(event, data):
    pass

def drawHomeTitle(canvas, data):
    # Draw title
    titleHeight = 150
    
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, titleHeight, \
    text = "NHL Playoff Predictor", fill = "red", font = "Arial 60")

def drawHomeButtons(canvas, data):
    # Draw buttons
    btn1Height, btn2Height = 350, 500
    btnHeight, btnWidth = 48, 144
    offset = 4

    # Button 1
    canvas.create_rectangle(data.width//2-btnWidth//2-offset, \
    btn1Height-btnHeight//2-offset, data.width//2+btnWidth//2+offset, \
    btn1Height+btnHeight//2+offset, fill = "white")
    canvas.create_rectangle(data.width//2-btnWidth//2, btn1Height-btnHeight//2,\
    data.width//2+btnWidth//2, btn1Height+btnHeight//2, fill = "gray")
    canvas.create_text(data.width//2, btn1Height, text = "Playoff Predictor", \
    fill = "white")
    # Button 2
    canvas.create_rectangle(data.width//2-btnWidth//2-offset, \
    btn2Height-btnHeight//2-offset, data.width//2+btnWidth//2+offset, \
    btn2Height+btnHeight//2+offset, fill = "white")
    canvas.create_rectangle(data.width//2-btnWidth//2, btn2Height-btnHeight//2,\
    data.width//2+btnWidth//2, btn2Height+btnHeight//2, fill = "gray")
    canvas.create_text(data.width//2, btn2Height, text = "Head-to-Head", \
    fill = "white")

def drawHomeText(canvas, data):
    # Draw button description text
    txt1Height = 400
    txt2Height = 550
    
    canvas.create_text(data.width//2, txt1Height, text = "(Press 'p')", \
    fill = "white")
    canvas.create_text(data.width//2, txt2Height, text = "(Press 'h')", \
    fill = "white")

def homeRedrawAll(canvas, data):
    # Title
    drawHomeTitle(canvas, data)
    # Buttons
    drawHomeButtons(canvas, data)    
    # Text
    drawHomeText(canvas, data)
    
### Bracket Entry Page

def drawTeamGrid(canvas, data):
    # Grid dimension variables
    divNameHeight = 15
    gridTop = 300
    gridLeft = 275
    cellWidth = 160
    cellHeight = 40
    # Write division names
    for div in TEAMSDICT:
        canvas.create_text(gridLeft + (div + 0.5)*cellWidth, \
        gridTop - divNameHeight, text = TEAMSDICT[div][0], fill = "white")
    # Draw grid and write team names
    for div in TEAMSDICT:
        for team in range(1, len(TEAMSDICT[div])):
            canvas.create_rectangle(gridLeft + div*cellWidth, \
            gridTop + (team - 1)*cellHeight, gridLeft + (div + 1)*cellWidth, \
            gridTop + (team)*cellHeight, outline = "white")
            canvas.create_text(gridLeft + (div + 0.5)*cellWidth, \
            gridTop + (team - 0.5)*cellHeight, text = TEAMSDICT[div][team], \
            fill = "white")

def checkBracketValidity(data):
    # Returns false if list of teams is not of length 16 or if
    # teams were entered in incorrect division order
    if len(data.teams) != 16:
        data.validTeams = False
    for t in range(len(data.teams)):
        if t//4 == 0:
            if data.teams[t].division != "Central":
                data.validTeams = False
        elif t//4 == 1:
            if data.teams[t].division != "Pacific":
                data.validTeams = False
        elif t//4 == 2:
            if data.teams[t].division != "Atlantic":
                data.validTeams = False
        elif t//4 == 3:
            if data.teams[t].division != "Metropolitan":
                data.validTeams = False    

def reorderTeams(data):
    # Reorders teams in seed formation (1, 4, 2, 3, etc.)
    for i in range(15, 0, -4):
        data.teams.insert(i - 2, data.teams.pop(i))
    for t in range(16):
        if t % 4 == 0:
            data.teams[t].seed = 1
        elif t % 4 == 1:
            data.teams[t].seed = 4
        elif t % 4 == 2:
            data.teams[t].seed = 2
        elif t % 4 == 3:
            data.teams[t].seed = 3

def bracketEntryKeyPressed(event, data):
    # Movement between pages
    if event.keysym == "b":
        init(data)
    elif event.keysym == "c":
        checkBracketValidity(data)
        if data.validTeams == True:
            reorderTeams(data)
            # Create a new list of team names instead of PlayoffTeam objects
            # to pass into getOverallWinner()
            data.newList = []
            for t in data.teams:
                data.newList.append(t.name)
            # Predict winner and generate percentages
            data.predictedWinner = simulateOverallWinner(data.newList, 10000)
            data.percentages = getPercentages(data.newList)
            data.mode = "bracket"
        else:
            data.mode = "error"

def bracketEntryMousePressed(event, data):
    data.clickX = event.x
    data.clickY = event.y

def addTeam(canvas, data):
    # Grid dimension variables
    gridTop = 300
    gridLeft = 275
    cellWidth = 160
    cellHeight = 40
    
    # Adds user-selected team to data.teams
    for div in TEAMSDICT:
        for team in range(1, len(TEAMSDICT[div])):
            if data.clickX > gridLeft + div*cellWidth and \
            data.clickX < gridLeft + (div + 1)*cellWidth and \
            data.clickY > gridTop + (team - 1)*cellHeight and \
            data.clickY < gridTop + team*cellHeight:
                canvas.create_text(gridLeft + (div + 0.5)*cellWidth, \
                gridTop + (team - 0.5)*cellHeight, \
                text = TEAMSDICT[div][team], fill = "blue")
                data.teams.append(PlayoffTeam(TEAMSDICT[div][team], \
                TEAMSDICT[div][0], div + 1))

def bracketEntryRedrawAll(canvas, data):
    # Text location variables
    infoHeight = 40
    titleHeight = 120
    instrHeight1 = 200
    instrHeight2 = 230
    continueHeight = 700
    
    # Draw text
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, infoHeight, \
    text = "(Press 'b' to go back to Home Page)", fill = "white", \
    font = "Arial 15")
    canvas.create_text(data.width//2, titleHeight, \
    text = "Select 16 Playoff Teams by Division", fill = "red", \
    font = "Arial 40")
    canvas.create_text(data.width//2, instrHeight1, \
    text = "Click 4 Central teams, 4 Pacific teams, 4 Atlantic teams", \
    fill = "white", font = "Arial 25")
    canvas.create_text(data.width//2, instrHeight2, \
    text = "and finally 4 Metropolitan teams:", \
    fill = "white", font = "Arial 25")
    canvas.create_text(data.width//2, continueHeight, \
    text = "(Press 'c' to continue)", fill = "white", \
    font = "Arial 20")
    
    # Draw team grid
    drawTeamGrid(canvas, data)
    addTeam(canvas, data)

### Bracket Page

def drawWesternSeedNumbers(canvas, data):
    # Draws seed numbers for Western conference
    margin = 8
    canvas.create_text(data.rl - margin, data.rh, text = "1", \
    font = "Arial 10")
    canvas.create_text(data.rl - margin, 2*data.rh, text = "4", \
    font = "Arial 10")
    canvas.create_text(data.rl - margin, 3*data.rh, text = "2", \
    font = "Arial 10")
    canvas.create_text(data.rl - margin, 4*data.rh, text = "3", \
    font = "Arial 10")
    canvas.create_text(data.rl - margin, 5*data.rh, text = "1", \
    font = "Arial 10")
    canvas.create_text(data.rl - margin, 6*data.rh, text = "4", \
    font = "Arial 10")
    canvas.create_text(data.rl - margin, 7*data.rh, text = "2", \
    font = "Arial 10")
    canvas.create_text(data.rl - margin, 8*data.rh, text = "3", \
    font = "Arial 10")

def drawEasternSeedNumbers(canvas, data):
    # Draws seed numbers for Eastern conference
    margin = 8
    canvas.create_text(10*data.rl + margin, data.rh, text = "1", \
    font = "Arial 10")
    canvas.create_text(10*data.rl + margin, 2*data.rh, text = "4", \
    font = "Arial 10")
    canvas.create_text(10*data.rl + margin, 3*data.rh, text = "2", \
    font = "Arial 10")
    canvas.create_text(10*data.rl + margin, 4*data.rh, text = "3", \
    font = "Arial 10")
    canvas.create_text(10*data.rl + margin, 5*data.rh, text = "1", \
    font = "Arial 10")
    canvas.create_text(10*data.rl + margin, 6*data.rh, text = "4", \
    font = "Arial 10")
    canvas.create_text(10*data.rl + margin, 7*data.rh, text = "2", \
    font = "Arial 10")
    canvas.create_text(10*data.rl + margin, 8*data.rh, text = "3", \
    font = "Arial 10")

def writeDivisionNames(canvas, data):
    width1 = 2.5*data.rl
    width2 = 8.5*data.rl
    height1 = 2.5*data.rh
    height2 = 6.5*data.rh
    
    canvas.create_text(width1, height1, text = "Central", font = "Arial 15")
    canvas.create_text(width1, height2, text = "Pacific", font = "Arial 15")
    canvas.create_text(width2, height1, text = "Atlantic", font = "Arial 15")
    canvas.create_text(width2, height2, text = "Metropolitan", font = "Arial 15")

def drawBracketAccessories(canvas, data):
    titleHeight = 120
    # Draw title
    canvas.create_text(data.width//2, titleHeight, \
    text = "NHL Playoff Predictor", fill = "red", font = "Arial 30 bold")
    # Draw winner box
    margin = 32
    canvas.create_rectangle(5*data.rl, 4.25*data.rh, 6*data.rl, 4.75*data.rh)
    canvas.create_text(data.width//2, data.height//2-margin, \
    text = "Champion", font = "Arial 14")
    infoHeight = 15
    # Draw back button
    canvas.create_text(data.width//2, infoHeight, \
    text = "(Press 'b' to go back to Home Page)", fill = "black", \
    font = "Arial 15")
    # Draw seed numbers and division names
    drawWesternSeedNumbers(canvas, data)
    drawEasternSeedNumbers(canvas, data)
    writeDivisionNames(canvas, data)

def writeTeamNames(canvas, data):    
    nameMargin = 5
    
    # Write Western conference team names on bracket
    for t in range(len(data.teams)//2):
        canvas.create_text(1.5*data.rl, (t+1)*data.rh-nameMargin, \
        text = data.teams[t].name, font = "Arial 10")
    
    # Write Eastern conference team names on bracket
    for t in range(len(data.teams)//2):
        canvas.create_text(9.5*data.rl, (t+1)*data.rh-nameMargin, \
        text = data.teams[t+len(data.teams)//2].name, font = "Arial 10")

def writePercentages(canvas, data, team):
    # Write percentages of team advancing to each round when clicked
    canvas.create_text(2.5*data.rl, 8.5*data.rh, text = "Quarter-Finals: " + \
    str(data.percentages[team][0]) + "%")
    canvas.create_text(4.5*data.rl, 8.5*data.rh, text = "Semi-Finals: " + \
    str(data.percentages[team][1]) + "%")
    canvas.create_text(6.5*data.rl, 8.5*data.rh, text = "Finals: " + \
    str(data.percentages[team][2]) + "%")
    canvas.create_text(8.5*data.rl, 8.5*data.rh, text = "Win Chamionship: " + \
    str(data.percentages[team][3]) + "%")

def highlight(canvas, data):
    ceil = 10
    
    # Highlight team path in divisional color and write its percentages
    for t in range(len(data.teams)//2):
        if data.clickX >= data.rl and data.clickX <= 2*data.rl and \
        data.clickY <= (t+1)*data.rh and data.clickY >= (t+1)*data.rh-ceil:
            data.teams[t].highlightWinningPath(canvas, data.width, \
            data.height, "blue")
            writePercentages(canvas, data, data.teams[t].name)
            canvas.create_text(data.width//2, data.height//2 - ceil//2, \
            text = data.teams[t].name, fill = "blue", font = "Arial 10")
    
    for t in range(len(data.teams)//2):
        if data.clickX >= 9*data.rl and data.clickX <= 10*data.rl and \
        data.clickY <= (t+1)*data.rh and data.clickY >= (t+1)*data.rh-ceil:
            data.teams[t+len(data.teams)//2].highlightWinningPath(canvas, \
            data.width, data.height, "red")
            writePercentages(canvas, data, data.teams[t+len(data.teams)//2].name)
            canvas.create_text(data.width//2, data.height//2 - ceil//2, \
            text = data.teams[t+len(data.teams)//2].name, fill = "red", \
            font = "Arial 10")

def bracketKeyPressed(event, data):
    # Movement between pages
    if event.keysym == "b":
        init(data)

def bracketMousePressed(event, data):
    data.clickX = event.x
    data.clickY = event.y

def bracketRedrawAll(canvas, data):
    # Draw bracket with accessories and team names
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "LightBlue1")
    drawBracketAccessories(canvas, data)
    writeTeamNames(canvas, data)
    for team in data.teams:
        team.drawPath(canvas, data.width, data.height, "black")
    
    # Write predicted winner
    canvas.create_text(data.width//2, 7*data.rh, \
    text = "Predicted Winner: " + data.predictedWinner[0], font = "Arial 20", \
    fill = "gold3")

### Head-2-Head Entry Page

def checkH2HValidity(data):
    # Returns false if length of list of teams is anything but two
    if len(data.teams) != 2:
        data.validTeams = False

def h2hEntryKeyPressed(event, data):
    # Movement between pages
    if event.keysym == "b":
        init(data)
    elif event.keysym == "c":
        checkH2HValidity(data)
        # If entry is valid, simulate odds and predict score
        if data.validTeams == True:
            data.simOdds = simulatedOdds(data.teams[0].name, \
            data.teams[1].name, 10000)
            data.predScore = predictScore(data.teams[0].name, \
            data.teams[1].name)
            data.mode = "h2h"
        else:
            data.mode = "error"
            data.teams = []

def h2hEntryMousePressed(event, data):
    data.clickX = event.x
    data.clickY = event.y

def h2hEntryRedrawAll(canvas, data):
    # Text location variables
    infoHeight = 40
    titleHeight = 100
    instrHeight = 200
    continueHeight = 700
    
    # Draw text
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, infoHeight, \
    text = "(Press 'b' to go back to Home Page)", fill = "white", \
    font = "Arial 15")
    canvas.create_text(data.width//2, titleHeight, \
    text = "Select 2 Teams", fill = "red", \
    font = "Arial 40")
    canvas.create_text(data.width//2, instrHeight, \
    text = "You may select 2 teams from any division:", fill = "white", \
    font = "Arial 25")
    canvas.create_text(data.width//2, continueHeight, \
    text = "(Press 'c' to continue)", fill = "white", \
    font = "Arial 20")
    
    # Draw team grid
    drawTeamGrid(canvas, data)
    addTeam(canvas, data)

### Head-2-Head Page

def h2hKeyPressed(event, data):
    # Movement between pages
    if event.keysym == "b":
        init(data)
    elif event.keysym == "c":
            # Recalculates stat based odds and predicted score
            data.simOdds = simulatedOdds(data.teams[0].name, \
            data.teams[1].name, 1000)
            data.predScore = predictScore(data.teams[0].name, \
            data.teams[1].name)
    elif event.keysym == "h":
        data.teams = []
        data.clickX = 0
        data.clickY = 0
        data.mode = "h2h entry"

def h2hMousePressed(event, data):
    pass

def writeGameOdds(canvas, data):
    # Text location variables
    krachOddsHeight = 300
    monteCarloOddsHeight = 350
    scoreHeight = 400
    
    # Draw text
    canvas.create_text(data.width//2, krachOddsHeight, text = \
    "KRACH System Odds - " + str(getKrachOdds(data.teams[0].name, data.teams[1].name)[0]) \
    + " : " + str(getKrachOdds(data.teams[0].name, data.teams[1].name)[1]) \
    + " (based on win/loss record)", fill = "gray80", font = "Arial 25")
    canvas.create_text(data.width//2, monteCarloOddsHeight, text = \
    "Season Statistics Based Odds - " + \
    str(data.simOdds[0]) + " : " + str(data.simOdds[1]) + \
    " (based on goals per game and goals against)", fill = "gray80", \
    font = "Arial 25")
    canvas.create_text(data.width//2, scoreHeight, \
    text = "Predicted Score: " + data.predScore, fill = "gray80", \
    font = "Arial 25")

def h2hRedrawAll(canvas, data):
    # Text location variables
    infoHeight = 40
    titleHeight = 100
    teamNameHeight = 200
    resimulateHeight = 450
    reenterHeight = 700
    
    # Draw text
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, infoHeight, \
    text = "(Press 'b' to go back to Home Page)", fill = "white", \
    font = "Arial 15")
    canvas.create_text(data.width//2, titleHeight, \
    text = "Head-to-Head Prediction", fill = "red", \
    font = "Arial 40")
    canvas.create_text(data.width//2, teamNameHeight, \
    text = data.teams[0].name + " vs " + data.teams[1].name, fill = "gray80", \
    font = "Arial 30")
    canvas.create_text(data.width//2, resimulateHeight, \
    text = "(Press 'c' to resimulate stat based odds via Monte Carlo method)", \
    fill = "red", font = "Arial 20")
    canvas.create_text(data.width//2, reenterHeight, \
    text = "(Press 'h' to enter 2 new teams)", fill = "white", \
    font = "Arial 20")
    
    # Write odds
    writeGameOdds(canvas, data)

### Error Page

def errorKeyPressed(event, data):
    # Movement between pages
    if event.keysym == "b":
        init(data)

def errorMousePressed(event, data):
    pass

def errorRedrawAll(canvas, data):
    # Text location variables
    infoHeight = 40
    errorHeight = data.height//2 - 50
    
    # Draw text
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    canvas.create_text(data.width//2, infoHeight, \
    text = "(Press 'b' to go back to Home Page)", fill = "white", \
    font = "Arial 15")
    canvas.create_text(data.width//2, errorHeight, \
    text = "Incorrect entry, try again...", fill = "white", \
    font = "Arial 35")    

### Run Function: Run function from 15-112 website (CITATION)

def runBracket(width=1200, height=800):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    
runBracket()