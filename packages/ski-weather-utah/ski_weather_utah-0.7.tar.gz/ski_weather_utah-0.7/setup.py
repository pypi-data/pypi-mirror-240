from setuptools import setup, find_packages

setup(
    name="ski_weather_utah",
    version="0.7",
    description="A server-side app that sends daily updates for weather at select Utah ski resorts.",
    author="Alex Calder",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "webdriver-manager",
        "configparser",
    ],
    entry_points={
        'console_scripts': [
            'ski-utah-config = ski_weather_utah.setup_script:run_setup_script',
        ]
    }
)
