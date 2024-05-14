import cv2
import os


class Tools:
    SUPPORT_CHARACTERS = " `.,-':<>;+!*/?%&98#"
    VERTICAL_STEP = 8
    HORIZONTAL_STEP = 4

    @classmethod
    def user_chose(cls):
        user_chose = input("\n Продолжить с шагом по умолчанию? д/н: ")
        if user_chose == "н":
            vertical_step = int(input("Введите шаг по вертикале: "))

            horizontal_step = int(input("Введите шаг по горизонтали: "))

            return [vertical_step, horizontal_step]

        return [cls.VERTICAL_STEP, cls.HORIZONTAL_STEP]

    @classmethod
    def convert_grayscale_to_ascii(cls, image, grayscale_image, steps: list):
        coefficient = 255 / (len(cls.SUPPORT_CHARACTERS) - 1)
        height, width, channels = image.shape

        ascii_lines = []

        for y in range(0, height - 1, steps[0]):
            ascii_line = ""
            for x in range(0, width - 1, steps[1]):
                ascii_line += cls.SUPPORT_CHARACTERS[
                    len(cls.SUPPORT_CHARACTERS) - int(grayscale_image[y, x] / coefficient) - 1]

            if len(ascii_line) != 0:
                ascii_lines.append(ascii_line)

        return ascii_lines

    @staticmethod
    def info():
        print("\nДля того-чтобы скрипт увидел файл, файл нужно добавить на тот же уровень, что и сам скрипт.")

    @staticmethod
    def image_path() -> str:
        return input("\nВведите название файла: ")

    @staticmethod
    def convert_image_to_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def read_image(image_path):
        return cv2.imread(image_path)

    @classmethod
    def check_image(cls, image_path):
        if not os.path.exists(image_path):
            print("Файл не найден.")
            return False
        return True

    @staticmethod
    def return_image_name(image_path):
        image_names, _ = os.path.splitext(image_path)
        return image_names

    @staticmethod
    def save_ascii_to_file(image_name, ascii_lines: dict):
        with open(f"{image_name}.txt", "w") as file:
            for line in ascii_lines:
                print(line)
                file.write(line + "\n")
        print(f"\nФайл сохранен: {os.getcwd()}\\{image_name}.txt")
