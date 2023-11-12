from setuptools import setup, find_packages

setup(
    name='esr_dt_model',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        "pandas",
        "onnx",
        "skl2onnx",
        "onnxmltools",
        "darts"
    ],
    entry_points={
        'console_scripts': [
            'esr_dt_model=esr_dt_model.esr_dt_model:write_to_file',
        ],
    },
)