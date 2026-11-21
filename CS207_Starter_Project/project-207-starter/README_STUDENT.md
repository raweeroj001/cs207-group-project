# CS207 Group Project — Starter Code

This is a **partially completed** version of the example application.
Keep the original three core features (Statistics, Bayes, Markov Text Prediction),
complete the TODOs, and create your group's Custom Application feature.
The starter UI is provided so that you can focus on implementing and applying the code.

## Setup

1. Open a terminal in the `project-207-starter` folder.
2. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate it:
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Windows CMD: `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`
4. Install the libraries:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   python -m streamlit run main.py
   ```

> The original archive included a virtual environment; this starter deliberately
> excludes it. Create your own `.venv` using the steps above.

## Required work

| Task | File | Requirement |
|---|---|---|
| TODO 1A–1B | `services/stats.py` | Calculate **population variance** and **population standard deviation** (`ddof=0`). Mean, Median and Mode are provided. |
| TODO 2A–2B | `pages/bayes.py` | Calculate **P(B)** and **P(A\|B)** with Bayes' theorem. Handle `P(B) = 0` without dividing by zero. |
| TODO 3A–3C | `services/textPrediction.py` | Count next words, calculate their probabilities, and finish sentence generation with the existing Markov model. |
| TODO 4 | `pages/custom.py` | Build one **new or extended** Mathematics-for-AI feature. Include input, processing and output. |

**Do not delete the existing sections to avoid the tasks.** Keep the Home,
Statistics, Bayes, Markov, Raw Text, Members and Custom App pages available.

## Simple checks

- **Statistics:** enter `2, 4, 4, 4, 5, 5, 7, 9`. The population
  variance should be **4.00** and standard deviation should be **2.00**.
- **Bayes:** use `P(A)=0.01`, `P(B|A)=0.95`, `P(B|not A)=0.05`.
  The displayed posterior should be **16.10%** (approximately).
- **Markov:** the available corpus is in `data/raw_data.json`.
  A word with multiple possible following words should show a probability
  distribution; generating a sentence should produce more than only the
  starting word when transitions exist.
- **Custom:** demonstrate a real input, calculation, and output.

Optional automated checks for the Statistics/Markov TODOs:
```bash
python -m unittest discover -s tests -v
```
These checks will **fail initially** because the TODOs have not been completed.

## Presentation

Demonstrate all features with real example inputs, then briefly explain
**what data goes in, what the program does, what comes out, and where it
could be applied**. Each group member should be able to explain the part
of the project that they worked on.

## Notes

- `data/raw_data.json` is the sample corpus for Markov.
- `data/members.json` contains placeholder member names; update for your team.
- Library usage is allowed; the goal is working, understandable, tested code,
  not manual calculations.
