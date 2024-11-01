---
layout: default
title: Battery Park
description: From Chemistry to Technology
---

# Computational Modeling <i class="arrow right"></i>

<hr style="background: linear-gradient(#a4f58e, #d8f5d0); height: 5px; border: none;">
<br>

> Computational modeling plays a crucial role in materials research and design. Various computational modeling methods have been employed to uncover battery reaction mechanisms and derive intrinsic material parameters, which are then used to predict battery performance at the system level based on complex electrochemical transport equations.
> Depending on the modeling approaches and scale, multiscale simulations, such as first-principles calculations, molecular dynamics simulations, phase field modeling, continuum simulations, and (electro-)thermal modeling, have been actively adopted to design batteries from the cell to the pack level.

## First-Principles Calculations:

- First-principles calculations involve atomic-level simulations used to predict the properties of previously unknown materials by solving the many-body time-indepedent Schrödinger equation through various numerical approximations, such as the Hartree-Fock (HF) method, Density Functional Theory (DFT), and hybrid approaches. These calculations provide inherent material properties, including atomic coordinates and electronic structure properties, without requiring any input from experiments, thereby aiding in the interpretation of experimental observations.
This computational approach offers key properties of lithium-ion batteries, such as the calculation of equilibrium voltages and voltage profiles, theoretical capacity, ionic mobilities, structural stability and corresponding volume changes, as well as thermal and electrochemical stabilities. This understanding provides significant insights into the intrinsic properties of batteries and aids in optimizing battery materials.

* Example results from calculations:
  - <b> Density of State (DOS) and Band structure calculation </b>

<img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/ElectronicStructure.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">


- Calculated electronic density of states and band structures of Sb, Li<sub>2</sub>Sb and Li<sub>3</sub>Sb using HSE functional.
The electrodes of an electrochemical cell should exhibit some degree of electronic conductivity to ensure that electrons can reach the electrode/electrolyte interface, where the electrochemical reactions occur. The electronic properties of each important intermediate phases can provide a better understanding of the reaction mechanism at the interface during the reaction. This insight can help identify the rate-determining steps and the origins of overpotential.

  - <b> Structural stability, corresponding volume changes, and equilibrium voltage profiles </b> 

<img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Calculated_results.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">


- The formation energies obtained from first-principles calculations are used to compare structural stability and determine the accessibility of metastable off-stoichiometric phases. The configurations with the lowest formation energies are the most stable structures at their compositions, known as ground state structures. The line connecting the ground state structures, known as the convex hull, can be used to calculate the equilibrium voltage and estimate reaction mechanisms and corresponding voltage profiles.
  
- These results provide a thermodynamic equilibrium reaction path with the corresponding theoretical voltage. By analyzing the deviation of the voltage from the equilibrium voltage, insights can be gained into the amount of overpotential applied to the system and the stable phases at specific states of charge. This fundamental information can reveal degradation mechanisms caused by structural changes. Additionally, the volumes of the different structures can be easily obtained from first-principles calculation results.


  - <b> Ionic mobility </b>
    
<figure>
  <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/ion_mobility.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">
  <figcaption>Visualization of the three potential diffusion paths and DFT+U energies of Na ion mobility in Na<sub>3</sub>TiP<sub>3</sub>O<sub>9</sub>N</figcaption>
</figure>

- To understand the diffusion process, first-principles calculations can be used to quantify hopping energies through nudged elastic band (NEB) calculations. This method allows the verification of kinetically accessible hopping pathways and the estimation of ionic conductivity.


## Molecular dynamics simulations:

- Molecular dynamics (MD) simulations are computational techniques used to study the physical movements of atoms and molecules by solving Newton's equations of motion for a system of interacting particles. Depending on how the system's state is described, MD simulations can be classified into several types: 1) Classical Molecular Dynamics (CMD): Utilizes Newtonian mechanics to model the interactions and movements of particles in the system. 2) Reactive Molecular Dynamics (ReaxFF MD): Employs reactive force fields to simulate chemical reactions by allowing bonds to form and break dynamically. 3) ab-initio Molecular Dynamics (AIMD): Combines quantum mechanics, specifically solving the Schrödinger equation, with classical MD to capture electronic structure effects. 4) Coarse-Grained Molecular Dynamics (CGMD): Simplifies the system by grouping atoms into larger particles, reducing the degrees of freedom and computational cost. This computational approach plays an increasingly important role in exploring electrolyte structures, physicochemical properties such as ionic conductivity, and interfacial reaction mechanisms.


## Phase field modeling:

- Phase-field modeling is a technique used to predict microstructure eveolution based on fundamental thermodynamic and kinetic principles, utilizing the structures and properties of individual features within a microstructure as input. By solving a set of Nernst-Planck equations or mass (or ion) transport equations and applying appropriate boundary conditions to simplify the equations but effectively describe phenomena, this modeling captures key features, such as the effects of microstructural features and defects on lithiation degradation and the kinetics of morphological and microstructural evolution during localized attacks at the mesoscale. This method is particularly useful for understanding and predicting the morphology, phase changes, and transformations of materials, especially in the context of complex degradation processes in metallic materials used in engineering applications.


## Continuum simulations:

- Continuum mechanics considers the different components of a battery as continuous media. By coupling multiple versions of a continuum model, it can describe the joint behavior of multiple cells or pack-level simulations. This approach can handle larger length and time scales. Depending on the numerical approach, continuum battery models generally fall into two categories: empirical and physics-based. Physics-based continuum models, also known as electrochemical battery models, describe the physical phenomena underpinning battery behavior. These models provide insights into the behavior of lithium-ion distribution in the electrolyte, the multiple internal variables depicted, the potential and current distributions in both the porous electrodes and the electrolyte, the lithium-ion concentration within the electrolyte, and the distribution of intercalated lithium within the electrode particles.
Due to their fast and accurate predictions of real batteries, these approaches have been used as design tools to facilitate the development of new electrode, cell, and pack architectures and to estimate their potential performance. Based on this modeling, these approaches are used for optimizing operating conditions and battery management systems for thermal management, state of charge (SOC), and state of health (SOH) estimation.


-----------------------------------------------------------------------------------------------

## References

- Sholl, David S., and Janice A. Steckel., "Density Functional Theory, A practical Introduction", Wiley,(2009)

- Donghee Chang, et. al., "Elucidating the origins of phase transformation hysteresis during electrochemical cycling of Li-Sb electrodes", Journal of Materials Chemistry A, 3, 18928-18943,(2015)

- Jue Liu, Donghee Chang, et. al., "Ionic Conduction in Cubic Na3TiP3O9N, a Secondary Na-Ion Battery Cathode with Extremely Low Volume Change", Journal of Chemistry of Materials, 26, 3295-3305,(2014)

- Alexander Urban, et. al., "Computational understanding of Li-ion batteries", Reviews in npj Computational Materials, 16002, (2016)

- Yawen Sun, et. al., "Boosting the Optimization of Lithium Metal Batteries by Molecular Dynamics Simulations:A Perspective", Reviews in Advanced Energy Materials, 2002373, (2020)

- Talha Qasim Ansari, et. al., "Phase field modeling for the morphological and microstructural evoltuion of metallic materials under environmnental attack", Reviews in npj Computational Materials, 143, (2021)

- F Brosa Planella, et. al., "A continuum of physics-based lithium-ion battery models reviewed", Reviews in Progress in Energy, 4, (2022)
