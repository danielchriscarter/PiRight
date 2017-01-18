import logic
from pygame_output import PygameOutput
#from terminal_output import TerminalOutput

quiz = logic.Quiz("./data/questions.csv")

if __name__ == "__main__":
    Window = PygameOutput(quiz, [24,25,8,7]) #Check these numbers work
    Window.Main()







#terminal = TerminalOutput(quiz)
#terminal.printAllQuestions()
#quiz.calculateTotalTime()
#print ("Total Time: " + "%.2f" % quiz.totalTime + "s")
