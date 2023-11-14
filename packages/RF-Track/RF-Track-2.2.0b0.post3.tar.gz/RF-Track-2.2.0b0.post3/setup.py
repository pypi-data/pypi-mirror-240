from setuptools import setup

setup(
    name='RF-Track',
    version='2.2.0b0-3',
    description='The CERN tracking code RF-Track',
    long_description= 'RF-Track is a tracking code developed at CERN for the optimization of particle accelerators, which offers outstanding flexibility and rapid simulation speed.\n\nRF-Track can simulate beams of particles with arbitrary energy, mass, and charge, even mixed, solving fully relativistic equations of motion.  It can simulate the effects of space-charge forces, both in bunched and continuous-wave beams. It can transport the beams through common elements as well as through special ones: 1D, 2D, and 3D static or oscillating radio-frequency electromagnetic field maps (real and complex), flux concentrators, and electron coolers. It allows element overlap, and direct and indirect space-charge calculation using fast parallel algorithms.\n\nRF-Track is written in optimized and parallel C++ and uses the scripting languages Octave and Python as user interfaces. General knowledge of Octave or Python is recommended to get the best out of RF-Track.',
    url='https://gitlab.cern.ch/rf-track',
    author='Andrea Latina',
    author_email='andrea.latina@cern.ch',
    license='Proprietary',
    packages=['RF_Track'],
    py_modules = ["RF_Track"],
    package_data={'': ['_RF_Track.so']},
    install_requires=['numpy', 'gsl' ],
    provides = ['RF_Track'],
    classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: C++",
    "License :: Other/Proprietary License",
    'Intended Audience :: Science/Research',
    "Operating System :: POSIX :: Linux",
    ],
    python_requires = "~=3.10",
    project_urls={
     'Documentation': 'https://gitlab.cern.ch/rf-track/download/-/raw/master/rf-track-2.2.0beta/RF_Track_reference_manual.pdf?ref_type=heads',
     'Tracker': 'https://gitlab.cern.ch/rf-track/rf-track-2.1/-/issues',
    },
)


