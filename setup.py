# for pypi package information
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynvme",
    version="2.0.3",
    author="Crane Chu",
    author_email="cranechu@gmail.com",
    description="builds your own tests.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pynvme/pynvme",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: C",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.5',
    install_requires=['pytest', 'pytemperature', 'pylspci', 'quarchpy'],
    data_files=[
        ('pynvme',
         ['nvme.so',
          'Makefile',
          'conftest.py',
          'driver_test.py',
          'pytest.ini']),
        ('pynvme/src',
         ['src/common.sh',
          'src/setup.sh']),
        ('pynvme/scripts',
         ['scripts/psd.py',
          'scripts/test_examples.py',
          'scripts/test_utilities.py']),
        ('pynvme/scripts/stress',
         ['scripts/stress/dirty_power_cycle_test.py']),
        ('pynvme/include/spdk',
         ['include/spdk/pci_ids.h']),
        ('pynvme/scripts/conformance/01_admin',
         ['scripts/conformance/01_admin/abort_test.py',
          'scripts/conformance/01_admin/identify_test.py',
          'scripts/conformance/01_admin/queue_test.py',
          'scripts/conformance/01_admin/firmware_test.py',
          'scripts/conformance/01_admin/dst_test.py',
          'scripts/conformance/01_admin/format_test.py',
          'scripts/conformance/01_admin/aer_test.py',
          'scripts/conformance/01_admin/sanitize_test.py',
          'scripts/conformance/01_admin/mi_test.py',
          'scripts/conformance/01_admin/features_test.py',
          'scripts/conformance/01_admin/logpage_test.py'
          ]),
        ('pynvme/scripts/conformance/02_nvm',
         ['scripts/conformance/02_nvm/compare_test.py',
          'scripts/conformance/02_nvm/flush_test.py',
          'scripts/conformance/02_nvm/read_test.py',
          'scripts/conformance/02_nvm/write_uncorrectable_test.py',
          'scripts/conformance/02_nvm/deallocate_test.py',
          'scripts/conformance/02_nvm/write_test.py',
          'scripts/conformance/02_nvm/verify_test.py',
          'scripts/conformance/02_nvm/write_zeroes_test.py'
          ]),
        ('pynvme/scripts/conformance/03_features',
         ['scripts/conformance/03_features/hmb_test.py',
          'scripts/conformance/03_features/write_protect_test.py',
          'scripts/conformance/03_features/power_management_test.py',
          'scripts/conformance/03_features/reset_test.py'
          ]),
        ('pynvme/scripts/conformance/04_registers',
         ['scripts/conformance/04_registers/controller_test.py',
          'scripts/conformance/04_registers/power_test.py',
          'scripts/conformance/04_registers/pcie_test.py'
          ]), 
        ('pynvme/scripts/conformance/05_controller',
         ['scripts/conformance/05_controller/sq_cq_test.py',
          'scripts/conformance/05_controller/sqe_cqe_test.py',
          'scripts/conformance/05_controller/interrupt_test.py',
          'scripts/conformance/05_controller/prp_test.py',
          'scripts/conformance/05_controller/arbitration_test.py'
          ]),
        ('pynvme/scripts/conformance/06_tcg',
         ['scripts/conformance/06_tcg/use_case_test.py'
          ]),
        ]
)
