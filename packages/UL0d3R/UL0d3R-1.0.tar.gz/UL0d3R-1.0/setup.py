from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='UL0d3R',
    version='1.0',
    license='MIT License',
    author='Paulocesar0073',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='',
    keywords=['udemy'],
    description=u'Obter informações de Videos dos seus cursos da udemy.',
    packages=['UL0d3Rlib'],
    install_requires=['requests','colorama','ffmpeg-python','pyfiglet'],)



