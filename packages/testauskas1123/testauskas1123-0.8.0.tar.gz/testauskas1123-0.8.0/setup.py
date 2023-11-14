from setuptools import setup, find_packages

setup(
    name='testauskas1123',
    version='0.8.0',
    packages=find_packages(),
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your project',
    long_description=""" test description """,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_package_name',
    project_urls={
        'Documentation': 'https://your-package-name.readthedocs.io',
        'Source': 'https://github.com/your_username/your_package_name',

    },
    keywords='your, keywords, here',
    license='MIT',

    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6',
)
