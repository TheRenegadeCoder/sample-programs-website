import os


def project_section(section: str, bound: str):
    for item in os.listdir("archive/projects/"):
        if item != "index.md":
            doc = open(f"archive/projects/{item}/index.md", encoding="utf-8").readlines()
            try:
                start = doc.index(f"## {section}\n") 
                end = doc.index(f"## {bound}\n")
                description = "".join(doc[start + 2: end - 1])
                with open(f"sources/projects/{item}/{section.lower()}.md", "w") as desc:
                    desc.write(description)
            except ValueError:
                print(f"{item} has no {section}")


if __name__ == "__main__":
    project_section("Description", "Requirements")
    project_section("Requirements", "Testing")
    project_section("Testing", "Articles")
