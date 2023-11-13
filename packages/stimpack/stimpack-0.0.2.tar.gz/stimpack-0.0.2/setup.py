from setuptools import setup

setup(
    name='stimpack',
    version='0.0.2',
    description='Precise and flexible generation of stimuli for neuroscience experiments.',
    url='https://github.com/ClandininLab/stimpack',
    author='Minseung Choi',
    author_email='minseung@stanford.edu',
    packages=[
        'stimpack',
        'stimpack.rpc',
        'stimpack.experiment',
        'stimpack.experiment.util',
        'stimpack.visual_stim',
        'stimpack.device'
    ],
    package_dir = {"": "src"},
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        
        'platformdirs',
        'PyQT6',
        'h5py',
        'pyYaml',
        
        'moderngl',
        'scikit-image',
    ],
    entry_points={
        'console_scripts': [
            'stimpack=stimpack.experiment.gui:main'
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
