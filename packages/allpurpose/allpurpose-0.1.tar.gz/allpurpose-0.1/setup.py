from setuptools import setup, find_packages

setup(
    name             = 'allpurpose',
    version          = '0.1',
    packages         = find_packages(),
    install_requires = [
        'Pillow==10.1.0'
    ],
    # More configurations can be added here.
)