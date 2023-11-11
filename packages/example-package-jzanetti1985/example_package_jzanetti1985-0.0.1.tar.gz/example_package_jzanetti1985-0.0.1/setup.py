from setuptools import setup, find_packages

setup(
    name='esr_dt_model',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'esr_dt_model=esr_dt_model.mymodule:write_to_file',
        ],
    },
)