#!/usr/bin/env python

try:
    from setuptools import setup

    setup(name='document_classifier',
          version='1.0.0',
          description='document classification using machine learning and OCR',
          long_description=open('README.rst', 'rt').read(),
          author='Subrata Sarkar',
          author_email='subrotosarkar32@gmail.com',
          url='https://github.org/SubrataSarkar32/document_classifier/',
          packages=['document_classifier'],
          package_data = {'': ['*.txt', '*.json','*.rst','*.dll','*.exe']},
          include_package_data = True,
          install_requires=["nltk"],
          dependency_links=['git+ssh://git@github.com/deanmalmgren/textract.git@master', ],
          license='Apache v2.0',
          classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Environment::Console',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: Microsoft::Windows',
            'Topic::Scientific/Engineering::Information Analysis',
            'Programming Language :: Python :: 3.6',
            ]
          )

except ImportError:
    print('Install setuptools')
