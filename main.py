import tkinter as tk
from tkinter import messagebox
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def estimate_nutrition():
    food = food_entry.get()
    quantity = quantity_entry.get()

    if not food or not quantity:
        messagebox.showwarning("Input Required", "Please enter both food and quantity.")
        return

    prompt = f"Estimate the nutritional content (especially protein and kcal) for this: {quantity} of {food}. Format clearly."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content.strip()
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("NutriGPT - Nutrition Estimator (Demo Only)")
root.geometry("500x400")

tk.Label(root, text="Food or Meal:").pack()
food_entry = tk.Entry(root, width=50)
food_entry.pack()

tk.Label(root, text="Quantity / Portion Size:").pack()
quantity_entry = tk.Entry(root, width=50)
quantity_entry.pack()

tk.Button(root, text="Estimate Nutrition", command=estimate_nutrition).pack(pady=10)

output_box = tk.Text(root, height=15, width=60)
output_box.pack()

root.mainloop()
