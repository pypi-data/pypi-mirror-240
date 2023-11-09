from setuptools import find_packages, setup

setup(
    name="planned",
    version="0.1.2",
    description="planned is job monitoring library which designed to observe user-defined triggers",  # noqa: E501
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nisaji/planned",
    author="nisaji",
    author_email="nisaji27@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
