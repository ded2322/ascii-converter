from core.tools import Tools


class AsciiConverter:
    @staticmethod
    def ascii_converter():

        Tools.info()

        while True:
            image_path = Tools.image_path()
            if Tools.check_image(image_path):
                break

        image = Tools.read_image(image_path)
        grayscale_image = Tools.convert_image_to_grayscale(image)

        steps = Tools.user_chose()

        ascii_lines = Tools.convert_grayscale_to_ascii(image, grayscale_image, steps)

        image_name = Tools.return_image_name(image_path)

        Tools.save_ascii_to_file(image_name, ascii_lines)
