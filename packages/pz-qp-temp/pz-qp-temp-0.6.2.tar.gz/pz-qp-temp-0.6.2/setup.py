from setuptools import setup

setup(
    name="pz-qp-temp",
    author="Alex Malz, Phil Marshall, Eric Charles",
    author_email="aimalz@nyu.edu, pjm@slac.stanford.edu, echarles@slac.stanford.edu",
    url = "https://github.com/LSSTDESC/qp",
    packages=["qp"],
    description="Quantile parametrization of probability distribution functions",
    setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
    long_description=open("README.md").read(),
    package_data={"": ["README.md", "LICENSE", "*.npy"]},
    use_scm_version={"write_to":"qp/_version.py"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    install_requires=["matplotlib",
                      "numpy",
                      "scipy>=1.9.0",
                      "scikit-learn",
                      "tables_io>=0.7.7"]                     
)
