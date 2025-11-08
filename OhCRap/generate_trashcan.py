import string
import random as rd
import numpy as np
from PIL import Image, ImageDraw, ImageFont

n_words = 10

# returns a random word of size l
def rd_word(l: int) -> str:
    return "".join(
        np.random.choice(
            list(string.ascii_letters),
            l
        )
    )

# returns n_words words including the secret
def get_words(n_words: int) -> tuple[list[str], str]:
    secret = rd_word(5) + "gWILheRm" + rd_word(3)

    words = []
    for _ in range(n_words):
        w = rd_word(len(secret))
        while w == secret:
            w = rd_word(len(secret))

        words.append(w)

    words[rd.randint(0, n_words - 1)] = secret

    return words, secret

font = ImageFont.truetype("Arial.TTF", 16)

def create_image(text: str) -> Image.Image:
    bg_color = tuple([rd.randint(150, 256) for _ in range(3)])
    tx_color = tuple([rd.randint(0, 100) for _ in range(3)])
    angle = rd.uniform(-70, 70)

    image = Image.new('RGB', (256, 256), bg_color)
    draw = ImageDraw.Draw(image)

    x = rd.randint(30, 70)
    y = rd.randint(50, 170)
    draw.text((x, y), text, font=font, fill=tx_color)

    image = image.rotate(angle, resample=Image.BICUBIC, fillcolor=bg_color)

    return image


words, secret = get_words(500)
for i, w in enumerate(words):
    img = create_image(w)
    img.save(f"corbeille/{i}.png")
