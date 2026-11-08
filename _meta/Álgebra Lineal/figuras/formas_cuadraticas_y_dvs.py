import sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
D18, D19 = sys.argv[1:3]
RO, VE, AZ, GR = "#c53030", "#2f855a", "#2b6cb0", "#a0aec0"
x = np.linspace(-2, 2, 300); X, Y = np.meshgrid(x, x)
casos = [(np.array([[3, -1], [-1, 3]]), "Definida positiva\n3x² − 2xy + 3y²  (λ = 2, 4)"),
         (np.array([[1, -4], [-4, -5]]), "Indefinida\nx² − 8xy − 5y²  (λ = 3, −7)"),
         (np.array([[1, -3], [-3, 9]]), "Semidefinida positiva\nx² − 6xy + 9y²  (λ = 0, 10)")]
fig, axs = plt.subplots(1, 3, figsize=(12, 4.4))
for ax, (A, t) in zip(axs, casos):
    Q = A[0, 0]*X**2 + 2*A[0, 1]*X*Y + A[1, 1]*Y**2
    lim = np.abs(Q).max()
    cs = ax.contourf(X, Y, Q, levels=21, cmap="RdBu_r", vmin=-lim, vmax=lim)
    ax.contour(X, Y, Q, levels=[-2, -1, 0, 1, 2] if A[0,0] != 3 else [1, 2, 4, 8], colors="k", linewidths=.6)
    w, V = np.linalg.eigh(A)
    for lam, v in zip(w, V.T):
        ax.annotate("", xy=1.4*v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.6))
        ax.text(*(1.55*v), f"λ={lam:.0f}", fontsize=8, ha="center")
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(t, fontsize=9)
fig.suptitle("Curvas de nivel de Q(x) = xᵀAx (rojo: Q > 0, azul: Q < 0). Las flechas son los ejes principales (vectores propios de A)", fontsize=9)
fig.tight_layout(rect=[0, 0, 1, 0.9]); fig.savefig(f"{D18}/Formas cuadráticas definida, indefinida y semidefinida.png", dpi=110, facecolor="white"); plt.close(fig)
# DVS
A = np.array([[3., 0.], [4., 5.]]); U, s, Vt = np.linalg.svd(A)
th = np.linspace(0, 2*np.pi, 300); c = np.vstack([np.cos(th), np.sin(th)])
fig, axs = plt.subplots(1, 2, figsize=(9, 4.6))
axs[0].plot(*c, color=GR)
for i, col in enumerate((RO, VE)):
    v = Vt[i]; axs[0].annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2)); axs[0].text(*(1.15*v), f"v{i+1}", color=col)
axs[0].set_title("Círculo unitario y vectores singulares derechos", fontsize=9)
e = A @ c; axs[1].plot(*e, color=GR)
for i, col in enumerate((RO, VE)):
    w = A @ Vt[i]; axs[1].annotate("", xy=w, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2)); axs[1].text(*(w*1.08), f"A v{i+1} = σ{i+1} u{i+1}\nσ{i+1} = {s[i]:.2f}", color=col, fontsize=8)
axs[1].set_title("Su imagen: elipse con semiejes σ1 u1 y σ2 u2", fontsize=9)
for ax, L in zip(axs, (1.4, 7)):
    ax.axhline(0, color="k", lw=.5); ax.axvline(0, color="k", lw=.5); ax.set_xlim(-L, L); ax.set_ylim(-L - (0.8 if L > 2 else 0), L); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
fig.suptitle("A = [[3, 0], [4, 5]] = U Σ Vᵀ: rotar (Vᵀ), estirar los ejes (Σ) y rotar (U)", fontsize=10)
fig.tight_layout(rect=[0, 0, 1, 0.94]); fig.savefig(f"{D19}/Descomposición en valores singulares de una matriz 2x2.png", dpi=110, facecolor="white"); plt.close(fig)
print(s)
