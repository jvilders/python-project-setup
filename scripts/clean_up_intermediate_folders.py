import os
import shutil


def clean_up_intermediate_folders() -> None:
    print(os.listdir())
    shutil.rmtree("package_name_here")
    shutil.rmtree("out")
