---
layout: default
title: Battery Park
description: Battery Chemistry to Technology
---

# Li ion battery


<div class="columns">
  <div class="column">
    - Lithium-ion batteries are consisting of a host material with a high redox potential (> 3V vs Li) as a cathode and that of a low electrochemical potential (vs Li) as an anode. Typically, lithium transition metal oxides are cathodes while graphite is an anode, both of which undergo Li (de-)intercalation during charge and discharge.
    
    - Upon discharge, lithium ions migrate from the anode (e.g. lithiated graphite) towards the electrolyte while electrons move through the external circuit. Lithium ions are then carried by the electrolyte and flow into the cathode along with electrons. Upon charge, the process is reversed with the help of electrical energy injected.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Li%20ion%20battery.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
  </div>
</div>


# Cell reaction mechanism

> The way Li-ions react with electrode active materials during charge/discharge can be categorized into following:

## Intercalation reaction:
- Li-ions are inserted or extracted from interstitital sites of the host structure without causing substantial structural changes. This makes intercalation compounds ideal for electrochemical energy storage applications. Indeed, most commercialized Li-ions batteries use electrodes with this type of reaction mechanism. However, intercalation compounds have a limited capacity due to crystallographic constrains of the host and thermodynamic instabilities arising from large changes in Li concentrations within the host.

## Alloying reaction:
- Li reacts directly with active element/compound (M) to form an intermetallic phase (LixM). Despite providing a high specific capacity for the electrode, alloying reactions generally lead to multiple phase transformations during (de-)lithiation with large volume changes, resulting in a large hysteresis in the voltage profile and poor reversibility. This hysteresis leads to irreversible energy loss upon cycling, making commercialization difficult.

## Conversion reaction:
- The reaction involves full reduction of the metal ions by lithium. It can accommodate as many electrons per transitional metal as needed to reduce its ions to the metallic state M. Therefore, materials undergoing conversion reaction can achieve much higher capacities than the intercalation compounds. When the starting compound has a strong structural relationship with its lithiated products, the conversion reaction is usually called a displacement reaction. Since these reactions involve phase transformations to extrude the transition metal, large voltage polarization and hysteresis are common.


--------------------------------------------------------------------------


# Cathode Materials


<div class="columns">
  <div class="column">
    - Since the voltage is dictated by the redox energy difference between the cathode and the anode, it is imperative to have the cathode to reach the lower energy band of a metal ion at the higher oxidation state to increase the cell voltage.
    
    - The use of transition metal oxide instead of sulfide (e.g. TiS2) enables an increase in cell voltage by accessing the energy bands lying low in the energy band diagram as the O2- 2p band lies at a lower energy below a S2- 3p band.
    
    - Typical transition metal oxides used for the cathode have spinel, layered, or olivine structures that undergo Li (de-)intercalation.
    
    - There is also a conversion-based cathode material such as FeF2, with a theoretical capacity of 571 mAh/g with average operating voltage of ~2.5V.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Energy%20band%20diagram.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
    Image Courtesy: A. Manthiram, Nature Commun. 11, 1550 (2020)
  </div>
</div>  

## Cathode Comparison Table

|Cathode Name|Crystal Structure|Chemical Formula|Specific Capacity (mAh/g) (The/Exp)|Average Voltage (V)|Electrical Conductivity (S/cm)|Li Diffusivity (cm2/s)|Exothermic Rxn T (Deg)|Heat Release (J/g)|Pros|Cons|
|:-------------|:-----------------|:-----------------|:----------|:--------------|:----------|:-------------|:------------|:------------|:-----------|:------------|
|Lithium Cobalt Oxide|Layered|LiCoO<sub>2</sub>|274/148<sup>a</sup>|3.8<sup>a</sup>||10<sup>-11</sup>-10<sup>-10</sup><sup> f</sup>|||*Good structural stability|*Co expensive / *Unstable upon charging >50%"|
|Lithium Manganese Oxide|Spinel|LiMn<sub>2</sub>O<sub>4</sub>|148/120<sup>a</sup>|4.1<sup>a</sup>||10<sup>-10</sup>-10<sup>-7</sup><sup> f</sup>|||*Cost efficient|* Mn dissolution in electrolyte|
|Lithium Iron Phosphate|Olivine|LiFePO<sub>4</sub>|170/165<sup>a</sup>|3.4<sup>a</sup>|10<sup>-10</sup>-10<sup>-9</sup><sup> e</sup>|10<sup>-14</sup>-10<sup>-11</sup><sup> f</sup>|250-360<sup>d</sup>|147<sup>d</sup>|*Cost affordable / *Thermal stability|* Low ionic conductivity / * Low energy density|
|Lithium Iron Manganese Phosphate|Olivine|LiFe<sub>x</sub>Mn<sub>1-x</sub>PO<sub>4</sub>|170/150|3.7-3.8||2.4x10<sup>-13</sup><sup> g</sup>||
|Lithium Nickel Cobalt Manganese Oxide (NCM111)|Layered|Li[Ni<sub>0.33</sub>Co<sub>0.33</sub>Mn<sub>0.33</sub>]O<sub>2</sub>|280/160<sup>a</sup>|3.7<sup>a</sup>|5.2x10<sup>-8</sup><sup>c</sup>|10<sup>-10</sup>-10<sup>-9</sup><sup> f</sup>|306<sup>d</sup>|512.5<sup>d</sup>|
|Lithium Nickel Cobalt Manganese Oxide(NCM622)|Layered|Li[Ni<sub>0.6</sub>Co<sub>0.2</sub>Mn<sub>0.2</sub>]O<sub>2</sub>|275/170<sup>b</sup>|3.7<sup>b</sup>|1.6x10<sup>-6</sup><sup>c</sup>||264<sup>d</sup>|721.4<sup>d</sup>|
|Lithium Nickel Cobalt Manganese Oxide (NCM811)|Layered|Li[Ni<sub>0.8</sub>Co<sub>0.1</sub>Mn<sub>0.1</sub>]O<sub>2</sub>|275/190<sup>b</sup>|3.7<sup>b</sup>|1.7x10<sup>-5</sup><sup>c</sup>||232<sup>d</sup>|904.8<sup>d</sup>|*High specific capacity / *High energy density|*Cycle instability for high Ni content / *Co expensive|
|Lithium Nickel Cobalt Aluminum Oxide|Layered|LiNi<sub>0.8</sub>Co<sub>0.15</sub>Al<sub>0.05</sub>O<sub>2</sub>|279/200<sup>a</sup>|3.7<sup>a</sup>|||||* High specific capacity / *High energy density|*Cycle/Thermal instability / *Co expensive|


# Global Demand for Cathode Chemistries


<div class="columns">
  <div class="column">
    - According to the review paper by Degen et al., both High-Ni NCM cathode and LFP cathode chemistry continue to rise in their demands while those of NCM532/622 and NCA will be stagnant until 2040. It is also forecasted that the market share will be gradually dominated by the post-Li batteries in future although it is currently unknown which of the batteries (e.g. all-solid-state, lithium-sulfur, lithium-air, sodium-ion, etc) will reach industrial-scale production.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Global%20Demand_Cathode%20Chemistry.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
  </div>
</div>

-------------------------------------------------------------------

# Anode Materials


## 1. Intercalation-based:
> Carbon-based anode such as graphite has the theoretical capacity of 372 mAh/g and has a good (de-)lithiation potential vs. Li. Many carbon-based materials are engineered at nanoscale to optimize their morphologies for high structural stability and better electrochemical reversibility and capacity retention. In terms of safety, stability, and power capability, titanium-based anodes such as Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub> and TiO<sub>2</sub> have an advantage over graphite, but their electronic conductivity is poor and specific capacities (175-330 mAh/g) and energy densities are low.
   
## 2. Alloying-based:
> Si, Ge, and Sn are the alloying anodes with specific capacity, which is much higher than that of intercalation anode system. For example, Si can reach a specific capacity of upto ~4200 mAh/g (practically, 3590 mAh/g), while, for Sn, it is 993 mAh/g. However, their large volumetric expansion (Si ~ 400%, Sn ~ 250%, and Sb ~ 135%) upon lithiation poses a great threat to its mechanical stability (e.g. delamination from a current collector or loss of inter-particle cohesion) and contributes to a capacity fade of the cell. Nano-structuring of Si as an anode has attracted interest to overcome such problems. In fact, Si or SiOx is considered to be added in small percentage amount (e.g. 2-10 wt%) inside the graphite anode to boost energy density of the anode.

## 3. Conversion-based:
> Conversion-based anodes such as metal oxides undergo the following reaction: M<sub>x</sub>O<sub>y</sub> + 2yLi<sup>+</sup> + 2ye<sup>-</sup> → yLi<sub>2</sub>O + xM. Despite their high specific capacities, they suffer from multiple issues including structural instability due to pulverization and voltage hysteresis owing to sluggish kinetics during the conversion process to different phases.




Below is the comparison of key anode materials currently in industry for commercialization. The data were taken from the paper - Gebrekidan Gebresilassie Eshetu, et al., "Production of high-energy Li-ion batteries comprising silicon-containing anodes and insertion-type cathodes", Nature Commun. 12, 5459 (2021). As noticeable from the table, silicon has exceptionally high theoretical capacity (comparable or even higher than Li metal) but also undergoes extremely large volumetric variation upon cycling causing capacity decay due to mechanical instability. Its electronic conductivity and Li ion diffusivity are also lower than that of the carbon/graphite counterpart. These make the material very challenging for commercialization.


|Anode System|C|Si|Sb|SiO<sub>x</sub>|Li|Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub>|
|:-------------|:-----------------|:-----------------|:----------|:--------------|:----------|:-------------|
|Type of reaction|Intercalation|Alloying|Alloying|Conversion||Intercalation|
|Density (g/cm<sup>3</sup>)|LiC<sub>6</sub>|Li<sub>3.75</sub>Si|Li<sub>3</sub>Sb|SiO (x~1)|Li|Li<sub>7</sub>Ti<sub>5</sub>O<sub>12</sub>|
|Lithiated Phase|Olivine|LiFe<sub>x</sub>Mn<sub>1-x</sub>PO<sub>4</sub>|170/150|3.7-3.8||2.4x10<sup>-13</sup><sup> g</sup>|
|Reaction Potential vs. Li/Li<sup>+</sup> (V)|0.05|0.31|||0|1.55|
|Theoretical gravimetric specific capacity (mAh/g)|372|3590|660|1710|3862|175|
|Theoretical volumetric specific capacity (mAh/cm<sup>3</sup>)|837|8360|1890|3172|2061|613|
|Volumetric change|10-12|&gt;280|135|160|100|1|
|Lithium diffusion coefficient|10<sup>-11</sup> - 10<sup>-7</sup>|10<sup>-13</sup> - 10<sup>-11</sup>||||10<sup>-12</sup> - 10<sup>-11</sup>|


# Moving from graphite to silicon for the Li-ion battery anode


<img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Si%20Graphite_NCM811.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">


The graphs above display estimated gravimetric and volumetric energy densities vs cathode areal capacity of the cell consisting of NCM811 and Graphite/Si. The data are excerpted/re-calculated based on the review article by Eshetu, et al., “Production of high-energy Li-ion batteries comprising silicon-containing anodes and insertion-type cathodes”, Nature Commun., 12 (2021). A slight modification was made to the estimations after taking cell tabs and packaging components into consideration to make them more realistic at the cell level.

As shown in the graphs above, transition from graphite and silicon can yield drastic improvement in both metrics. At the areal capacity of 10 mAh/cm<sup>2</sup>, the transition from the graphite/NCM811 chemistry to that of Si/NCM811 can boost gravimetric energy density from 342 Wh/kg to 536 Wh/kg, while the increase is much greater for volumetric density (817 Wh/kg to 1568 Wh/kg). At the industry with the typical areal capacity (>3 mAh/cm<sup>2</sup>), a Si/NCM811 cell is estimated to yield 395 Wh/kg and 1123 Wh/L, which is way above the current energy goal. Again, this is estimation and more like an ideal case since Si is mechanically unstable during electrochemical cycling due to its drastic volumetric changes. With micro-scale (or even nano-scale) structure tuning, this can be mitigated, leading to better capacity retention.

------------------------------------------------------------------------

# Electrolyte

<div class="columns">
  <div class="column">
    -Electrolyte acts as a medium for ion transport between the cell cathode and anode during (dis-)charging. It can be in liquid, solid or even polymer gel-type. Liquid non-aqueous electrolyte, most commonly used, consists of salt(s) dissolved in solvent(s) along with additive(s).
    
    -Ionic transport (i.e. ionic conductivity) is the key aspect of the non-aqueous Li-ion battery electrolyte. It is important for the electrolyte to possess high dielectric constant for salt dissolution, low viscosity for good ion transport, and chemical/thermal stability over a wide operating voltage/temperature range. When inserted in a cell, reductive and oxidative stability against anode and cathode (i.e. wide electrochemical stability window) is also desired for safe/stable operation of the cell.
    
    -As no single salt and solvent mixture can provide many of desired characteristics above, electrolyte studied typically consists of multiple salts and/or solvents mixed. A good example is lithium hexafluorophosphate (LiPF6) dissolved in mixture of cyclic carbonate like ethylene carbonate (for high dielectric constant) and aliphatic carbonate such as diethyl, dimethyl, or ethyl methyl carbonate (for low viscosity and melting point).
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Electrolyte.png?raw=true' alt="Capacity" style="width:300px; height:auto;">
  </div>
</div>


# Salt

- LiPF<sub>6</sub> has no outstanding property but has the combination of its well-balanced characteristics that meet stringent requirements for commercialization. It also has good anodic stability up to >5V when mixed in carbonates and ionic conductivity. However, its poor thermal stability and moisture sensitivity requires the additive for performance enhancement.

<b>Ion Mobility (Descending order)</b>: LiBF<sub>4</sub> > LiClO<sub>4</sub> > LiPF<sub>6</sub> > LiAsF<sub>6</sub> > LiTFSI

<b>Dissociation Constant (Descending order)</b>: LiTFSI > LiAsF<sub>6</sub> > LiPF<sub>6</sub> > LiClO<sub>4</sub> > LiBF<sub>4</sub>


<b> - Other salts/additives studied/considered are: </b>

    > LiBF<sub>4</sub>: Better thermal and stability against hydrolysis than LiPF<sub>6</sub>. However, it has mediocre ionic conductivity due to its low dissociation ability than LiPF<sub>6</sub>.
