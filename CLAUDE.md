# College Algebra Recitation Workbook — Project Context

## What this is
A Ximera-based interactive workbook for Math 1148 (College Algebra) recitation sections. LaTeX source compiles to both interactive HTML (via Ximera) and PDF. The repo is `git@github.com:OnceUponABlastoid/CollegeAlgebra.git`.

## File locations
- **Workbook activities**: `CollegeAlgebra/Workbook/*.tex`
- **Master file**: `CollegeAlgebra/Workbook/Workbook.tex` (lists all 23 `\activity{}` entries)
- **Shared preamble**: `xmPreamble.tex` (defines `\ds`, `\AND`, `\OR`, `\closeddot`, `\opendot`, includes pgfplots/tikz)
- **MCQ source**: `/Users/vutha.1/Downloads/1148_MCQDraftsA.tex`
- **Worksheet source**: `/Users/vutha.1/Downloads/00 Math 1148 Worksheets LaTeX - Shared/WORKSHEET/`

## Status — all 23 sections complete and pushed

| File | Section |
|---|---|
| `compoundLinearInequalities.tex` | Compound Linear Inequalities |
| `absoluteValueInequalities.tex` | Absolute Value Inequalities |
| `functionsAndRelations.tex` | §2.3 Functions and Relations |
| `linearFunctions.tex` | §2.4 Linear Functions |
| `applicationsOfLinearEquations.tex` | §2.5 Applications |
| `systemsOfLinearEquations2Var.tex` | §9.1 Systems (2 variables) |
| `systemsOfLinearEquations3Var.tex` | §9.2 Systems (3 variables) |
| `transformationsOfGraphs.tex` | §2.6 Transformations |
| `analyzingGraphsPiecewiseFunctions.tex` | §2.7 Piecewise Functions |
| `algebraOfFunctionsComposition.tex` | §2.8 Function Composition |
| `quadraticFunctionsApplications.tex` | §3.1 Quadratics |
| `introToPolynomialFunctions.tex` | §3.2 Polynomial Functions |
| `polynomialDivisionFactorRemainder.tex` | §3.3 Division / Factor / Remainder |
| `introToRationalFunctions.tex` | §3.5 Rational Functions (intro) |
| `graphsOfRationalFunctions.tex` | §3.6 Graphs of Rational Functions |
| `polynomialAndRationalInequalities.tex` | §3.7 Inequalities |
| `inverseFunctions.tex` | §4.1 Inverse Functions |
| `exponentialFunctions.tex` | §4.2 Exponential Functions |
| `logarithmicFunctions.tex` | §4.3 Logarithmic Functions |
| `propertiesOfLogarithms.tex` | §4.4 Properties of Logarithms |
| `exponentialEquations.tex` | §4.5A Exponential Equations |
| `logarithmicEquations.tex` | §4.5B Logarithmic Equations |
| `modelingExponentialLogarithmic.tex` | §4.6 Modeling |

## Standard file structure (every activity follows this)
```latex
\documentclass{ximera}
\title{...}
\outcome{...}  % one per learning objective

\begin{document}
\begin{abstract}\end{abstract}
\maketitle

\textbf{Learning Objectives:}
\begin{itemize} ... \end{itemize}
\medskip

\noindent\textbf{Key facts/rules...}  % summary box

\bigskip
\section*{Quick Check}
% 5 MCQs, each with \begin{hint}...\end{hint} and \begin{multipleChoice}...\end{multipleChoice}
% Exactly 5 \choice entries per MCQ; one marked \choice[correct]{...}
% Use \begin{selectAll} when multiple answers are correct

\bigskip
\section*{Extended Practice}
% FRQ problems with \begin{solution}...\end{solution}
\end{document}
```

## Key conventions
- **5 choices per MCQ** — always exactly 5 `\choice` entries
- **`\begin{selectAll}`** when the answer key lists multiple correct answers
- **No `\import{WORKSHEET/GRAPHS/}{...}`** — those imported graphs can't be replicated; describe the graph's key features in the problem text instead and give algebraic solutions
- **TikZ graphs in MCQs** — reproducible graphs are embedded directly using `pgfplots`; use `log2(x)` syntax in pgfplots (not `\log_2`)
- **`\ds`** = `\displaystyle` (defined in xmPreamble)
- **`\AND`, `\OR`** — defined macros for compound inequalities
- **`\closeddot`, `\opendot`** — defined in xmPreamble for number line tikz diagrams
- **Synthetic division** — displayed as tabular with `\mid` (no `\polyhornerscheme`)
- **No "Co-Authored-By: Claude"** in any git commits

## Source file mapping (worksheet → activity)
- `33blank/solutions` → `polynomialDivisionFactorRemainder`
- `35blank/solutions` → `introToRationalFunctions`
- `36blank/solutions` → `graphsOfRationalFunctions`
- `37blank/solutions` → `polynomialAndRationalInequalities`
- `41blank/solutions` → `inverseFunctions`
- `42blank/solutions` → `exponentialFunctions`
- `43blank/solutions` → `logarithmicFunctions`
- `44blank/solutions` → `propertiesOfLogarithms`
- `45Ablank/solutions` → `exponentialEquations`
- `45Bblank/solutions` → `logarithmicEquations`
- `46blank/solutions` → `modelingExponentialLogarithmic`

## Known answer key quirks
- **§3.3 Q4** (Remainder Theorem): correct answer is E "Not listed" — f(2)=25 is not among the choices
- **§4.5A Q2**: correct answer is E "Not listed" — exact answer is `(log(93)−log(9))/(2·log(9))`
- **§4.5A Q3**: correct answer is E "Not listed; x=3" — none of the original choices is correct
- **§4.6 Q4**: two equivalent correct answers (B and D) — uses `\begin{selectAll}`

## Potential next steps
1. Compile and test the Ximera build to catch LaTeX/rendering errors
2. Deploy to Ximera hosting for student access
