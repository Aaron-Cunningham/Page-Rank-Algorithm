import sys
import time
import argparse
from networkx import DiGraph
from random import choice
# Graph object created
graObj = DiGraph()


def load_graph(args):
    """Load graph from text file
    Parameters:
    args -- arguments named tuple
    Returns:
    A dict mapling a URL (str) to a list of target URLs (str).
    """
    # Iterate through the file line by line
    for line in args.datafile:
        # And split each line into two URLs
        node, target = line.split()
        # Code "G.add_node" & "G.add_edges" referenced from https://networkx.org/documentation/stable/tutorial.html
        # Added node
        graObj.add_node(node)
        # Added Edges
        graObj.add_edge(node, target)
    return graObj


def print_stats(graObj):
    """Print number of nodes and edges in the given graph"""
    # Code "G.number_of_nodes" & "G.number_of_edges" referenced from https://networkx.org/documentation/stable/tutorial.html
    print("The number of nodes is:", graObj.number_of_nodes())
    print("The number of edges is:", graObj.number_of_edges())


def stochastic_page_rank(graObj, args):
    """Stochastic PageRank estimation
    Parameters:
    graObj -- a graph object as returned by load_graph()
    args -- arguments named tuple
    Returns:
    A dict that assigns each page its hit frequency
    This function estimates the Page Rank by counting how frequently
    a random walk that starts on a random node will after n_steps end
    on each node of the given graph.
    """

    # Sets nodes to nodes in dict
    nodes = graObj.nodes
    # List of the nodes
    nodes_list = list(graObj.nodes)
    # initialize hit_count[node] with 0 for all nodes
    hit_count = dict.fromkeys(nodes, 0)

    # repeat n_repetitions times:
    for i in range(args.repeats):
        # current_node <- randomly selected node
        current_node = choice(nodes_list)
        # repeat n_steps times:
        for n in range(args.steps):
            # current_node <- uniformly randomly chosen among the out edges of current_node
            # Code "G.neighbors(x)" referenced from https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.neighbors.html
            current_node = choice(list(graObj.neighbors(current_node)))
        # hit_count[current_node] += 1/n_repetitions
        hit_count[current_node] += 1 / args.repeats
    return hit_count


def distribution_page_rank(graObj, args):
    """Probabilistic PageRank estimation

    Parameters:
    graObj -- a graph object as returned by load_graph()
    args -- arguments named tuple

    Returns:
    A dict that assigns each page its probability to be reached

    This function estimates the Page Rank by iteratively calculating
    the probability that a random walker is currently on any node.
    """

    node_prob = {}
    nodes = graObj.nodes
    # initialize node_prob[node] = 1/(number of nodes) for all nodes
    for node in nodes:
        node_prob[node] = 1 / len(nodes)
    # repeat n_steps times:
    for i in range(args.steps):
        # initialize next_prob[node] = 0 for all nodes
        next_prob = dict.fromkeys(nodes, 0)
        # for each node:
        for node in nodes:
            # p <- node_prob[node] divided by its out degree
            # Code "G.out_degree(X)" referenced from https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.out_degree.html
            p = node_prob[node] / graObj.out_degree(node)
            # for each target among out edges of node
            for target in graObj[node]:
                # next_prob[target] += p
                next_prob[target] += p
        # node_prob <- next_prob
        node_prob = next_prob
    return node_prob

parser = argparse.ArgumentParser(description="Estimates page ranks from link information")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                    help="Textfile of links among web pages as URL tuples")
parser.add_argument('-m', '--method', choices=('stochastic', 'distribution'), default='stochastic',
                    help="selected page rank algorithm")
parser.add_argument('-r', '--repeats', type=int, default=1_000_000, help="number of repetitions")
parser.add_argument('-s', '--steps', type=int, default=100, help="number of steps a walker takes")
parser.add_argument('-n', '--number', type=int, default=20, help="number of results shown")

if __name__ == '__main__':
    args = parser.parse_args()
    algorithm = distribution_page_rank if args.method == 'distribution' else stochastic_page_rank

    graph = load_graph(args)

    print_stats(graph)

    start = time.time()
    ranking = algorithm(graph, args)
    stop = time.time()
    time = stop - start

    top = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    sys.stderr.write(f"Top {args.number} pages:\n")
    print('\n'.join(f'{100 * v:.2f}\t{k}' for k, v in top[:args.number]))
    sys.stderr.write(f"Calculation took {time:.2f} seconds.\n")




