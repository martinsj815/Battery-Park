---
layout: default
title: Battery Park
description: From Chemistry to Technology
---

<head>
  <h1> Thermal properties of cells<i class="arrow right"></i></h1>
  <hr style="background: linear-gradient(#4a8049, #d8f5d0); height: 5px; border: none;">
  <br>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script>
</head>
<body>
  <h2>&#9672; Thermal transfer </h2>
  <ul>Thermal conductivity is important as it affects the cell’s temperature distribution and influences cooling. The anisotropic thermal conduction of the battery can be characterized by in-plane (axial) thermal conductivity parallel to the cell layers and cross-plane (radial) thermal conductivity perpendicular to the layers. In-plane conductivity is roughly one order of magnitude higher than cross-plane conductivity. With the increase in SOC and the operating temperature, thermal conductivity goes up.</ul>
  <hr>
  <ul>According to the Fourier’s Law of heat conduction with steady-state heat flow (∂T/∂t=0), it reads:
    <br>
    $$ {q = - \kappa\nabla{T}} $$ , where q is heat flux vector and &#x3BA; is thermal conductivity, and T is temperature.
    <br><br>
    For the 1-d heat conduction, it is simply q = &#x3BA; dx/dT or more generally it can be written as:
    <br>
     $$ {Q = - \kappa{A}\frac{dT}{dx}} $$ , where Q is heat and A is the cross-sectional area, and d is the legth of the heat conduction in the cartesian coordinate.
    <br>
    For the cylindrical case (relevant to the cylindrical cell), the equation becomes:
    <br><br>
    $$ {Q = - \kappa (2\pi RL)\frac{dT}{dR}} $$ , where R is radius of the cylinder.
    <br>
  </ul>
  <hr>
  <h2>&#9672; Pipe Method: </h2>
  <ul>The whole cell radial thermal conductivity can be estimated for the cylindrical cell by using the thermocouples placed at the inside (spindle) and outside the cell to measure the temperature difference and the metal alloy wire to heat the cell’s center using a DC power supply for applying different currents. The effective radial thermal conductivity is derived based on following equation: 
    <br>
    $$ {Q = \frac{2\pi\kappa_{eff}L(T_{1}-T_{2})}{ln(\frac{R_{2}}{R_{1}})}} $$  , where T<sub>1</sub>, R<sub>1</sub> and T<sub>2</sub>, R<sub>2</sub> are temperature and radius of the inner part and outer part of the cell, respectively. 
  </ul>
  <br>
  <h2>&#9672; Transient Method </h2>
  <ul>Thermal conductivity of the cell is dependent on the internal components and their configuration. Hence, the equations for in-plane and cross-plane conductivities are dependent on the effective thermal conductivity of each component layer and its respective thickness as follows: 
    <br><br>
    $${Radial thermal conductivity = \frac{\Sigma_{j} L_{j}}{\Sigma_{j} \frac{L_{j}}{k_{eff, j}}}} $$  
    <br>
    $${Axial thermal conductivity = \frac{\Sigma_{j} L_{j}{k_{eff, j}}}{\Sigma_{j}{L_{j}}}} $$  
    <br>
    <br>
    To measure the thermal conductivity of each material, a combination of methods is considered – such as laser flash method (LF) and differential scanning calorimetry (DSC) – to measure the transient response of the temperature vs time. Thermal diffusivity can be derived based on the sample thickness and half time measured. The heat capacity is then extracted by applying the DSC method based on the following equation:
    <br>
    $${c_{p} = dQ / dT} $$
    <br>
    The thermal conductivity <i>k</i> is then equal to 
  </ul>
  
  
  <h2> References: </h2>
  <li> Thomas Waldmann, et al., "Review—Post-Mortem Analysis of Aged Lithium-Ion Batteries: Disassembly Methodology and Physico-Chemical Analysis Techniques", J. Electrochem. Soc., 163, A2149-A2164 (2016) </li>
</body>


