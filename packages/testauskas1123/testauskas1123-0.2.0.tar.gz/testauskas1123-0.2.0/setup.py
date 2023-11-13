from setuptools import setup, find_packages

setup(
    name='testauskas1123',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        # your dependencies go here
    ],
    entry_points={
        'console_scripts': [
            'your_script_name = your_package_name.module_name:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your project',
    long_description='A longer description of your project, typically from a README.md file',
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_package_name',
    project_urls={
        'Documentation': 'https://your-package-name.readthedocs.io',
        'Source': 'https://github.com/your_username/your_package_name',
        'Bug Reports': 'https://github.com/your_username/your_package_name/issues',
    },
    keywords='your, keywords, here',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6',
    extras_require={
        'dev': [
            # development dependencies go here
        ],
        'test': [
            # testing dependencies go here
        ],
    },
)
