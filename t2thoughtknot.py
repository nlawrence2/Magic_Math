import random

def generateDeck(dorks = 0, ouat = 0, etemple = 4, thoughtknot = 4, greensources = 16):
    deck = []
    for i in range(thoughtknot):
        deck.append("TKS")
    for i in range(etemple):
        deck.append("Temple")
    for i in range(ouat):
        deck.append("OUAT")
    for i in range(dorks):
        deck.append("Dork")
    for i in range(greensources):
        deck.append("Green")
    for i in range(60 - thoughtknot - etemple - ouat - dorks - greensources):
        deck.append("Blank")

    random.shuffle(deck)
    return deck


def turn2percentage(iterations = 100000, dorks = 0, ouat = 0, etemple = 4, thoughtknot = 4, greensources = 16):
    turn2count = 0
    for i in range(iterations):
        tutor = []
        has_TKS = False
        has_temple = False
        has_ramp = False
        deck = generateDeck(dorks, ouat, etemple, thoughtknot, greensources)
        hand = deck[0:7]
        if "TKS" in hand:
            has_TKS = True
        if "Temple" in hand:
            has_temple = True
            hand.remove("Temple")
        if "Temple" in hand or ("Dork" in hand and "Green" in hand):
            has_ramp = True
        if (has_TKS + has_temple + has_ramp) >= 2 and "OUAT" in hand:
            tutor = deck[7:12]
            if "TKS" in tutor:
                has_TKS = True
            if "Temple" in tutor:
                has_temple = True
            if "Dork" in hand and "Green" in tutor:
                has_ramp = True
            if "Dork" in tutor and "Green" in hand:
                has_ramp = True
        if (has_TKS + has_temple + has_ramp) == 3:
            turn2count += 1
    print("Turn 2 TKS percentage = ", float(turn2count) / float(iterations)*100, "%")

def turn2RampPercentage(iterations = 100000, dorks = 0, ouat = 0, etemple = 4, greensources = 16):
    turn2count = 0
    for i in range(iterations):
        tutor = []
        has_ramp = False
        deck = generateDeck(dorks, ouat, etemple, greensources)
        hand = deck[0:7]
        if "Temple" in hand:
            has_ramp = True
        if "Dork" in hand and "Green" in hand:
            has_ramp = True
        if "OUAT" in hand:
            tutor = deck[7:12]
            if "Temple" in tutor:
                has_ramp = True
            if "Dork" in hand and "Green" in tutor:
                has_ramp = True
            if "Dork" in tutor and "Green" in hand:
                has_ramp = True
        turn2count += has_ramp
    print("Turn 2 Ramp percentage = ", float(turn2count) / float(iterations)*100, "%")

print("With 7 dorks:")
print(turn2percentage(dorks=7))
print(turn2RampPercentage(dorks=7))
print("With 7 dorks and 4 OUAT:")
print(turn2percentage(dorks = 7, ouat = 4))
print(turn2RampPercentage(dorks = 7, ouat = 4))
