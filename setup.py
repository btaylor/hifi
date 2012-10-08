from distutils.core import setup

setup(
    name='hifi',
    version='0.1.0',
    author='Brad Taylor',
    author_email='bradt@ign.com',
    packages=['hifi'],
    url='https://github.com/btaylor/hifi',
    license='MIT',
    description='Get high-fidelity feedback from user emails',
    install_requires=[
        'PyYAML==3.10',
        'nltk==2.0.3',
        'numpy==1.6.2',
        'wsgiref==0.1.2', 
    ],
)
