#Вариант 4

#тоже пример взял из лекции на кнопках
class TextEditor: #класс текстового редактора и его возможности
    def save_file(self):
        print("Файл успешно сохранен на диск.")

    def copy_text(self):
        print("Текст скопирован.")


class SaveCommand: #два класса различных команд редактора
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.save_file()


class CopyCommand:
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.copy_text()


class Button: #сам класс кнопки, которая вызывает команду редактора
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def click(self):
        print(f"[Нажата кнопка '{self.name}']")
        self.command.execute()  