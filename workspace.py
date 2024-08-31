import tkinter as tk
import random
from tkinter import messagebox

word_categories = {
    'Fruits': [
        'apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple',
        'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry',
        'peach', 'lychee', 'muskmelon', 'kiwi', 'pear', 'plum', 'raspberry',
        'blueberry', 'blackberry', 'cantaloupe', 'pomegranate', 'fig', 'guava',
    ],
    'Animals': [
        'elephant', 'tiger', 'lion', 'giraffe', 'zebra', 'kangaroo', 'panda',
        'rhinoceros', 'hippopotamus', 'crocodile', 'alligator', 'chimpanzee',
        'gorilla', 'orangutan', 'leopard', 'cheetah', 'hyena', 'antelope',
        'buffalo', 'wildebeest', 'meerkat', 'gazelle', 'otter', 'seal', 'whale',
    ],
    'Countries': [
        'brazil', 'argentina', 'canada', 'mexico', 'china', 'japan', 'germany',
        'france', 'italy', 'spain', 'portugal', 'india', 'russia', 'australia',
        'newzealand', 'switzerland', 'sweden', 'norway', 'finland', 'denmark',
        'poland', 'hungary', 'czechrepublic', 'slovakia', 'romania', 'greece',
    ],
    'Colors': [
        'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'violet', 'indigo',
        'black', 'white', 'gray', 'brown', 'pink', 'peach', 'silver', 'gold',
        'maroon', 'cyan', 'magenta', 'turquoise', 'beige', 'lavender', 'teal',
        'coral', 'olive', 'khaki',
    ],
    'Shapes': [
        'circle', 'triangle', 'square', 'rectangle', 'pentagon', 'hexagon',
        'heptagon', 'octagon', 'nonagon', 'decagon', 'ellipse', 'parabola',
        'hyperbola', 'rhombus', 'trapezoid', 'quadrilateral', 'parallelogram',
        'kite', 'cylinder', 'cone', 'sphere', 'cube', 'cuboid', 'pyramid',
        'prism', 'torus', 'frustum',
    ],
    'Planets': [
        'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus',
        'neptune',
    ],
    'Languages': [
        'english', 'spanish', 'french', 'german', 'italian', 'portuguese',
        'dutch', 'russian', 'chinese', 'japanese', 'korean', 'arabic',
        'turkish', 'hindi', 'urdu', 'bengali', 'punjabi', 'marathi', 'tamil',
        'telugu', 'kannada', 'malayalam', 'gujarati', 'odia', 'sanskrit',
    ],
    'Sports': [
        'football', 'cricket', 'hockey', 'tennis', 'badminton', 'basketball',
        'volleyball', 'baseball', 'golf', 'rugby', 'soccer', 'boxing', 'fencing',
        'wrestling', 'swimming', 'cycling', 'athletics', 'gymnastics', 'karate',
        'judo', 'taekwondo', 'shooting', 'archery', 'weightlifting', 'rowing',
    ],
    'Professions': [
        'doctor', 'engineer', 'teacher', 'lawyer', 'artist', 'musician',
        'scientist', 'astronaut', 'pilot', 'soldier', 'police', 'firefighter',
        'chef', 'farmer', 'nurse', 'actor', 'actress', 'dancer', 'singer',
        'writer', 'poet', 'designer', 'architect', 'photographer', 'journalist',
    ],
    'Furniture': [
        'table', 'chair', 'sofa', 'bed', 'wardrobe', 'bookshelf', 'diningtable',
        'dressingtable', 'cabinet', 'cupboard', 'stool', 'bench', 'ottoman',
        'rockingchair', 'recliner', 'futon', 'cot', 'hammock', 'swing', 'divan',
        'chaise', 'settee', 'loveseat', 'sectional', 'beanbag', 'pouf',
    ],
    'Vegetables': [
        'potato', 'tomato', 'onion', 'garlic', 'ginger', 'carrot', 'beetroot',]
}
class Hangman_game(tk.Tk):
    def __init__(self, player_name, category):
        super().__init__()
        self.title = 'Hangman Game'
        self.geometry('800x600')
        self.player_name = player_name
        self.category = category
        self.word = random.choice(word_categories[self.category])
        self.guesses = ''
        self.chances = len(self.word) + 2
        self.correct_guesses = 0

        self.create_widgets()

    def create_widgets(self):
        welcome_message = f"Welcome {self.player_name} ! Guess the word in the category: {self.category}"
        self.label = tk.Label(self, text=welcome_message)
        self.label.pack(pady=20)

        self.word_display = tk.StringVar()
        self.word_display.set(' '.join('_' * len(self.word)))
        self.word_label = tk.Label(self, textvariable=self.word_display, font=('Arial', 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self, font=('Arial', 24))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self, text='Guess', font=('Arial', 24), command=self.guess_letter)
        self.guess_button.pack(pady=10)

        self.full_guess_button = tk.Button(self, text='Guess the whole word', font=('Arial', 24), command=self.guess_whole_word)
        self.full_guess_button.pack(pady=10)

        self.chances_left = tk.Label(self, text=f'Chances left: {self.chances}', font=('Arial', 24))
        self.chances_left.pack(pady=10)

    def guess_letter(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showerror('Error', 'Please enter a single alphabet')
            return

        if guess in self.guesses:
            messagebox.showwarning('Error', 'You have already guessed this letter')
            return

        self.guesses += guess

        if guess in self.word:
            self.word_display.set(' '.join([c if c in self.guesses else '_' for c in self.word]))
            self.guesses += guess

            if all([char in self.guesses for char in self.word]):
                messagebox.showinfo("Congratulations", "You won!")
                self.quit()
        else:
            self.chances -= 1

        self.chances_left.config(text=f"Chances left: {self.chances}")

        if self.chances <= 0:
            messagebox.showinfo("Game Over", f"You lost! The word was '{self.word}'.")
            self.quit()
    def guess_whole_word(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if guess == self.word:
            messagebox.showinfo("Congratulations", "You won!")
            self.quit()
        else:
            self.chances -= 1
            self.chances_left.config(text=f"Chances left: {self.chances}")

    def quit(self):
        self.destroy()
        start_screen = StartScreen()
        start_screen.mainloop()

    def update_word_status(self):
        display_text = ''
        for char in self.word:
            if char in self.word:
                display_text += char + ' '
            else:
                display_text += '_ '
        self.word_display.set(display_text)


class StartScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hangman Game - Start Screen")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter your name:")
        self.label.pack(pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=10)

        self.category_label = tk.Label(self, text="Select a category:")
        self.category_label.pack(pady=10)

        self.category_var = tk.StringVar(value="Fruits")
        self.category_menu = tk.OptionMenu(self, self.category_var, *word_categories.keys())
        self.category_menu.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        player_name = self.name_entry.get()
        category = self.category_var.get()

        if not player_name:
            messagebox.showerror("Input Error", "Please enter your name.")
            return

        self.destroy()
        game = Hangman_game(player_name, category)
        game.mainloop()


if __name__ == "__main__":
    start_screen = StartScreen()
    start_screen.mainloop()