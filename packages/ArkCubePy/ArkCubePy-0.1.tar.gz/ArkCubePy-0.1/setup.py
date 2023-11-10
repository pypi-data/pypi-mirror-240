from setuptools import setup, find_packages

setup(
    name='ArkCubePy',
    version='0.1',
    packages=find_packages(),
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ronan_wang_cw',
    author_email='rwang@cubewise.com',
    url='https://github.com/Cubewise-Asia/ArkCubePy',
    license='MIT',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)