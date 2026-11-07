import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')
ax.set_facecolor('#1e1e2e')
fig.patch.set_facecolor('#1e1e2e')

MASTER_COLOR = '#89b4fa'
FEATURE_COLOR = '#a6e3a1'
ACTION_COLOR = '#f38ba8'
TEXT_COLOR = '#cdd6f4'
ARROW_COLOR = '#6c7086'

steps = [
    (5, 13,   MASTER_COLOR,  "1. git checkout master\n   git pull"),
    (5, 11,   FEATURE_COLOR, "2. git checkout -b feature/my-feature"),
    (5, 9,    FEATURE_COLOR, "3. work + git add + git commit\n   (repeat)"),
    (5, 7,    MASTER_COLOR,  "4. git checkout master\n   git pull"),
    (5, 5,    FEATURE_COLOR, "5. git checkout feature/my-feature\n   git rebase master"),
    (5, 3,    ACTION_COLOR,  "6. git push origin feature/my-feature"),
    (5, 1.2,  '#cba6f7',     "7. Open Pull Request on GitHub\n   → review → merge → delete branch"),
]

labels = [
    "pull latest master",
    "create feature branch",
    "do your work",
    "pull master again",
    "rebase onto master",
    "push to remote",
    "PR + review + merge",
]

for i, (x, y, color, cmd) in enumerate(steps):
    ax.add_patch(mpatches.FancyBboxPatch(
        (1, y - 0.6), 8, 1.2,
        boxstyle="round,pad=0.1",
        facecolor=color + '33',
        edgecolor=color,
        linewidth=2
    ))
    ax.text(2, y + 0.2, f"Step {i+1}: {labels[i]}", color=color,
            fontsize=10, fontweight='bold', va='center')
    ax.text(2, y - 0.25, cmd, color=TEXT_COLOR,
            fontsize=8.5, va='center', family='monospace')

    if i < len(steps) - 1:
        next_y = steps[i+1][1]
        ax.annotate('', xy=(5, next_y + 0.65), xytext=(5, y - 0.65),
                    arrowprops=dict(arrowstyle='->', color=ARROW_COLOR, lw=2))

ax.text(5, 13.7, 'Git Collaborative Workflow', color=TEXT_COLOR,
        fontsize=14, fontweight='bold', ha='center', va='center')

plt.tight_layout()
plt.savefig('/Users/popo/Desktop/learn_work/learn_git/mds/git_flow.png',
            dpi=150, bbox_inches='tight', facecolor='#1e1e2e')
print("saved to mds/git_flow.png")
