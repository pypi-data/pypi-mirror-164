|conda| |github ci| |Documentation| |PyPI Upload| |Conda Upload| |LICENSE| |Stable version| |Latest version|

.. |github ci| image::
   https://github.com/kocherlab/naps/actions/workflows/ci.yml/badge.svg?branch=main
   :target: https://github.com/kocherlab/naps/actions/workflows/ci.yml
   :alt: Continuous integration status

.. |Documentation| image::
   https://readthedocs.org/projects/naps/badge/?version=latest
   :target: https://naps.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |conda| image::
   https://anaconda.org/kocherlab/naps-track/badges/version.svg
   :target: https://anaconda.org/kocherlab/naps-track

.. |Conda Upload| image::
   https://github.com/kocherlab/naps/actions/workflows/upload_conda.yml/badge.svg
   :target: https://github.com/kocherlab/naps/actions/workflows/upload_conda.yml

.. |PyPI Upload| image::
   https://github.com/kocherlab/naps/actions/workflows/python-publish.yml/badge.svg
   :target: https://github.com/kocherlab/naps/actions/workflows/python-publish.yml

.. |LICENSE| image::
   https://anaconda.org/kocherlab/naps-track/badges/license.svg
   :target: https://github.com/kocherlab/naps/blob/main/LICENSE.md

.. |Stable version| image:: https://img.shields.io/github/v/release/kocherlab/naps?label=stable
   :target: https://github.com/kocherlab/naps/releases/
   :alt: Stable version

.. |Latest version| image:: https://img.shields.io/github/v/release/kocherlab/naps?include_prereleases&label=latest
   :target: https://github.com/kocherlab/naps/releases/
   :alt: Latest version

*******************************
NAPS (NAPS is ArUco Plus SLEAP)
*******************************

NAPS is a tool for researchers with two goals: (1) to quantify animal behavior over a long timescale and high resolution, with minimal human bias, and (2) to track the behavior of individuals with a high level of identity-persistence. This could be of use to researchers studying social network analysis, animal communication, task specialization, or gene-by-environment interactions. By combining deep-learning based pose estimation software with easily read and minimally invasive fiducial markers ("tags"), we provide an easy-to-use solution for producing high-quality, high-dimensional behavioral data.

.. figure:: https://naps.readthedocs.io/en/latest/_static/example_tracking.gif
   :width: 600px
   :align: center
   :alt: Example usage of NAPS to track a colony of common eastern bumblebees.

=============
Documentation
=============
NAPS documentation can be found at `naps.rtfd.io <https://naps.rtfd.io/>`_.

========
Features
========
* Easy, direct installation across platforms
* Built directly on top of `OpenCV <https://opencv.org/>`_ and `SLEAP <https://sleap.ai/>`_ with a modular, extensible codebase
* Flexible API that allows drop in of different methods for marker identification
* Multiprocessing through `Ray <https://docs.ray.io/>`_


============
Getting NAPS
============

------------
Easy install
------------
`conda` **(Windows/Linux)**:

.. code-block:: bash

    conda create -n naps naps-track -c kocherlab -c sleap -c nvidia -c conda-forge


`pip` **(any OS)**:

.. code-block:: bash

    pip install naps-track

==========
References
==========

If you use NAPS in your research, please cite:

   \S. W. Wolf, D. M. Ruttenberg*, D. Y. Knapp*, A. W. Webb, I. M. Traniello, G. C. McKenzie-Smith, J. W. Shaevitz, and S. D. Kocher. `Hybrid tracking to capture dynamic social networks <https://naps.rtfd.io/>`__. *In Prep*, n.d.

-------
BibTeX:
-------
.. code-block::

   @UNPUBLISHED{Wolf_undated,
      author = {Wolf, Scott W and Ruttenberg, Dee M and Knapp, Daniel Y and Webb,
               Andrew E and Traniello, Ian M and McKenzie-Smith, Grace C and Shaevitz, Joshua W and Kocher, Sarah D},
      title = {Hybrid tracking to capture dynamic social networks},
      year = {n.d.}
   }

======
Issues
======

------------------
Issues with NAPS?
------------------

1. Check the `docs <https://naps.rtfd.io/>`_.
2. Search the `issues on GitHub <https://github.com/kocherlab/naps/issues>`_ or open a new one.

============
Contributors
============

* **Scott Wolf**, Lewis-Sigler Institute for Integrative Genomics, Princeton University
* **Dee Ruttenberg**, Lewis-Sigler Institute for Integrative Genomics, Princeton University
* **Daniel Knapp**, Department of Physics, Princeton University
* **Andrew Webb**, Department of Ecology and Evolutionary Biology and Lewis-Sigler Institute for Integrative Genomics, Princeton University
* **Ian Traniello**, Lewis-Sigler Institute for Integrative Genomics, Princeton University
* **Grace McKenzie-Smith**, Department of Physics and Lewis-Sigler Institute for Integrative Genomics, Princeton University
* **Joshua Shaevitz**, Department of Physics and Lewis-Sigler Institute for Integrative Genomics, Princeton University
* **Sarah Kocher**, Department of Ecology and Evolutionary Biology and Lewis-Sigler Institute for Integrative Genomics, Princeton University

NAPS was created in the  `Kocher <https://kocherlab.princeton.edu/>`_  and `Shaevitz <https://shaevitzlab.princeton.edu/>`_ labs at Princeton University.

=======
License
=======

NAPS is licensed under the MIT license. See the `LICENSE <https://github.com/kocherlab/naps/blob/main/LICENSE.md>`_ file for details.

================
Acknowledgements
================

Much of the structure and content of the README and the documentation is borrowed from the `SLEAP repository <https://github.com/talmolab/sleap>`_.
