ValAlgn: Value Alignment
========================

Description
-----------

Welcome to the documentation of the Value-Alignment (``valalgn``) package. This
package provides tools and functionalities for computing the *alignment* of a
normative system with respect to a *value* (or a set of values). The package
provides two modules:

1. ``valalgn.sampling`` computes the value alignment of a set of norms with
   respect to a value using simulation and approximate methods. It also includes
   functionalities for value-driven optimization of norms and evaluation
   metrics [1]_.
2. ``valalgn.asl`` implements the *Action Situation Language* (ASL) and
   interprets a set of norms written in this language and builds their
   operational semantics as an extensive-form game. This game can then be
   analyzed using standard game theoretical tools and solution concepts to
   derive the alignment of the norms that generated it [2]_.

References
----------

.. [1] Montes, N., & Sierra, C. (2022). Synthesis and properties of optimally
    value-aligned normative systems. Journal of Artificial Intelligence
    Research, 74, 1739–1774. https://doi.org/10.1613/jair.1

.. [2] Montes, N., Osman, N., & Sierra, C. (2022a). A computational model of
    Ostrom’s Institutional Analysis and Development framework. Artificial
    Intelligence, 311, 103756. https://doi.org/10.1016/j.artint.2022.103756

Credits
-------

Nieves Montes (IIIA-CSIC)
