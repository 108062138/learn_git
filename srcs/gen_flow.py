import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

MASTER_COLOR = '#89b4fa'
FEATURE_COLOR = '#a6e3a1'
ACTION_COLOR = '#f38ba8'
REMOTE_COLOR = '#fab387'
TEXT_COLOR = '#cdd6f4'
ARROW_COLOR = '#6c7086'

fig, axes = plt.subplots(1, 2, figsize=(18, 14))
fig.patch.set_facecolor('#1e1e2e')

# ── Left panel: Collaborative Workflow ──────────────────────────────
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')
ax.set_facecolor('#1e1e2e')

steps = [
    (MASTER_COLOR,  "1. pull latest main",         "git checkout main\ngit pull"),
    (FEATURE_COLOR, "2. create feature branch",    "git checkout -b feature/my-feature"),
    (FEATURE_COLOR, "3. do your work",             "git add <file> && git commit -m 'msg'\n(repeat)"),
    (MASTER_COLOR,  "4. pull main again",          "git checkout main\ngit pull"),
    (FEATURE_COLOR, "5. rebase onto main",         "git checkout feature/my-feature\ngit rebase main"),
    (ACTION_COLOR,  "6. push to remote",           "git push origin feature/my-feature"),
    ('#cba6f7',     "7. PR + review + merge",      "Open Pull Request on GitHub\n→ review → merge → delete branch"),
]

ys = [13, 11, 9, 7, 5, 3, 1.2]

for i, ((color, label, cmd), y) in enumerate(zip(steps, ys)):
    ax.add_patch(mpatches.FancyBboxPatch(
        (0.5, y - 0.65), 9, 1.3,
        boxstyle="round,pad=0.1",
        facecolor=color + '33', edgecolor=color, linewidth=2
    ))
    ax.text(1.2, y + 0.25, f"Step {i+1}: {label}", color=color,
            fontsize=9.5, fontweight='bold', va='center')
    ax.text(1.2, y - 0.25, cmd, color=TEXT_COLOR,
            fontsize=8, va='center', family='monospace')
    if i < len(steps) - 1:
        ax.annotate('', xy=(5, ys[i+1] + 0.7), xytext=(5, y - 0.7),
                    arrowprops=dict(arrowstyle='->', color=ARROW_COLOR, lw=2))

ax.text(5, 13.75, 'Git Collaborative Workflow', color=TEXT_COLOR,
        fontsize=13, fontweight='bold', ha='center')

# ── Right panel: fetch vs pull ───────────────────────────────────────
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 14)
ax2.axis('off')
ax2.set_facecolor('#1e1e2e')

ax2.text(5, 13.75, 'git fetch vs git pull', color=TEXT_COLOR,
         fontsize=13, fontweight='bold', ha='center')

# pull box
ax2.add_patch(mpatches.FancyBboxPatch(
    (0.5, 11.2), 9, 2,
    boxstyle="round,pad=0.1",
    facecolor=MASTER_COLOR + '33', edgecolor=MASTER_COLOR, linewidth=2
))
ax2.text(5, 13, 'git pull  (fetch + merge)', color=MASTER_COLOR,
         fontsize=10, fontweight='bold', ha='center')
ax2.text(5, 12.4, 'git pull', color=TEXT_COLOR,
         fontsize=9, ha='center', family='monospace')
ax2.text(5, 11.9, 'Quick. Downloads + applies in one step.\nLess control — use for solo work.', color=TEXT_COLOR,
         fontsize=8.5, ha='center', va='center')

# fetch box
ax2.add_patch(mpatches.FancyBboxPatch(
    (0.5, 7.8), 9, 3,
    boxstyle="round,pad=0.1",
    facecolor=REMOTE_COLOR + '33', edgecolor=REMOTE_COLOR, linewidth=2
))
ax2.text(5, 10.6, 'git fetch  (inspect first)', color=REMOTE_COLOR,
         fontsize=10, fontweight='bold', ha='center')
fetch_steps = [
    "git fetch                   # download only",
    "git diff main origin/main   # inspect changes",
    "git merge origin/main       # apply when ready",
]
for j, line in enumerate(fetch_steps):
    ax2.text(1.5, 9.9 - j * 0.65, line, color=TEXT_COLOR,
             fontsize=8.5, family='monospace')
ax2.text(5, 8.1, 'Safer for teams — see changes before applying.', color=TEXT_COLOR,
         fontsize=8.5, ha='center')

# conflict resolution box
ax2.add_patch(mpatches.FancyBboxPatch(
    (0.5, 3.8), 9, 3.6,
    boxstyle="round,pad=0.1",
    facecolor=ACTION_COLOR + '33', edgecolor=ACTION_COLOR, linewidth=2
))
ax2.text(5, 7.2, 'Resolving Remote Conflicts', color=ACTION_COLOR,
         fontsize=10, fontweight='bold', ha='center')
conflict_lines = [
    "1. git fetch",
    "2. git merge origin/main   ← triggers conflict",
    "3. VS Code shows buttons above each conflict:",
    "   • Accept Current Change  (keep local)",
    "   • Accept Incoming Change (keep remote)",
    "   • Accept Both Changes    (keep both)",
    "4. git add <file> && git commit",
]
for j, line in enumerate(conflict_lines):
    ax2.text(1.2, 6.7 - j * 0.55, line, color=TEXT_COLOR,
             fontsize=8.2, family='monospace')

# origin vs local box
ax2.add_patch(mpatches.FancyBboxPatch(
    (0.5, 1.2), 9, 2.2,
    boxstyle="round,pad=0.1",
    facecolor='#cba6f7' + '33', edgecolor='#cba6f7', linewidth=2
))
ax2.text(5, 3.2, 'local vs remote', color='#cba6f7',
         fontsize=10, fontweight='bold', ha='center')
ax2.text(1.5, 2.6, 'main         →  your local branch', color=TEXT_COLOR,
         fontsize=9, family='monospace')
ax2.text(1.5, 2.0, 'origin/main  →  branch on GitHub', color=TEXT_COLOR,
         fontsize=9, family='monospace')
ax2.text(1.5, 1.4, 'origin       →  name for your remote repo', color=TEXT_COLOR,
         fontsize=9, family='monospace')

plt.tight_layout()
plt.savefig('/Users/popo/Desktop/learn_work/learn_git/mds/git_flow.png',
            dpi=150, bbox_inches='tight', facecolor='#1e1e2e')
print("saved to mds/git_flow.png")
