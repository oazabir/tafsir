import os
import yaml


# Generate index.md (homepage)
with open("index.md", "w") as index_file:
    index_file.write("---\nlayout: default\ntitle: Home\n---\n\n")
    for subdir, dirs, files in os.walk('quran_yamls'):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if file.endswith(".yml"):
                with open(filepath, "r") as f:
                    data = yaml.safe_load(f)

                    for surah in data.items():
                        index_file.write(f"## {surah}\n\n")
                        index_file.write(f"{summary}\n\n")

                        for theme_data in themes.values():
                            title = f"{surah} - {theme_data['name']} (verse {theme_data['verse_range']})"
                            page_name = title.lower().replace(" ", "-").replace("--", "-").replace(":", "");
                            page_filename = page_name + ".md"
                            link = f"{page_name}.html"

                            index_file.write(f"- [{title}]({link})\n")
                            index_file.write(f"  - {theme_data['summary']}\n\n")

                            # Generate individual pages for each theme
                            with open(f"_articles/{page_filename}", "w") as page_file:
                                page_file.write(f"---\nlayout: post\ntitle: {title}\npermalink: {link}\n---\n\n")
                                page_file.write(f"## {title}\n\n")
                                page_file.write(theme_data['Summary'])
