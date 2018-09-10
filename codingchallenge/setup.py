from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name="marsrovers",
            maintainer="David Bartalos",
            maintainer_email="",
            description="Mars rovers coding challenge",
            long_description="",
            url="https://github.com/dbartalos/boring-jennings/",
            download_url="https://github.com/dbartalos/boring-jennings/",
            license="MIT",
            packages=PACKAGES)


if __name__ == '__main__':
    setup(**opts)
