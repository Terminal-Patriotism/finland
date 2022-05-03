from setuptools import setup

setup(
    name = "finland",
    version = "0.1.0",
    description = "Prints finland flag",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/finland",
    packages = ["finland"],
    entry_points = {
        'console_scripts': [
            'finland = finland.__main__:main'
        ]
    },
)
