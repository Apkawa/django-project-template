Установка зависимостей
======================
::

    sudo apt-get install python-sphinx python-alabaster

Для сборки latexpdf::

    sudo apt-get install  texlive-latex-recommended texlive-latex-extra  \
        texlive-fonts-recommended  texlive-xetex \
        ttf-liberation

Для сборки pdf::

    sudo apt-get install rst2pdf


Сборка документации
===================


Используется доработанный Makefile, сборка осуществляется так
Собирать нужно находясь в корне документации.

* Собрать всю документацию в определенную папку::


     BUILDDIR=path/to/compiled/doc/dir make html -e

* Собрать только часть документации, например nexta.
    Используется переменная SOURCEDIR, которая указывает на подпапку с документацией, в которой есть conf.py файл::


     BUILDDIR=path/to/compiled/doc/dir \
     SOURCEDIR: nexta \
        make singlehtml -e
