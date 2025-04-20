import os

def generate_tree(root_path, prefix=""):
    tree = ""
    try:
        items = sorted(os.listdir(root_path))
    except PermissionError:
        return f"{prefix}└── [Permission Denied]\n"

    for index, item in enumerate(items):
        path = os.path.join(root_path, item)
        connector = "└── " if index == len(items) - 1 else "├── "
        tree += f"{prefix}{connector}{item}\n"
        if os.path.isdir(path):
            extension = "    " if index == len(items) - 1 else "│   "
            tree += generate_tree(path, prefix + extension)
    return tree

# Get the absolute path of the script directory
script_dir = os.path.abspath(os.path.dirname(__file__))

# Set relative paths based on your directory structure
base_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "APPLICATION"))
output_path = os.path.abspath(os.path.join(script_dir, "..", "information", "directory.txt"))

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Generate the tree with "APPLICATION" as the root title
tree_text = "APPLICATION\n" + generate_tree(base_dir)

# Write the tree to file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(tree_text)

print(f"✔️ Directory tree saved to: {output_path}")
