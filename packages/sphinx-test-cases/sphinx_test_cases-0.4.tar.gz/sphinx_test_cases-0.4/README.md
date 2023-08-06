# Pytest description

Add a description of the test scenario in *reStructuredText*. Also
autodoc extension added.

## Thanks

Based on the two examples from the
[sphinx](https://www.sphinx-doc.org/en/master/development/tutorials/index.html) documentation:
+ recipies
+ intenum

## Gramma

Currently, there is only one directive (**test:test**) with few roles
- reqs (TODO: change from option)
- suite (TODO: read from mark)
- init
- passcrit
- step(s)
- desc

## Examples

1. Standalone (the `example/standalone/my_tests.rst` reStructuredText)
1. Docstring (embedded in the python script as a docstring of the
	`test_` functions)

## containerization

The examples could be executed using the docker container build by the `Dockerfile` from docker directory. On the docker hub, you can find the [image](https://hub.docker.com/repository/docker/arturim13/sphinx-testdec)

> docker pull arturim13/sphinx-testdec:01

## Build image

Execute in main repository directory (same as this README.md file)
> docker build -t arturim/sphinx-testdec -f docker/Dockerfile .
