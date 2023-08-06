from setuptools import setup, find_packages


setup(
    name="standing-timer",
    version="0.0.1",
    license="MIT",
    author="Dante Poleselli",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/dpoleselli/StandingTimer/apps/timer",
    entry_points={
        "console_scripts": ["standing-timer=standing_timer.standing_timer:main"],
    },
    install_requires=["PySimpleGUI", "tinydb", "configparser"],
)
