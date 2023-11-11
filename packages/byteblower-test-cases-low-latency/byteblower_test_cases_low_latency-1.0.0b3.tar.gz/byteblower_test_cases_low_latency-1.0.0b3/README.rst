*****************************************************
ByteBlower - Traffic tests for Low Latency validation
*****************************************************

Usage
=====

Prepare runtime environment
---------------------------

We recommend managing the runtime environment in a Python virtual
environment. This guarantees proper separation of the system-wide
installed Python and pip packages.

Important: Working directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the following sections expect that you first moved to the directory where
you checked out this project.

On Unix-based systems (Linux, WSL, macOS):

.. code-block:: shell

   cd '/path/to/project/checkout'

On Windows systems using PowerShell:

.. code-block:: shell

   cd 'c:\path\to\project\checkout'

Python virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^

Prepare the Python virtual environment

On Unix-based systems (Linux, WSL, macOS):

.. note::
   *Mind the leading* ``.`` *which means* **sourcing** ``./env/bin/activate``.

.. code-block:: shell

   python3 -m venv --clear env
   . ./env/bin/activate
   pip install -U pip build

On Windows systems using PowerShell:

   **Note**: On Microsoft Windows, it may be required to enable the
   Activate.ps1 script by setting the execution policy for the user.
   You can do this by issuing the following PowerShell command:

   .. code-block:: shell

      PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

   See About Execution Policies for more information.

.. code-block:: shell

   python3.8.exe -m venv --clear env
   & ".\env\Scripts\activate.ps1"
   python -m pip install -U pip build

Project requirements
^^^^^^^^^^^^^^^^^^^^

Install this project as an *editable package*, including its runtime
dependencies.

.. code-block:: shell

   pip install -U -e .

Run the traffic test
--------------------

Command-line interface
^^^^^^^^^^^^^^^^^^^^^^

The test script can be run either as python module or as a command-line script:

For example (*to get help for the command-line arguments*):

#. As a python module:

   .. code-block:: shell

      python -m byteblower.test_cases.low_latency --help

#. As a command-line script:

   .. code-block:: shell

      byteblower-test-cases-low-latency --help

Run the traffic test with default/example configuration file
(``examples/low_latency.json``).

The reports will be stored under a subdirectory ``reports/``.

On Unix-based systems (Linux, WSL, macOS):

.. code-block:: shell

   . ./env/bin/activate

   # create the reports directory
   mkdir reports

   byteblower-test-cases-low-latency --report_path reports

On Windows systems using PowerShell:

.. code-block:: shell

   & ".\env\Scripts\activate.ps1"
   md reports
   byteblower-test-cases-low-latency --report_path reports

Integrated
^^^^^^^^^^

.. code-block:: python

   from byteblower.test_cases.low_latency import run

   # Defining test configuration, report path and report file name prefix:
   test_config = {}
   report_path = 'my-output-folder'
   report_prefix = 'my-dut-feature-test'

   # Run the traffic test:
   run(test_config, report_path=report_path, report_prefix=report_prefix)
