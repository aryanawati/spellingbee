import customtkinter as ctk
from app.game import generate_letters

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.lift()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))
        self.focus_force()

        self.title("spellingbee")
        self.geometry("400x600")

        self.grid_columnconfigure(0, weight=1)

        self.titleFrame = ctk.CTkFrame(self, height = 50, fg_color= "#f7da21")
        self.titleFrame.grid(row = 0, column = 0, padx = 20, pady = 10, sticky='ew')
        self.titleFrame.columnconfigure(0, weight=1)
        self.titleLabel = ctk.CTkLabel(self.titleFrame, text="Spelling Bee", font= ("NYTKarnak", 28), text_color="black")
        self.titleLabel.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.currentWord = ""
        self.letters = generate_letters()

        self.outputFrame = ctk.CTkFrame(self)
        self.outputFrame.grid(row = 1, column = 0, padx = 20, pady = 10, sticky='ew')
        self.outputFrame.columnconfigure(0, weight=1)
        self.outputLabel = ctk.CTkLabel(self.outputFrame, text = self.currentWord, font=("NYTFranklin",36), text_color="white")
        self.outputLabel.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.letterFrame = ctk.CTkFrame(
            self,
            width=300,
            height=260,
            fg_color="transparent"
        )
        self.letterFrame.grid(row=2, column=0, pady=20)

        positions = [
            (70, 30),     # top-left
            (163, 30),    # top-right

            (30, 95),     # middle-left
            (120, 95),    # center
            (200, 95),    # middle-right

            (70, 165),    # bottom-left
            (163, 165)    # bottom-right
        ]   

        def letterButtonClick(currentLetterIndex):
            self.currentWord += self.letters[currentLetterIndex].upper()
            self.outputLabel.configure(text=self.currentWord)

        def resetButtonClick():
            self.currentWord = ""
            self.outputLabel.configure(text=self.currentWord)


        for i in range(len(self.letters)):
            x, y = positions[i]
            button = ctk.CTkButton(
                self.letterFrame,
                text=f"{self.letters[i].upper()}",
                width=65,
                height=65,
                corner_radius=500,
                text_color="black",
                fg_color="gray" if i == 3 else "#f7da21",
                font=("NYTFranklin",36),
                command=lambda i=i: letterButtonClick(i)
            )

            button.place(x=x, y=y)

        self.otherFrame = ctk.CTkFrame(self, height=50)
        self.otherFrame.columnconfigure(0, weight=1)
        self.otherFrame.columnconfigure(1, weight=1)
        self.otherFrame.grid(row=3, column = 0, padx = 0, pady = 0, sticky="ew")

        self.resetButton = ctk.CTkButton(self.otherFrame, text="Reset", command=resetButtonClick)
        self.resetButton.grid(row=0, column=0, padx=10, pady=10)
        self.submitButton = ctk.CTkButton(self.otherFrame, text="Submit")
        self.submitButton.grid(row=0, column=1, padx=10, pady=10)