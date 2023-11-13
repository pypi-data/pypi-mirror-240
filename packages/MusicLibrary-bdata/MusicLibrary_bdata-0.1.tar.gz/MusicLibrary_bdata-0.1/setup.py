from distutils.core import setup
setup(
  name = 'MusicLibrary_bdata',         
  packages = ['MusicLibrary_bdata'],   
  version = '0.1',      
  license='MIT',        
  description = 'Allows users to search for songs and artist or albums and get inforation about them',
  author = 'Peio and Paule',                   
  author_email = 'peio.diaz@alumni.mondragon.edu',     
  url = 'https://github.com/pauleaguirre/MusicLibrary_bdata',   
  download_url = 'https://github.com/pauleaguirre/MusicLibrary_bdata/archive/refs/tags/v_02.tar.gz',    
  keywords = ['MUSIC', 'API', 'SEARCH'],   
  install_requires=[            
          'pandas',
          'numpy',
          'spotipy',
          'time',
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)