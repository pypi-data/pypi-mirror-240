from setuptools import setup

with open("README.MD", "r") as arq:
    readme = arq.read()

setup(name='UL0d3R',
    version='0.0.1',
    license='MIT License',
    author='Paulocesar0073',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='',
    keywords=['udemy'],
    description=u'Obter informações de Videos dos seus cursos da udemy.',
    packages=['root'],
    install_requires=['requests','colorama','ffmpeg-python','pyfiglet'],)



