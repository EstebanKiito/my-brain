import sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
D12, D13, D14 = sys.argv[1:4]
AZ, RO, VE, GR, NA = "#2b6cb0", "#c53030", "#2f855a", "#a0aec0", "#dd6b20"
# --- 12: GIF x en el círculo y Ax
A = np.array([[2., 1.], [1., 2.]])
th = np.linspace(0, 2*np.pi, 300); circ = np.vstack([np.cos(th), np.sin(th)]); elip = A @ circ
frames = []
for t in np.linspace(0, 2*np.pi, 73)[:-1]:
    x = np.array([np.cos(t), np.sin(t)]); y = A @ x
    cosang = abs(x @ y) / np.linalg.norm(y)
    prop = cosang > 0.9995
    fig, ax = plt.subplots(figsize=(4, 4.2))
    ax.plot(*circ, color=GR, lw=1, ls="--"); ax.plot(*elip, color=GR, lw=1)
    ax.annotate("", xy=x, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=AZ, lw=2))
    ax.annotate("", xy=y, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=VE if prop else RO, lw=2.4 if prop else 2))
    for v in ([1, 1], [1, -1]):
        v = np.array(v)/np.sqrt(2); ax.plot([-3.2*v[0], 3.2*v[0]], [-3.2*v[1], 3.2*v[1]], color=GR, lw=.5, ls=":")
    ax.axhline(0, color="k", lw=.5); ax.axvline(0, color="k", lw=.5)
    ax.set_xlim(-3.3, 3.3); ax.set_ylim(-3.3, 3.3); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("A = [[2, 1], [1, 2]]   x (azul), Ax", fontsize=9, family="monospace")
    msg = f"Ax = {x@y:.0f} x  ->  x es vector propio" if prop else "Ax no es paralelo a x"
    ax.text(.03, .03, msg, transform=ax.transAxes, fontsize=8.5, bbox=dict(facecolor="white", edgecolor="none", alpha=.85))
    fig.tight_layout(); fig.canvas.draw()
    im = Image.fromarray(np.asarray(fig.canvas.buffer_rgba())).convert("RGB").quantize(64, method=Image.Quantize.MEDIANCUT)
    frames += [im] * (8 if prop else 1); plt.close(fig)
frames[0].save(f"{D12}/Vectores propios como direcciones que A no gira.gif", save_all=True, append_images=frames[1:], duration=90, loop=0, optimize=True)
# --- 13: grilla de vectores propios
A = np.array([[1.5, .5], [.5, 1.5]]); v1, v2 = np.array([1, 1])/np.sqrt(2), np.array([1, -1])/np.sqrt(2)
fig, axs = plt.subplots(1, 2, figsize=(9, 4.6))
for ax, M, tit in ((axs[0], np.eye(2), "Cuadrícula de vectores propios"), (axs[1], A, "Su imagen bajo A")):
    for s in np.arange(-3, 4):
        for P, Q in ((s*v1 - 3*v2, s*v1 + 3*v2), (s*v2 - 3*v1, s*v2 + 3*v1)):
            seg = M @ np.array([P, Q]).T; ax.plot(*seg, color=GR, lw=.8)
    cell = np.array([[0, 0], v1, v1 + v2, v2, [0, 0]]).T
    ax.fill(*(M @ cell), color=AZ, alpha=.3)
    for v, c, lab in ((v1, RO, "v1 (λ = 2)"), (v2, VE, "v2 (λ = 1)")):
        w = M @ v; ax.annotate("", xy=w, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=2.2))
        ax.text(*(w*1.15), lab, color=c, fontsize=9)
    ax.axhline(0, color="k", lw=.5); ax.axvline(0, color="k", lw=.5)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(tit, fontsize=10)
fig.suptitle("A = [[1.5, 0.5], [0.5, 1.5]] = P D P⁻¹ con D = diag(2, 1): en la base {v1, v2}, A solo estira", fontsize=10)
fig.tight_layout(); fig.savefig(f"{D13}/Acción de una matriz diagonalizable en la base de vectores propios.png", dpi=110, facecolor="white"); plt.close(fig)
# --- 14: órbitas
fig, axs = plt.subplots(1, 2, figsize=(9, 4.6))
cases = ((np.array([[.5, -.6], [.75, 1.1]]), np.array([2., 0.]), 40, "A = [[0.5, -0.6], [0.75, 1.1]]\nλ = 0.8 ± 0.6i, |λ| = 1: órbita elíptica"),
         (0.9*np.array([[np.cos(.4), -np.sin(.4)], [np.sin(.4), np.cos(.4)]]), np.array([2.5, 0.]), 30, "C = 0.9·rotación(0.4 rad)\nλ = 0.9 e^(±0.4i), |λ| = 0.9 < 1: espiral hacia 0"))
for ax, (M, x, n, tit) in zip(axs, cases):
    pts = [x]
    for _ in range(n): pts.append(M @ pts[-1])
    pts = np.array(pts).T
    if n < 35: ax.plot(*pts, color=GR, lw=.8)
    ax.scatter(*pts, c=np.arange(pts.shape[1]), cmap="viridis", s=18, zorder=3)
    ax.annotate("x0", xy=pts[:, 0], xytext=pts[:, 0] + [.15, .15], fontsize=9)
    ax.axhline(0, color="k", lw=.5); ax.axvline(0, color="k", lw=.5)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(tit, fontsize=9)
fig.suptitle("Iteraciones x(k+1) = A x(k): con valores propios complejos los puntos giran", fontsize=10)
fig.tight_layout(); fig.savefig(f"{D14}/Órbitas de matrices con valores propios complejos.png", dpi=110, facecolor="white"); plt.close(fig)
print("ok")
