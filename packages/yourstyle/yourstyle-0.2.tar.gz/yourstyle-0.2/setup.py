from setuptools import setup, find_packages

setup(
    name='yourstyle',
    version='0.2',
    packages=find_packages(),
    install_requires=['pygments>=2.0'],
    entry_points='''
        [pygments.styles]
        yourstyle = yourstyle.your_custom_style:YourCustomStyle
    '''
)
