import os
from typing import Any, Callable, Generator, Tuple, cast

import cv2

from olympict.files.o_image import OlympImage
from olympict.files.o_video import OlympVid
from olympict.types import Img, ImgFormat


class PathOperation:
    def __init__(self, func: Callable[[str], str]) -> None:
        self.func = func

    def task(self, o: OlympImage) -> OlympImage:
        o.ensure_load()
        o.path = self.func(o.path)
        return o


class ExtensionOperation:
    def __init__(self, format: ImgFormat) -> None:
        self.format = format

    def change_format(self, o: OlympImage) -> OlympImage:
        o.ensure_load()
        base, _ = os.path.splitext(o.path)

        fmt = f".{self.format}" if "." != self.format[0] else self.format

        o.path = base + fmt

        return o


class FolderOperation:
    def __init__(self, folder: str) -> None:
        self.folder = folder
        os.makedirs(folder, exist_ok=True)

    def change_folder_path(self, o: OlympVid) -> OlympVid:
        o.change_folder_path(self.folder)
        return o


def filter_none_packets(p: Any) -> bool:
    return p is not None


class VideoSequencer:
    def __init__(self) -> None:
        pass

    def generator(self, o: "OlympVid") -> Generator[OlympImage, None, None]:
        print(o)
        capture: Any = cv2.VideoCapture(o.path)
        res, frame = cast(Tuple[bool, Img], capture.read())
        idx = 0
        while res:
            print(idx)
            new_path = f"{o.path}_{idx}.png"
            yield OlympImage.from_buffer(
                frame, new_path, {"video_path": o.path, "video_frame": idx}
            )
            res, frame = cast(Tuple[bool, Img], capture.read())
            idx += 1
        capture.release()
        return
