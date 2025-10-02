# **AI Bingo Slop** 🎱🤖

**The only AI tool that admits it’s a joke.**

Some tool to spice-up a bit your average AI presentation day

> If you can’t beat the hype, at least you can bingo it.

## **What is AI Bingo Slop?**

AI Bingo Slop is a **CLI tool** that generates bingo charts from a list of **AI startup buzzwords, clichés, and slop**. Perfect for:

- **VC meetings** where someone says "AGI is 2 years away."
- **Tech Twitter threads** where every startup is "disrupting [industry]."
- **Your own existential crisis** about the state of AI.

**We used AI to rate AI.** (The AI said: _"This is fine."_)

## **Features** ✨

- **4 Bingo Sizes**: `bullet` (3x3), `blitz` (5x5), `normal` (7x7), `100dayslater` (9x9).
- **Randomized Slop**: Pick from a curated list of **buzz-words** (or provide your own).
- **PDF or Image Output**: Because nothing says "professional" like a bingo card in **Times New Roman**.
- **Multiplayer Mode**: Generate cards for all your friends.
- **Capitalized First Letters**: Because `aI` looks unprofessional.

## **Installation** 🛠️

### **Prerequisites**

- Python 3.12+
- [UV](https://docs.astral.sh/uv/) (because `pip` is too slow for AI hype)

Flake.nix env is provided

### **Install**

Install the CLI with

```bash
uv pip install -e .
```

## **Usage** 🚀

Get some help with

```bash
uv run aibingoslop --help
```

Or run the following example with

```bash
uv run aibingoslop examples/AIStartup.txt bullet 3 outputs/ --output-format pdf

```

- Generates **3 random 3x3 bingo cards** from `examples/AIStartup.txt`.
- Saves them as **PDFs** in `output/`.

**🚨 Warning:** May cause existential dread about the state of tech. Use at your own risk.

> This README was generated with [LeChat](https://chat.mistral.ai) because 🥖 (and around 95% of the code as well...)
