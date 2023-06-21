import os
import argparse
import logging

from config_project_structure import ProjectStructureConfig


class InitProject:
    @staticmethod
    def run(destination_dir: str, is_clean: bool):
        #
        project_structure = ProjectStructureConfig()

        #
        if is_clean:
            clean_destination(destination_dir, project_structure)

        #
        folder_dir = [
            os.path.join(destination_dir, f) for f in project_structure.PROJECT_FOLDER
        ]

        file_dir = [
            os.path.join(destination_dir, f) for f in project_structure.PROJECT_FILE
        ]

        #
        for dir in folder_dir:
            if not os.path.exists(dir):
                os.mkdir(dir)
                print("created: {}".format(dir))
            else:
                print("exist dir: {}".format(dir))

        #
        for dir in file_dir:
            if not os.path.exists(dir):
                open(dir, "a").close()
                print("created: {}".format(dir))
            else:
                print("exist dir: {}".format(dir))

        #
        print("finished init project")


def clean_destination(dir: str, structure):
    #
    print(
        "it will removes all folder/file in {}. please type 'yes' to confirm.".format(
            dir
        )
    )

    #
    while True:
        try:
            confirm = str(input("confirmation: "))
            if confirm == "yes":
                break
        except ValueError:
            pass

    #
    for root, _, files in os.walk(dir):
        if any(f in root for f in structure.PROJECT_FOLDER) or any(
            f in files for f in structure.PROJECT_FILE
        ):
            for file in files:
                remove_dir = os.path.join(root, file)
                os.remove(os.path.join(root, file))
                print("removed: {}".format(remove_dir))
            try:
                os.rmdir(root)
                print("removed: {}".format(root))
            except OSError:
                pass

    print("finished clean folder")


if __name__ == "__main__":
    #
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--destination_dir",
        required=True,
        help="destination to init project",
        type=str,
    )
    parser.add_argument(
        "--clean",
        action=argparse.BooleanOptionalAction,
        help="true if wanted to remove all sub-folder/file in destination folder. --clean: true | --no-clean: false | else none",
    )
    args = parser.parse_args()

    #
    destination_dir = args.destination_dir
    is_clean = args.clean if args.clean == True else False

    #
    InitProject.run(destination_dir, is_clean)
