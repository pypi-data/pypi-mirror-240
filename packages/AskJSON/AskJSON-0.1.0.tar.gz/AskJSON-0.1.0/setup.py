from setuptools import setup, find_packages

setup(
    name='AskJSON',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'termcolor',
        'python-dotenv',
        'langchain',
        'stdlib-list',
        
        'python-Levenshtein'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A library to ask questions to JSON data and get Python code in response.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/AskJSON',  # Replace with the URL to your repository
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
