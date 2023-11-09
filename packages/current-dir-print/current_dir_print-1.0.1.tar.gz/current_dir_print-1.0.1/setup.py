from setuptools import setup, find_packages

setup(
    name="current_dir_print",
    version="1.0.1",
    description="Your package description",
    author="safafdaf Name",
    author_email="asfdsafasfa@email.com",
    packages=find_packages(),
    install_requires=[],
    entry_points = {
        "console_scripts": [
            "mycmd = current_dir_print:get_current_dir"
        ]
    }
)
