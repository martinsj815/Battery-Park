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
    <img src='https://dl.dropboxusercontent.com/scl/fi/mnfhk96vozvp0veahzl83/CCCV.png?rlkey=j03bhamgmu41fmygfir5bw8ff&st=12w7sd7b&raw=1' alt="Capacity" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Capacity basically represents the amount of electric charge stored in a cell and is one of the key parameters in Li-ion batteries. Hence, measuring its decay over the cell life is important. For charge, CC-CV (constant current – constant voltage) profile is used – constant current used until a voltage limit is reached and constant voltage is applied until current becomes negligible. For discharge, constant current (galvanostatic) is most common due to its easy interpretability and repeatability. A range of C-rates at various temperatures needs to be carefully considered for performance evaluation.
  </div>
</div>


### Galvanostatic Intermittent Titration Technique (GITT):

<div class="columns">
  <div class="column">
    <img src='https://dl.dropboxusercontent.com/scl/fi/pkok1beky5c1zyms7oj9k/gitt_mod.png?rlkey=20yio4dtzrphtryu52kfdb2pr&st=zdk5kq1w&raw=1' alt="GITT" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Discharge/charge is done in steps at designated pulse current and lengths, each followed by prolonged relaxation periods for systematic adjustment for cell’s SoC as electrolyte concentration gradient changes along with solid phase redistribution. Much accurate OCV can be obtained by clearing out the kinetic contribution in a cell’s behavior. The technique is employed to measure Li ion diffusion coefficient and structurally driven (e.g. phase transformation, stress) OCV hysteresis and understand ageing behavior.
  </div>
</div>


### Pseudo-OCV:

<div class="columns">
  <div class="column">
    <img src='https://dl.dropboxusercontent.com/scl/fi/n32gbcioobl9b7t2cykqh/pseudoOCV.png?rlkey=34v6p8ij6sualjgtl29g9r8m6&st=g6aykazi&raw=1' alt="PseudoOCV" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Discharge/charge is performed at very low constant current rate to avoid electrode polarization and ohmic loss despite that there still is hysteresis. “Pseudo-OCV” can be measured by taking an average of the charge and discharge profiles.
  </div>
</div>


### EVS test (Electrochemistry voltage spectroscopy):

<div class="columns">
  <div class="column">
    <img src='https://dl.dropboxusercontent.com/scl/fi/m2zwxsaxocipsdeqmlvkd/EVS.png?rlkey=cmwv6sc33m0x4mbvxu9i44u6d&st=fqn9ftpu&raw=1' alt="EVS" style="width:500px; height:auto;">
  </div>
  <div class="column">
    The technique is used to determine the degradation mechanism of the cell. It can either be done using incremental capacity (IC) method dQ/dV or differential voltage (DV) analysis dV/dQ, whichever reflects the degradation in the cell better for its origins and mechanisms. IC curve reveals the phase transformations as the peaks shown are associated with voltage plateaus while the DV curve better presents the single-phase regions.
  </div>
</div>

### Pulse power test:

<div class="columns">
  <div class="column">
    <img src='https://dl.dropboxusercontent.com/scl/fi/442o07rz7p54217gkyzb2/pulse-power.png?rlkey=16w3qjtzygg4xk9ftrbg18tpy&st=0pnxq7jv&raw=1' alt="EVS" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Hybrid pulse power characterization (HPPC) is a widely adopted technique to measure the voltage drop from a current load applied to a cell. The resistance (ΔV/ ΔI) from the pulse is then characterized into three different categories: Ohmic resistance, Charge transfer resistance, and Polarization resistance, of which their ratio is dependent upon the cell design.
  </div>
</div>


### EIS (Electrochemical impedance spectroscopy):

<div class="columns">
  <div class="column">
    <img src='https://dl.dropboxusercontent.com/scl/fi/yrtaa71tz70wopwzkho9q/EIS.png?rlkey=dqwbedvzmuts00hz6xl8msock&st=p8sc90t4&raw=1' alt="EVS" style="width:500px; height:auto;">
  </div>
  <div class="column">
    A sinusoidal ac potential (or current) is applied over a wide range of frequencies (e.g. between 10 kHz and 10 MHz) to the cell, inducing perturbation of the system in equilibrium to measure its sinusoidal current (or voltage) response. The output behavior has linear correlation with the input signal (linear Butler-Volmer kinetics) as the input signal being small as contrast to pulse power test that uses large current loads causing non-linear behavior.
  </div>
</div>


### Pulsed multisine test:

<div class="columns">
  <div class="column">
    <img src='https://dl.dropboxusercontent.com/scl/fi/kd9mckvnf9sw3wx7o1xgr/multisine-test.png?rlkey=qxh1h1t2zd4k4mk4p8wlfgcrk&st=ag9tiyr0&raw=1' alt="EVS" style="width:500px; height:auto;">
  </div>
  <div class="column">
    Pulsed multisine test combines a wide-range frequency measurements over the high pulse current tests for which its profile is constructed by superimposing the base pulse profile for discharge/charge with a multisine wave with distinct multi-frequency bandwidth depending on the application. The test usually involves obtaining a cell’s voltage response to a multisine current followed by applying an equivalent circuit model to obtain resistance parameters. The test is better than the EIS as it can be more applicable towards the automotive duty cycles despite its estimation accuracy not as good as that of EIS. Also, when compared to the pulse power test, the obvious advantage is that the resistance parameters (e.g. RO, RCT, and RP) can be better separable.
  </div>
</div>

----------------------------------------------------------------------------------
