from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='legendador',
    version='0.0.1',
    description='Legendador de videos para o portugues ou esperanto',
    packages=['legendador'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    url = "",
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="PCO, Felipe Bombardelli",
    author_email="felipebombardelli@gmail.com",
    # url="https://github.com/bombark/iotproj",
    entry_points={'console_scripts': [
        'legendador = legendador:legenda',
    ]},
    install_requires=[
        'pathlib',
        'click',
        'opencv-python',
        'ffmpeg',
        'googletrans',
        'numpy',
        'sh'
    ]
)
