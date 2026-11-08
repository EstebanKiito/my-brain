#!/usr/bin/env python3
"""Genera las gráficas de seno, coseno y tangente del tema Funciones trigonométricas.

La clase las dibuja como gráficos vectoriales; se regeneran aquí calculando los
puntos en Python (stdlib) y rasterizando el SVG con ImageMagick.
"""
import hashlib
import math
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
DEST = RAIZ / "Introducción al Álgebra" / "08-Funciones trigonométricas e identidades" / "adjuntos"


def _map(x, y, xmin, xmax, ymin, ymax, W=600, H=320, M=50):
    X = M + (x - xmin) / (xmax - xmin) * (W - 2 * M)
    Y = H - M - (y - ymin) / (ymax - ymin) * (H - 2 * M)
    return X, Y


def _eje(xmin, xmax, ymin, ymax):
    x0, y0 = _map(0, 0, xmin, xmax, ymin, ymax)
    x1, _ = _map(xmax, 0, xmin, xmax, ymin, ymax)
    _, y1 = _map(0, ymax, xmin, xmax, ymin, ymax)
    _, y2 = _map(0, ymin, xmin, xmax, ymin, ymax)
    return (
        f'<line x1="{x0}" y1="{y1}" x2="{x0}" y2="{y2}" stroke="#888888" stroke-width="1.5"/>'
        f'<line x1="{M0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="#888888" stroke-width="1.5"/>'
    )


def _curva(pts, color):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="2.5"/>'


def _texto(x, y, s, size=18, fill="#1a202c", anchor="middle"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-family="Helvetica, Arial, sans-serif">{s}</text>'


M0 = 50


def seno_coseno():
    xmin, xmax, ymin, ymax = -0.6, 2 * math.pi + 0.6, -1.4, 1.4
    xs = [xmin + i * (xmax - xmin) / 600 for i in range(601)]
    seno = [_map(x, math.sin(x), xmin, xmax, ymin, ymax) for x in xs]
    cose = [_map(x, math.cos(x), xmin, xmax, ymin, ymax) for x in xs]
    cuerpo = (
        _eje(xmin, xmax, ymin, ymax)
        + _curva(cose, "#2b6cb0")
        + _curva(seno, "#c53030")
        + _texto(*_map(0.7, 1.12, xmin, xmax, ymin, ymax), "cos", 18, "#2b6cb0")
        + _texto(*_map(1.6, 1.12, xmin, xmax, ymin, ymax), "sen", 18, "#c53030")
        + _texto(*_map(math.pi, -1.22, xmin, xmax, ymin, ymax), "2π (período)", 16, "#1a202c")
    )
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="320" viewBox="0 0 600 320"><rect width="600" height="320" fill="#ffffff"/>{cuerpo}</svg>'


def tangente():
    xmin, xmax, ymin, ymax = -0.6, 2 * math.pi + 0.6, -4.2, 4.2
    cuerpo = _eje(xmin, xmax, ymin, ymax)
    for a in (math.pi / 2, 3 * math.pi / 2):
        xa, y_top = _map(a, ymax, xmin, xmax, ymin, ymax)
        xa2, y_bot = _map(a, ymin, xmin, xmax, ymin, ymax)
        cuerpo += f'<line x1="{xa}" y1="{y_top}" x2="{xa2}" y2="{y_bot}" stroke="#b7791f" stroke-width="1.5" stroke-dasharray="6 5"/>'
    xs = [xmin + i * (xmax - xmin) / 2000 for i in range(2001)]
    pts = []
    for x in xs:
        if abs(math.cos(x)) > 0.04:  # evita la asíntota
            pts.append(_map(x, math.tan(x), xmin, xmax, ymin, ymax))
        elif pts:
            pts.append(None)
    segmentos = []
    actual = []
    for p in pts:
        if p is None:
            if actual:
                segmentos.append(_curva(actual, "#b7791f"))
                actual = []
        else:
            actual.append(p)
    if actual:
        segmentos.append(_curva(actual, "#b7791f"))
    cuerpo += "".join(segmentos)
    cuerpo += _texto(*_map(math.pi / 2, ymin + 0.4, xmin, xmax, ymin, ymax), "asíntotas", 14, "#b7791f")
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="320" viewBox="0 0 600 320"><rect width="600" height="320" fill="#ffffff"/>{cuerpo}</svg>'


def guardar(nombre, svg):
    DEST.mkdir(parents=True, exist_ok=True)
    svg_tmp = DEST / (nombre + ".svg")
    png = DEST / (nombre + ".png")
    svg_tmp.write_text(svg, encoding="utf-8")
    subprocess.run(["magick", "convert", str(svg_tmp), str(png)], check=True, capture_output=True)
    svg_tmp.unlink()
    h = hashlib.sha256(png.read_bytes()).hexdigest()
    print(f"{png.relative_to(RAIZ)}  sha256={h}")


if __name__ == "__main__":
    guardar("grafico de seno y coseno", seno_coseno())
    guardar("grafico de la tangente", tangente())
