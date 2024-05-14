import cv2


# BIG SHIT CODE
# Примерный вид кода, если бы я писал пару лет назад
# Текущий стиль в ascii_image_converter.py
class AsciiVideoConverter:
    @classmethod
    def ascii_video_converter(cls):
        support_characters = " `.,-':<>;+!*/?%&98#"
        coef = 255 / (len(support_characters) - 1)

        file_path = input("Введите путь до видео: ")
        # Открываем видеофайл
        video = cv2.VideoCapture(file_path)

        # Проверяем, был ли успешно открыт видеофайл
        if not video.isOpened():
            print("Ошибка при открытии видеофайла")
            exit()

        while True:
            # Считываем следующий кадр из видео
            ret, frame = video.read()

            # Если кадр пустой, значит достигли конца видео
            if not ret:
                break

            # Преобразуем кадр в оттенки серого
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            height, width = gray_frame.shape

            # Обрабатываем кадр и выводим ASCII-арт в консоль
            for y in range(0, height - 1, 8):
                ascii_line = ""
                for x in range(0, width - 1, 4):
                    try:
                        ascii_line += support_characters[len(support_characters) - int(gray_frame[y, x] / coef) - 1]
                    except IndexError:
                        ascii_line += ' '
                print(ascii_line)

            # Добавляем небольшую задержку для замедления вывода
            cv2.waitKey(30)

        # Освобождаем ресурсы
        video.release()
        cv2.destroyAllWindows()
