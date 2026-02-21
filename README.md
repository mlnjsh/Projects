# 🎮 RL Book Interactive Labs

**Companion interactive apps for [Complete Reinforcement Learning Journey: From Basics to RLHF]()**

> *Don't just read about algorithms — watch them think.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/demo-live-brightgreen)](https://mlnjsh.github.io/rl-book-labs/)

---

## 🧪 What Is This?

Each chapter of the book has a companion **browser-based interactive lab** where you can:

- 🔵 **Step through algorithms** cell-by-cell and see values update in real-time
- 🎛️ **Tweak parameters** (γ, ε, learning rate) with sliders and instantly see the effect
- 🤖 **Watch agents navigate** grids, solve problems, and learn from mistakes
- 📊 **Inspect Q-values**, policy arrows, and convergence logs live

**No installation required.** Open in any browser. Works on desktop and mobile.

---

## 📚 Available Labs

| Chapter | Lab | Concepts Covered | Try It |
|---------|-----|-----------------|--------|
| Ch 2 | **MDP Explorer** | States, Actions, Rewards, Transitions, Deterministic vs Stochastic, Policy, Value Function | [▶ Launch](https://mlnjsh.github.io/rl-book-labs/ch2/) |
| Ch 3 | **Policy Iteration on FrozenLake** | Bellman equations, policy evaluation (sweep-by-sweep), policy improvement, convergence | [▶ Launch](https://mlnjsh.github.io/rl-book-labs/ch3/) |
| Ch 4 | Monte Carlo Blackjack *(coming soon)* | First-visit MC, exploring starts, episode replay | — |
| Ch 5 | TD Learning & SARSA *(coming soon)* | TD(0), SARSA, Q-learning, cliff walking | — |
| Ch 6 | DQN on CartPole *(coming soon)* | Experience replay, target networks, training curves | — |
| Ch 7 | Policy Gradients *(coming soon)* | REINFORCE, baselines, variance reduction | — |

---

## 🌐 Ch2: MDP Explorer

**Understand the building blocks of every RL algorithm.** Explore a 5×5 Gridworld MDP interactively.

### Three Modes

| Mode | What You Learn |
|------|---------------|
| **🔍 Explore** | Click any cell → see its state (r,c), reward, transition probabilities for each action, and Q-values |
| **π Policy** | See policy arrows on every cell. Click to cycle actions and build your own policy |
| **V Value** | Color-coded heatmap of V(s). Green = high value, red = low value |

### Key Features
- **Deterministic vs Stochastic** — slide slip from 0 to 0.6 and watch transition probabilities change
- **Click any cell** → full breakdown of transitions, rewards, and Q(s,a) for all 4 actions
- **⚡ Solve Optimal Policy** — finds π* and shows value heatmap
- **🤖 Run Robot** — animated step-by-step episode
- **🤖×10 Run 10 Episodes** — shows success rate (deterministic vs stochastic)
- **✏️ Edit Grid** — paint walls, pits, goals, and start positions to create your own MDP

### What to Try
1. Click cells → inspect State, Action, Reward, Transition
2. ⚡ Solve with **slip=0** → observe shortest path
3. Set **slip=0.3** → Solve again → policy becomes cautious near pits!
4. Run 🤖 with slip=0 → always reaches goal
5. Run 🤖×10 with slip=0.3 → some episodes fail!
6. Compare **γ=0.3** vs **γ=0.99** → value function changes dramatically
7. Edit grid: add more pits near the goal → watch policy adapt

---

## 🚀 Ch3: Policy Iteration Visualizer

**Step through the Policy Iteration algorithm on a 4×4 FrozenLake grid.**

### What You Can Do

| Button | What Happens |
|--------|-------------|
| **① One Eval Sweep** | Each cell lights up blue as its value updates via the Bellman equation |
| **① Full Evaluation** | Runs all sweeps until V^π converges |
| **② Improve Policy** | Arrows change one-by-one to the greedy action — green flash on changes |
| **▶▶ Auto-Run** | Runs the full evaluate → improve loop with pauses between iterations |
| **🤖 Run Robot** | Animated robot walks the grid following the current policy |
| **↺ Reset** | Start fresh with new parameters |

### What to Try
1. Press ① One Sweep — watch cells light up one by one
2. Press ① again — values get more accurate each sweep
3. Press ① Full Eval — converge V^π completely
4. Press ② — watch arrows change direction!
5. Repeat ①→② until π* found
6. Press 🤖 — watch the robot navigate!
7. Try **γ=0.5** vs **γ=0.99** — compare policies
8. Try **Slip=0** vs **Slip=0.5** — deterministic vs stochastic

---

## 🏗️ Project Structure

```
rl-book-labs/
├── README.md
├── ch2/
│   └── index.html          # MDP Explorer (5×5 Gridworld)
├── ch3/
│   └── index.html          # Policy Iteration on FrozenLake
├── ch4/                    # (coming soon)
├── ch5/                    # (coming soon)
└── ch6/                    # (coming soon)
```

Each lab is a **single HTML file** — no build step, no dependencies, no frameworks. Just open in any browser.

---

## 🎓 About the Book

**Complete Reinforcement Learning Journey: From Basics to RLHF**

The only book that takes you from "What is a Markov Decision Process?" all the way to "How do we align language models with human values?" — with intuition, math, code, and interactive labs at every step.

### Key Features
- 📖 **Intuition → Math → Code** triple for every concept
- 🤖 **DeliBot** running example that grows with the theory
- 🧠 **Think Like an Agent** boxes for building intuition
- ⚠️ **Common Misconceptions** boxes to prevent errors
- 🔬 **Interactive Labs** (this repo!) for hands-on learning
- 📝 **Quizzes with detailed answer keys** for each chapter

---

## 🤝 Contributing

Found a bug in a lab? Have an idea for a new visualization? Contributions are welcome!

1. Fork the repo
2. Create a branch (`git checkout -b feature/new-lab`)
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<p align="center">
  <i>Built with ❤️ as a companion to the book.</i><br>
  <i>"The best way to learn an algorithm is to watch it think."</i>
</p>
