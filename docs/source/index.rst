Welcome to QSM's documentation!
===============================

Introduction
=====================

The Qubit Simulation Module (QSM) is a software package that facilitates the full design process for
superconducting qubits and resonators. It is designed to be highly modular and accommodate any user-defined models,
but by default it uses those found in Chapter 4 of Dr. Long’s doctoral thesis found
`here <https://sites.google.com/view/junlings-research-homepage/thesis?authuser=0>`_.

It is written in Python with external calls to the Ansys HFSS, Q3D, and Nexxim simulators.

An example is included for reference. 

Overview
========

The QSM partitions the design process into two sequential phases: "Layout" and "Simulation/Calculation".
In the 'layout' phase, the user defines the geometry of their system, along with some basic properties such as
qubit inductance and CPW phase velocity.
In the 'simulation/calculation' phase they run various analyses based on the layout.
'Simulations' are analyses sufficiently complex to warrant saving the
results to data files for later use (includes all Ansys simulations, system quantization, and generally anything
involving matrix inversions), and 'calculations' are faster analyses that don't require saving. Note that both
simulations and calculations can be dependent on the results of other simulations/calculations, so the user needs to pay
careful attention to the order in which analyses are run.

The QSM user interface is a python script in which the user creates a qSysLayout object, then passes that object as
a parameter into their desired simulations/calculations.

Setup
^^^^^
To use the QSM the user needs to have a python 3 environment with the following installed:

* numpy
* gdspy
* sympy
* shapely
* matplotlib
* pathlib

To begin a design, make a fresh directory containing the template version of “driver.py” (found in the source
directory). In the header there is a variable called "computeLocation". This is used to differentiate between running
the QSM on a single Windows workstation ("Windows") and running it on a cluster ("Cluster").

Regardless of computeLocation, the variable "QSMSourceFolder" needs to be appropriately set. Nothing else in the header
needs to be touched by the user.

Layout
^^^^^^

Once the design directory is set up, the the user needs to generate and populate the following three layout files:

* systemParameters.json
* componentParameters.json
* componentGeometries.json

systemParams is generated via adding the following to driver.py::

    QSM.generateSystemParams(projectFolder)

The user then navigates to the design directory and runs driver.py, generating systemParameters.json.
Note that moving forward this process of entering a line into driver.py then running it will just be referred to as
"running a command".

Once systemParameters is generated the user needs to populate it with the numbers of each elements, along with various
other values.

Now that the system information is set, the qSysLayout object can be created. This is achieved via the command::

    qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)

**For all subsequent runs of driver.py this must be the first line after the header**. The only part of this line the
user needs to modify is layoutCompleted, which should remain false until the end of the layout phase.

Once systemParameters is populated, the user needs to generate and populate componentParameters.json. These are more
detailed inquiries about the various elements of the system. This is accomplished by running: ::

    qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
    qSys.generateComponentParams()

On populating componentParams the user needs to generate and populate componentGeometries.json via ::

    qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
    qSys.generateGeometries()

Once all three layout files are populated the user can generate the layout GDS via: ::

	qSys.generateGDS(addMesh=False, invertGDS=False)
	
Finally, the user switches layoutCompleted to True and can begin running analyses.

Simulation
^^^^^^^^^^

Simulations are classes found in simulations.py, and are used via instantiated objects taking qSys as their
sole argument: ::

    myFooSim = FooSim(qSys)

Methods of this object then perform the various stages of the simulation: ::

    myFooSim.initialize() # Creates the simulation directory and parameters file that requires user input
    myFooSim.run() # Runs all associated ansys simulations
    myFooSim.postProcess() # Runs all post processing steps once the ansys simulations are completed.

Note that because initialize() is typically followed by user input, and postProcess() can only be run once all
Ansys simulations are completed (which may be asynchronously computed on a cluster), the above commands are typically
run *one at a time*.

QSM comes with many built-in simulations for carrying out the NIST models. These simulations share the common
characteristic of not modifying the qSys object. For simulations that require results from other simulations, the
associated simulation objects are created and their results read. For example, the Quantize simulation requires the
output of CapMatGE, so CapMatGE has the getter function: ::

    CapMatGE(qSys).CapMatGE

that returns the simulated value, and Quantize will call that getter to access the value. In this way the qSys object
remains completely decoupled from the simulations, only ever containing layout information. While this is not a
forced paradigm, it is recommended from an extensibility standpoint.

Calculation
^^^^^^^^^^^
Because calculations do not involve ansys or cluster simulations, they are methods rather than classes.
They are simply called e.g. ::

	anharmonicityQCalc(qSys, q1Index, q2Index)


Details
=======

Layout
^^^^^^

Some fields in the layout files require specific input. The current available options are:

* systemParameters

  * Material -> perfect conductor, aluminum, etc. -> see Ansys material list.
  
  * Flip Chip? -> Currently just No, will be available shortly. 
  
  * Simulate Feedline? -> Yes, No. This determines if the feedline is included in the capacitance matrix simulation.
    For designs with known capacitances to the feedline it is faster to set this to No.
  
  * Chip Markers -> Pappas, Schmidt
  
  * Simulation -> 2D,3D. 3D is slower but likely more accurate for components that aren't approximately flat.
  
* componentParameters

  * Qubit Type: {Floating,Grounded}-rectangularPads-{single,double}JJ i.e. Floating-rectangularPads-singleJJ
  
  * Resonator/Qubit indices: Qubit/Readout resonator pairs **must share the same index**. Furthermore, the resonators 
    **must be numbered according to their position along the feedline**, with 0 being the left-most (for a straight unrotated feedline). 
    This is so the simulation knows how to model the feedline as a series of transmission lines of various lengths.  
  
  * Resonator Pad Type: T
  
  * Control line type: 
    
	* “feedline”: Launch pad at both ends. **There can be at most one feedline and if it exists it must be index 0**

	* “fluxBias”: grounded flux bias, launch pad at only one end.
	
	* “drive”: Launch pad at just one end.

* componentGeometries: Most of these definitions can be found in the “GeometryParameters” powerpoint. A few extra notes:
  
  * All angles are in radians and distance units in microns. "Angle" refers to a rotation of the entire component from the default orientation. 

  * Implied view is top-down on the x-y plane, looking along the negative z-axis. Geometry references to “width” correspond
    to the pre-rotated x-dimension, “length” correspond to the pre-rotated y-dimension, and height/thickness correspond to the z-dimension.
    For resonators “Length” instead corresponds to the actual length of the CPW (including the extra length due to the end pads). 

  * JJ Location must be specified as “[x:y]” (without the quotations). Here x is the shift to the right and y is the shift up of the normalized JJ location. 

  * Section Code is how the path of the control line meander is specified. It is best explained by example. Consider (S:100)(R:-1.5708:100)(S:1900)(R:3.14159:100) 
    This corresponds to a straight segment (“S”) of length 100um, followed by a turn (“R”) of angle -pi/2 radians and turn radius of 100um followed by 
    a straight segment of length 1900um followed by a turn of angle pi and turn radius 100um. Any number of these parentheses-delimited S or R “codes” 
    can be strung together to generate an arbitrary meander.

  * All meander turn radii must be greater than twice the mesh boundary parameter or the meander’s meshPeripheryPolyLine will not be a well-defined polygon.  

Simulations/Calculations
^^^^^^^^^^^^^^^^^^^^^^^^
The currently available models can be found in the simulations.py and calculations.py files. 

The NIST quantization model involves running the following analyses in order:

* CapMat

* LumpedR(i) for each readout resonator index

* CapMatGE

* ECQ(i) for each qubit index

* ECR(i) for each readout resonator index

* L_iQ(i) for each qubit index (to verify consistency of L_i in componentParams)

* Quantize

See QSM_Quantization.pdf for more details.

The following calculations (in calculations.py) are also available for convenience:

* ZZQ

* anharmonicityQ

* dispersiveShiftR

Extensibility
^^^^^^^^^^^^^

To define new geometries, the user needs to define the parameters of that geometry, then add a corresponding
section to the node class in node.py.

QSM currently contains API methods for Ansys Q3D and Circuit simulations, so adding analyses that
require variations of these should be straightforward. HFSS APIs will be coming shortly,
along with flip chip functionality. Other NIST simulations and calculations will also be added periodically.


License
=======
This software package was a joint project by the
`Singh <https://inside.mines.edu/~msingh/>`_/`Gong <https://quantum.mines.edu/project/gong-zhexuan/>`_
groups at the Colorado School of Mines and the
`Quantum Processing Group <https://www.nist.gov/pml/quantum-electromagnetics/quantum-processing>`_
at the National Institute of Standards and Technology in Boulder, CO.
It is free for public use with proper credit/attribution.


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`