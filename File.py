def modify_content(text):
    """
    Modify the file content in some way.
    For demo: convert everything to uppercase.
    """
    return text.upper()


def main():
    # Ask user for input filename
    input_file = input("Enter the filename to read: ").strip()

    try:
        # Try reading the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify content
        modified_content = modify_content(content)

        # Create output filename
        output_file = "modified_" + input_file

        # Write modified content to new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ File processed successfully! Modified file saved as: {output_file}")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied to read '{input_file}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
