from setuptools import setup

with open("README.md") as file:
    long_description = file.read()

setup(
    name="google_play_scrapper",
    packages=["google_play_scrapper"],
    version="0.0.1",
    license="MIT",
    description="This package is used to scrap data from google play for Feedbackio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Feedbackio",
    author_email="dev@feedbackio.com",
    url="https://bitbucket.org/feedbackio1/google-play-scraper/src/master/",
    keywords=["python"],
    install_requires=["tqdm>=4.62.0"],
)
