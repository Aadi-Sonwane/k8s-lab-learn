import os
import yaml

# Function to read the existing mkdocs.yml and return existing navigation
def read_existing_mkdocs_yml(base_path):
    mkdocs_yml_path = os.path.join(base_path, 'mkdocs.yml')
    if os.path.exists(mkdocs_yml_path):
        with open(mkdocs_yml_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

# Function to generate navigation dynamically, while avoiding duplicates
def generate_nav_section(folder_path, base_dir, existing_nav):
    nav = []
    for root, dirs, files in os.walk(folder_path):
        # Consider directories as well
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), base_dir)
            # Avoid duplicating entries
            if relative_path not in existing_nav:
                # Add files to nav (no {} braces)
                nav.append(f"        - {file}: {relative_path}")
                existing_nav.add(relative_path)  # Mark this file as processed
        # Now process directories, even empty ones
        for dir in dirs:
            section_path = os.path.join(root, dir)
            section_relative_path = os.path.relpath(section_path, base_dir)
            if section_relative_path not in existing_nav:
                nav.append(f"        - {dir}: {section_relative_path}")
                existing_nav.add(section_relative_path)  # Mark this folder as processed
    return nav, existing_nav

# Function to update mkdocs.yml dynamically based on existing folder structure
def update_mkdocs_yml(base_path):
    # Read the existing mkdocs.yml to avoid overwriting existing entries
    existing_data = read_existing_mkdocs_yml(base_path)
    
    # Start the mkdocs.yml content, only adding new sections to the existing one
    mkdocs_content = """site_name: Kubernetes Documentation
site_url: https://your-site-url.com
theme:
    name: 'material'
nav:
    - Home: index.md
"""
    
    # Base directory for the docs folder
    docs_folder = os.path.join(base_path, "docs")
    existing_nav = set()  # Track files and directories to avoid duplication
    existing_sections = set()

    # List all existing sections (folders) from the existing mkdocs.yml file
    for section in existing_data.get('nav', []):
        if isinstance(section, dict):
            for sec_name in section.keys():
                existing_sections.add(sec_name)

    # Traverse all the sections (folders) in the docs folder
    all_nav_items = []  # To hold all the sections for the new mkdocs.yml
    for section in os.listdir(docs_folder):
        section_path = os.path.join(docs_folder, section)
        if os.path.isdir(section_path) and section not in existing_sections:  # If it's a new section (folder)
            mkdocs_content += f"    - {section}:\n"
            nav_items, existing_nav = generate_nav_section(section_path, base_path, existing_nav)
            for nav_item in nav_items:
                mkdocs_content += f"{nav_item}\n"
            all_nav_items.append({section: [nav_item for nav_item in nav_items]})
    
    # If mkdocs.yml exists, update navigation by adding new items and removing deleted ones
    if existing_data:
        existing_nav_data = existing_data.get('nav', [])
        updated_nav_data = []

        # Iterate over the existing navigation in mkdocs.yml to remove deleted folders
        for item in existing_nav_data:
            if isinstance(item, dict):
                for section, subsections in item.items():
                    # If the section exists in the docs folder, preserve it
                    if section in os.listdir(docs_folder):
                        updated_nav_data.append(item)
                    else:
                        print(f"Section '{section}' has been deleted and will be removed from mkdocs.yml.")

        # Add the newly added sections (from the current folder structure) to mkdocs.yml
        for section in all_nav_items:
            updated_nav_data.append(section)

        # Rebuild the entire nav section in mkdocs.yml
        mkdocs_content += "nav:\n"
        for item in updated_nav_data:
            for section, subsections in item.items():
                mkdocs_content += f"    - {section}:\n"
                for subsection in subsections:
                    mkdocs_content += f"        - {subsection}\n"
    
    # Write or update the mkdocs.yml file
    with open(os.path.join(base_path, 'mkdocs.yml'), 'w') as f:
        f.write(mkdocs_content)

# Define the base path for the project folder
base_path = r"."  # Update to your full path if necessary

# Update the mkdocs.yml file based on existing folders and files
update_mkdocs_yml(base_path)

print(f"mkdocs.yml has been updated successfully at {base_path}.")
