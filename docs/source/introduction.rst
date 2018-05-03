
Introduction
============

This document describes the Little Hill Lab's initial requirements for an online application (Oh My Genes) which allows our scientists to upload gene expression files and quickly get differentially expressed genes.

Key words
----------

* Easy
* Quick
* Biologists
* Web application
* Data analyse

Purpose
------------

To identify differentially expressed genes given a gene expression file containing two cell samples.

Overview
--------------

This web application is a easy tool for biologists to quickly analyse genes.

User characteristics
----------------------

Biologists are busy analysing datas.
Biologists don't know much about computer science.
Biologists don't want the application so complicated.

Terminologies
------------

* Control sample - a cell sample prepared in its normal condition.
* Treatment sample - a cell sample treated by special chemicals, or in which some genes are altered.
* Differentially expressed genes - the genes which have significantly different expression levels between two samples.
* Up-regulation - a gene is said to be up-regulated if it has higher expression in treatment than in control.
* logFC - log fold change of gene expression. log_2 [T/C], where T is the gene expression level from a treatment sample, while C is the gene expression evel from a control sample.