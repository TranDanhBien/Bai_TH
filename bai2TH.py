import tkinter as tk
from tkinter import messagebox
from solver import solve_equation, integrate_function
from plotter import plot_function
from content import CONTENT

def solve():
    equation = entry_equation.get()
    result = solve_equation(equation)
    result_label.config(text=f'Kết quả: {result}')

def integrate():
    function = entry_integrate.get()
    result = integrate_function(function)
    result_label.config(text=f'Tích phân: {result}')

def plot():
    function = entry_plot.get()
    plot_function(function)

def show_document(doc_key):
    content = CONTENT['docs'].get(doc_key, 'Không tìm thấy tài liệu.')
    messagebox.showinfo("Tài liệu học tập", content)

def check_quiz(quiz_key):
    answer = entry_quiz.get()
    correct_answer = CONTENT['quizzes'][quiz_key]['answer']
    if answer == correct_answer:
        messagebox.showinfo("Kết quả", "Chính xác!")
    else:
        messagebox.showinfo("Kết quả", f"Sai. Đáp án đúng là: {correct_answer}")

app = tk.Tk()
app.title('Hỗ trợ học tập môn Giải tích')

# Giải phương trình
tk.Label(app, text='Giải phương trình:').pack()
entry_equation = tk.Entry(app)
entry_equation.pack()
solve_button = tk.Button(app, text='Giải', command=solve)
solve_button.pack()

# Tính tích phân
tk.Label(app, text='Tính tích phân:').pack()
entry_integrate = tk.Entry(app)
entry_integrate.pack()
integrate_button = tk.Button(app, text='Tính', command=integrate)
integrate_button.pack()

# Vẽ đồ thị
tk.Label(app, text='Vẽ đồ thị:').pack()
entry_plot = tk.Entry(app)
entry_plot.pack()
plot_button = tk.Button(app, text='Vẽ', command=plot)
plot_button.pack()

# Hiển thị kết quả
result_label = tk.Label(app, text='')
result_label.pack()

# Tài liệu học tập
tk.Label(app, text='Tài liệu học tập:').pack()
for doc_key in CONTENT['docs'].keys():
    doc_button = tk.Button(app, text=doc_key, command=lambda key=doc_key: show_document(key))
    doc_button.pack()

# Kiểm tra kiến thức
tk.Label(app, text='Kiểm tra kiến thức:').pack()
quiz_key = list(CONTENT['quizzes'].keys())[0]  # Lấy quiz đầu tiên làm ví dụ
tk.Label(app, text=CONTENT['quizzes'][quiz_key]['question']).pack()
entry_quiz = tk.Entry(app)
entry_quiz.pack()
quiz_button = tk.Button(app, text='Kiểm tra', command=lambda key=quiz_key: check_quiz(key))
quiz_button.pack()

app.mainloop()
