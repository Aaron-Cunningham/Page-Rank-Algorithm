Page Rank
=========
This application calculates the page rank of the webpages stored in school_web.txt.
It utilises two methods:
1) Stochastic method
2) Distribution method

### PC SPECS

* CPU: Intel i9-13900k
* RAM: 32GB Corsair DDR5 5600MHz
* GPU: RTX 3080Ti
* Windows 11

### Optimization times
I have made a PDF file called ```Stochastic method before and after optimization evidence.pdf``` which is in the docs
folder with results before and after optimization for evidence that my program improved.

Furthermore, my optimization steps can be found in: ```Optimization.md``` 


Arguments:
=========
### In order to run the program from terminal please use the arguments listed below.

#### To run Stochastic method use:
```
python page_rank.py --method stochastic school_web.txt
```
```
python page_rank.py -m stochastic school_web.txt
```
#### To run Distribution method use:
```
python page_rank.py --method distribution school_web.txt
```
```
python page_rank.py -m distribution school_web.txt
```
#### To set number of repeats use (Default = 1,000,000):
```
python page_rank.py --method=stochastic --repeats=1000000 school_web.txt
```
```
python page_rank.py --method=distribution --repeats=1000000 school_web.txt
```
#### To set the number of steps use (Default = 100):
```
python page_rank.py --method=stochastic --steps=100 school_web.txt
```
```
python page_rank.py --method=distribution --steps=100 school_web.txt
```
#### To change number of Top Pages that show up in the results use (Default = 20):
```
python page_rank.py --method=stochastic --number=20 school_web.txt
```
```
python page_rank.py --method=distribution --number=20 school_web.txt
```