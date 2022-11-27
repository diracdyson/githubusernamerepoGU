from github import Github
import PySimpleGUI as sg
import pandas as pd
# let us create a gui class for this quesiton
class GUI():
    # will not initialize as normally just pass
    def __init__(self):
        pass 
    def createGUI(self):
        sg.theme('SandyBeach')     
  
    # create a layout in accordance witth pysimplegui
    # customizing the buttons
        layout = [
        [sg.Text('Please enter the GitHub Username you would like to see all public repos of')],
        [sg.Text('Github Username', size =(20, 1)), sg.InputText()],
        [sg.Text('File Location', size =(20, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]]
      # label of window
        window = sg.Window('GitHub Repository Retrieval', layout)
        event, values = window.read()
        username=values[0]
        window.close()
        g = Github()

        user = g.get_user(username) # extracted user from gui input
        repos = user.get_repos()
        ## loop through repos and append
        non_forks = []
        for repo in user.get_repos():
            if repo.fork is False:
                non_forks.append(repo.name)
        # save to csv
        repos=pd.DataFrame(non_forks)
        repos.to_csv("repos.csv")
        
GUI.createGUI([])
        
