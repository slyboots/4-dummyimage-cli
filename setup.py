from setuptools import setup

setup(
    name='dummyimage',
    version='0.1',
    description='Download dummy images from dummyimage.com',
    url='http://github.com/slyboots/dummyimage-cli',
    author='Slyboots',
    author_email='admin@slyb--ts.com',
    license='MIT',
    packages=['dummyimage'],
    zip_safe=False,
    scripts=['bin/dummyimage']
)