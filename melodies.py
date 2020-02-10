import winsound
import random
import json

notes = json.loads(open('notes.JSON').read())
n = 0
count = 1 #set count to 0 for infinate music
length = random.randint(1, 12)

while n < length:
    note = random.choice(list(notes))
    dur = random.randint(1000, 5000)

    print(str(n) + ": " + note + ", "+ str(dur))
    winsound.Beep(int(notes[note]/4), dur)
    n += count