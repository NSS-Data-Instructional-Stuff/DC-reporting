from setuptools import setup

setup(
      name='dc',
      version='0.1',
      description='Shows summary reports for DataCamp team assignments.',
      author='Taylor Perkins',
      author_email='taylorperkins.dev@gmail.com',
      license='MIT',
      packages=['dc'],
      scripts=['bin/dc-reports'],
      install_requires=[
            'selenium==3.141.0',
            'pandas==0.25.3',
            # 'lxml===4.4.2',
            # 'html5lib==1.0.1'
      ],
      zip_safe=False
)
