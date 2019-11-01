from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['Keras==2.3.1',
                     'h5py==2.10.0',
                     'pandas-gbq==0.11.0',
                     'scikit-learn==0.20.2',
                     'joblib==0.14.0']

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Keras trainer application',
    scripts=['predictor.py']
)
