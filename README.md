# NBA Game Winner Prediction

**Course:** UW CSE 163 (Intermediate Data Programming), Autumn 2026  
**Authors:** Ethan Kwan, Gabriel Kan

This project explores whether machine learning can predict NBA game winners from historical game and team statistics. We are currently completing Part 2: Exploratory Data Analysis (EDA). We have **not** trained or evaluated a final machine learning model yet.

## Research Questions

1. How accurately can machine learning predict NBA game winners using historical data?
2. How does feature selection affect prediction accuracy?
3. How does accuracy change when training on one NBA season and testing on the following season?

## Dataset

We use **Historical NBA Data and Player Box Scores** by Eoin Moore on Kaggle:

https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores

For EDA and later modeling, we focus on:

- `Games.csv` — one row per game
- `TeamStatistics.csv` — one row per team per game (two rows per game)

These CSV files are **not** stored in this repository. Each teammate should download them locally into a `data/` folder.

## Project Status

- [x] Project setup (virtual environment, dependencies, `.gitignore`)
- [x] Initial dataset inspection in `exploration.ipynb`
- [ ] Summary statistics and visualizations
- [ ] Machine learning models (scikit-learn)
- [ ] Model explanation with SHAP

## How to Clone This Repository

```bash
git clone https://github.com/ethan-kwan/nba-prediction.git
cd nba-prediction
```

## How to Set Up the Python Environment

### 1. Create a virtual environment

```bash
python3 -m venv .venv
```

This creates a local folder named `.venv` that holds an isolated Python install for this project.

### 2. Activate the virtual environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (Command Prompt):**

```bash
.venv\Scripts\activate
```

After activation, your terminal prompt usually shows `(.venv)`.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

This installs packages such as `pandas`, `matplotlib`, `scikit-learn`, `shap`, and `flake8`.

## How to Download the Data

1. Open the Kaggle dataset page:  
   https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores
2. Download the dataset (requires a free Kaggle account).
3. Create a `data/` folder in the project root if it does not already exist:

   ```bash
   mkdir -p data
   ```

4. Copy these files into `data/`:

   - `Games.csv`
   - `TeamStatistics.csv`

Your folder should look like:

```text
nba-prediction/
  data/
    Games.csv
    TeamStatistics.csv
  exploration.ipynb
  eda.py
  requirements.txt
  README.md
```

## How to Open the Notebook

### Option A: Jupyter in the terminal

```bash
source .venv/bin/activate
python -m pip install jupyter
jupyter notebook exploration.ipynb
```

### Option B: VS Code / Other IDE

1. Open the `nba-prediction` folder in your IDE.
2. Open `exploration.ipynb`.
3. Select the notebook kernel:
   - Click **Select Kernel** (top-right of the notebook).
   - Choose **Python Environments…**
   - Select `.venv` (the interpreter at `.venv/bin/python`).
4. Run the cells in order from the top.

If you also want the editor’s default Python interpreter to match:

1. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux).
2. Run **Python: Select Interpreter**.
3. Choose `.venv/bin/python`.

## Useful Project Files

| File | Purpose |
|------|---------|
| `exploration.ipynb` | Interactive EDA notebook (initial inspection started) |
| `eda.py` | Runnable Python script for basic dataset exploration |
| `test_eda.py` | Placeholder for future tests |
| `requirements.txt` | Exact Python package versions |
| `.gitignore` | Ignores `.venv/`, `data/`, CSVs, caches, and generated files |

## Notes for Teammates

- Do **not** commit large CSV files or virtual environments.
- Keep exploration work beginner-friendly and flake8-compliant for `.py` scripts.
- Ask before making major changes to shared files.
