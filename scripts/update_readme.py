from pathlib import Path


README = Path("README.md")
DOCS_DIR = Path("docs")
IMAGES_DIR = Path("images")

start_marker = "<!-- PLANTUML:START -->"
end_marker = "<!-- PLANTUML:END -->"


def diagram_title(path: Path) -> str:
    return path.stem.replace("-", " ").title()


def generate_diagram_section() -> str:
    diagrams = sorted(DOCS_DIR.glob("*.puml"))

    lines = [start_marker, ""]

    for diagram in diagrams:
        title = diagram_title(diagram)
        image_name = f"{diagram.stem}.png"
        svg_name = f"{diagram.stem}.svg"

        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"![{title}](images/{image_name})")
        lines.append("")
        lines.append(f"[View SVG](images/{svg_name})")
        lines.append("")

    lines.append(end_marker)

    return "\n".join(lines)


def main():
    content = README.read_text(encoding="utf-8")

    new_section = generate_diagram_section()

    if start_marker in content and end_marker in content:
        before = content.split(start_marker, 1)[0]
        after = content.split(end_marker, 1)[1]

        content = before + new_section + after
    else:
        if not content.endswith("\n"):
            content += "\n"

        content += "\n## UML Diagrams\n\n"
        content += new_section
        content += "\n"

    README.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()