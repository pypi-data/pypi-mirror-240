import os
import click
import json
import pyperclip


# Create a command line group
@click.group(help='Codarcane - Your go-to repository for code snippets.')
def cli():
    pass


# The path to the JSON file
JSON_FILE_PATH = 'snippets/snippets.json'


# Helper function to load snippets from the JSON file
def load_snippets():
    snippets = []
    try:
        with open(JSON_FILE_PATH, 'r') as f:
            snippets = json.load(f)
    except FileNotFoundError:
        # If the file is not found, create an empty list
        snippets = []
    except json.JSONDecodeError:
        # Handle JSON decoding errors (invalid JSON)
        print('Error: Invalid JSON format in the snippets file.')
    return snippets


# Helper function to save snippets to the JSON file
def save_snippets(snippets):
    try:
        with open(JSON_FILE_PATH, 'w') as f:
            json.dump(snippets, f, indent=4)
    except FileNotFoundError:
        # If the file is not found, create the necessary directories and then save
        os.makedirs(os.path.dirname(JSON_FILE_PATH), exist_ok=True)
        with open(JSON_FILE_PATH, 'w') as f:
            json.dump(snippets, f, indent=4)
    except Exception as e:
        # Handle other exceptions (e.g., permission denied)
        print(f'Error: An error occurred while saving snippets - {e}')


# Helper function to export snippets as Markdown
def export_as_markdown(snippets, output_file):
    for snippet in snippets:
        output_file.write(f"**Title:** {snippet['title']}\n")
        output_file.write(f"**Language:** {snippet['language']}\n")
        output_file.write(f"```\n{snippet['code']}\n```\n\n")


# Helper function to export snippets as plain text
def export_as_text(snippets, output_file):
    for snippet in snippets:
        output_file.write(f"Title: {snippet['title']}\n")
        output_file.write(f"Language: {snippet['language']}\n")
        output_file.write(f"Code:\n{snippet['code']}\n\n")


# Command to add a new code snippet
@click.command(help='Add a new code snippet.')
def add():
    # Prompt the user for snippet details
    title = input('Enter snippet title: ')
    while not title.strip():  # Check for empty input
        print('Title cannot be empty.')
        title = input('Enter snippet title: ')

    # Validate title length (optional)
    max_title_length = 100
    if len(title) > max_title_length:
        print(
            f'Title is too long. Maximum length is {max_title_length} characters.')
        return

    language = input('Enter snippet language: ')
    while not language.strip():  # Check for empty input
        print('Language cannot be empty.')
        language = input('Enter snippet language: ')

    # Validate language length (optional)
    max_language_length = 20
    if len(language) > max_language_length:
        print(
            f'Language is too long. Maximum length is {max_language_length} characters.')
        return

    code = input('Enter the code snippet: ')

    # Load existing snippets from the JSON file
    snippets = load_snippets()

    # Append the new snippet to the list of snippets
    snippets.append({"title": title, "language": language, "code": code})

    # Write the updated list of snippets back to the JSON file
    save_snippets(snippets)

    print('Snippet added successfully!')


# Command to display all code snippets
@click.command(help='Display all code snippets.')
def display():
    # Load existing snippets from the JSON file
    snippets = load_snippets()

    # Display details of each snippet
    for snippet in snippets:
        print(f"Title: {snippet['title']}")
        print(f"Language: {snippet['language']}")
        print(f"Code: {snippet['code']}")


# Command to search for code snippets
@click.command(help='Search for code snippets by keyword.')
@click.argument('keyword')
def search(keyword):
    # Load existing snippets from the JSON file
    snippets = load_snippets()

    # Filter snippets based on the keyword in title or language
    results = [snippet for snippet in snippets if keyword.lower(
    ) in snippet['title'].lower() or keyword.lower() in snippet['language'].lower()]

    if results:
        # Display details of matching snippets
        for result in results:
            print(f"Title: {result['title']}")
            print(f"Language: {result['language']}")
            print(f"Code: {result['code']}")
    else:
        print('No matching snippets found')


# Command to copy a code snippet to the clipboard
@click.command(help='Copy a code snippet to the clipboard.')
def copy():
    # Load existing snippets from the JSON file
    snippets = load_snippets()

    # Display a list of snippets to choose from
    for idx, snippet in enumerate(snippets):
        print(f"{idx + 1}. {snippet['title']} - {snippet['language']}")

    # Prompt the user to select a snippet by number
    choice = int(input('Enter the number of the snippet to copy: ')) - 1

    if 0 <= choice < len(snippets):
        # Copy the selected snippet's code to the clipboard
        snippet = snippets[choice]
        pyperclip.copy(snippet['code'])
        print('Snippet copied to Clipboard!')

    else:
        print('Invalid choice.')


# Command to edit a code snippet
@click.command(help='Edit an existing code snippet.')
def edit():
    # Load existing snippets from the JSON file
    snippets = load_snippets()

    # Display a list of snippets to choose from
    for idx, snippet in enumerate(snippets):
        print(f"{idx + 1}. {snippet['title']} - {snippet['language']}")

    # Prompt the user to select a snippet by number for editing
    choice = int(input('Enter the number of the snippet to edit: ')) - 1

    if 0 <= choice < len(snippets):
        # Allow the user to choose which field to edit (title, language, or code)
        print("Select an option to edit:")
        print("1. Title")
        print("2. Language")
        print("3. Code")

        # Prompt the user to choose an option and validate it
        valid_options = [1, 2, 3]
        edit_option = None
        while edit_option not in valid_options:
            try:
                edit_option = int(
                    input('Enter the number of the field to edit: '))
            except ValueError:
                print('Invalid option. Please enter a number (1, 2, or 3).')

        if edit_option == 1:
            # Edit the snippet's title
            new_title = input('Enter the new snippet title: ')
            while not new_title.strip():  # Check for empty input
                print('Title cannot be empty.')
                new_title = input('Enter the new snippet title: ')
            # Validate title length (optional)
            max_title_length = 100
            if len(new_title) > max_title_length:
                print(
                    f'Title is too long. Maximum length is {max_title_length} characters.')
            else:
                snippets[choice]['title'] = new_title
        elif edit_option == 2:
            # Edit the snippet's language
            new_language = input('Enter the new snippet language: ')
            while not new_language.strip():  # Check for empty input
                print('Language cannot be empty.')
                new_language = input('Enter the new snippet language: ')
            # Validate language length (optional)
            max_language_length = 20
            if len(new_language) > max_language_length:
                print(
                    f'Language is too long. Maximum length is {max_language_length} characters.')
            else:
                snippets[choice]['language'] = new_language
        elif edit_option == 3:
            # Edit the snippet's code
            new_code = input('Enter the new code snippet: ')
            snippets[choice]['code'] = new_code

        # Write the updated list of snippets back to the JSON file
        save_snippets(snippets)

        print('Snippet edited successfully!')
    else:
        print('Invalid choice.')


# Command to delete a code snippet
@click.command(help='Delete an existing code snippet.')
def delete():
    # Load existing snippets from the JSON file
    snippets = load_snippets()

    # Display a list of snippets to choose from
    for idx, snippet in enumerate(snippets):
        print(f"{idx + 1}. {snippet['title']} - {snippet['language']}")

    # Prompt the user to select a snippet by number for deletion
    choice = int(input('Enter the number of the snippet to delete: ')) - 1

    if 0 <= choice < len(snippets):
        # Delete the selected snippet
        del snippets[choice]

        # Write the updated list of snippets back to the JSON file
        save_snippets(snippets)

        print('Snippet deleted successfully!')

    else:
        print('Invalid choice.')


# Command to export snippets to a different format
@click.command(help='Export snippets to a different format (markdown or text).')
@click.option('--format', type=click.Choice(['markdown', 'text']), default='markdown',
              help='Export format (markdown or text)')
@click.argument('output_file', type=click.File('w'))
def export(format, output_file):
    # Load existing snippets from the JSON file
    snippets = load_snippets()

    if format == 'markdown':
        export_as_markdown(snippets, output_file)
    elif format == 'text':
        export_as_text(snippets, output_file)

    print(f'Snippets exported to {format} file: {output_file.name}')


# Add the command function to the command group
cli.add_command(add)
cli.add_command(display)
cli.add_command(search)
cli.add_command(copy)
cli.add_command(edit)
cli.add_command(delete)
cli.add_command(export)


if __name__ == '__main__':
    cli()
