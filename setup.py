from setuptools import setup, find_packages

setup(
    name='pyfuscator',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pyfuscator=pyfuscator:main',
        ],
    },
    author='Skyler Knecht',
    description='A Python obfuscation tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pyfuscator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
