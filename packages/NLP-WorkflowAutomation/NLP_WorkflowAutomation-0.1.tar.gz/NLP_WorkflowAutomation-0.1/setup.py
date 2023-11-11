from distutils.core import setup
setup(
  name = 'NLP_WorkflowAutomation',         # How you named your package folder (MyLib)
  packages = ['NLP_WorkflowAutomation'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Este script Python proporciona un conjunto de funciones para realizar tareas comunes de procesamiento de lenguaje natural (NLP). Desde traducción de texto hasta análisis de sentimiento y resúmenes de archivos PDF, esta herramienta versátil simplifica la automatización de flujos de trabajo NLP.',   # Give a short description about your library
  author = 'Asier',                   # Type in your name
  author_email = 'asier.arnaz@alumni.mondragon.edu',      # Type in your E-Mail
  url = 'https://github.com/juneealonso/NLP_WorkflowAutomation.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/juneealonso/NLP_WorkflowAutomation/archive/refs/tags/v_0.1.tar.gz',    # I explain this later on
  keywords = ['NLP', 'TEXT', 'ANALYSES'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'deepl',
          'nltk',
          'math',
          'PyPDF2'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)