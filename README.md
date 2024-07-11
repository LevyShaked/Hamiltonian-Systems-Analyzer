<div align="center">
  <h1 style="background-color: yellow; padding: 10px; border-radius: 10px;">Hamiltonian Systems Analysis Tool</h1>
</div> 

<div align="center">
  
***This program analyzes trajectories for a given Hamiltonian with various mathematical tools***

</div> 
 
 
## Motivation
In our lab, we investigate mechanical systems. In most cases, these systems cannot be solved analytically, necessitating numerical calculations. There are various computational tools available for investigating these systems, but an interactive program that can conduct preliminary investigations would be very helpful. This project aims to integrate the tools our lab uses, initially focusing on generating the First Recurrence Map.

For example, here is a map generated in our lab for the three-dimensional [Toda lattice](https://doi.org/10.1143/PTP.50.1547) 

 
<div align="center">
  
![image-1](https://github.com/LevyShaked/Hamiltonian-Systems-Analyzer/assets/167014554/9e790042-24c6-47b3-b568-262ec9181aee)

</div>

The "closed" symmetrical curves indicate that this system is stable and non-chaotic. Without exhibiting these geometrical curves, it is not possible to determine in advance whether the system is chaotic, even with current mathematical knowledge!

## Theory 

### [Hamiltonian Mechanics](https://books.google.co.il/books?id=fnO3XYYpU54C&pg=PA19&hl=iw&source=gbs_toc_r&cad=1#v=onepage&q&f=false) 

The Hamiltonian is a function of time **t**, position **q**, and momentum **p**: 
<div align="center">
  
$H=H{(q,p,t)}$

</div>
which satisfies the Hamilton's equations of motion.

By knowing the Hamiltonian, one has the condition of a physical system for any time t. 

By placing a particle in a known system, it will start to move. Its momentum and position will change over time. The trajectory is defined as all the positions and corresponding momentum values that the particle has during its motion, represented as:

<div align="center">

$p_(q)$

</div>

In most cases, even if the Hamiltonian is known, it is not possible to solve it analytically, and therefore numerical calculations are necessary to reveal the physical behavior of the system. 

### [First Recurrence Map (FRM)](https://books.google.co.il/books?id=fnO3XYYpU54C&pg=PA87&hl=iw&source=gbs_toc_r&cad=1#v=onepage&q&f=false) 
Instead of presenting p(q) at all times, it is possible to choose times periodically, 
and for 1.5 dimentions this will be a Stroboscopic Map with the requirement:
<div align="center">

$t_{n} = nT$

where $n \in \mathbb{N}$ and $T \in \mathbb{R}$, $T>0$

</div>

This map reveals the geometrical features of dynamical systems. These features represent physical properties of the system, which are hard to know in advance.

## Program Stages of Processing 

### [Runge-Kutta (RK)](https://doi.org/10.1016/B978-0-12-811753-8.00008-6)
To solve the Hamilton-Jacobi equations for a given Hamiltonian, we will use the 4<sup>th</sup> order Runge-Kutta method. 

The algorithm for this method will be included as part of the program to control the parameters of the algorithm according to the user's requirements.

### Creating the Map 

1. For user-specified parameters, the RK method will generate a single trajectory.
2. The FRM sequence will be calculated:

<div align="center">

$(p(t_{n}), q(t_{n}))$

</div>

and will be stored in the FRM matrix of the map.

3. Repeat steps 1-2 until all desired trajectories are generated.

## Programming

The program interface will solely be through an interactive GUI
 
### Input 

1. Time interval (for determination of convergance)
2. Time legnth of the dynamics
3. Initial conditions:
   - Boundary
   - Amount
4. Mass
5. Force expression (function of (q,p,t,m))
6. Surface choice (t0) as a scroller

### Output 

1. CSV file of the trajectories and the time interval
2. Map as a picture 

## Guide

1. Insatll the dependencies:

`pip install -r requirements.txt.`

2. Run the program on terminal:

<<<<<<< HEAD
'python Hamiltonian_Analyzer.py'
=======
`pytest`
>>>>>>> 8c533ef3dbff012ae530e30945c297cc8df16480

The test will be the data that is filled in the entries by default

<div align="center">

$f=-x+\frac{1}{2}*sign(p)\abs{x}$

</div>





 
## 

> This project was originally implemented as part of the [Python programming course](https://github.com/szabgab/wis-python-course-2024-04)
> at the [Weizmann Institute of Science](https://www.weizmann.ac.il/) taught by [Gabor Szabo](https://szabgab.com/)

