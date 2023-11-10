from setuptools import setup, find_packages

setup(
    name='pySynaptics',
    version='0.0.1', 
    author='Vincent Huang',
    author_email='vincenthsw@gmail.com',
    description='Python module for Synaptics touchpad and fingerprint sensors',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/',  # Replace with your repository URL
    packages=find_packages(),
    package_data={
        # Include the .so file in the package
        'pySynaptics': ['lib/csynaptics.so'],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update the license as needed
        'Operating System :: OS Independent',
    ],
    install_requires=[
        # List any Python dependencies here
        # e.g., 'numpy', 'pandas'
    ],
    python_requires='>=3.6',
)
