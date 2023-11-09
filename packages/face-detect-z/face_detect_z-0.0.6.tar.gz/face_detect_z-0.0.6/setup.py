from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
  long_description = f.read()

setup(name='face_detect_z',  # 包名
      version='0.0.6',  # 版本号
      description='A small example package',
      long_description=long_description,
      author='aa',
      author_email='aa@qq.com',
      url='',
      install_requires=[],
      license='BSD License',
      packages=find_packages(),
      package_data={'': ['module2/*.bin'],
                  },
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )
