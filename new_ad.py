import os
import yaml

# Function to create the mkdocs.yml file
def create_or_update_mkdocs_yml(base_path):
    # Start with the basic mkdocs.yml content
    mkdocs_content = {
        'site_name': 'Kubernetes Documentation',
        'site_url': 'https://your-site-url.com',
        'theme': {
            'name': 'material'
        },
        'nav': [
            {'Home': 'index.md'}
        ]
    }

    # Function to generate the nav structure from the folder structure
    def generate_nav_structure(base_path):
        nav = []
        # Traverse the docs directory to auto-detect sections and subsections
        for root, dirs, files in os.walk(os.path.join(base_path, 'docs')):
            # Skip files at the root level and only focus on directories
            if root == os.path.join(base_path, 'docs'):
                continue
            
            # Extract the section and subsection structure
            section_parts = root.split(os.path.sep)[-3:]  # Get last 3 parts (section -> subsection -> category)
            section = section_parts[0]
            subsection = section_parts[1] if len(section_parts) > 1 else None
            category = section_parts[2] if len(section_parts) > 2 else None

            # Ensure section exists in the nav structure
            section_nav = next((item for item in nav if section in item), None)
            if not section_nav:
                section_nav = {section: []}
                nav.append(section_nav)

            # Add files under the correct subsection category
            if subsection and category:
                file_paths = [os.path.join(root, f) for f in files if f.endswith('.md')]
                for file_path in file_paths:
                    file_name = os.path.basename(file_path)
                    subsection_name = file_name.replace('.md', '')
                    section_nav[section].append({subsection_name: file_path.replace(base_path + os.sep, '')})

        return nav

    # Generate the nav structure
    nav_structure = generate_nav_structure(base_path)
    
    # Add the dynamically generated nav sections
    mkdocs_content['nav'].extend(nav_structure)

    # Write the mkdocs.yml content to the file, creating or updating it
    with open(os.path.join(base_path, 'mkdocs.yml'), 'w') as f:
        yaml.dump(mkdocs_content, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"mkdocs.yml has been created/updated successfully at {base_path}/mkdocs.yml.")

# Define the base path for the project folder
base_path = '.'  # Adjust this to the path where you want to generate/update mkdocs.yml

# Create or update the mkdocs.yml file
create_or_update_mkdocs_yml(base_path)
