from setuptools import setup
setup(
  name = 'Organize-my-photos',
  py_modules=['organize_my_photos'],
  version = '1.0.1',
  python_requires='>3.6',
  description = 'Terminal program that organizes and organizes the photographs in folders by year, month and day.',
  author = 'Andros Fenollosa',
  author_email = 'andros@fenollosa.email',
  url = 'https://github.com/tanrax/organize-my-photos',
  keywords = ['jpg', 'jpeg', 'sort', 'organize'],
  classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
  ),
  install_requires=[
      'Click>=6.7',
  ],
  entry_points='''
      [console_scripts]
      organize_my_photos=organize_my_photos:organize_my_photos
  '''
)
