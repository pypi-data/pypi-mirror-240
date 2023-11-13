from setuptools import setup, find_packages

setup(
    name="antagonistic_game",
    version='0.7',
    package_data={'': ['*.ipynb']},
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26.1",
        "sciPy>=1.11.3"
    ],
    author="Fostenko O.A.| Buzin N.I., CMC MSU",
    author_email="oleg.fostenko.03@gmail.com",
    url="https://github.com/oscar-foxtrot/antagonistic_game_solver",
    project_urls={
        'Author (Fostenko O.A.)': 'https://vk.com/av1at0r',
        'Author (Buzin N.I.)': 'https://vk.com/buzin93',
        'Source Code': 'https://github.com/oscar-foxtrot/antagonistic_game_solver',
    },
    license='MIT'
)