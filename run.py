import os

def replace_text_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        new_content, number_of_replacements = content.replace(old_text, new_text), content.count(old_text)
        if number_of_replacements > 0:
            with open(file_path, 'w') as file:
                file.write(new_content)
            print(f"Replaced text in: {file_path} ({number_of_replacements} replacements)")
        return number_of_replacements
    except Exception as e:
        print(f"Could not process file {file_path}: {e}")
        return 0

def scan_and_replace_in_directory(directory, old_text, new_text):
    total_replacements = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            replacements = replace_text_in_file(file_path, old_text, new_text)
            total_replacements += replacements
    return total_replacements

if __name__ == "__main__":
    parent_directory = "your_directory_path_here"  # Replace with your directory path
    old_text = "3306"
    new_text = "3307"

    total_replacements = scan_and_replace_in_directory(parent_directory, old_text, new_text)
    print(f"Total replacements made: {total_replacements}")
