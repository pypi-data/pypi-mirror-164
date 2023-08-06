---
title: KymoKnot - A software package and webserver to identify and locate knots
bibliography: pandoc/ref.bib
---
KymoKnot provides programs and libraries to localize the knotted portion of
knotted rings and linear chains.  A complete overview of this package and of the
webserver can be found in @kymoknot.  An interactive web-server interface is available at
[http://kymoknot.sissa.it/interactive.php](http://kymoknot.sissa.it/interactive.php).
When using Kymoknot, please cite @kymoknot.

Kymoknot adopts the Minimally-Interfering closure @minint to circularize both linear
chains and chain subportions.

This package currently provides 3 programs.

* `KymoKnot_ring.x`
* `KymoKnot_linear.x`
* `K_close.x`


The first two programs locate knots, respectively on ring and linear chains,
using the simplification only as a mean to reduce the number of chain
subportions to be considered in the search for the knotted portion. The
topology of each chain subportion is evaluated by closing the corresponding
portion of the original, unsimplified chain.  `K_close.x` takes an open chain
in input and closes it using the Minimally-Interfering closure scheme.

When searching for knotted portions, different search schemes identify
different entanglement properties of a chain and may in general give different
results.  For a detailed study, see ref @multiscale.  In the current version, the
bottom-up, top-down and  'unsafe' bottom-up search schemes can be used. The
bottom-up is enabled by default if no search scheme is specified by the user.

**Important.** KymoKnot identifies knots based on the Alexander determinants in
$t=-1$ and $t=-2$ @minint.
Prime knots with 8 or more crossings can have the same
Alexander determinants of other knots, including composite one; therefore the
code must be used with caution when analyzing complex knots.
The table of known knots is in the header file `KNT_table.h`.

[1]: 1. Tubiana L., Orlandini E, Micheletti C
[Probing the Entanglement and Locating Knots in Ring Polymers: A Comparative Study of Different Arc Closure Schemes](http://ptp.ipap.jp/link?PTPS/191/192) Progress of Theoretical Physics supplement, 192, 192-204 (2011)

[2]: 2. Tubiana L., Orlandini E, Micheletti C
[Multiscale entanglement in ring polymers under spherical confinement](http://prl.aps.org/pdf/PRL/v107/i18/e188302)
Phys. Rev. Lett. 107, pg 188302 (2011).

## 15-02-2018

KymoKnot is a direct evolution of [LocKnot](https://bitbucket.org/locknot/locknot)

## References
<div id="refs"></div>

## Installation
This project makes use of [qhull](http://www.qhull.org/).   
In case your package manager provides the library and it is installed, the build
system will use that version, otherwise it will compile also the local version of libqhull.
The library is needed by the Minimally-Interfering closure algorithm.

Run `make docs` to produce a README file in pdf. Requires [pandoc](https://pandoc.org/).


The project builds three targets:
- the C binaries
- the python bindings module for C binaries
- the python bindings binary, just for development purposes

### cmake build

The build system of kymoknot is cmake.
To build:
```console
$ git clone --recursive https://gitlab.physics.unitn.it/luca.tubiana/kymoknot-devel.git
$ cd kymoknot-devel/
$ mkdir build
$ cd build/
$ cmake ..
$ make
$ sudo make install
```

The cmake build offers the following parameters:

- BUILD_OWN_LIBS (default value OFF)  
    the parameter forces cmake to build also the external dependencies, even if already present in the system.
    Currently the only dependency is libqhull.

It is possible to change cmake build parameters using the standard cmake syntax.    
```
$ cmake -DBUILD_OWN_LIBS=ON ..
```


### Python bindings package build

This project provides some python bindings distributed as a python module called `kymoknot`.  

Prerequisites:
```console
$ pip3 install build
```

Then the build is launched with:
```console
$ python3 -m build
```

The build procedure will create the directory `kymoknot-devel/dist` containing the .whl python package.
```console
$ pip3 install dist/kymoknot_py-*.whl
```

The python package that provides the module can be built to use the system qhull libraries or 
to use the local version of the qhull library in a static fashion.
To switch between the dynamically linked build and the static one, users are required to define the QHULL_PREFIX environment
variable with the qhull installation path.
When the variable is defined, the kymoknot/build.py script will use that path instead of relying on pkg-build.

```console
$ export QHULL_PREFIX="/usr/local"
$ python3 -m build
```

If your OS does not provide a libqhull package or the provided one is ignored by cmake (for example on Ubuntu 18.04 and Ubuntu 20.04),
you will have to compile libqhull before building the python module.
See [cmake build](#cmake-build) section.


```console
$ git clone --recursive https://gitlab.physics.unitn.it/luca.tubiana/kymoknot-devel.git
$ cd kymoknot-devel/
$ mkdir build
$ cd build/
$ cmake ..
$ make
$ sudo make install
$ cd .. 
$ export QHULL_PREFIX="/usr/local"
$ python3 -m build
$ pip3 install dist/kymoknot_py-*.whl
```


### Python bindings binary build

```console
$ python3 kymoknot/build.py dev
```

Please note that when building the module binary this way, when calling 
```python
import kymoknot
```
from a script, the python code is actually loaded from ```kymoknot-devel/kymoknot``` directory and using the 
binary produced by cffi compilation (i.e.: ```_kymoknot_bindings.cpython-310-x86_64-linux-gnu.so```).
The first line of ```kymoknot/__init__.py``` will load the python module from the .so file:
```python
from _kymoknot_bindings import ffi, lib
```

#### Build and Installation on macOS

Prerequisites:

```
brew install cmake qhull pkg-config
```


After having activated your preferred conda or virtual environment:
```console
$ cd kymoknot-devel/
$ mkdir build
$ cd build/
$ cmake ..
$ make
$ cd ..
$ python3 -m build
$ pip3 install dist/kymoknot_py-0.9-*.whl


```

Building python module on macOS using own qhull sources:

```
$ cd kymoknot-devel/
$ mkdir build/ install/
$ cd build/
$ cmake -DBUILD_OWN_LIBS=ON -DCMAKE_INSTALL_PREFIX=$(pwd)/../install ..
$ make
$ make install
$ cd ..
$ export QHULL_PREFIX=$(pwd)/install/
$ python -m build
```

#### Docker builds
Some docker containers are provided to test build procedure in docker/ directory.
To build in a docker container:

```console
$ cd kymoknot-devel
$ docker build -t kymoknot_build_u1804 $(pwd)/docker/ubuntu_18.04 
$ docker run -it --rm -v $(pwd):/root/kymoknot-devel kymoknot_build_u1804
```

The build script will create the executables and the python module in build/ and
dist/ directories.
However, the build results are suited for the docker image, hence cannot be used in 
the host system (unless it matches the one of the docker image).

        
## Usage
usage: `KymoKnot_ring.x [options] input_file` (the same holds for KymoKnot_linear.x).

The input file must use the format:
```
        N
        x y z
        x y z
        ...
```
where N is the length of the coordinate sets.  If the input files contain
coordinate of rings, the edges `x_0 y_0 z_0` and `x_(N-1) y_(N-1) z_(N-1)` must
coincide.  **A sequence of configurations can be passed one after the other in
the same input file.**


### OUTPUT
- `BU__`  [ -b option ]: shortest knotted portion. Bottom-up search
- `NBU__` [ -u option ]: bottom-up search, without unknottedness check on complementar arc
- `TD__`  [ -t option ]: shortest continuosly knotted portion. Top-down search

### OUTPUT FILE FORMAT:
For `Kymoknot_linear.x` and `Kymoknot_ring.x`:
```
index Adet_1 Adet_2 Knot_id start end length
```
* index: index of the chain in the input sequence, starting from 0.
* Adet_1, Adet_1: Alexander determinants
* Knot_id: Rolfsen knot id, see `KNT_table.h`
* start: knot starting bead
* end: knot ending bead
* lenght: length of the knotted portion

#### Notes on the output
1. When several knotted portions are found they are printed on the same line.
Therefore, **the number of columns in output is not fixed**
2. The knot is identified on the whole chain, knotted portion will have the
topology of the whole chain.
3. In rings, the start of the knot can come after its end, if the knot includes
the first bead on the chain.
4. When performing a bracketed knot search with options `-F` and `-T`, it is
possible that no knot is found in the given search window. In that case the
output line is left empty and a Warning is printed to screen.

-------------------------------------------------------
## OPTIONS:
* `-h`:              print this help and exit.
* `-s <max_stride>`:         maximum stride for rectification. Default is 2% the chain length. Negative values in input set the stride to unlimited
* `-m <mem_size>`:   USE WITH CAUTION! Set the size of memory manually. Insert the expected length of the chain after simplification.
* `-r <seed>`:       set the pseudo random number generator's seed. Default: use time()+getpid().
* `-b`:      		Perform bottom-up search. ( DEFAULT )
* `-t`:      		Perform top-down search.  ( DEFAULT )
* `-u`:      		Perform bottom-up search without checking the complementar arc.
* `-F <start>`: ("From", use only in conjunction with -T) perform knot search between `<start>` and `<end>`, included.
* `-T <end>`: 	("To", use only in conjunction with -F) perform knot search between `<start>` and `<end>`, included.

Options `-F` and `-T` can be used also on rings, with `<start>` > `<end>` in
which case kymoknot will look for knots passing through the first bead in the
chain.

## Usage examples

* `Kymoknot_linear.x  linear_confs.dat`  Performs  a bottom-up search for knots,
with simplification stride set to 2% the length of each chain stored in `linear_confs.dat`
* `Kymoknot_ring.x -t ring_confs.dat`  Performs  a top-down search for knots,
with simplification stride set to 2% the length of each chain stored in `linear_confs.dat`
* `Kymoknot_ring.x -b -t -u ring_confs.dat` Performs bottom-up, top-down and
  "unsafe" searches.
* `Kymoknot_ring.x -s 5 ring_confs.dat` Performs a bottom-up search with maximum
stride set to 5 beads.
* `Kymoknot_ring.x -F 100 -T 20 ring_confs.dat` Performs a bottom-up search between
beads 100 and 20 of the rings, looking for knots passing through the origin.


### Python usage

The module can be used mainly in two ways:
- passing one or more numpy arrays
- passing the path of a file containing the data

The main purpose of the second way is to let the C code open and read the input data in a faster way 
(at least rather than reading them from python).

Here is an example of passing the input as numpy arrays:
```python

#!/bin/env/python

import kymoknot
from kymoknot.searchtype import SearchType
import numpy as np


if __name__ == "__main__":

    file_path = "example_configurations/linear/start_A_3_1_N1024.knt"
    chains = [x for x in kymoknot.read_file(file_path)]

    kl = kymoknot.KymoKnotSearch(
            seed=0,
            closure_type=kymoknot.CL_QHULLHYB,
            close_subchain=kymoknot.CL_QHULLHYB,
            search_type=[SearchType.BU],
            )

    chain_res = kl.search(chains, kymoknot.INP_LINEAR)
    res = chain_res[SearchType.BU]

    #res[0] because res is a list containing an entry for each chain in input
    #and the example file contains 1 chain
    for ke in res[0]:
        print("{}".format(ke))

```

To pass the input data as a file the sketch becomes:

```python
#!/usr/bin/env python

import kymoknot
from kymoknot.searchtype import SearchType
import numpy as np

if __name__ == "__main__":

    file_path = "example_configurations/linear/start_A_3_1_N1024.knt"

    kl = kymoknot.KymoKnotSearch(
            seed=0,
            search_type=[SearchType.BU, SearchType.TD],
            )

    chain_res = kl.search(file_path, kymoknot.INP_LINEAR)
    res_bu = chain_res[SearchType.BU]
    res_td = chain_res[SearchType.TD]

    print("RES - bottom-up")
    for idx, chain_res in enumerate(res_bu):
        print(f"chain: {idx}")
        for ke in chain_res:
            print(ke)
        print("")

    print("RES - top-down")
    for idx, chain_res in enumerate(res_td):
        print(f"chain: {idx}")
        for ke in chain_res:
            print(ke)
        print("")

```


## Changelog

### 31-07-2020
* Expanded `README.md`
* Corrected a bug which caused Kymoknot to fail if run on files containing a
sequence of rings with different lengths.

### 15-02-2018
KymoKnot is a direct evolution of [LocKnot](https://bitbucket.org/locknot/locknot)

