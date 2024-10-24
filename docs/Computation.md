---
layout: default
title: Battery Park
description: From Chemistry to Technology
---

# Computational Modeling

> Computational modeling plays a crucial role in materials research and design. Various computational modeling methods have been employed to uncover battery reaction mechanisms and derive intrinsic material parameters, which are then used to predict battery performance at the system level based on complex electrochemical transport equations.
> Depending on the modeling approaches and scale, multiscale simulations, such as first-principles calculations, molecular dynamics simulations, phase field modeling, continuum simulations, and (electro-)thermal modeling, have been actively adopted to design batteries from the cell to the pack level.

## First-Principles Calculations:

- First-principles calculations involve atomic-level simulations used to predict the properties of previously unknown materials by solving the many-body time-indepedent Schrödinger equation through various numerical approximations, such as the Hartree-Fock (HF) method, Density Functional Theory (DFT), and hybrid approaches. These calculations provide inherent material properties, including atomic coordinates and electronic structure properties, without requiring any input from experiments, thereby aiding in the interpretation of experimental observations.
This computational approach offers key properties of lithium-ion batteries, such as the calculation of equilibrium voltages and voltage profiles, theoretical capacity, ionic mobilities, structural stability and corresponding volume changes, as well as thermal and electrochemical stabilities. This understanding provides significant insights into the intrinsic properties of batteries and aids in optimizing battery materials.

* Example results from calculations:
  - Density of State (DOS) and Band structure calculation

<img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/ElectronicStructure.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">


- Calculated electronic density of states and band structures of Sb, Li2Sb and Li3Sb using HSE functional.
The electrodes of an electrochemical cell should exhibit some degree of electronic conductivity to ensure that electrons can reach the electrode/electrolyte interface, where the electrochemical reactions occur. The electronic properties of each important intermediate phases can provide a better understanding of the reaction mechanism at the interface during the reaction. This insight can help identify the rate-determining steps and the origins of overpotential.

  - Structural stability, corresponding volume changes, and equilibrium voltage profiles

<img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Calculated_results.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">


- The formation energies obtained from first-principles calculations are used to compare structural stability and determine the accessibility of metastable off-stoichiometric phases. The configurations with the lowest formation energies are the most stable structures at their compositions, known as ground state structures. The line connecting the ground state structures, known as the convex hull, can be used to calculate the equilibrium voltage and estimate reaction mechanisms and corresponding voltage profiles.
  
- These results provide a thermodynamic equilibrium reaction path with the corresponding theoretical voltage. By analyzing the deviation of the voltage from the equilibrium voltage, insights can be gained into the amount of overpotential applied to the system and the stable phases at specific states of charge. This fundamental information can reveal degradation mechanisms caused by structural changes. Additionally, the volumes of the different structures can be easily obtained from first-principles calculation results.

<figure>
  <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/ion_mobility.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">
  <figcaption>Visualization of the three potential diffusion paths and DFT+U energies of Na ion mobility in Na<sub>3</sub>TiP<sub>3</sub>sub>O<sub>9</sub>sub>N</figcaption>
</figure>





