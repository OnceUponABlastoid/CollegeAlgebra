import os, glob

for path in glob.glob("*.tex"):
    if path == "Workbook.tex":
        continue
    with open(path) as f:
        content = f.read()
    if "\\begin{abstract}" not in content:
        content = content.replace(
            "\\maketitle",
            "\\begin{abstract}\n\\end{abstract}\n\\maketitle"
        )
        with open(path, "w") as f:
            f.write(content)
        print(f"Fixed {path}")

print("Done.")
