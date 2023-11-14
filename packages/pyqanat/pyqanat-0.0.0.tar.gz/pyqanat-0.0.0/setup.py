from setuptools import setup, find_packages

setup(
    name='pyqanat',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        'paho-mqtt>=1.6.1',
        'networkx>=3.2.1',
    ],
    python_requires='>=3.11',
    # Metadata
    author='Your Name',
    author_email='',
    description='Create simple event-driven, distributed data pipelines in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jarombouts/qanat',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='data pipelines event-driven architecture microservices mqtt',
)
