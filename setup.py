from setuptools import setup, find_packages

setup(
    name="aifootprintcleaner",
    version="0.1.0",
    author="Adriano A. Santos",
    author_email="adriano@copin.ufcg.edu.br",
    description="Package for removes invisible Unicode characters, control codes, and non-printable artifacts commonly introduced by AI assistants like ChatGPT, Copilot, and others",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
