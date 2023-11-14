from setuptools import setup, find_packages

setup(
    name='Baouly-packageIlogger',
    version='0.1.0',
    packages=find_packages(),
    author="Nelson Baouly",
    python_requires=">=3.2",
    url="https://github.com/BaoulyNelson/projetModule.git",
    description="",
    author_email="elconquistadorbaoulyn@gmail.com",
    install_requires=[
        # Ajoutez vos dépendances ici
    ],
    entry_points={
        'console_scripts': [
            'monprojet = monprojet.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        # Ajoutez d'autres classifications appropriées
    ],
)
