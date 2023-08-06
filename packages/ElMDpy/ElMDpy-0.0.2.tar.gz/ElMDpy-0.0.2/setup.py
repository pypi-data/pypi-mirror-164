from setuptools import setup, find_packages

setup(
  name = 'ElMDpy',        
  packages = ['ElMD'],  
  version = '0.0.2',
  license='GPL3',       
  description = 'An implementation of the Element movers distance for chemical similarity of ionic compositions',  
  author = 'Cameron Hagreaves',            
  author_email = 'cameron.h@rgreaves.me.uk', 
  url = 'https://github.com/lrcfmd/ElMD/',   
  download_url = 'https://github.com/lrcfmd/ElMDpy/archive/v0.0.2.tar.gz',    
  keywords = ['ChemInformatics', 'Materials Science', 'Machine Learning', 'Materials Representation'],  
  package_data={"elementFeatures": ["el_lookup/*.json"]}, 
  include_package_data=True,
  install_requires=[ 
          'setuptools',
          'numpy',
          'scipy',
          'flit',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',  
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3) ',   
  ],
)
