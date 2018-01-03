import tkinter
import tkinter.messagebox
import global_alignment
import datetime
from tkinter import ttk

class GlobalAlignmentGUI:
    def __init__(self,master):
        self.master = master
        self.mainwindow = tkinter.Frame(self.master)
        self.mainwindow.pack(fill=tkinter.BOTH, expand=True)
        self.build_grid()
        self.create_logo()
        self.create_dna_protein_choice()
        self.create_sequence_prompt()
        self.create_score_prompt()
        self.create_filename_prompt()
        self.create_button()

    
    def build_grid(self):
        self.mainwindow.columnconfigure(0,weight=1)
        self.mainwindow.rowconfigure(0,weight=0)
        self.mainwindow.rowconfigure(1,weight=0)
        self.mainwindow.rowconfigure(2,weight=0)
        self.mainwindow.rowconfigure(3,weight=0)
        self.mainwindow.rowconfigure(4,weight=0)
        self.mainwindow.rowconfigure(5,weight=0)
        self.mainwindow.rowconfigure(6,weight=0)
        self.mainwindow.rowconfigure(7,weight=0)
    
    def create_logo(self):
        logo = tkinter.Label(self.mainwindow,text="Global Alignment - Bioinformatics Project",fg="black",font=('Helvetica',15))
        logo.grid(row=0,column=0,sticky='ew',padx=10,pady=10)
    
    def create_dna_protein_choice(self):
        self.is_protein = tkinter.StringVar(self.master)
        sequence1_frame = tkinter.Frame(self.mainwindow)
        sequence1_frame.grid(row=1,column=0,sticky='ew',padx=3,pady=3)
        sequence1_frame.columnconfigure(0,weight=0)
        sequence1_frame.columnconfigure(1,weight=1)
        self.sequence1_label = tkinter.Label(sequence1_frame,text="Protein/DNA : ",bg="black",fg="white")
        self.choice_text = tkinter.StringVar(self.master)
        self.sequence1_label.grid(row=0,column=0,sticky='nesw',padx=5,pady=2)
        self.proteinDNA_combobox = tkinter.ttk.Combobox(sequence1_frame,state='readonly')
        self.proteinDNA_combobox.grid(row=0,column=1,sticky='nesw',padx=5,pady=2)
        self.proteinDNA_combobox['values']=('DNA','Protein')
        self.proteinDNA_combobox.current(0)

    def create_sequence_prompt(self):
        self.sequence1 = tkinter.StringVar(self.master)
        self.sequence2 = tkinter.StringVar(self.master)
        sequence1_frame = tkinter.Frame(self.mainwindow)
        sequence1_frame.grid(row=2,column=0,sticky='ew',padx=3,pady=3)
        sequence1_frame.columnconfigure(0,weight=0)
        sequence1_frame.columnconfigure(1,weight=1)
        self.sequence1_label = tkinter.Label(sequence1_frame,text="Sequence 1 : ",bg="black",fg="white")
        self.sequence1_label.grid(row=0,column=0,sticky='nesw',padx=5,pady=2)
        self.sequence1_text = tkinter.Entry(sequence1_frame,width=10)
        self.sequence1_text.grid(row=0,column=1,sticky='nsew',padx=5,pady=2)
        #-------------------------Sequence 2----------------------------------
        sequence2_frame = tkinter.Frame(self.mainwindow)
        sequence2_frame.grid(row=3,column=0,sticky='ew',padx=3,pady=3)
        sequence2_frame.columnconfigure(0,weight=0)
        sequence2_frame.columnconfigure(1,weight=1)
        self.sequence2_label = tkinter.Label(sequence2_frame,text="Sequence 2 : ",bg="black",fg="white")
        self.sequence2_label.grid(row=0,column=0,sticky='nesw',padx=5,pady=2)
        self.sequence2_text = tkinter.Entry(sequence2_frame,width=10)
        self.sequence2_text.grid(row=0,column=1,sticky='nsew',padx=5,pady=2)
    
    def create_score_prompt(self):
        self.gap_opening = tkinter.StringVar(self.master)
        self.gap_extension = tkinter.StringVar(self.master)
        gap_opening_frame = tkinter.Frame(self.mainwindow)
        gap_opening_frame.grid(row=4,column=0,sticky='ew',padx=3,pady=3)
        gap_opening_frame.columnconfigure(0,weight=0)
        gap_opening_frame.columnconfigure(1,weight=1)
        self.gap_opening_label = tkinter.Label(gap_opening_frame,text="Gap Open : ",bg="black",fg="white")
        self.gap_opening_label.grid(row=0,column=0,sticky='nsew',padx=5,pady=2)
        self.gap_opening_text = tkinter.Entry(gap_opening_frame,width=10)
        self.gap_opening_text.grid(row=0,column=1,sticky='nsew',padx=5,pady=2)
        ####
        gap_extension_frame = tkinter.Frame(self.mainwindow)
        gap_extension_frame.grid(row=5,column=0,sticky='ew',padx=3,pady=3)
        gap_extension_frame.columnconfigure(0,weight=0)
        gap_extension_frame.columnconfigure(1,weight=1)
        self.gap_extension_label = tkinter.Label(gap_extension_frame,text="Gap Extension : ",bg="black",fg="white")
        self.gap_extension_label.grid(row=0,column=0,sticky='nsew',padx=5,pady=2)
        self.gap_extension_text = tkinter.Entry(gap_extension_frame,width=10)
        self.gap_extension_text.grid(row=0,column=1,sticky='nsew',padx=5,pady=2)

    def create_filename_prompt(self):
        filename_frame = tkinter.Frame(self.mainwindow)
        filename_frame.grid(row=6,column=0,sticky='ew',padx=3,pady=3)
        filename_frame.columnconfigure(0,weight=0)
        filename_frame.columnconfigure(1,weight=1)
        self.filename_label = tkinter.Label(filename_frame,text="Output File Name : ",bg="black",fg="white")
        self.filename_label.grid(row=0,column=0,sticky='nesw',padx=5,pady=2)
        self.filename_text = tkinter.Entry(filename_frame,width=10)
        self.filename_text.grid(row=0,column=1,sticky='nsew',padx=5,pady=2)
    
    def create_button(self):
        button_frame = tkinter.Frame(self.mainwindow)
        button_frame.grid(row=7,column=0,sticky='ew',padx=5,pady=3)
        button_frame.columnconfigure(0,weight=0)
        button_frame.columnconfigure(1,weight=1)
        self.run_button = tkinter.Button(button_frame,text='Run Alignment',command=self.button_onclick)
        self.run_button.grid(row=0,column=1,sticky='nsew',padx=5,pady=2)
    
    def button_onclick(self):
        if(self.proteinDNA_combobox.get()=="DNA"):
            self.is_protein = False
        else:
            self.is_protein=True
        self.sequence1 = self.sequence1_text.get()
        self.sequence2 = self.sequence2_text.get()
        self.filename = self.filename_text.get()
        self.gap_opening = self.gap_opening_text.get()
        self.gap_extension = self.gap_extension_text.get()
        alignment = global_alignment.GlobalAlignment(self.sequence1,self.sequence2,int(self.gap_opening),int(self.gap_extension),self.is_protein)
        alignment.run_alignment()
        file = open(self.filename +".txt",'w')
        file.write(str(datetime.datetime.now())+"\n")
        file.write('S1 : ' + self.sequence1+"\n")
        file.write('S2 : ' + self.sequence2+"\n")
        file.write(self.proteinDNA_combobox.get()+"\n")
        file.write("Gap Open : " + self.gap_opening+"\n")
        file.write("Gap Extension : " + self.gap_extension+"\n")
        file.write("-------------------------------------------------------------------------------\n")
        file.write("Output : \n")
        file.write("Final Score : "+ str(alignment.final_score)+"\n")
        file.write("-------------------------------------------------------------------------------\n")
        file.write("Alignments: \n")
        #tkinter.messagebox.showinfo("Completed","Alignment Done.")
        i = 0
        for align in alignment.all_alignments:
            tkinter.messagebox.showinfo("Alignment " + str(i), align[0].replace('-','- ')+"\n"+align[1].replace(' ','S')+"\n"+align[2].replace('-','- ')+"\n")
            print(align[0])
            print(align[1])
            print(align[2])
            file.write(align[0]+"\n"+align[1]+"\n"+align[2]+"\n\n")
            i+=1
        
        file.close()
        print(self.sequence1,self.sequence2,self.filename,self.is_protein)

    


root = tkinter.Tk()
root.title("Global Alignment with Affinity Gap Score")
root.resizable(False,False)
GlobalAlignmentGUI(root)
root.mainloop()