Installation
################

Create environment
**********************

If desired, install ``tafelvoetbal`` from an isolated Python environment using conda:

.. code-block:: python

    conda create -n env_tafelvoetbal python=3.8
    conda activate env_tafelvoetbal


Pypi
**********************

.. code-block:: console

    # Install from Pypi:
    pip install tafelvoetbal

    # Force update to latest version
    pip install -U tafelvoetbal


Github source
************************************

.. code-block:: console

    # Install directly from github
    pip install git+https://github.com/erdogant/tafelvoetbal


Uninstalling
################

Remove environment
**********************

.. code-block:: console

   # List all the active environments. tafelvoetbal should be listed.
   conda env list

   # Remove the tafelvoetbal environment
   conda env remove --name tafelvoetbal

   # List all the active environments. tafelvoetbal should be absent.
   conda env list


Remove installation
**********************

Note that the removal of the environment will also remove the ``tafelvoetbal`` installation.

.. code-block:: console

    # Install from Pypi:
    pip uninstall tafelvoetbal

