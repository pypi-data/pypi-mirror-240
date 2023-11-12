from distutils.core import setup

setup(
  name='PredixJaueneko',
  packages=['PredixJaueneko'],
  version='0.1',
  license='MIT',
  description='A package for data analysis and modeling by Jaueneko',
  author='Jaueneko',
  author_email='joneneko.echeandia@alumni.mondragon.edu',
  url='https://github.com/enekoeo/jauenekoobtenermodelo',  # Reemplaza con el enlace de tu repositorio en GitHub
  download_url='https://github.com/enekoeo/jauenekoobtenermodelo/archive/refs/tags/v_01.tar.gz',  # Reemplaza con el enlace del archivo de descarga
  keywords=['data analysis', 'modeling', 'machine learning'],
  install_requires=[
    'scikit-learn',
    'matplotlib',
    'shap',
    'pandas',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
