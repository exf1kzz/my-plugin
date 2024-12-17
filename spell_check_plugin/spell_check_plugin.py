import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from spellchecker import SpellChecker


class SpellCheckPlugin:
    def __init__(self, root):
        self.root = root
        self.root.title("Spell Checker Plugin")
        self.root.geometry("600x400")
        self.spell_checker = SpellChecker(language='en')  
        self.create_menu()
        self.create_output_area()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        plugin_menu = tk.Menu(menu_bar, tearoff=0)
        plugin_menu.add_command(label="Check Spelling in Comments", command=self.check_spelling)
        plugin_menu.add_separator()
        plugin_menu.add_command(label="Exit", command=self.root.quit)

        menu_bar.add_cascade(label="Spell Checker", menu=plugin_menu)

    def create_output_area(self):
        self.output_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.output_area.pack(expand=True, fill='both', padx=10, pady=10)
        self.output_area.insert(tk.END, "Spell Checker Results will appear here...\n")

    def check_spelling(self):
        file_path = filedialog.askopenfilename(title="Выберите Python файл", filetypes=[("Python Files", "*.py")])
        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            self.output_area.delete(1.0, tk.END)  
            errors = []
            for line_number, line in enumerate(lines, 1):
                if line.strip().startswith("#"):  
                    words = line.split()
                    comment_words = [word.strip("#.,!?():;\"'") for word in words if word.strip()]
                    misspelled = self.spell_checker.unknown(comment_words)

                    for word in misspelled:
                        error_message = f"Line {line_number}: '{word}' is misspelled.\n"
                        errors.append(error_message)

            if errors:
                self.output_area.insert(tk.END, "Spelling Errors Found:\n\n")
                for error in errors:
                    self.output_area.insert(tk.END, error)
            else:
                self.output_area.insert(tk.END, "No spelling errors found in comments.\n")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def load_plugin():
    try:
        root = tk.Tk()
        SpellCheckPlugin(root)
        root.mainloop()
    except Exception as e:
        print(f"Failed to load Spell Check Plugin: {e}")


if __name__ == "__main__":
    load_plugin()
