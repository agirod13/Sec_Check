from setuptools import setup, find_packages

setup(
    name="sec_check",
    version="1.0.0",
    author="Anthony Girod",
    description="A tool to check for security.txt and robots.txt files and capture screenshots",
    packages=find_packages(),
    install_requires=[
        "requests",
        "playwright",
        "tldextract"
    ],
    entry_points={
        "console_scripts": [
            "sec-check=sec_check.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Security"
    ],
    python_requires='>=3.7',
)