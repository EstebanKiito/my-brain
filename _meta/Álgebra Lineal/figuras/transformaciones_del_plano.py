import sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
OUT = sys.argv[1]
SQ = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]]).T
F = np.array([[.3,.15],[.3,.85],[.75,.85],[.75,.72],[.43,.72],[.43,.56],[.68,.56],[.68,.43],[.43,.43],[.43,.15],[.3,.15]]).T
AZ, RO, VE, GR = "#2b6cb0", "#c53030", "#2f855a", "#a0aec0"

def panel(ax, A, titulo, lim=2.7):
    A = np.array(A, float)
    ax.fill(*SQ, color=GR, alpha=.15); ax.plot(*SQ, color=GR, lw=1, ls="--")
    ax.fill(*F, color=GR, alpha=.35)
    S2, F2 = A @ SQ, A @ F
    ax.fill(*S2, color=AZ, alpha=.18); ax.plot(*S2, color=AZ, lw=1.6)
    ax.fill(*F2, color=AZ, alpha=.75)
    for v, c in ((A[:, 0], RO), (A[:, 1], VE)):
        ax.annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=2))
    ax.axhline(0, color="k", lw=.6); ax.axvline(0, color="k", lw=.6)
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(titulo, fontsize=10)
    m = A.round(2)
    fmt = lambda x: f"{x:g}"
    w = max(len(fmt(x)) for x in m.flat)
    fila = lambda r: "[ " + "  ".join(fmt(x).rjust(w) for x in r) + " ]"
    ax.text(.03, .03, fila(m[0]) + chr(10) + fila(m[1]), transform=ax.transAxes, fontsize=8.5, va="bottom", family="monospace",
            bbox=dict(facecolor="white", edgecolor="none", alpha=.8, pad=1.5))

c = np.sqrt(2)/2
casos = [([[1,0],[0,-1]], "Reflexión en el eje $x_1$"),
         ([[0,1],[1,0]], "Reflexión en $x_2 = x_1$"),
         ([[-1,0],[0,-1]], "Reflexión en el origen"),
         ([[c,-c],[c,c]], "Rotación de 45°"),
         ([[.5,0],[0,1]], "Contracción horizontal, $k=0.5$"),
         ([[1,1.5],[0,1]], "Trasquilado horizontal, $k=1.5$"),
         ([[1,0],[-1,1]], "Trasquilado vertical, $k=-1$"),
         ([[1,0],[0,0]], "Proyección sobre el eje $x_1$")]
plt.rcParams["mathtext.fontset"] = "cm"
fig, axs = plt.subplots(2, 4, figsize=(13, 7.2))
for ax, (A, t) in zip(axs.flat, casos): panel(ax, A, t)
fig.suptitle(r"Cuadrado unitario (gris) y su imagen (azul); flechas: $T(\mathbf{e}_1)$ en rojo, $T(\mathbf{e}_2)$ en verde", fontsize=11)
fig.tight_layout(); fig.savefig(f"{OUT}/Cuadrado unitario bajo transformaciones del plano.png", dpi=110, facecolor="white"); plt.close(fig)

def gif(nombre, matrices, titulos, lim=2.6):
    frames = []
    for A, t in zip(matrices, titulos):
        fig, ax = plt.subplots(figsize=(3.6, 3.8))
        # cuadrícula transformada
        for s in np.linspace(-2, 2, 9):
            for P in (np.array([[s, s], [-2, 2]]), np.array([[-2, 2], [s, s]])):
                ax.plot(*(np.array(A) @ P), color="#cbd5e0", lw=.7, zorder=0)
        panel(ax, A, t, lim)
        fig.tight_layout(); fig.canvas.draw()
        frames.append(Image.fromarray(np.asarray(fig.canvas.buffer_rgba())).convert("RGB").quantize(64, method=Image.Quantize.MEDIANCUT))
        plt.close(fig)
    frames[0].save(f"{OUT}/{nombre}.gif", save_all=True, append_images=frames[1:], duration=110, loop=0, optimize=True)

ks = np.concatenate([np.linspace(0, 1.5, 14), np.full(6, 1.5), np.linspace(1.5, -1, 20), np.full(6, -1), np.linspace(-1, 0, 9)])
gif("Trasquilado horizontal animado", [[[1, k], [0, 1]] for k in ks], [rf"Trasquilado, $k = {k:+.2f}$" for k in ks])
fs = np.linspace(0, 2*np.pi, 37)[:-1]
gif("Rotación animada", [[[np.cos(f), -np.sin(f)], [np.sin(f), np.cos(f)]] for f in fs], [rf"Rotación, $\varphi$ = {np.degrees(f):.0f}°" for f in fs])
print("ok")
