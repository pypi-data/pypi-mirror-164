from setuptools import setup, find_packages


setup(
    name='os_emu',
    version='0.1',
    license='MIT',
    author="Korin",
    author_email='korin.mist@mail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/BendAndBlend/osemu',
    keywords='osemu',
)