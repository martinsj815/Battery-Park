---
layout: default
title: Battery Park
description: Battery Chemistry to Technology
---

# Methodologies

## Non-invasive tests

> The following “in-cell” non-invasive tests are designed to track the cell performance changes over cell lifetime by measuring its dynamic and thermodynamic properties. They are done prior to actual disassembly of cells.

----------------------------------------------------

### Capacity Test: 

<div class="columns">
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/CCCV.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Capacity basically represents the amount of electric charge stored in a cell and is one of the key parameters in Li-ion batteries. Hence, measuring its decay over the cell life is important. For charge, CC-CV (constant current – constant voltage) profile is used – constant current used until a voltage limit is reached and constant voltage is applied until current becomes negligible. For discharge, constant current (galvanostatic) is most common due to its easy interpretability and repeatability. A range of C-rates at various temperatures needs to be carefully considered for performance evaluation.
  </div>
</div>


### Galvanostatic Intermittent Titration Technique (GITT):

<div class="columns">
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/gitt_mod.png?raw=true' alt="GITT" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Discharge/charge is done in steps at designated pulse current and lengths, each followed by prolonged relaxation periods for systematic adjustment for cell’s SoC as electrolyte concentration gradient changes along with solid phase redistribution. Much accurate OCV can be obtained by clearing out the kinetic contribution in a cell’s behavior. The technique is employed to measure Li ion diffusion coefficient and structurally driven (e.g. phase transformation, stress) OCV hysteresis and understand ageing behavior.
  </div>
</div>


### Pseudo-OCV:

<div class="columns">
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/pseudoOCV.png?raw=true' alt="PseudoOCV" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Discharge/charge is performed at very low constant current rate to avoid electrode polarization and ohmic loss despite that there still is hysteresis. “Pseudo-OCV” can be measured by taking an average of the charge and discharge profiles.
  </div>
</div>


### EVS test (Electrochemistry voltage spectroscopy):

<div class="columns">
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/EVS.png?raw=true' alt="EVS" style="width:500px; height:auto;">
  </div>
  <div class="column">
    The technique is used to determine the degradation mechanism of the cell. It can either be done using incremental capacity (IC) method dQ/dV or differential voltage (DV) analysis dV/dQ, whichever reflects the degradation in the cell better for its origins and mechanisms. IC curve reveals the phase transformations as the peaks shown are associated with voltage plateaus while the DV curve better presents the single-phase regions.
  </div>
</div>

### Pulse power test:

<div class="columns">
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/pulse%20power.png?raw=true' alt="Pulse power" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Hybrid pulse power characterization (HPPC) is a widely adopted technique to measure the voltage drop from a current load applied to a cell. The resistance (ΔV/ ΔI) from the pulse is then characterized into three different categories: Ohmic resistance, Charge transfer resistance, and Polarization resistance, of which their ratio is dependent upon the cell design.
  </div>
</div>


### EIS (Electrochemical impedance spectroscopy):

<div class="columns">
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/EIS.png?raw=true' alt="EIS" style="width:500px; height:auto;">
  </div>
  <div class="column">
    A sinusoidal ac potential (or current) is applied over a wide range of frequencies (e.g. between 10 kHz and 10 MHz) to the cell, inducing perturbation of the system in equilibrium to measure its sinusoidal current (or voltage) response. The output behavior has linear correlation with the input signal (linear Butler-Volmer kinetics) as the input signal being small as contrast to pulse power test that uses large current loads causing non-linear behavior.
  </div>
</div>


### Pulsed multisine test:

<div class="columns">
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/multisine%20test.png?raw=true' alt="multisine" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Pulsed multisine test combines a wide-range frequency measurements over the high pulse current tests for which its profile is constructed by superimposing the base pulse profile for discharge/charge with a multisine wave with distinct multi-frequency bandwidth depending on the application. The test usually involves obtaining a cell’s voltage response to a multisine current followed by applying an equivalent circuit model to obtain resistance parameters. The test is better than the EIS as it can be more applicable towards the automotive duty cycles despite its estimation accuracy not as good as that of EIS. Also, when compared to the pulse power test, the obvious advantage is that the resistance parameters (e.g. RO, RCT, and RP) can be better separable.
  </div>
</div>

----------------------------------------------------------------------------------

## Post-mortem characterization

> The following techniques are utilized for electrochemically tested cell materials after cell disassembly. They are typically treated carefully with appropriate solvents (under inert atmosphere) before conducting any measurement.

----------------------------------------------------

### - Optical microscopy (OM): 
Employed to image an overall landscape of the sample surface through the reflectance of visible light on the surface. However, due to its limited resolution (> 0.2 um), observing finer features such as cracks and defects is challenging.

### - Scanning electron microscopy (SEM) 
SEM takes advantage of the short wavelength of the electrons that are accelerated through the magnetic lens, allowing high resolution visualization of the local region of the sample. Secondary and back-scattered electrons from the sample are collected through separate detectors; the former provides surface information with great details and resolution, while the latter displays more imaging contrast among elements coming from the high sensitivity in atomic number differences. SEM imaging can be supplemented by the analytical method such as XEDS (X-ray energy dispersive technique) for chemical composition study and is primarily employed for ageing/degradation mechanism study of the electrode.

### - Transmission electron microscopy (TEM) 
TEM offers spatial resolution much higher than SEM, down to atomic resolution, as it uses high electron energy, typically 80-300 kV. Although large sample surveys are limited due to the localized area viewing and smaller field of view compared to SEM, the technique provides a plethora of structural characteristics of the sample, including crystallography, defect type, domain formation, and stress distribution. By employing state-of-the-art techniques like 4D-STEM/EELS, the atomic-scale electronic structure and chemistry of the sample can also be revealed. For optimal data acquisition, sample preparation (i.e., cleanliness and sample thickness < 20 nm) is key and can be time-consuming. Furthermore, for many e-beam-sensitive battery materials, data acquisition may require a cryogenic setup and fast acquisition detectors (e.g., direct electron detectors) to avoid beam damage, both of which can be quite costly to equip.


### - X-ray diffraction (XRD) 
Monochromatic X-rays incident on the sample gets diffracted after going through interaction with the crystal and is recorded using the detector. Constructive interference between the sample lattice and X-ray impinged upon the sample will generate the characteristic peaks. The technique is quite widely used for structural analysis of electrode active materials with some level of periodicity/crystallinity to determine the origins and mechanisms of their electrochemical behaviors upon cycling and ageing. 

### - X-ray photoelectron spectroscopy (XPS) 
The sample is irradiated by X-ray that emits electrons from a sample surface by transfer of photon energy. The emitted electrons are counted by measuring their kinetic energies, each of which is the fingerprint of its element of origin. XPS is the surface-sensitive technique and used primarily to find oxidation states and chemical environments of the sample surfaces. A depth profile with ion sputtering is possible but only in the extent of nm’s from the surface. The technique hence is quite popular to obtain the composition details on the SEI and/or decomposition mechanism of the particle surface.

### - X-ray fluorescence (XRF) 
A primary X-ray from the tube is irradiated on the sample with sufficient energy, electrons from inner orbital shells get excited towards the outer shell followed by outer shell electrons promptly filling up the vacancies left. This generates fluorescent X-rays that are characteristic of the elements of interest, which are displayed as characteristic energy peaks in the spectrum. The technique is applied to various electrode systems for compositional analysis.

### - X-ray absorption fine structure (XAFS) 
The technique involves the excitation of the core electron to be ejected outside the atom when the incident x-ray has an energy equal or greater than that of the binding energy of a core electron, including an absorption edge. Each element has its characteristic absorption profiles. XAFS spectrum displays absorption coefficient as a function of energy near and just above the absorption edges and can be divided into two parts: x-ray absorption near-edge spectroscopy (XANES) and extended x-ray absorption fine-structure spectroscopy (EXAFS). The former gives information about oxidation state and site symmetry of the absorbing atom, while the latter is concerned about bond distances and coordination with neighboring atoms. XAFS is a quite popular technique for the battery analysis, especially for elucidating the reaction mechanism of the electrodes by understanding their structural and electronic evolution.

### - Fourier transform infrared spectroscopy (FTIR) 
The technique involves sample interaction (either absorption or emission) with infrared radiation. The interferogram signal that is reflected from (or transmitted through) the same surface after interaction is collected by the detector at high resolution in the selected spectral range before being processed using a Fourier transformation to generate final resulting spectrum for the analysis and interpretation. The technique is good for sample composition/chemistry analysis with different bands characteristic of bonds at various modes or molecules at their vibrational states.

### - Raman spectroscopy (RS) 
When the incident monochromatic light interacts with the sample (either molecular vibration, phonons, or others) it undergoes inelastic scattering known as Raman scattering. (As opposed to much intense elastic scattering called Rayleigh scattering.) Raman shift is basically the energy difference between the scattered light and incident light, provides information about vibrational modes of molecules and thus helps identifying the sample structure. Raman has versatile applications for battery analysis including chemical and structural evolution of electrode and molecular configurations of electrolyte and polymeric materials.

### - Secondary ion mass spectrometry (SIMS) 
Primary ions are sputtered onto the sample surface to eject secondary ions, which are collected and analyzed by the mass spectrometer/analyzer for the elemental and molecular composition analysis. TOF-SIMS (Time of Flight SIMS) uses time of flight mass analyzer that separates ions by their mass – that is velocity and time of flight - given that they all possess the same kinetic energy. SIMS is particularly powerful for characterizing different types of thin layers including coating, passivation layer, SEI, etc., and investigating cell aging.

### - Inductively coupled plasma optical emission spectrometry (ICP-OES) 
The method uses inductively coupled plasma to excite atoms and ions that emit electromagnetic radiation characteristic of the element. ICP-OES has a wide window of element detection and sensitivity including Li although the composition analysis of the entire sample can be quite limited. Like SIMS, the application of the method is mostly for understanding the aging/degradation mechanism of the cell through elemental detection in various parts within the cell.

### - Nuclear magnetic resonance (NMR) 
The sample placed in a strong magnetic field is perturbed by the weak external radio frequency field. The excited nuclei with certain magnetic moment having energy transfer coinciding with radio frequency emits the energy at same frequency with spins coming back to their origin. The measured signal is then processed to generate a spectrum. There are NMRs both for liquids (e.g. electrolyte) and solids (e.g. electrodes) and full analysis of the sample can yield structural, chemical, thermodynamic, electronic, and magnetic information. Hence, it can be quite powerful for understanding novel chemistry behind Li-ion battery operation.

### - Gas chromatography Mass Spectrometry (GC-MS) 
This thermoanalytical technique measures the heat flow of the material by taking difference to that of the reference to identify heat absorbed and released when it is heated, cooled, and under constant temperature. It helps understanding the material’s thermal properties such as heat capacity and phase transitions. The technique can be applied for the study of material’s thermal stability (i.e. structural change and decomposition) and possible thermal runaway in the high temperature conditions.

### - Differential Scanning Calorimetry (DSC) 
The technique involves the process of separating components in a mixture by first injecting a gaseous and liquid sample into a carrier gas and passing through a stationary phase inside a column. Components, then, depending on their retention times or rates of passing, will be detected separately using mass spectrometer, which displays the chromatogram with quantity of each component detected vs retention time. GC-MS is used for post-mortem analysis of electrolytes and gas evolution in extreme charge-discharge conditions.

### - Thermogravimetric Analysis (TGA) 
It measures the mass change of the material using a precision balance over time with the temperature increase. The measurement can be done in a wide range of atmospheric environments such ambient air, inert/oxidizing/reducing gases, and pressures. The technique provides insight into thermal stability of the battery system in various electrode/electrolyte settings.



## References:

- Thomas Waldmann, et al., "Review—Post-Mortem Analysis of Aged Lithium-Ion Batteries: Disassembly Methodology and Physico-Chemical Analysis Techniques", J. Electrochem. Soc., 163, A2149-A2164 (2016)
- Matthew Newville, "Fundamentals of XAFS", Reviews in Mineralogy and Geochemistry, 78, 33 (2014)
- https://www.spectro.com/xrf-principle
- https://www.edmundoptics.com/knowledge-center/application-notes/lasers/basic-principles-of-raman-scattering-and-spectroscopy/
