import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
  name=os.getenv('LIBRARY_NAME'),
  version=os.getenv('LIBRARY_VERSION'),
  author = os.getenv('LIBRARY_AUTHOR'),
  author_email=os.getenv('LIBRARY_AUTHOR_EMAIL'),
  description=os.getenv('SETUP_DESCRIPTION'),
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=os.getenv('COMPANY_HOMEPAGE'),
  packages=setuptools.find_packages(),
  keywords = ['northgravity, utils'],
  install_requires=[
        'requests>=2.31.0',
        'urllib3>=2.0.6',
        'scikit-learn>=1.3.2',
        'statsmodels>=0.14.0'
        ],
  python_requires='>=3.6',
  classifiers=[
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)