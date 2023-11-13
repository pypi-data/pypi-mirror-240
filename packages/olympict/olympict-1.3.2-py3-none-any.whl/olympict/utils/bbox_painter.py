from typing import Callable, List, Optional, Sequence, Tuple

from olympict.files.o_image import OlympImage
from olympict.image_tools import ImTools
from olympict.types import (
    BBoxAbsolute,
    BBoxHF,
    Color,
    Img,
    LineAbsolute,
    LineRelative,
    PolygonAbsolute,
    PolygonRelative,
)


class BBoxHFPainter:
    def __init__(
        self,
        path_fn: Callable[[OlympImage], Sequence[BBoxHF]],
        font_scale: float,
    ):
        self.path_fn = path_fn
        self.font_scale = font_scale

    def draw_relatives(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for x1, y1, x2, y2, class_name, class_id, score, _ in self.path_fn(o):
            if score is None:
                score = 0
            color = ImTools.get_random_color(class_id)
            o.img = ImTools.draw_relative_bbox(
                o.img, (x1, y1, x2, y2, class_name, score), color, self.font_scale
            )
        return o

    @staticmethod
    def bbox_pipe_drawer(
        bbox_function: Optional[Callable[[OlympImage], Sequence[BBoxHF]]] = None,
        font_scale: float = ImTools.font_scale,
    ) -> Callable[[OlympImage], OlympImage]:
        if bbox_function is None:
            bbox_function = ImTools.default_bbox_path

        bp = BBoxHFPainter(bbox_function, font_scale)
        return bp.draw_relatives


class BBoxAbsolutePainter:
    def __init__(
        self,
        path_fn: Optional[Callable[[OlympImage], Sequence[BBoxAbsolute]]] = None,
        font_scale: float = 1.0,
    ):
        self.path_fn = BBoxAbsolutePainter.default_path if path_fn is None else path_fn
        self.font_scale = font_scale

    def default_path(self, o: "OlympImage") -> Sequence[BBoxAbsolute]:
        return o.metadata["pred_bboxes"]

    def draw_absolute(self, o: "OlympImage") -> "OlympImage":
        for x1, y1, x2, y2, class_name, score in self.path_fn(o):
            if score is None:
                score = 0
            class_id = abs(hash(class_name)) % (10**4)
            color = ImTools.get_random_color(class_id)
            o.img = ImTools.draw_bbox(
                o.img, (x1, y1, x2, y2, class_name, score), color, self.font_scale
            )

        return o


class PolygonRelativeOperation:
    def __init__(
        self,
        polygon_function: Callable[[OlympImage], List[Tuple[PolygonRelative, Color]]],
    ):
        self.polygon_function = polygon_function

    def draw_relative_polygons(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for polygon, color in self.polygon_function(o):
            o.img = ImTools.draw_relative_polygon(o.img, polygon, color)
        return o


class PolygonAbsoluteOperation:
    def __init__(
        self,
        polygon_function: Callable[[OlympImage], List[Tuple[PolygonAbsolute, Color]]],
    ):
        self.polygon_function = polygon_function

    def draw_absolute_polygons(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for polygon, color in self.polygon_function(o):
            o.img = ImTools.draw_polygon(o.img, polygon, color)
        return o


class LineRelativeOperation:
    def __init__(
        self,
        polygon_function: Callable[[OlympImage], List[Tuple[LineRelative, Color]]],
    ):
        self.line_function = polygon_function

    def draw_relative_lines(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for line, color in self.line_function(o):
            o.img = ImTools.draw_relative_line(o.img, line, color)

        return o


class LineAbsoluteOperation:
    def __init__(
        self,
        line_function: Callable[[OlympImage], List[Tuple[LineAbsolute, Color]]],
    ):
        self.line_function = line_function

    def draw_absolute_lines(
        self,
        o: OlympImage,
    ) -> OlympImage:
        for line, color in self.line_function(o):
            o.img = ImTools.draw_line(o.img, line, color)

        return o


class HeatmapOperation:
    def __init__(self, heatmap_function: Callable[[OlympImage], Img]):
        self.heatmap_function = heatmap_function

    def draw_heatmap(
        self,
        o: OlympImage,
    ) -> OlympImage:
        outputs = self.heatmap_function(o)
        o.img = ImTools.draw_heatmap(o.img, outputs)
        return o


class SegmentationOperation:
    def __init__(
        self, segmentation_function: Callable[[OlympImage], Img], color: Color
    ):
        self.segmentation_function = segmentation_function
        self.color = color

    def draw_segmentation(
        self,
        o: OlympImage,
    ) -> OlympImage:
        segmap = self.segmentation_function(o)
        o.img = ImTools.draw_segmentation_map(o.img, segmap, self.color)
        return o
