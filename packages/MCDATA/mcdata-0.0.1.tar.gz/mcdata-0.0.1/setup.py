import setuptools

with open("README.md", "r") as fh:
      long_description = fh.read()

setuptools.setup(
      name="mcdata",
      version="0.0.1",
      author="Seu Nome",
      author_email="seu.email@exemplo.com",
      description="Uma descrição do meu pacote",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/seu_usuario/meu_pacote",
      packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
  )
