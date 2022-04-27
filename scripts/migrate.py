import os
from pathlib import Path


def project_section(section: str, bound: str):
    for item in os.listdir("archive/projects/"):
        if item != "index.md":
            doc = open(f"archive/projects/{item}/index.md", encoding="utf-8").readlines()
            try:
                start = doc.index(f"## {section}\n") 
                end = doc.index(f"## {bound}\n")
                description = "".join(doc[start + 2: end - 1])
                with open(f"sources/projects/{item}/{section.lower()}.md", "w", encoding="utf-8") as desc:
                    desc.write(description)
            except ValueError as err:
                print(f"{item} has no {section}")
            generate_front_matter(
                Path(f"archive/projects/{item}/index.md"),
                Path(f"sources/projects/{item}/front_matter.yaml")
            )


def language_section(bound: str):
    for item in os.listdir("archive/languages/_posts/"):
        doc = open(f"archive/languages/_posts/{item}", encoding="utf-8").readlines()
        try:
            start = doc.index("---\n", 1)
            end = doc.index(f"## {bound}\n")
            description = "".join(doc[start + 2: end - 1])
            with open(f"sources/languages/{item.split('.')[0].split('-')[-1]}/description.md", "w", encoding="utf-8") as desc:
                desc.write(description)
        except ValueError as err:
            print(f"{item} has no {bound}")
        generate_front_matter(
            Path(f"archive/languages/_posts/{item}"),
            Path(f"sources/languages/{item.split('.')[0].split('-')[-1]}/front_matter.yaml")
        )


def program_section(section: str, bound: str):
    for item in os.listdir("archive/projects/"):
        if item != "index.md" and os.path.exists(f"archive/projects/{item}/_posts/"):
            for post in os.listdir(f"archive/projects/{item}/_posts/"):
                doc = open(f"archive/projects/{item}/_posts/{post}", encoding="utf-8").readlines()
                lower_copy = [x.lower().replace("the ", "") for x in doc]
                try:
                    start = lower_copy.index(f"## {section.lower().replace('the ', '')}\n") 
                    end = lower_copy.index(f"## {bound.lower().replace('the ', '')}\n")
                    description = "".join(doc[start + 2: end - 1])
                    Path(f"sources/programs/{item}/{'-'.join(post.split('.')[0].split('-')[3:])}/").mkdir(parents=True, exist_ok=True)
                    with open(f"sources/programs/{item}/{'-'.join(post.split('.')[0].split('-')[3:])}/{section.lower().replace(' ', '-')}.md", "w", encoding="utf-8") as desc:
                        desc.write(description)
                except ValueError as err:
                    print(f"{item}:{post} has no {section}")
                generate_front_matter(
                    Path(f"archive/projects/{item}/_posts/{post}"),
                    Path(f"sources/programs/{item}/{'-'.join(post.split('.')[0].split('-')[3:])}/front_matter.yaml")
                )



def generate_front_matter(input: Path, output: Path):
    with open(input, "r", encoding="utf-8") as f:
        doc = f.readlines()
    start = doc.index("---\n")
    end = doc.index("---\n", start + 1)
    front_matter = "".join(doc[start + 1: end])
    with open(output, "w", encoding="utf-8") as f:
        f.write(front_matter)


if __name__ == "__main__":
    project_section("Description", "Requirements")
    project_section("Requirements", "Testing")
    project_section("Testing", "Articles")
    language_section("Articles")
    program_section("How to Implement the Solution", "How to Run the Solution")
    program_section("How to Run the Solution", "Further Reading")
