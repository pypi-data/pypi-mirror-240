from setuptools import setup, find_packages

setup(
    name='mylib-namik',
    version='0.0.2',
    description='this is my first lib',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Namig Masimov',
    author_email='masimovnamik@gmail.com',
    url='https://github.com/namigm/library_test',
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "my_lib": ["app.py"],
    },
    entry_points={"pytest11": ["pytest_pyreport = pytest_pyreport.plugin"]},
    classifiers=["Framework :: Pytest",
                 "Operating System :: OS Independent",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 3",
                 "Topic :: Software Development :: Testing"],
    keywords='selenium, python, pytest, testing, automation',
    install_requires=[
        'pytest'
    ],
    python_requires='>=3.8',
    license='MIT'
)