import tkinter as tk
from tkinter import messagebox, filedialog
import os
import subprocess

class CryptoGUI:
    """визуальный интерфейс для шифра Виженера и частотного анализа."""
    
    def __init__(self, root):
    
        self.root = root
        self.root.title("Окно")
        self.root.geometry("400x300")

        # Часть 1 - Шифр Виженера
        self.vigenere_frame = tk.LabelFrame(root, text="Шифрование Виженера (Часть 1)", padx=10, pady=10)
        self.vigenere_frame.pack(padx=10, pady=5, fill="x")

        tk.Button(self.vigenere_frame, text="Проверить наличие файлов", command=self.check_part1_files).pack(pady=5)
        tk.Button(self.vigenere_frame, text="Запустить шифрование Виженера", command=self.run_vigenere).pack(pady=5)

        # Часть 2 - Частотный анализ
        self.freq_frame = tk.LabelFrame(root, text="Частотный анализ (Часть 2)", padx=10, pady=10)
        self.freq_frame.pack(padx=10, pady=5, fill="x")

        tk.Button(self.freq_frame, text="Проверить наличие файлов", command=self.check_part2_files).pack(pady=5)
        tk.Button(self.freq_frame, text="Запустить частотный анализ", command=self.run_frequency).pack(pady=5)

    def check_part1_files(self):
        """Проверяет наличие необходимых файлов в Part1."""
        required_files = {
            "Part1/old_text.txt": "Исходный текстовый файл",
            "Part1/key.json": "Файл ключа",
            "Part1/main.py": "Входная точка"
        }
        missing_files = []
        
        for file_path, description in required_files.items():
            if not os.path.exists(file_path):
                missing_files.append(f"{description} ({file_path})")
        
        if missing_files:
            messagebox.showwarning("Отсутствуют файлы", "Убедитесь, что существуют файлы:\n" + "\n".join(missing_files))
        else:
            messagebox.showinfo("Проверка файлов", "Все необходимые файлы присутствуют!")

    def check_part2_files(self):
        """Проверяет наличие необходимых файлов в Part2."""
        required_files = {
            "Part2/encrypted_code.txt": "Файл зашифрованного кода",
            "Part2/alphabet.txt": "Файл с алфавитом"
        }
        missing_files = []
        
        for file_path, description in required_files.items():
            if not os.path.exists(file_path):
                missing_files.append(f"{description} ({file_path})")
        
        if missing_files:
            messagebox.showwarning("Отсутствуют файлы", "Убедитесь, что существуют файлы:\n" + "\n".join(missing_files))
        else:
            messagebox.showinfo("Проверка файлов", "Все необходимые файлы присутствуют!")

    def run_vigenere(self):
        """Запускает шифрование Виженера."""
        if not (os.path.exists("Part1/old_text.txt") and os.path.exists("Part1/key.json")):
            messagebox.showerror("Ошибка", "Отсутствуют необходимые файлы для шифрования Виженера!")
            return
        
        try:
            result = subprocess.run(
                ["python", "main.py"],
                cwd="Part1",
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                messagebox.showinfo("Успех", "Шифрование Виженера успешно завершено!\nПроверьте Part1/new_text.txt")
            else:
                messagebox.showerror("Ошибка", f"Шифрование не удалось:\n{result.stderr}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def run_frequency(self):
        """Запускает частотный анализ."""
        if not (os.path.exists("Part2/encrypted_code.txt") and os.path.exists("Part2/alphabet.txt")):
            messagebox.showerror("Ошибка", "Отсутствуют необходимые файлы для частотного анализа!")
            return
        
        try:
            result = subprocess.run(
                ["python", "part2.py"],
                cwd="Part2",
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                messagebox.showinfo("Успех", "Частотный анализ успешно завершен!\nПроверьте Part2/preliminary_code.txt для авто-дешифровки,\nи\nPart2/probabilities.txt для проверки вероятности символов.")
            else:
                messagebox.showerror("Ошибка", f"Анализ не удалось выполнить:\n{result.stderr}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

def main():
    root = tk.Tk()
    app = CryptoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()