from setuptools import setup, find_packages

setup(
    name="adaptive-dbscan",
    version="0.1.0",
    description="A python package for density adaptive DBSCAN clustering",
    long_description="a Python package for Density Adaptive DBSCAN (Density-Based Spatial Clustering of Applications with Noise) that incorporates a dynamic number of neighbor points based on a density map function",
    author="Sina Sabermahani",
    author_email="sina.sabermahani@gmail.com",
    url="https://github.com/Sinamahani/AdaptiveDBSCAN",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.26.0',
        'geopandas>=0.14.0',
        'pandas>=2.1.1',
        'matplotlib>=2.2.0',
        'pyproj>=3.6.1',
        'scipy>=1.11.3']
    
    
)
