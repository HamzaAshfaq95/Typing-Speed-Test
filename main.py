from tkinter import *
COUNT = 5

# Creation of GUI
window = Tk()
# Title of GUI
window.title("Typing Test")
# Minimum size of GUI
window.minsize(width=500, height=500)
# Padding
window.config(padx=20, pady=20)

# Timer Function
def timer_with_compare(count):
    global words
    global characters
    characters = ""
    words_list = []
    window.after(1000)
    time_entry.delete(0, END)
    time_entry.insert(END, count)
    if count > 0:
        window.after(1000, timer_with_compare, count - 1)
    elif count == 0:
        text_output.config(state="disabled")
        for word1, word2 in zip(text_input.get("1.0", END).split(" "), text_output.get("1.0", END).split(" ")):
            if word1 == word2:
                words_list.append(word1)
        words = len(words_list)

        for character1, character2 in zip(text_input.get("1.0", END), text_output.get("1.0", END)):
            if character1 == character2:
                characters += character1
        characters = characters.replace(" ", "")

        wpm_entry.insert(END, words)
        wpm_entry.config(state="disabled")
        cpm_entry.insert(END, len(characters))
        cpm_entry.config(state="disabled")
        time_entry.config(state="disabled")
# Putting the above function in another function to prohibit starting timer when it already started
def count_down():
    if len(time_entry.get()) == 0:
        timer_with_compare(COUNT)

# Reset Function
def reset_app():
    text_input.config(state="normal")
    text_input.delete("1.0", END)
    text_output.config(state="normal")
    text_output.delete("1.0", END)
    time_entry.config(state="normal")
    time_entry.delete(0, END)
    cpm_entry.config(state="normal")
    cpm_entry.delete(0, END)
    wpm_entry.config(state="normal")
    wpm_entry.delete(0, END)

# Input Text Function
def input_text():
    text = "the quick brown fox jumps over the lazy dog while twelve vibrant zebras swiftly gallop across the quiet meadow silent winds carry whispers of ancient trees bending lightly with the rhythm of natures song underneath a golden sun shimmering streams reflect the endless sky as butterflies flutter between fragrant flowers a curious kitten explores the garden chasing after its own shadow while birds chirp in the distance announcing the arrival of a new day time seems to stand still in this serene moment where every sound is a soft reminder of the beauty that surrounds us"
    if len(text_input.get("1.0", END)) == 1:
        text_input.insert(END, text)
        text_input.config(state="disabled")
    else:
        text_input.insert(END, "")

# Main Label
main_label = Label(text="TYPING SPEED TEST", font=("courier", 40, "bold"))
main_label.grid(row=0, column=0, columnspan=8, pady=20)

# CPM Label & Entry
cpm_label = Label(text="Corrected CPM:", font=("courier", 14, "normal"))
# sticky="e" is added to align the labels to the right edge so they appear closer to the corresponding entry fields.
cpm_label.grid(row=1, column=0, padx=0, pady=0, sticky="e")
cpm_entry = Entry(width=10)
cpm_entry.grid(row=1, column=1, padx=0, pady=0)

# WPM Label & Entry
wpm_label = Label(text="WPM:", font=("courier", 14, "normal"))
wpm_label.grid(row=1, column=2, padx=0, pady=0, sticky="e")
wpm_entry = Entry(width=10)
wpm_entry.grid(row=1, column=3, padx=0, pady=0)

# Time Left Label & Entry
time_label = Label(text="Time Left:", font=("courier", 14, "normal"))
time_label.grid(row=1, column=4, padx=0, pady=0, sticky="e")
time_entry = Entry(width=10)
time_entry.grid(row=1, column=5, padx=0, pady=0)

# Start Button
start_button = Button(text="Start", command=lambda: [input_text(), count_down()])
start_button.grid(row=1, column=6, padx=20)

# Reset Button
reset_button = Button(text="Reset", command=reset_app)
reset_button.grid(row=1, column=7)

# Text Input
text_input = Text(width=110, height=6, font=("courier", 14, "normal"))
text_input.grid(row=2, column=0, columnspan=8, pady=20)

# Text Output
text_output = Text(width=110, height=6, font=("courier", 14, "normal"))
text_output.focus()
text_output.grid(row=3, column=0, columnspan=8)

window.mainloop()