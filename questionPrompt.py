import os

with open("edited_cards.txt") as f:
    lines = f.readlines()

    currentCard = ""

    for i in range(2289,len(lines)):
        if (i%3 == 0):
            prompt = "Question Number " +  str(int(i/3+1)) + "[[slnc 2000]]\n"
            currentCard = currentCard + prompt
        currentCard = currentCard + lines[i]
        if (i%3 == 2):
            print("Recording question #" + str(int(i/3+1)))
            os.system('say "'+currentCard+'" -o audioData/question'+str(int(i/3+1))+'.aiff')
            currentCard = ""
