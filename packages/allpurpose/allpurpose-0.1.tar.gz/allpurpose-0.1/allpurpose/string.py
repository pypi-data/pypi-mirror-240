import random


class String:
    @staticmethod
    def snake_to_camel(snake_str):
        words = snake_str.lower().split('_')
        return ''.join(x.capitalize() for x in words)

    @staticmethod
    def random_hex(length):
        hex_chars = '0123456789abcdef'
        return ''.join(random.choice(hex_chars) for _ in range(length))
