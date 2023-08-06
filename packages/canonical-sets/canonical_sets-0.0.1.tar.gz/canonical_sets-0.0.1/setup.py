# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['canonical_sets', 'canonical_sets.data', 'canonical_sets.models']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.2',
 'numpy>=1.22.3',
 'pandas>=1.4.2',
 'scikit-learn>=1.1.1',
 'scipy>=1.9.0',
 'tensorflow>=2.9.1',
 'torch>=1.11.0',
 'tqdm>=4.64.0']

setup_kwargs = {
    'name': 'canonical-sets',
    'version': '0.0.1',
    'description': 'Exposing Algorithmic Bias through Inverse Design.',
    'long_description': '.. |nbsp| unicode:: U+00A0 .. NO-BREAK SPACE\n\n.. |pic1| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue\n.. |pic2| image:: https://img.shields.io/github/license/mashape/apistatus.svg\n.. |pic3| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n.. |pic4| image:: https://img.shields.io/badge/%20type_checker-mypy-%231674b1?style=flat\n.. |pic5| image:: https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey\n.. |pic6| image:: https://github.com/Integrated-Intelligence-Lab/canonical_sets/actions/workflows/testing.yml/badge.svg\n.. |pic7| image:: https://img.shields.io/readthedocs/canonical_sets\n.. |pic8| image:: https://img.shields.io/pypi/v/canonical_sets\n\n.. _canonical_sets: https://github.com/Integrated-Intelligence-Lab/canonical_sets/tree/main/canonical_sets\n.. _examples: https://github.com/Integrated-Intelligence-Lab/canonical_sets/tree/main/examples\n.. _contribute: https://github.com/Integrated-Intelligence-Lab/canonical_sets/blob/main/CONTRIBUTING.rst\n\n.. _Twitter: https://twitter.com/DataLabBE\n.. _website: https://data.research.vub.be/\n.. _papers: https://researchportal.vub.be/en/organisations/data-analytics-laboratory/publications/\n\n\nCanonical sets \n==============\n\n|pic2| |nbsp| |pic5| |nbsp| |pic1| |nbsp| |pic8|\n\n|pic6| |nbsp| |pic7| |nbsp| |pic3| |nbsp| |pic4|\n\nAI systems can create, propagate, support, and automate bias in decision-making processes. To mitigate biased decisions,\nwe both need to understand the origin of the bias and define what it means for an algorithm to make fair decisions.\nBy Locating Unfairness through Canonical Inverse Design (LUCID), we generate a canonical set that shows the desired inputs\nfor a model given a preferred output. The canonical set reveals the model\'s internal logic and exposes potential unethical\nbiases by repeatedly interrogating the decision-making process. By shifting the focus towards equality of treatment and\nlooking into the algorithm\'s internal workings, LUCID is a valuable addition to the toolbox of algorithmic fairness evaluation.\nRead our paper on LUCID for more details.\n\nWe encourage everyone to `contribute`_ to this project by submitting an issue or a pull request!\n\n\nInstallation\n------------\n\nInstall ``canonical_sets`` from PyPi.\n\n.. code-block:: bash\n\n    pip install canonical_sets\n\nFor development install, see `contribute`_.\n\n\nUsage\n-----\n``LUCID`` can be used for the gradient-based inverse design to generate canonical sets, and is available for both\n``PyTorch`` and ``Tensorflow`` models. It\'s fully customizable, but can also be used out-of-the-box for a wide range of\nmodels by using its default settings:\n\n.. code-block:: python\n\n    from canonical_sets import LUCID\n\n    lucid = LUCID(model, outputs, example_data)\n    lucid.results.head()\n\nIt only requires a model, a preferred output, and an example input (which is often a part of the training data).\nThe results are stored in a ``pd.DataFrame``, and can be accessed by calling ``results``.\n\nFor detailed examples see `examples`_ and for the source code see `canonical_sets`_. We advice to start with either the\n``tensorflow`` or ``pytorch`` example, and then the advanced example. If you have any remaining questions, feel free to\nsubmit an issue or PR!\n\n\nData\n----\n``canonical_sets`` contains some functionality to easily access commonly used data sets in the fairness literature:\n\n.. code-block:: python\n\n    from canonical_sets import Adult, Compas\n\n    adult = Adult()\n    adult.train_data.head()\n\n    compas = Compas()\n    compas.train_data.head()\n\nThe default settings can be customized to change the pre-processing, splitting, etc. See `examples`_  for details.\n\n\nCommunity\n---------\n\nIf you are interested in cross-disciplinary research related to machine learning, feel free to:\n\n* Follow DataLab on `Twitter`_.\n* Check the `website`_.\n* Read our `papers`_.\n\n\nDisclaimer\n----------\n\nThe package and the code is provided "as-is" and there is NO WARRANTY of any kind. \nUse it only if the content and output files make sense to you.\n\n\nAcknowledgements\n----------------\n\nThis project benefited from financial support from Innoviris.\n\n\nCitation\n--------\n\n.. code-block::\n\n    @inproceedings{mazijn_canonicalsets_2022,\n      title={{Exposing Algorithmic Bias through Inverse Design}},\n      author={Mazijn, Carmen and Prunkl, Carina and Algaba, Andres and Danckaert, Jan and Ginis, Vincent},\n      booktitle={Workshop at International Conference on Machine Learning},\n      year={2022},\n    }\n',
    'author': 'Integrated Intelligence Lab',
    'author_email': None,
    'maintainer': 'Andres Algaba',
    'maintainer_email': 'andres.algaba@vub.be',
    'url': 'https://data.research.vub.be/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
