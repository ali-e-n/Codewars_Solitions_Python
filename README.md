# Codewars Solotions For Python Problems

## Python Basics
- python is a high level programming language
- python is an interpreted language
- python is a dynamically typed language
- python is a general purpose language
- python is a scripting language
- python is a object oriented language
- python is a functional language
- python is a modular language
- python is a portable language
- python is a extensible language
- python is a embeddable language
- python is a embeddable language
- python is a extensible language
- python is a embeddable language

## Python Installation
- Download python from [python.org](https://www.python.org/downloads/)
- Install python
- Check python version by typing `python --version` in terminal
- Check pip version by typing `pip --version` in terminal
- Install pipenv by typing `pip install pipenv` in terminal
- Check pipenv version by typing `pipenv --version` in terminal

## Python Virtual Environment
- Create virtual environment by typing `pipenv shell` in terminal
- Install python packages by typing `pipenv install <package_name>` in terminal
- Install python packages by typing `pipenv install <package_name>==<version>` in terminal
## Table of python Data Types with description
| Data Type | Description |
| --- | --- |
| Text Type: | str |
| Numeric Types: | int, float, complex |
| Sequence Types: | list, tuple, range |
| Mapping Type: | dict |
| Set Types: | set, frozenset |
| Boolean Type: | bool |
| Binary Types: | bytes, bytearray, memoryview |

## Python Famous Libraries with description
| Library | Description |
| --- | --- |
| Numpy | NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. |
| Pandas | Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data. |
| Matplotlib | Matplotlib is a Python library used for plotting. It can create various types of plots and charts, and is rather easy to use. |
| Scikit-learn | Scikit-learn is a free software machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. |
| Scipy | SciPy is a free and open-source Python library used for scientific computing and technical computing. SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering. |
| Tensorflow | TensorFlow is a free and open-source software library for machine learning. It can be used across a range of tasks but has a particular focus on training and inference of deep neural networks. Tensorflow is a symbolic math library based on dataflow and differentiable programming. It is used for both research and production at Google. |
| Keras | Keras is an open-source software library that provides a Python interface for artificial neural networks. Keras acts as an interface for the TensorFlow library. |
| Pytorch | PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing, primarily developed by Facebook's AI Research lab. It is free and open-source software released under the Modified BSD license. |

## Python Famous Frameworks with description
| Framework | Description |
| --- | --- |
| Django | Django is a Python-based free and open-source web framework that follows the model-template-views architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit. Django's primary goal is to ease the creation of complex, database-driven websites. |
| Flask | Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. |

## Python Famous IDEs with description
| IDE | Description |
| --- | --- |
| Pycharm | PyCharm is an integrated development environment used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains. It provides code analysis, a graphical debugger, an integrated unit tester, integration with version control systems, and supports web development with Django. |
| Spyder | Spyder is an open source cross-platform integrated development environment for scientific programming in the Python language. Spyder integrates NumPy, SciPy, Matplotlib and IPython, as well as other open source software. |
| Jupyter Notebook | The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more. |
| Visual Studio Code | Visual Studio Code is a free source-code editor made by Microsoft for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git. Users can change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality. |

Codewars Kata training Solutions

# Katta 1
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

