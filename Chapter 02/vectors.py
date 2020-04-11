from math import sqrt, sin, cos, atan2
from typing import List, Tuple

V2 = Tuple[float, float]


# def add(v1,v2):
#     return (v1[0] + v2[0], v1[1] + v2[1])


def subtract(v1: V2, v2: V2) -> V2:
    return v1[0] - v2[0], v1[1] - v2[1]


def add(*vectors: V2) -> V2:
    return sum(v[0] for v in vectors), sum(v[1] for v in vectors)


def length(v: V2) -> float:
    return sqrt(v[0] ** 2 + v[1] ** 2)


def distance(v1: V2, v2: V2) -> float:
    return length(subtract(v1, v2))


def perimeter(vectors: List[V2]) -> float:
    distances = (distance(vectors[i], vectors[(i + 1) % len(vectors)])
                 for i in range(0, len(vectors)))
    return sum(distances)


def scale(scalar: float, v: V2) -> V2:
    return scalar * v[0], scalar * v[1]


def to_cartesian(polar_vector: V2) -> V2:
    magnitude, angle = polar_vector[0], polar_vector[1]
    return magnitude * cos(angle), magnitude * sin(angle)


def rotate(angle: float, vectors: List[V2]) -> List[V2]:
    polars = (to_polar(v) for v in vectors)
    return [to_cartesian((l, a + angle)) for l, a in polars]


def translate(translation: V2, vectors: List[V2]) -> List[V2]:
    return [add(translation, v) for v in vectors]


def to_polar(vector: V2) -> V2:
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return length(vector), angle
