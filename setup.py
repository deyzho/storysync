cat <<EOL > setup.py
from setuptools import setup, find_packages

setup(
    name="storysync",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    author="Your Organization",
    author_email="contact@your-org.com",
    description="Open-source framework for story-driven development",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/your-org/storysync",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
EOL