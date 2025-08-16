from pybuilder.core import use_plugin, init

use_plugin("python.core")
#use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("pypi:pybuilder_pytest")
#use_plugin("pypi:pybuilder_pytest_coverage")
use_plugin("python.distutils")

default_task = "publish"
name = "pybuilder_project"

@init
def initialize(project):
    pass
    # project.set_property_if_unset("pytest_coverage_break_build_threshold", 50)
    # project.set_property("dir_source_main_python", "src/main/python")
    # project.set_property("dir_source_unittest_python", "src/unittest/python")
    # project.set_property("dir_source_main_scripts", "src/main/scripts")
    # project.set_property("dir_docs", "docs")
    # # Add other configurations as needed, e.g., project name, version
    # project.set_property("name", "python_dev_project")
