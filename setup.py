import setuptools

with open('README.md', 'r') as f:
  long_description = f.read()

setuptools.setup(
  name='saneschema',
  version='2.3',
  scripts=['saneschema.py'],
  author='Murray Steele',
  author_email='contact@murto.dev',
  description='A simple JSON schema package',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/murto/saneschema',
  packages=setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
)
