from setuptools import setup, find_packages

setup(
    name='colorpattern',
    version='1.0',
    author='croketillo',
    author_email='croketillo@gmail.com',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    description='ColorPattern is a Python module designed for enhancing text output in the console by applying color to specific patterns. It offers a flexible way to define patterns and apply different text colors, background colors, styles, and underlines to matching text in the output.',
    url='https://github.com/croketillo/colorpattern',
    classifiers=[
        'Environment :: Console',  # Proyecto diseñado para ejecutarse en la consola
        'Intended Audience :: Developers',  # Audiencia a la que se dirige el proyecto
        'Programming Language :: Python :: 3',  # Indica que el proyecto es compatible con Python 3
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Terminals',  # Relacionado con la manipulación de terminales y consolas
        'Topic :: Software Development :: Libraries :: Python Modules',  # Relacionado con desarrollo de software
        'Topic :: Utilities',  # Utilidades generales
    ],
    keywords='color pattern console',
    entry_points={
        'console_scripts': [
            'colorpattern = colorpattern.colorpattern:main',
        ],
    },
)
