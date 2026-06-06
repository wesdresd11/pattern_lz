from builder import BrickHouseBuilder, Director
from composite import File, Folder
from command import TextEditor, CopyCommand, SaveCommand, Button
#Вариант 4


def main():
    print("Строитель строит домик:")
    builder1 = BrickHouseBuilder()
    director1 = Director(builder1)
    director1.build_minimal_house()
    print(builder1.get_result())

    builder2 = BrickHouseBuilder()
    director2 = Director(builder2)
    director2.build_super_mansion()
    print(builder2.get_result())

    print("Компоновщик файловой системы:")
    file1 = File("document.txt")
    file2 = File("photo.png")
    
    root = Folder("Главная")
    subfolder = Folder("Вложенная папка")

    subfolder.add(file2)
    root.add(file1)
    root.add(subfolder)

    root.show()

    print("Команды от кнопок:")
    my_editor = TextEditor()

    save = SaveCommand(my_editor)
    copy = CopyCommand(my_editor)

    save_button = Button("Сохранить", save)
    copy_button = Button("Скопировать", copy)

    save_button.click()
    copy_button.click()




if __name__ == "__main__":
    main()