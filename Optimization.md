Code optimization
=================
This part of my documentation is where I talk about the optimization steps I took to increase the speeds of the two methods used in my page rank algorithm.

## Imports
As part of my optimization, I used a few different methods. The first method I used to directly increase the speed of my stochastic
method was to directly import the random.choice module. I did this so the program didn't need to go searching through the
large random module. This saved some seconds but not much. 

## Initilizing
Another optimization I did was initializing current node at the start of my stochastic method. Although this didn't 
massively improve the speed of my algorithm it still showed some improvement. 

## Fromkeys()
The next step I took was for both distribution and stochastic methods. I used the fromkeys() method to set next_prob[node] = 0 for all nodes
and hit_count[node] = 0 for all nodes. Although this didn't save much time, it made the code shorter and in my opinion easier to read.

## Using networkx methods
The next step I took was for the stochastic method, I was originally using ```graObj[current_node]``` to access the out_edge of current_node
but since I was using networkx I thought it was more appropriate to use ```graObj.neighbors(current_node)```. This method is a part of
the networkx module. The implementation of this proved night and day, it was the main factor in reducing my stochastic 
algorithm time. The neighbors() method "Returns an iterator over all neighbors of node n. This is identical to iter(G[n])" (Referenced from 
 [https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.neighbors.html](https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.neighbors.html)).

## Dict comprehensions
The next optimization step I took was for the distribution method. Originally when initializing the node_prob[node] I was 
using the way it was described to me in the pseudocode```for node in nodes```. I noticed that in the notes on canvas it suggested using a list or dict 
comprehension to optimize, so I took advantage of this advice and made that part of the pseudocode into a dict comprehension.
Since the distribution method is already lightning fast, I didn't see any improvement as I was still getting the same
speeds. But I thought it was a good step to implement into my code.