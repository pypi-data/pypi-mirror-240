import json
import os
from datetime import datetime
from dataclasses import dataclass
from typing import Dict
from jinja2 import Environment, FileSystemLoader
import markdown
from packaging import version


# pylint: disable=invalid-name
@dataclass
class Config:
    searchPath: str
    template: str
    outputFile: str
    templateParameters: Dict[str, str]

    @staticmethod
    def init_from_file():
        with open('relnotegen.config.json', 'r', encoding='utf-8') as config_file:
            config = json.load(config_file)
            result = Config(**config)
            return result
# pylint: enable=invalid-name


def collect_markdown_files(folder_path):
    markdown_files = []
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                markdown_files.append(filepath)
    return markdown_files


def extract_release_info(data):
    # Check that data is a dictionary
    if not isinstance(data, dict):
        raise ValueError("Data is not a dictionary.")

    # Initialize variables
    release_date = None
    version_number = None

    # Check for 'release-date' and 'version' keys and their associated values
    if 'release-date' in data and isinstance(data['release-date'], list) and len(data['release-date']) > 0:
        release_date = data['release-date'][0]
    else:
        raise ValueError("Malformed frontmatter: 'release-date' key not found, or its value is not a non-empty list.")

    if 'version' in data and isinstance(data['version'], list) and len(data['version']) > 0:
        version_number = data['version'][0]
    else:
        raise ValueError("Malformed frontmatter: 'version' key not found, or its value is not a non-empty list.")

    return release_date, version_number


def collect_releases(search_path):
    md = markdown.Markdown(extensions = ['meta'])
    releases = []
    for filepath in collect_markdown_files(search_path):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = md.convert(f.read())
            try:
                release_date, version_number = extract_release_info(md.Meta) # pylint: disable=no-member
                releases.append({
                    'version': version_number,
                    'release_date': release_date,
                    'contents': html
                })
                print(f"Including release {version_number}, described in {filepath}")
            except ValueError:
                pass
                # print(f"Following markdown file does not have the needed frontmatter, skipping: {filepath}")

    releases.sort(key=lambda x: version.parse(x['version']), reverse=True)
    return releases


def render_html(releases, template, template_parameters):
    env = Environment(loader=FileSystemLoader('.'))
    env.filters['format_date'] = lambda value: datetime.strptime(value, '%Y-%m-%d').strftime('%B %d, %Y')
    template = env.get_template(template)
    return template.render(params=template_parameters, releases=releases)


def generate_tailwind_config(content_files):
    filename = "tailwind.config.js"

    # Check if the file already exists. If so, don't overwrite.
    # This way, the user can - but doesn't have to - provide his own tailwind config file.
    if os.path.exists(filename):
        return

    content = ', '.join([f'"{file}"' for file in content_files])

    config_content = (
        f"/** @type {{import('tailwindcss').Config}} */\n"
        "module.exports = {\n"
        f"  content: [{content}],\n"
        "  theme: {\n"
        "    extend: {},\n"
        "  },\n"
        "  plugins: [],\n"
        "}\n"
    )

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(config_content)


def generate_css_file(output_file, template):
    css_filename = os.path.splitext(output_file)[0] + ".css"
    css_template_filename = os.path.splitext(template)[0] + ".css"
    generate_tailwind_config([output_file])
    syscmd = f"npx tailwindcss build -i {css_template_filename} -o {css_filename}"
    print(syscmd)
    os.system(syscmd)


def main():
    cfg = Config.init_from_file()

    # Search for release markdown files and collect release information
    releases = collect_releases(cfg.searchPath)

    # Apply HTML template to stitch releases together into one combined HTML file
    combined_html = render_html(releases, cfg.template, cfg.templateParameters)

    # Save the HTML file
    with open(cfg.outputFile, "w", encoding='utf-8') as f:
        f.write(combined_html)

    # Build the CSS file
    generate_css_file(cfg.outputFile, cfg.template)


if __name__ == "__main__":
    main()
