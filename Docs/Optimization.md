Code optimization
=================
1) As part of the optimization in the stochastic_page_rank method I directly 
imported the choice function instead of the full random Library 
and that saved roughly 2.5 seconds.
2) As part of the optimization for stochastic_page_rank I initilizaed current_node
at the start of the method and then called it when carrying out the 
repeats which saved roughly 1.5 seconds