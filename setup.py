from setuptools import setup, find_packages

setup(
  name = 'bidirectional-cross-attention',
  packages = find_packages(exclude=[]),
  version = '0.0.5',
  license='MIT',
  description = 'Bidirectional Cross Attention',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/bidirectional-cross-attention',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'attention mechanism'
  ],
  install_requires=[
    'einops>=0.7',
    'torch>=2.0',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
