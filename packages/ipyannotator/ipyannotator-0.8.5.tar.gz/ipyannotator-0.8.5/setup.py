# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ipyannotator',
 'ipyannotator.custom_input',
 'ipyannotator.custom_widgets',
 'ipyannotator.datasets',
 'ipyannotator.docs',
 'ipyannotator.ipytyping',
 'ipyannotator.services']

package_data = \
{'': ['*']}

install_requires = \
['PyPubSub>=4.0.0,<4.1.0',
 'ipycanvas>=0.10.2',
 'ipyevents>=0.8.0',
 'ipykernel>=5.3.4',
 'ipython>=8.0.1',
 'ipywidgets>=7.6.0',
 'matplotlib>=3.4.3',
 'pandas>=1.2.0',
 'pooch>=1.5.0,<1.6.0',
 'pydantic>=1.8.0,<1.9.0',
 'scikit-image>=0.19.3',
 'tqdm>=4.64',
 'traitlets>=5.1.1',
 'voila>=0.3.1']

setup_kwargs = {
    'name': 'ipyannotator',
    'version': '0.8.5',
    'description': 'The infinitely hackable annotation framework',
    'long_description': '# Ipyannotator - the infinitely hackable annotation framework\n\n![CI-Badge](https://github.com/palaimon/ipyannotator/workflows/CI/badge.svg)\n\nIpyannotator is a flexible annotation system. Developed to allow users to hack its features by extending and customizing it. \n\nThe large variety of annotation tasks, data formats and data visualizations is a challenging when dealing with multiple domains of supervised machine learning (ML). The existent tooling is often not flexible enough which imposes limitations to the user. By providing a framework where users can use, customize and create their own annotation tooling this projects aims to solve this problem.\n\nThe library contains some pre-defined annotators that can be used out of the box, but it also can be extend and customized according to the users needs. Check our [tutorials](https://palaimon.github.io/ipyannotator/docs/tutorials.html) for a quickly understanding of it\'s usage and check our [API](https://palaimon.github.io/ipyannotator/nbs/21_api_doc.html) for quick reference.\n\nThis library has been written in the [literate programming style](https://en.wikipedia.org/wiki/Literate_programming) popularized for jupyter notebooks by [nbdev](https://www.fast.ai/2019/12/02/nbdev/). In addition to our [online documentation](palaimon.github.io/ipyannotator) the jupyter notebooks located at `nbs/` allow an interactive exploration of the inner workings of Ipyannotator.\n\nWe hope this repository helps you to explore how annotation UI\'s can be quickly built using only python code and leveraging many awesome libraries ([ipywidgets](https://github.com/jupyter-widgets/ipywidgets), [voila](https://github.com/voila-dashboards/voila), [ipycanvas](https://github.com/martinRenou/ipycanvas), etc.) from the [jupyter Eco-system](https://jupyter.org/).\n\nAt https://palaimon.io we have used the concepts underlying Ipyannotator internally for various projects and this is our attempt to contribute back to the OSS community some of the benefits we have had using OOS software.\n\n## Please star, fork and open issues!\n\nPlease let us know if you find this repository useful. Your feedback will help us to turn this proof of concept into a comprehensive library.\n\n## Install\n\nIpyannotator is available on Pypi and can be installed using:\n\n`pip install ipyannotator`\n\n## Running ipyannotator\n\nIpyannotator provides a [simple API](https://palaimon.github.io/ipyannotator/nbs/21_api_doc.html) that provides the ability to explore, create and improve annotation datasets by using a pair of input/outputs. All pair of input/output are [listed on Ipyannotator\'s docs](https://palaimon.github.io/ipyannotator/nbs/22_input_output_doc.html). Check [Ipyannotator tutorials](https://palaimon.github.io/ipyannotator/docs/tutorials.html) for a quickly demonstration of the library.\n\n### Run ipyannotator tests\n\nTo run Ipyannotator\'s tests:\n\n1. Install [poetry](https://python-poetry.org/docs/#installation)\n2. Create the test environment with `poetry install`\n3. Activate the poetry environment using `poetry shell`\n4. Run tests by executing `nbdev_test_nbs`\n\n### Run ipyannotator as stand-alone web app using voila\n\nIpyannotator can be executed as a web app using the [voila](https://github.com/voila-dashboards/voila) library. The following sections describe how to run using poetry and pip.\n\n#### Using poetry\n\nOn your terminal:\n\n```shell\ncd {project_root}\npoetry install --no-dev\n```\n\nAny jupyter notebook with ipyannotator can be executed as an standalone web application. An example of voila usage it\'s available in the current repository and can be executed as it follow:\n\n```shell\npoetry run voila nbs/09_voila_example.ipynb --enable_nbextensions=True\n```\n\n#### Using pip\n\nThe installation and execution process can also be done using pip.\n\n```shell\n   cd {project_root}\n   \n   pip install .\n   pip install voila\n   \n   voila nbs/09_voila_example.ipynb --enable_nbextensions=True\n```\n\n## Jupyter lab trouble shooting\n\nFor clean (re)install make sure to have all the lab extencions active:\n\n`jupyter lab clean` to remove the staging and static directories from the lab \n\n _ipywidgets_:\n \n `jupyter labextension install @jupyter-widgets/jupyterlab-manager`\n \n _ipycanvas_:\n \n `jupyter labextension install @jupyter-widgets/jupyterlab-manager ipycanvas`\n \n _ipyevents_:\n \n `jupyter labextension install @jupyter-widgets/jupyterlab-manager ipyevents`\n \n _nbdime_:\n \n `nbdime extensions --enable [--sys-prefix/--user/--system]`\n \n _viola_:\n \n `jupyter labextension install @jupyter-voila/jupyterlab-preview`\n\n## How to contribute\n\nCheck out `CONTRIBUTING.md` and since ipyannotator is build using nbdev reading\nthe [nbdev tutorial](https://nbdev.fast.ai/tutorial.html) and related docs will be very helpful.\n\n## Additional resources\n\n![jupytercon 2020](https://jupytercon.com/_nuxt/img/5035c8d.svg)\n\n- [jupytercon 2020 talk](https://cfp.jupytercon.com/2020/schedule/presentation/237/ipyannotator-the-infinitely-hackable-annotation-framework/).\n\n- [Recording of jupytercon 2020](https://www.youtube.com/watch?v=jFAp1s1O8Hg) talk explaining the high level concepts / vision of ipyannotator.\n\n## Acknowledgements\n\nThe authors acknowledge the financial support by the Federal Ministry for Digital and Transport of Germany under the program mFUND (project number 19F2160A).\n\n## Copyright\n\nCopyright 2022 onwards, Palaimon GmbH. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this project\'s files except in compliance with the License. A copy of the License is provided in the LICENSE file in this repository.\n\n\n\n<!-- Matomo Image Tracker-->\n<img referrerpolicy="no-referrer-when-downgrade" src="https://matomo.palaimon.io/matomo.php?idsite=4&amp;rec=1" style="border:0" alt="" />\n<!-- End Matomo -->\n',
    'author': 'palaimon.io',
    'author_email': 'oss@mail.palaimon.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/palaimon/ipyannotator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
