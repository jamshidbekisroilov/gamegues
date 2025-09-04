import tkinter as tk
import random

# Tasodifiy raqam tanlash
secret_number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < secret_number:
            result_label.config(text="📉 Juda kichik!")
        elif guess > secret_number:
            result_label.config(text="📈 Juda katta!")
        else:
            result_label.config(text="🎉 Tabriklayman! To‘g‘ri topdingiz!")
    except ValueError:
        result_label.config(text="❗ Iltimos, raqam kiriting.")

# Oyna yaratish
window = tk.Tk()
window.title("🎯 Raqam Topish O‘yini")
window.geometry("750x600")
window.configure(bg="#f0f0f0")  # Fon rangini o‘zgartirish

# O‘yinga kirish matni
intro_label = tk.Label(window, text="1 dan 100 gacha bo‘lgan sonni taxmin qiling 🎯", font=("Arial", 20), bg="#f0f0f0")
intro_label.pack(pady=20)

# Kirish oynasi
entry = tk.Entry(window, font=("Arial", 25))
entry.pack(pady=10)

# Tugma
guess_button = tk.Button(window, text="✅ Taxmin qilish", font=("Arial", 20), command=check_guess)
guess_button.pack(pady=10)

# Natija
result_label = tk.Label(window, text="", font=("Arial", 25), bg="#f0f0f0")
result_label.pack(pady=10)

# Pastki banner
footer = tk.Label(
    window,
    text="IT va Buxgalteriya xizmatlari:\n https://t.me/ITvabuxgalteriyaxizmatlari\nMuallif: Isroilov Jamshidbek",
    font=("Arial", 20),
    fg="green",
    bg="#f0f0f0",
    justify="center"
)
footer.pack(side="bottom", pady=20)

window.mainloop()