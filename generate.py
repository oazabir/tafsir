import os
import yaml

with open("quran_themes.yaml", "r") as f:
    data = yaml.safe_load(f)

# Generate index.md (homepage)
with open("index.md", "w") as index_file:
    index_file.write("---\nlayout: default\ntitle: Home\n---\n\n")

    for surah, themes in data.items():
        index_file.write(f"## {surah}\n\n")

        for theme_data in themes.values():
            title = f"{surah} - {theme_data['Name']} ({theme_data['Verse Start']} - {theme_data['Verse End']})"
            page_name = title.lower().replace(" ", "-").replace("--", "-").replace(":", "");
            page_filename = page_name + ".md"
            link = f"{page_name}.html"

            index_file.write(f"- [{title}]({link})\n")
            index_file.write(f"  - {theme_data['Summary']}\n\n")

            # Generate individual pages for each theme
            with open(f"_articles/{page_filename}", "w") as page_file:
                page_file.write(f"---\nlayout: post\ntitle: {title}\npermalink: {link}\n---\n\n")
                page_file.write(f"## {title}\n\n")
                page_file.write(theme_data['Summary'])
