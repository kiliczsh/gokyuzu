from setuptools import setup, find_packages

setup(
    name='gokyuzu',
    version='0.0.1',
    description='bsky.social client library',
    author='Muhammed Kılıç',
    author_email='muhammeddkilicc@gmail.com',
    url='https://github.com/kiliczsh/gokyuzu',
    packages=find_packages(),
    install_requires=[
        'requests>=2.22.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
