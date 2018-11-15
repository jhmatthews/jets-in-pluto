### Hydrodynamic jet simulations with PLUTO

This repository contains the files needed to reproduce the simulations from Matthews et al. 2018.

To compile, install PLUTO 4.3 then run 

```
python $PLUTO_DIR/setup.py 
```

in either the 2D or 3D directory. Follow the instructions to set up the problem and create the makefile (the definitions.h file will set the defaults). Choose gcc or mpicc definitions accordingly Then:

```
make
```

will produce a pluto executable. You can run a simulation with e.g.

```
./pluto -i f1.ini -x2jet
```
where the x2jet flag limits integration along the x2 axis. See pluto manual. 

Warning!: The 3D run takes a few days on 256 cores! The 2D run is much more tractable and from memory can be run overnight on 48 cores or so. 

Warning 2!: The code comments are out of date but I will try and fix this soon!

Warning 3!: I have not tested this with PLUTO 4.3 AT ALL. 
