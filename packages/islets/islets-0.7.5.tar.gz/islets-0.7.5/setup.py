# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['islets', 'islets.serialization']

package_data = \
{'': ['*']}

install_requires = \
['bidict>=0.22,<0.23',
 'dash>=2.6.1,<3.0.0',
 'ffmpeg-python>=0.2,<0.3',
 'jupyter-dash>=0.4,<0.5',
 'jupyter-plotly-dash>=0.4,<0.5',
 'llvmlite==0.38.0',
 'matplotlib>=3.5,<4.0',
 'mgzip>=0.2,<0.3',
 'nd2reader>=3.3,<4.0',
 'numba>=0.55',
 'opencv-python>=4.6,<5.0',
 'openpyxl>=3.0.10,<4.0.0',
 'orjson>=3.7,<4.0',
 'pandas>=1.3.5,<1.4.0',
 'plotly>=5.9,<6.0',
 'python-bioformats>=4,<5',
 'python-javabridge>=4,<5',
 'scikit-image>=0.19,<0.20',
 'scikit-learn>=1.1,<2.0',
 'scipy>=1.9,<2.0',
 'statsmodels>=0.13,<0.14',
 'tqdm>=4.64,<5.0',
 'xlrd>=2.0,<3.0']

setup_kwargs = {
    'name': 'islets',
    'version': '0.7.5',
    'description': '',
    'long_description': '=========\nPhysio_Ca\n=========\n\n.. image:: https://img.shields.io/docker/v/hannsen/cell-tissue-networks_server/latest?logo=docker\n   :alt: Docker Image Version (tag latest semver)\n\n.. image:: https://img.shields.io/docker/image-size/hannsen/cell-tissue-networks_server/latest\n   :alt: Docker Image Size (tag)\n\n\nA toolbox to analyze and interact with Ca imaging data, developed within the Cell and Tissue Networks research group led by `prof. Marjan Slak-Rupnik <https://www.meduniwien.ac.at/web/index.php?id=688&res_id=37&name=Marjan_Slak%20Rupnik>`_ at the Medical University of Vienna. \n\nhttps://user-images.githubusercontent.com/2512087/162633046-b26d7c49-3501-4e78-9a33-433119157537.mp4\n\nA typical experiment involving imaging of pancreatic slices in our lab concerns a single field of view\nshowing up to hundreds of cells, in a recording of at least several, often dozens, gigabytes.\nCurrent tools (i.e. ImageJ) rely on loading the recording, or its part, into memory, for viewing, analysis, and processing.\nIt also requires laborious and long human engagement.\nWe have developed a set of interdependent tools to automatize as much as possible the analysis pipeline. \n\nThe main elements of our pipeline are the following:\n - Automatic detection of regions of interest (ROIs);\n - Transformation of ROI time traces into standard score ("z-score") and correction for filtering distortion;\n - Representation of the phenotype for each trace (height, auc, or halfwidth statistics, event rate...).\n - Quantification of the effect magnitude for acute pharmacological manipulations, and/or different experimental branches (different mice, or diet, of genetic manipulations).\n\n.. image:: https://user-images.githubusercontent.com/2512087/162617713-efd571a5-784e-4b2c-99ee-663f25457527.png\n\n\nDocumentation\n=============\n\nThe usage of the framework in practical terms is documented in the original repository at `https://github.com/szarma/Physio_Ca/ <https://github.com/szarma/Physio_Ca/>`_\n\n\nFeatures\n--------\n\nOne of our most used tools is the _\'\'roi examiner\'\'_ for live interaction with the ROIs and their traces within a jupyter notebook.\n\n.. image:: https://user-images.githubusercontent.com/2512087/162623035-c054b171-c222-47b0-905e-6f91fcb0caab.gif\n\nWe have a similar app to examine line scans.\n\n.. image:: https://user-images.githubusercontent.com/2512087/162633612-ad71e643-14bb-4e62-b0f0-21188ec4c10c.gif\n\nFor examine detected events, one at a time, we also have a app.\n\n.. image:: https://user-images.githubusercontent.com/2512087/162635307-6dea02ec-c56f-41ed-a275-efee595c1b9a.gif\n\nWe have also built a dashboard for fast intreaction with our storage filesystem. Given a folder, it finds all processed recordings in it and its subfolders, collects metadata and presents it in a table form. It further enables entering of the experimental protocol, and additional data, which are then also searchable. It also provides a link to an automaticaly generated notebook for a brief glimpse into actual results of an experiment. See demo on youtube (https://youtu.be/tj4TjL_PJ1Q).\n\nInstallation\n------------\n\nWe are working on an easy way of installation. For this purpose we use poetry as install tool.\nHowever, there will be ready-to-go packages available on PyPI via pip.\nFor easy deployment, there will be a docker image as well.\nDocumentation will be updated as soon as it is ready.\n\n\nDocker\n------\n\nA dockerfile is included in the root of the framework. It contains everything to run python code in the base environment. It can be built with the following command:\n\n.. code-block:: sh\n\n   docker build -t ctn_server .\n\nIf you do not want to build it yourself there is a prebuilt version on docker-hub. It can be pulled simly by:\n\n.. code-block:: sh\n\n   docker pull hannsen/cell-tissue-networks_server:latest\n\nAs an example, to run the server with custom data and access it in a shell you can use it like this:\n\n.. code-block:: sh\n   \n   docker run -it -v /path/to/real/data:/data:rw hannsen/cell-tissue-networks_server:latest /bin/bash\n\n\n',
    'author': 'Srdjan Sarikas',
    'author_email': 'srdjan.sarikas@meduniwien.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Hannnsen/Physio_Ca_framework',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
