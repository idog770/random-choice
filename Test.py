import tkinter
import random

global games
root = tkinter.Tk()
count = 0
question = tkinter.Label(root, text="what games do you want to play?")
question.pack()
games = []


def game(vname, gname):
    if vname.get() == 1:
        games.append(gname)
    else:
        games.remove(gname)


# MultiPlayer:
# Riot Games:

# League of legends
LeagueVar = tkinter.IntVar()
League = tkinter.Checkbutton(root, text="League of Legends", variable=LeagueVar,
                             command=lambda: game(LeagueVar, "League Of Legends"))
League.pack()

# Valorant
ValorantVar = tkinter.IntVar()
Valorant = tkinter.Checkbutton(root, text="Valorant", variable=ValorantVar,
                               command=lambda: game(ValorantVar, "Valorant"))
Valorant.pack()

# Legends of Runeterra
LORVar = tkinter.IntVar()
LOR = tkinter.Checkbutton(root, text="Legends of Runeterra", variable=LORVar,
                          command=lambda: game(LORVar, "Legends of Runeterra"))
LOR.pack()

# Blizzard:
# Overwatch
OwVar = tkinter.IntVar()
Ow = tkinter.Checkbutton(root, text="Overwatch", variable=OwVar, command=lambda: game(OwVar, "Overwatch"))
Ow.pack()

# Ubisoft:
# For Honor
FHVar = tkinter.IntVar()
FH = tkinter.Checkbutton(root, text="For Honor", variable=FHVar, command=lambda: game(FHVar, "For Honor"))
FH.pack()

# Rainbow
RSSVar = tkinter.IntVar()
Rainbow = tkinter.Checkbutton(root, text="Rainbow Six Siege", variable=RSSVar,
                              command=lambda: game(RSSVar, "Rainbow Six Siege"))
Rainbow.pack()

# Dead By Daylight
DBDVar = tkinter.IntVar()
DBD = tkinter.Checkbutton(root, text="Dead by Daylight", variable=DBDVar,
                          command=lambda: game(DBDVar, "Dead by Daylight"))
DBD.pack()

# Satisfactory
SfVar = tkinter.IntVar()
Sf = tkinter.Checkbutton(root, text="Satisfactory", variable=SfVar, command=lambda: game(SfVar, "Satisfactory"))
Sf.pack()

# Single Player:
# Subnautica: Below Zero
SNVar = tkinter.IntVar()
SN = tkinter.Checkbutton(root, text="Subnautica: Below Zero", variable=SNVar,
                         command=lambda: game(SNVar, "Subnautica: Below Zero"))
SN.pack()

# No Man's Sky
NMSVar = tkinter.IntVar()
NMS = tkinter.Checkbutton(root, text="No Man's Sky", variable=NMSVar, command=lambda: game(NMSVar, "No Man's Sky"))
NMS.pack()

# Control
CVar = tkinter.IntVar()
C = tkinter.Checkbutton(root, text="Control", variable=CVar, command=lambda: game(CVar, "Control"))
C.pack()

# VR
VRVar = tkinter.IntVar()
VR = tkinter.Checkbutton(root, text="VR", variable=VRVar, command=lambda: game(VRVar, "VR"))
VR.pack()

# nothing
NOTVar = tkinter.IntVar()
Nothing = tkinter.Checkbutton(root, text="Nothing", variable=NOTVar,
                              command=lambda: game(NOTVar, "don't play now\ngo watch tv or talk to the family"))
Nothing.pack()

# PS5
PS5Var = tkinter.IntVar()
PS5 = tkinter.Checkbutton(root, text="Playstation 5", variable=PS5Var, command=lambda: game(PS5Var, "Playstation 5"))
PS5.pack()

# randomization
def randomization():
    global count
    count += 1
    # Multiplayer:
    # Riot games:
    League.destroy()
    Valorant.destroy()
    LOR.destroy()
    # Blizzard:
    Ow.destroy()
    # Ubisoft:
    Rainbow.destroy()
    FH.destroy()
    DBD.destroy()
    # Single player:
    SN.destroy()
    NMS.destroy()
    Sf.destroy()
    C.destroy()
    VR.destroy()
    Nothing.destroy()
    PS5.destroy()
    choice.pack_forget()
    rgame = random.choice(games)
    question["text"] = rgame
    if rgame == "Playstation 5":
        if count == 1:
            games.clear()
            question["text"] = "what games do you want to play in ps5?"
            global GOW
            global HZD
            global RDR
            global SDM
            GOWVar = tkinter.IntVar()
            SDMVar = tkinter.IntVar()
            HZDVar = tkinter.IntVar()
            RDRVar = tkinter.IntVar()
            GOW = tkinter.Checkbutton(root, text="God Of War", variable=GOWVar,
                                      command=lambda: game(GOWVar, "God Of War"))
            HZD = tkinter.Checkbutton(root, text="Horizon Zero Dawn", variable=HZDVar,
                                      command=lambda: game(HZDVar, "Horizon Zero Dawn"))
            SDM = tkinter.Checkbutton(root, text="Spider-Ma", variable=SDMVar,
                                      command=lambda: game(SDMVar, "Spider-Man"))
            RDR = tkinter.Checkbutton(root, text="Red Dead Redemption", variable=RDRVar,
                                      command=lambda: game(RDRVar, "Red Dead Redemption 2"))
            HZD.pack()
            GOW.pack()
            SDM.pack()
            RDR.pack()
            choice.pack()
    if count == 2:
        GOW.destroy()
        HZD.destroy()
        SDM.destroy()
        RDR.destroy()
        rgame = random.choice(games)
        question["text"] = rgame


choice = tkinter.Button(root, text="randomize", command=randomization)
choice.pack()
root.mainloop()
