from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='MusicLibrary_bdata',
    packages=['MusicLibrary_bdata'],
    version='0.4',
    license='MIT',
    description='Allows users to search for songs and artist or albums and get information about them',
    author='Peio and Paule',
    author_email='peio.diaz@alumni.mondragon.edu',
    url='https://github.com/pauleaguirre/MusicLibrary_bdata',
    download_url='https://github.com/pauleaguirre/MusicLibrary_bdata/archive/refs/tags/v_03.tar.gz',
    keywords=['MUSIC', 'API', 'SEARCH'],
    install_requires=[
        'pandas',
        'numpy',
        'spotipy',
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
