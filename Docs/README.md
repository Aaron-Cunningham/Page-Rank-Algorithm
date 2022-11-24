### PC SPECS

* CPU: Intel i9-13900k
* RAM: 32GB Corsair DDR5 5600MHz
* GPU: RTX 3080Ti
* Windows 11

### Initial test timings unoptimized:
In these initial tests Repeats were set at 1,000,000
and Steps were set at 100.

Stochastic method average (Seconds): 
* 56.08 (Average after 5 tests)
* 5.04 (max hit_count over 5 tests)




Arguments:
=========
To run Stochastic method use:
```
python page_rank.py --method stochastic
```
Or:
```
python page_rank.py -m stochastic
```
To run Distribution method use:
```
python page_rank.py --method distribution
```
Or:
```
python page_rank.py -m distribution
```
To set number of repeats and steps use:
```
python page_rank.py --repeats= --steps= --method 
```

Optimized run Stochastic
========================
```
python3 page_rank.py --repeats=500_000 --steps=40 --method stochastic 
```