from core.ascii_image_converter import AsciiConverter
from core.ascii_video_converter import AsciiVideoConverter
from core.menu_help import MenuHelp

class Menu:
    """
    Класс Menu представляет меню выбора пользователя.
    """

    @classmethod
    def user_choice(cls):
        """
        Метод user_choice() обрабатывает выбор пользователя из меню.
        Используется бесконечный цикл для повторного отображения меню после каждого выбора.
        """
        while True:
            user_input = int(
                input(
                    "Выберете подходящий режим:\n"
                    "1. Конвертация изображения в ascii-рисунок\n"
                    "2. Конвертация видео в ascii-рисунок (в консоли)\n"
                    "3. Меню помощь\n"
                    "4. Выйти из программы\n"
                    "Ваш выбор: "
                )
            )

            match user_input:
                case 1:
                    AsciiConverter.ascii_converter()
                case 2:
                    AsciiVideoConverter.ascii_video_converter()
                case 3:
                    MenuHelp.menu_help()
                case 4:
                    break
