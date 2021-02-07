from distutils.version import StrictVersion
import setuptools
import subprocess
from os.path import dirname, exists, join

setup_dir = dirname(__file__)
git_dir = join(setup_dir, ".git")
version_file = join(setup_dir, "version.py")

# Automatically generate a version.py based on the git version
if exists(git_dir):
    # See https://www.python.org/dev/peps/pep-0440/#pre-releases for the version
    # number format the tag should follow. If there's no tag, "git describe"
    # will fail with exit status 128.
    version = (
        subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
        .decode()
        .rstrip()
    )

    # Verify tag follows version number format
    StrictVersion(version)

    # Create the version.py file
    with open(version_file, "w") as fp:
        fp.write('# Autogenerated by setup.py\n__version__ = "{0}"'.format(version))

if exists(version_file):
    with open(version_file, "r") as fp:
        exec(fp.read(), globals())
else:
    raise FileNotFoundError("No .git directory found")

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="frc-characterization",
    version=__version__,
    author="Eli Barnett, Dustin Spicuzza",
    author_email="emichaelbarnett@gmail.com, dustin@virtualroadside.com",
    description="FRC Characterization Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "frc_characterization",
        "frc_characterization.logger_analyzer",
        "frc_characterization.cli",
        "frc_characterization.logger_gui",
        "frc_characterization.newproject",
        "frc_characterization.robot",
        "frc_characterization.utils",
    ],
    entry_points={
        "console_scripts": ["frc-characterization = frc_characterization.cli:main"]
    },
    url="https://github.com/wpilibsuite/robot-characterization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy==1.19.3;platform_system=='Windows'",
        "control",
        "frccontrol",
        "matplotlib",
        "pynetworktables>=2018.1.2",
        "statsmodels",
        "argcomplete",
        "console-menu",
        "mako",
        "pint",
        "ruamel.yaml>=0.15",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
