from setuptools import setup, find_packages

setup(
    name='envrypt',
    version='0.0.5',
    author='Robin Syihab',
    license='MIT',
    author_email='robinsyihab@gmail.com',
    description='Python tool/library designed to secure environment variables by encrypting them both in disk and memory.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=2.7',
)
