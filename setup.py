from setuptools import setup, find_packages
import switch_case


setup(
    name="switch_case",
    version=switch_case.__version__,
    author="Nikita Tsvetkov",
    author_email="nikitanovosibirsk@yandex.com",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nikitanovosibirsk/switch_case",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
    ],
)
