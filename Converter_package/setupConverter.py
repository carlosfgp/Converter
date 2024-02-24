import os


def setup_file_directory(dir_file_name):
    current_directory = os.path.dirname(__file__)
    print(f"Setting up directory/file \"{dir_file_name}\" on directory... \"{current_directory}\"")

    path = os.path.join(current_directory, dir_file_name)

    if not os.path.exists(path):
        os.makedirs(os.path.join(current_directory,dir_file_name))
        print(f"{dir_file_name} directory created")
    else:
        print(f"{dir_file_name} directory not created")

    if os.path.isfile(path):
        if not os.path.exists(path):
            with open(path, 'w') as file:
                file.write(f"{dir_file_name} file created.")
                print(f"{dir_file_name} file created successfully at:", path)
        else:
           print(f"{path} file already exists at:", path)


setup_file_directory("logs")
setup_file_directory(os.path.join(os.path.expanduser("~"),"Runbooks"))
setup_file_directory("config")
setup_file_directory("tmp")
