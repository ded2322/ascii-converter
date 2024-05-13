import cv2
import os


class AsciiConverter:
    SUPPORT_CHARACTERS = " `.,-':<>;+!*/?%&98#"

    @classmethod
    def ascii_converter(cls):

        cls.info()

        image_path = cls.image_path()

        if not os.path.exists(image_path):
            return print("Изображение не найдено.\n")

        image = cv2.imread(image_path)  #

        grayscale_image = cls.convert_image_to_grayscale(image)

        user_chose = input("\n Продолжить с шагом по умолчанию? д/н: ")
        if user_chose == "н":
            vertical_step = int(input("Введите шаг по вертикале: "))

            horizontal_step = int(input("Введите шаг по горизонтали: "))

            ascii_lines = cls.convert_grayscale_to_ascii(image, grayscale_image, vertical_step, horizontal_step)
            # что это делает?
            image_names, _ = os.path.splitext(image_path)  #

            cls.save_ascii_to_file(image_names, ascii_lines)
        else:
            ascii_lines = cls.convert_grayscale_to_ascii(image, grayscale_image)
            # что это делает?
            image_names, _ = os.path.splitext(image_path)  #

            cls.save_ascii_to_file(image_names, ascii_lines)

    @staticmethod
    def info():
        print("\nДля того-чтобы скрипт увидел файл, файл нужно добавить на тот же уровень, что и сам скрипт.")

    @classmethod
    def image_path(cls) -> str:
        return input("\nВведите название изображения: ")

    @classmethod
    def convert_image_to_grayscale(cls, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @classmethod
    def convert_grayscale_to_ascii(cls, image, grayscale_image, vertical_step=8, horizontal_step=4):
        coefficient = 255 / (len(cls.SUPPORT_CHARACTERS) - 1)
        height, width, channels = image.shape

        ascii_lines = []

        for y in range(0, height - 1, vertical_step):
            ascii_line = ""
            for x in range(0, width - 1, horizontal_step):
                ascii_line += cls.SUPPORT_CHARACTERS[
                    len(cls.SUPPORT_CHARACTERS) - int(grayscale_image[y, x] / coefficient) - 1]

            if len(ascii_line) != 0:
                ascii_lines.append(ascii_line)

        return ascii_lines

    @classmethod
    def save_ascii_to_file(cls, image_name, ascii_lines: dict):
        with open(f"{image_name}.txt", "w") as file:
            for line in ascii_lines:
                print(line)
                file.write(line + "\n")
        print(f"\nФайл сохранен: {os.getcwd()}\\{image_name}.txt")
