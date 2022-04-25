import os

for item in os.listdir("archive/projects/"):
    if item != "index.md":
        doc = open(f"archive/projects/{item}/index.md", encoding="utf-8").readlines()
        try:
            start = doc.index("## Description\n") 
            end = doc.index("## Requirements\n")
            description = "".join(doc[start + 2: end])
            with open(f"sources/projects/{item}/description.md", "w") as desc:
                desc.write(description)
        except ValueError:
            print(f"{item} has no description")