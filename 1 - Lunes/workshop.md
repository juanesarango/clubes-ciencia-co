
# Taller de Programación con Python 🐍


## Pre-requisitos 🗿 

Para comenzar haremos uso de una terminal. Y chequearemos que las siguientes instalaciones estén disponibles. Y sino realizarlas:

* **Python**

    Instalaremos la version 3.x. Una buena guía de instalación es esta: [The Hitchhiker's Guide to Python][python-guide]. Para asegurarse de qué está instalado.

        python --version

    **Para Windows:** Descargar e instalar en la página de [descargas][python-windows].

    **Para MacOS** Recomendado utilizar [homebrew]:

        brew install python 

* **Pip**

    Pip es el instalador oficial de paquetes de python. Desde la versión 3.4 viene por defecto cuando se instala python.

        pip --version

    [Instalación][install-pip] de pip en caso de no estar instalado.
    

* **Virtualenvwrapper**

    Se utiliza para crear entornos locales. Los paquetes installados con pip solo pueden ser utilizados en esos ambientes.

    Para [Instalar][virtualenvwrapper] (En windows, se puede instalar con [virtualenvwrapper-win])



## Configuración de virtualenv y del Jupyter Lab 👩🏻‍🔬

1. **Virtualenv**

    Crear un virtualenv, llamado clubes-de-ciencia:

        mkvirtualenv clubes-de-ciencia

    Para activar de ahora en adelante el virtualenv:

        workon clubes-de-ciencia

    Para desactivar:

        deactivate

2. **Jupyter Lab**

    Installar [jupyter lab]

        pip install jupyterlab
    
    Ejecutar una instancia:

        jupyter lab



## Data Science Tutorials

* Jupyter Data science [tutorial][jupyter-data-science-tutorial].

    [Download](https://www.dataquest.io/blog/large_files/fortune500.csv) +500 fortune companies data. 50 años (1955-2005)

* [Tutorial][tutorial-ml-python] on machine learning and Data Science with Python




<!-- Referencias -->
[python-guide]: https://docs.python-guide.org/starting/installation/
[python-windows]: https://www.python.org/downloads/
[homebrew]: https://brew.sh/
[install-pip]: https://packaging.python.org/tutorials/installing-packages/
[virtualenvwrapper]:https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation
[virtualenvwrapper-win]: https://pypi.org/project/virtualenvwrapper-win/
[jupyter lab]: https://github.com/jupyterlab/jupyterlab
[jupyter-data-science-tutorial]:https://www.dataquest.io/blog/jupyter-notebook-tutorial/

[tutorial-ml-python]:(https://www.researchgate.net/publication/311555646_A_Tutorial_on_Machine_Learning_and_Data_Science_Tools_with_Python)
