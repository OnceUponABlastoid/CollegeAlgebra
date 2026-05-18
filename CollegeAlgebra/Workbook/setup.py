activities = [
    ("compoundLinearInequalities", "Compound Linear Inequalities"),
    ("absoluteValueInequalities", "Absolute Value Inequalities"),
    ("functionsAndRelations", "Functions and Relations"),
    ("linearFunctions", "Linear Functions"),
    ("applicationsOfLinearEquations", "Applications of Linear Equations"),
    ("systemsOfLinearEquations2Var", "Systems of Linear Equations in 2 Variables"),
    ("systemsOfLinearEquations3Var", "Systems of Linear Equations in 3 Variables"),
    ("transformationsOfGraphs", "Transformations of Graphs"),
    ("analyzingGraphsPiecewiseFunctions", "Analyzing Graphs and Piecewise Functions"),
    ("algebraOfFunctionsComposition", "Algebra of Functions and Composition"),
    ("quadraticFunctionsApplications", "Quadratic Functions and Applications"),
    ("introToPolynomialFunctions", "Intro to Polynomial Functions"),
    ("polynomialDivisionFactorRemainder", "Polynomial Division; Factor and Remainder Theorems"),
    ("introToRationalFunctions", "Intro to Rational Functions"),
    ("graphsOfRationalFunctions", "Graphs of Rational Functions"),
    ("polynomialAndRationalInequalities", "Polynomial and Rational Inequalities"),
    ("inverseFunctions", "Inverse Functions"),
    ("exponentialFunctions", "Exponential Functions"),
    ("logarithmicFunctions", "Logarithmic Functions"),
    ("propertiesOfLogarithms", "Properties of Logarithms"),
    ("exponentialEquations", "Exponential Equations"),
    ("logarithmicEquations", "Logarithmic Equations"),
    ("modelingExponentialLogarithmic", "Modeling with Exponential and Logarithmic Equations"),
]

template = r"""\documentclass{{ximera}}
\title{{{title}}}
\begin{{document}}
\maketitle

\end{{document}}
"""

for filename, title in activities:
    with open(f"{filename}.tex", "w") as f:
        f.write(template.format(title=title))

print(f"Created {len(activities)} activity files.")