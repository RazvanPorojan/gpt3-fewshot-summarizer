import random

fakeSummaryData = [
    ("I have a lot of work to do but I will finish my task today.", "{a} will finish their task today. "),
    ("We have many things to discuss but {t} is the most important.", "{a} proposed {t} as the most important topic to discuss. "),
    ("I am sharing my screen. I will present {t}.", "{a} presented {t}. "),
    ("I agree to be in charge of {t}", "{a} will be in charge of {t}. "),
    ("If we still have time after completing the agenda, we should also discuss {t}", "{t} was proposed by {a} as a low priority topic. ")
]

hTemplate = "-	Highlight:<<{h}>>\n\n"

def getFakeData(attendee, topic, start_time, index): #TODO index = -1 for random
    if index == -1: index = random.randint(0, len(fakeSummaryData) - 1)
    speech, summary = fakeSummaryData[index]
    speech = speech.format(a=attendee, t=topic)
    speech = f'{attendee} // {start_time}\n{speech}\n\n'
    summary = summary.format(a=attendee, t=topic)
    return speech, summary

def generateFakeShots(meeting, shots):
    start_timeF = 0.0
    prompt = ""
    att = meeting["attendees"].copy()
    top = meeting["keywords"].copy()
    
    for _ in range(shots):
        fakeHighlight = ""
        entriesPerSection = 3
        while att and top and entriesPerSection > 0:
            a = att[random.randint(0, len(att) - 1)]
            t = top.pop(random.randint(0, len(top) - 1))
            speech, summary = getFakeData(a, t, start_timeF, -1)
            entriesPerSection -= 1
            start_timeF += 0.5
            prompt += speech
            fakeHighlight += summary
        prompt += hTemplate.format(h=fakeHighlight)
    return prompt

# Example test
if __name__ == "__main__":
    meeting = {
        "keywords": ["Migration Plan", "Risk Review", "Budget Approval"],
        "attendees": ["Alex", "Jordan", "Morgan"]
    }
    print(generateFakeShots(meeting, 2))
