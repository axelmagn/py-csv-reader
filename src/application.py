import os
import csv
import tkinter as tk

import gui


class Application(tk.Frame):
    data = "";
    
    """
    The main application.

    Allows a user to specify a csv file and display it.

    """
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(fill="both")
        self.create_widgets()

        

    def create_widgets(self):
        self.file_selector = gui.FileSelector(self, command=self.select_file)
        self.status_pane = gui.StatusPane(self)
        self.status_pane["pwd"] = os.getcwd()
        self.status_pane["status"] = "Ready to open file"
        self.data_pane = gui.DataPane(self, data=[])
        self.file_selector.pack(side="top", fill="x")
        self.status_pane.pack(side="top", fill="x")
        self.data_pane.pack(fill="both")

    def removeColumn(self,index):
        for row in self.data:
            del row[index]
            
    def columnContainsFilter(self,cindex,cfilter):
        for row in range(1,len(self.data)):
            if(cfilter not in self.data[row][cindex]):
                del self.data[row];
                row += -1;
                
    def padData(self): 
        maxColumnLength = [];
        for column in range(len(self.data[0])):
             maxColumnLength.append(0);
             for row in self.data:
                if len(row[column]) > maxColumnLength[column]:
                     maxColumnLength[column] = len(row[column])
        for column in range(len(self.data[0])):
            maxColumnLength.append(0);
            for row in range(0,len(self.data)):
                self.data[row][column] = self.data[row][column].ljust(maxColumnLength[column]," ");
                
    def printDataAsHTML(self):
        print('<table style="border-spacing: 5px"><tbody>');
        print('<tr>')
        for column in self.data[0]:
            print('<th>'+column+'</th>');
        print('</tr>')
        
        for row in range(1,len(self.data)):
            print('<tr>')
            for item in self.data[row]:
                print('<td>'+item+'</td>');
            print('</tr>')    
        
        
    
    def select_file(self, file_path):
        try:
            with open(file_path, 'r') as f: 
                self.status_pane["status"] = "Reading File"
                self.status_pane["file"] = file_path
                self.status_pane.update()
                r = csv.reader(f)
                self.data = list(r)
                self.padData();
                self.data_pane.data = self.data                
                self.data_pane.refresh()
                self.status_pane["status"] = "Displaying File"
                self.status_pane.update()
        except Exception as e:
            self.status_pane["status"] = "ERROR: " + str(e)
	
	

		
 

def main():
    app = Application()
    app.master.title("CSV Reader")
    app.mainloop()
   


if __name__ == "__main__":
    main()
