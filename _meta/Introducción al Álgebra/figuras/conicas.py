#!/usr/bin/env python3
"""Genera la figura de la parábola con foco y directriz (tema Cónicas).

La clase la dibuja como gráfico vectorial; se regenera aquí calculando los puntos
en Python (stdlib) y rasterizando el SVG con ImageMagick.
"""
import hashlib
import math
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
DEST = RAIZ / "Introducción al Álgebra" / "11-Cónicas: parábola, elipse e hipérbola" / "adjuntos"


def _map(x, y, xmin, xmax, ymin, ymax, W=440, H=340, M=60):
    X = M + (x - xmin) / (xmax - xmin) * (W - 2 * M)
    Y = H - M - (y - ymin) / (ymax - ymin) * (H - 2 * M)
    return X, Y


def _texto(x, y, s, size=17, fill="#1a202c", anchor="middle"):
    return f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-family="Helvetica, Arial, sans-serif">{s}</text>'


def parabola():
    p = 1.0
    xmin, xmax, ymin, ymax = -3.4, 3.4, -1.6, 3.0
    ox, oy = _map(0, 0, xmin, xmax, ymin, ymax)
    xr, _ = _map(xmax, 0, xmin, xmax, ymin, ymax)
    _, yt = _map(0, ymax, xmin, xmax, ymin, ymax)
    _, yb = _map(0, ymin, xmin, xmax, ymin, ymax)
    cuerpo = (
        f'<line x1="{ox:.0f}" y1="{yt:.0f}" x2="{ox:.0f}" y2="{yb:.0f}" stroke="#cccccc" stroke-width="1.5"/>'
        f'<line x1="60" y1="{oy:.0f}" x2="{xr:.0f}" y2="{oy:.0f}" stroke="#cccccc" stroke-width="1.5"/>'
    )
    # directriz x = -p
    dx, dy1 = _map(-p, ymin, xmin, xmax, ymin, ymax)
    dx2, dy2 = _map(-p, ymax, xmin, xmax, ymin, ymax)
    cuerpo += f'<line x1="{dx:.0f}" y1="{dy1:.0f}" x2="{dx2:.0f}" y2="{dy2:.0f}" stroke="#b7791f" stroke-width="2" stroke-dasharray="6 5"/>'
    cuerpo += _texto(dx, dy1 - 12, "directriz x = −p", 15, "#b7791f")
    # parábola y = x^2/(4p)
    pts = []
    for i in range(401):
        x = xmin + i * (xmax - xmin) / 400
        y = x * x / (4 * p)
        if ymin <= y <= ymax:
            pts.append(_map(x, y, xmin, xmax, ymin, ymax))
    cuerpo += '<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" fill="none" stroke="#2b6cb0" stroke-width="2.5"/>'
    # foco y vértice
    fx, fy = _map(p, 0, xmin, xmax, ymin, ymax)
    vx, vy = _map(0, 0, xmin, xmax, ymin, ymax)
    cuerpo += f'<circle cx="{fx:.0f}" cy="{fy:.0f}" r="4" fill="#c53030"/>'
    cuerpo += f'<circle cx="{vx:.0f}" cy="{vy:.0f}" r="4" fill="#1a202c"/>'
    cuerpo += _texto(fx, fy + 22, "F(p, 0)", 16, "#c53030")
    cuerpo += _texto(vx - 10, vy + 20, "V", 16)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="440" height="340" '
            f'viewBox="0 0 440 340"><rect width="440" height="340" fill="#ffffff"/>{cuerpo}</svg>')


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
    guardar("parabola con foco y directriz", parabola())
