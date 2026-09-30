from setuptools import setup, find_packages


setup(
    name="enterprise-python-automation",
    version="1.0.0",
    description="Automated PDF Report Generator",
    packages=find_packages(),
    install_requires=[
        "reportlab"
    ],
    entry_points={
        "console_scripts": [
            "report-generator=app.main:main"
        ]
    }
)
