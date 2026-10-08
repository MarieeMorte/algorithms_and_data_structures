# pip install numpy matplotlib
# для сохранения в gif: pip install pillow

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_buffon(l=0.8, d=1.0, n_total=300, fps=15,
                   save_path=None, seed=42):
    """
    Анимированная модель Бюффона.
    l — длина иглы, d — расстояние между прямыми (l <= d).
    n_total — сколько игл бросить (число кадров).
    fps — скорость анимации.
    save_path — если задан (например, 'buffon.gif'), сохранит анимацию.
    """
    rng = np.random.default_rng(seed)

    # --- Заранее генерируем все случайные величины ---
    x_all = rng.uniform(0, d / 2, n_total)  # расстояние до ближайшей прямой
    phi_all = rng.uniform(0, np.pi / 2, n_total)  # угол наклона
    crossed_all = x_all <= (l / 2) * np.sin(phi_all)  # условие пересечения

    # Положение центра иглы для визуализации
    L = 10 * d
    H = 5 * d
    cx_all = rng.uniform(0, L, n_total)
    k_line_all = rng.integers(0, 5, n_total)
    side_all = rng.integers(0, 2, n_total)  # игла сверху или снизу от прямой
    cy_all = k_line_all * d + np.where(side_all == 1, x_all, d - x_all)

    # Накопленная оценка вероятности по шагам
    est = np.cumsum(crossed_all) / np.arange(1, n_total + 1)

    # --- Фигура ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Левая панель: поле с прямыми и иглами
    for k in range(6):
        ax1.axhline(k * d, color='black', lw=1)
    ax1.set_xlim(0, L)
    ax1.set_ylim(0, H)
    ax1.set_aspect('equal')
    ax1.set_title(f'Бросаем иглы  (l = {l}, d = {d})')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    info = ax1.text(0.02, 0.98, '', transform=ax1.transAxes,
                    va='top', ha='left', fontsize=11, family='monospace',
                    bbox=dict(boxstyle='round', fc='white', ec='gray', alpha=0.9))

    # Правая панель: сходимость
    P_theor = 2 * l / (np.pi * d)
    ax2.axhline(P_theor, color='red', ls='--',
                label=f'Теория: {P_theor:.4f}')
    line_mc, = ax2.plot([], [], color='steelblue', lw=1.8, label='Монте-Карло')
    ax2.set_xlim(0, n_total)
    ax2.set_ylim(0, 1)
    ax2.set_xlabel('Число бросков')
    ax2.set_ylabel('Оценка вероятности')
    ax2.set_title('Сходимость оценки к формуле Бюффона')
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    n_crossed = 0

    def update(frame):
        nonlocal n_crossed
        i = frame
        ang = phi_all[i]
        dx = (l / 2) * np.cos(ang)
        dy = (l / 2) * np.sin(ang)
        color = 'crimson' if crossed_all[i] else 'steelblue'

        # Добавляем одну новую иглу
        ax1.plot(
            [cx_all[i] - dx, cx_all[i] + dx],
            [cy_all[i] - dy, cy_all[i] + dy],
            color=color, lw=1.8, alpha=0.85, solid_capstyle='round'
        )

        if crossed_all[i]:
            n_crossed += 1

        info.set_text(
            f'Брошено:     {i + 1}\n'
            f'Пересечений: {n_crossed}\n'
            f'Оценка P:    {est[i]:.4f}'
        )

        # Обновляем график сходимости
        line_mc.set_data(np.arange(1, i + 2), est[:i + 1])
        return []

    anim = FuncAnimation(
        fig, update,
        frames=n_total,
        interval=1000 / fps,
        blit=False,
        repeat=False
    )

    if save_path:
        anim.save(save_path, fps=fps, dpi=110)
        print(f'Анимация сохранена: {save_path}')

    return anim


if __name__ == '__main__':
    anim = animate_buffon(l=0.8, d=1.0, n_total=300, fps=15)
    plt.show()
