from setuptools import setup, find_packages


VERSION = "0.0.11"
DESCRIPTION = f"""
Chordix uses harmony theories to analyse chords, chord progressions and midi music segments.
"""
PACKAGES = [p for p in find_packages() if 'test' not in p]


setup(
    name="Chordix",
    version=VERSION,
    author="Jason Lee",
    author_email="2593292614@qq.com",
    description=DESCRIPTION,
    long_description=open('README.md', 'r', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    install_package_data=True,
    package_data={'': ['*.txt', '*.md', '*.json', '*.png']},
    url="https://github.com/JasonLee-p/Chordix",
    install_requires=[
        'numpy==1.21.2',
    ],
    packages=PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
)
