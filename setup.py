from setuptools import setup, find_packages

setup(
    name="cascade2p",
    version="1.0",
    description="Calibrated inference of spiking from calcium ΔF/F data using deep networks",
    author="Peter Rupprecht",
    author_email="",
    packages=find_packages(),
    python_requires=">=3.7, <3.13",
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "tensorflow>=2.3, <=2.19",  # pip install CPU and GPU tensorflow
        "keras",
        "h5py",
        "seaborn",
        "ruamel.yaml",
    ],
)
