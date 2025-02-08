import os


def get_file_paths():
    file_paths = []
    print("Enter file paths separated by commas or new lines. Type 'n' to stop.")

    while True:
        user_input = input("File paths (or 'n' to stop): ")
        if user_input.strip().lower() == "n":
            break

        # Split input by commas or new lines and strip whitespace
        paths = [path.strip() for path in user_input.split(",") if path.strip()]
        for path in paths:
            if os.path.exists(path):
                file_paths.append(path)
            else:
                print(f"File {path} not found. Skipping.")

        print(f"Current valid file paths: {len(file_paths)}")

    if not file_paths:
        print("No valid file paths were provided.")
    return file_paths


def convert_compose_files(file_paths, output_directory="k8s"):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_path in file_paths:
        print(f"Converting {file_path}...")
        os.system(f"kompose --file {file_path} convert -o {output_directory}")


def main():
    file_paths = get_file_paths()
    if not file_paths:
        print("No valid files were provided. Exiting.")
        return

    convert_compose_files(file_paths)


if __name__ == "__main__":
    main()
