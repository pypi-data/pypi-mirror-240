from setuptools import setup, find_packages
from setuptools.command.install import install


setup(
    name="ski_weather_utah",
    version="1.1",
    description="A server-side app that sends daily updates for weather at select Utah ski resorts.",
    author="Alex Calder",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "webdriver-manager",
        "configparser",
        "chromedriver-autoinstaller",
    ],
    entry_points={
        'console_scripts': [
            'ski-utah-config = ski_weather_utah.setup_script:run_setup_script',
            'ski-utah-cron = ski_weather_utah.configure_cron:main',
        ]
    }
)
