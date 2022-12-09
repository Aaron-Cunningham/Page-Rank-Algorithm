Code optimization
=================
1) As part of the optimization in the stochastic_page_rank method I directly 
imported the choice function instead of the full random Library.
2) As part of the optimization for stochastic_page_rank I initilizaed current_node
at the start of the method and then called it when carrying out the 
repeats.
3) As part of the distribution and stochastic method I used the fromkeys() method to set the next_prob[node] = 0 for all nodes
and hit_count[node] = 0 for all nodes. Although this didn't save much time, it made the code shorter and in my opinion easier to read.