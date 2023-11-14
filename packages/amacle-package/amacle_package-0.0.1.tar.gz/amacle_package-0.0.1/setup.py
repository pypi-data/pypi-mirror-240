from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'amacle_package'
LONG_DESCRIPTION = 'A package made by Amacle studio'

# Setting up
setup(
    name="amacle_package",
    version=VERSION,
    author="Amacle Studio (Gulshan Kumar)",
    author_email="<amacelstudio@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    # install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)