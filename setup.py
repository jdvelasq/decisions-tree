from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='hardDecisions',
      version='0.0.0',
      description='Decision making tree modeling using Python',
      long_description='Decision making tree modeling using Python',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Office/Business :: Financial',
      ],
      keywords='decision-tree decision-making operations-research analytics',
      url='http://github.com/jdvelasq/hardDecisions',
      author='Juan D. Velasquez & Ibeth K. Vergara',
      author_email='jdvelasq@unal.edu.co',
      license='MIT',
      packages=['hardDecisions'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
