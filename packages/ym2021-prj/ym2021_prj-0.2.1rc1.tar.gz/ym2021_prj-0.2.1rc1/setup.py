import setuptools
import setuptools_scm


setuptools.setup(
    version=setuptools_scm.get_version(),
    # use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
