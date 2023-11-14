from setuptools import setup, find_packages

setup(
    name='pyprogramsimp',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        # Any dependencies you need can be listed here. For example:
        # 'numpy',
    ],
    author='Ziyan Zhou',
    author_email='5578699@qq.com',
    description='A simple package.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    # Add entry points if your package provides any executable scripts
    entry_points={
        'console_scripts': [
            'bop-cli = bop.command_line:main',
        ],
    },
)
