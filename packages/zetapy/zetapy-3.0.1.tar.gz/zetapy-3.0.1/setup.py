from setuptools import setup
from setuptools import find_packages

setup(
    name='zetapy',
    version='3.0.1',
    description='Implementations of the ZETA family of statistical tests.',
    url='https://github.com/JorritMontijn/zetapy',
    author='Jorrit Montijn, Guido Meijer & Alexander Heimel',
    author_email='j.s.montijn@gmail.com',
    license='GNU General Public License',
    packages=find_packages(),
    install_requires=['scipy', 'numpy', 'matplotlib'],

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
