from setuptools import setup, find_packages

setup(
    name="Aplikacja Azon",
    version="0.3",
    author="Michał Pasierbiewicz",
    author_email="226001@student.pwr.edu.pl",
    description="Aplikacja do używania AZONu",
    license='MIT',
    url='https://github.com/Michal314-p/MPasierbiewicz_Python_pip.git',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.6',
    long_description=open('README.md').read(),
    zip_safe=False
)
