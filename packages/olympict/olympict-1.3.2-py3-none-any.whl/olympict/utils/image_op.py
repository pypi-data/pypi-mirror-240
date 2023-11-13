from random import randint
from typing import Any, Callable

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import Color, Img, Size


class ImageOperation:
    def __init__(self, func: Callable[[Img], Img]) -> None:
        self.func = func

    def task(self, o: OlympImage) -> OlympImage:
        o.ensure_load()
        o.img = self.func(o.img)
        return o


class CropOperation:
    def __init__(
        self,
        left: int = 0,
        top: int = 0,
        right: int = 0,
        bottom: int = 0,
        pad_color: Color = (0, 0, 0),
    ) -> None:
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.pad_color = pad_color

    def task(self, o: OlympImage) -> OlympImage:
        o.img = ImTools.crop_image(
            o.img,
            top=self.top,
            left=self.left,
            bottom=self.bottom,
            right=self.right,
            pad_color=self.pad_color,
        )
        return o


class RandomCropOperation:
    def __init__(
        self,
        output_size: Size,
    ) -> None:
        self.output_size = output_size

    def task(self, o: OlympImage) -> OlympImage:
        h, w, _ = o.img.shape
        t_w, t_h = self.output_size

        off_x: int = randint(0, w - t_w - 1)
        off_y: int = randint(0, h - t_h - 1)

        o.img = o.img[off_y : off_y + t_h, off_x : off_x + t_w, :]
        return o


class DiscarderOperation:
    def __init__(self, keep_n: int = 1, discard_n: int = 0):
        self.keep_n = keep_n
        self.discard_n = discard_n
        self.idx = 0

    def get_next(self, _: Any) -> bool:
        res = self.idx % (self.keep_n + self.discard_n) < self.keep_n

        self.idx += 1

        return res
