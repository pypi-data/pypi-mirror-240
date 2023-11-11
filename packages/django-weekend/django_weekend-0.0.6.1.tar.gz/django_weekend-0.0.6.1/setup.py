from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='django_weekend',
  version='0.0.6.1',
  author='Maksim Prilepsky',
  author_email='maksimprilepsky@yandex.ru',
  description='A simple library for tracking weekends and working days',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/MaksimJames/django_weekend',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='django calendar settings weekend',
  project_urls={
    'GitHub': 'https://github.com/MaksimJames/django_weekend'
  },
  python_requires='>=3.6'
)