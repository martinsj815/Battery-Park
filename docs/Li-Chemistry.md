---
layout: default
title: Battery Park
description: From Chemistry to Technology
---

# Li ion battery <i class="arrow right"></i>

<hr style="background: linear-gradient(#4a8049, #d8f5d0); height: 5px; border: none;">
<br><br>

<div class="columns">
  <div class="column">
    <li> Lithium-ion batteries are consisting of a host material with a high redox potential (> 3V vs Li) as a cathode and that of a low electrochemical potential (vs Li) as an anode. Typically, lithium transition metal oxides are cathodes while graphite is an anode, both of which undergo Li (de-)intercalation during charge and discharge.</li>
    
    <li> Upon discharge, lithium ions migrate from the anode (e.g. lithiated graphite) towards the electrolyte while electrons move through the external circuit. Lithium ions are then carried by the electrolyte and flow into the cathode along with electrons. Upon charge, the process is reversed with the help of electrical energy injected</li>.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Li%20ion%20battery.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
  </div>
</div>


<h2>&#9672; Cell reaction mechanism</h2>

> The way Li-ions react with electrode active materials during charge/discharge can be categorized into following:

### Intercalation reaction:
- Li-ions are inserted or extracted from interstitital sites of the host structure without causing substantial structural changes. This makes intercalation compounds ideal for electrochemical energy storage applications. Indeed, most commercialized Li-ions batteries use electrodes with this type of reaction mechanism. However, intercalation compounds have a limited capacity due to crystallographic constrains of the host and thermodynamic instabilities arising from large changes in Li concentrations within the host.

### Alloying reaction:
- Li reacts directly with active element/compound (M) to form an intermetallic phase (Li<sub>x</sub>M). Despite providing a high specific capacity for the electrode, alloying reactions generally lead to multiple phase transformations during (de-)lithiation with large volume changes, resulting in a large hysteresis in the voltage profile and poor reversibility. This hysteresis leads to irreversible energy loss upon cycling, making commercialization difficult.

### Conversion reaction:
- The reaction involves full reduction of the metal ions by lithium. It can accommodate as many electrons per transitional metal as needed to reduce its ions to the metallic state M. Therefore, materials undergoing conversion reaction can achieve much higher capacities than the intercalation compounds. When the starting compound has a strong structural relationship with its lithiated products, the conversion reaction is usually called a displacement reaction. Since these reactions involve phase transformations to extrude the transition metal, large voltage polarization and hysteresis are common.


--------------------------------------------------------------------------


<h2>&#9672; Cathode Materials</h2>


<div class="columns">
  <div class="column">
    - Since the voltage is dictated by the redox energy difference between the cathode and the anode, it is imperative to have the cathode to reach the lower energy band of a metal ion at the higher oxidation state to increase the cell voltage.
    
    - The use of transition metal oxide instead of sulfide (e.g. TiS<sub>2</sub>) enables an increase in cell voltage by accessing the energy bands lying low in the energy band diagram as the O2- 2p band lies at a lower energy below a S2- 3p band.
    
    - Typical transition metal oxides used for the cathode have spinel, layered, or olivine structures that undergo Li (de-)intercalation.
    
    - There is also a conversion-based cathode material such as FeF<sub>2</sub>, with a theoretical capacity of 571 mAh/g with average operating voltage of ~2.5V.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Energy%20band%20diagram.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
    Image Courtesy: A. Manthiram, Nature Commun. 11, 1550 (2020)
  </div>
</div>  

## Cathode Comparison Table

|Cathode Name|Crystal Structure|Chemical Formula|Specific Capacity (mAh/g) (The/Exp)|Average Voltage (V)|Electrical Conductivity (S/cm)|Li Diffusivity (cm<sup>2</sup>/s)|Exothermic Rxn T (Deg)|Heat Release (J/g)|Pros|Cons|
|:-------------|:-----------------|:-----------------|:----------|:--------------|:----------|:-------------|:------------|:------------|:-----------|:------------|
|Lithium Cobalt Oxide|Layered|LiCoO<sub>2</sub>|274/148<sup>a</sup>|3.8<sup>a</sup>||10<sup>-11</sup>-10<sup>-10</sup><sup> f</sup>|||*Good structural stability|*Co expensive / *Unstable upon charging >50%"|
|Lithium Manganese Oxide|Spinel|LiMn<sub>2</sub>O<sub>4</sub>|148/120<sup>a</sup>|4.1<sup>a</sup>||10<sup>-10</sup>-10<sup>-7</sup><sup> f</sup>|||*Cost efficient|* Mn dissolution in electrolyte|
|Lithium Iron Phosphate|Olivine|LiFePO<sub>4</sub>|170/165<sup>a</sup>|3.4<sup>a</sup>|10<sup>-10</sup>-10<sup>-9</sup><sup> e</sup>|10<sup>-14</sup>-10<sup>-11</sup><sup> f</sup>|250-360<sup>d</sup>|147<sup>d</sup>|*Cost affordable / *Thermal stability|* Low ionic conductivity / * Low energy density|
|Lithium Iron Manganese Phosphate|Olivine|LiFe<sub>x</sub>Mn<sub>1-x</sub>PO<sub>4</sub>|170/150|3.7-3.8||2.4x10<sup>-13</sup><sup> g</sup>||
|Lithium Nickel Cobalt Manganese Oxide (NCM111)|Layered|Li[Ni<sub>0.33</sub>Co<sub>0.33</sub>Mn<sub>0.33</sub>]O<sub>2</sub>|280/160<sup>a</sup>|3.7<sup>a</sup>|5.2x10<sup>-8</sup><sup>c</sup>|10<sup>-10</sup>-10<sup>-9</sup><sup> f</sup>|306<sup>d</sup>|512.5<sup>d</sup>|
|Lithium Nickel Cobalt Manganese Oxide(NCM622)|Layered|Li[Ni<sub>0.6</sub>Co<sub>0.2</sub>Mn<sub>0.2</sub>]O<sub>2</sub>|275/170<sup>b</sup>|3.7<sup>b</sup>|1.6x10<sup>-6</sup><sup>c</sup>||264<sup>d</sup>|721.4<sup>d</sup>|
|Lithium Nickel Cobalt Manganese Oxide (NCM811)|Layered|Li[Ni<sub>0.8</sub>Co<sub>0.1</sub>Mn<sub>0.1</sub>]O<sub>2</sub>|275/190<sup>b</sup>|3.7<sup>b</sup>|1.7x10<sup>-5</sup><sup>c</sup>||232<sup>d</sup>|904.8<sup>d</sup>|*High specific capacity / *High energy density|*Cycle instability for high Ni content / *Co expensive|
|Lithium Nickel Cobalt Aluminum Oxide|Layered|LiNi<sub>0.8</sub>Co<sub>0.15</sub>Al<sub>0.05</sub>O<sub>2</sub>|279/200<sup>a</sup>|3.7<sup>a</sup>|||||* High specific capacity / *High energy density|*Cycle/Thermal instability / *Co expensive|


<h2><li> Global Demand for Cathode Chemistries </li></h2>

<div class="columns">
  <div class="column">
    - According to the review paper by Degen et al., both High-Ni NCM cathode and LFP cathode chemistry continue to rise in their demands while those of NCM532/622 and NCA will be stagnant until 2040. It is also forecasted that the market share will be gradually dominated by the post-Li batteries in future although it is currently unknown which of the batteries (e.g. all-solid-state, lithium-sulfur, lithium-air, sodium-ion, etc) will reach industrial-scale production.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Global%20Demand_Cathode%20Chemistry.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
  </div>
</div>

-------------------------------------------------------------------

<h2>&#9672; Anode Materials</h2>

### 1. Intercalation-based:
> Carbon-based anode such as graphite has the theoretical capacity of 372 mAh/g and has a good (de-)lithiation potential vs. Li. Many carbon-based materials are engineered at nanoscale to optimize their morphologies for high structural stability and better electrochemical reversibility and capacity retention. In terms of safety, stability, and power capability, titanium-based anodes such as Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub> and TiO<sub>2</sub> have an advantage over graphite, but their electronic conductivity is poor and specific capacities (175-330 mAh/g) and energy densities are low.
   
### 2. Alloying-based:
> Si, Ge, and Sn are the alloying anodes with specific capacity, which is much higher than that of intercalation anode system. For example, Si can reach a specific capacity of upto ~4200 mAh/g (practically, 3590 mAh/g), while, for Sn, it is 993 mAh/g. However, their large volumetric expansion (Si ~ 400%, Sn ~ 250%, and Sb ~ 135%) upon lithiation poses a great threat to its mechanical stability (e.g. delamination from a current collector or loss of inter-particle cohesion) and contributes to a capacity fade of the cell. Nano-structuring of Si as an anode has attracted interest to overcome such problems. In fact, Si or SiO<sub>x</sub> is considered to be added in small percentage amount (e.g. 2-10 wt%) inside the graphite anode to boost energy density of the anode.

### 3. Conversion-based:
> Conversion-based anodes such as metal oxides undergo the following reaction: M<sub>x</sub>O<sub>y</sub> + 2yLi<sup>+</sup> + 2ye<sup>-</sup> → yLi<sub>2</sub>O + xM. Despite their high specific capacities, they suffer from multiple issues including structural instability due to pulverization and voltage hysteresis owing to sluggish kinetics during the conversion process to different phases.




Below is the comparison of key anode materials currently in industry for commercialization. The data were taken from the paper - Gebrekidan Gebresilassie Eshetu, et al., "Production of high-energy Li-ion batteries comprising silicon-containing anodes and insertion-type cathodes", Nature Commun. 12, 5459 (2021). As noticeable from the table, silicon has exceptionally high theoretical capacity (comparable or even higher than Li metal) but also undergoes extremely large volumetric variation upon cycling causing capacity decay due to mechanical instability. Its electronic conductivity and Li ion diffusivity are also lower than that of the carbon/graphite counterpart. These make the material very challenging for commercialization.


|Anode System|C|Si|Sb|SiO<sub>x</sub>|Li|Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub>|
|:-------------|:-----------------|:-----------------|:----------|:--------------|:----------|:-------------|
|Type of reaction|Intercalation|Alloying|Alloying|Conversion||Intercalation|
|Density (g/cm<sup>3</sup>)|2.25|2.3|3|2.13|0.53|3.5|
|Lithiated Phase|LiC<sub>6</sub>|Li<sub>3.75</sub>Si|Li<sub>3</sub>Sb|SiO (x~1)|Li|Li<sub>7</sub>Ti<sub>5</sub>O<sub>12</sub>|
|Reaction Potential vs. Li/Li<sup>+</sup> (V)|0.05|0.31|||0|1.55|
|Theoretical gravimetric specific capacity (mAh/g)|372|3590|660|1710|3862|175|
|Theoretical volumetric specific capacity (mAh/cm<sup>3</sup>)|837|8360|1890|3172|2061|613|
|Volumetric change|10-12|&gt;280|135|160|100|1|
|Lithium diffusion coefficient|10<sup>-11</sup> - 10<sup>-7</sup>|10<sup>-13</sup> - 10<sup>-11</sup>||||10<sup>-12</sup> - 10<sup>-11</sup>|


<h2><li> Moving from graphite to silicon for the Li-ion battery anode </li></h2>


<img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Si%20Graphite_NCM811.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">


The graphs above display estimated gravimetric and volumetric energy densities vs cathode areal capacity of the cell consisting of NCM811 and Graphite/Si. The data are excerpted/re-calculated based on the review article by Eshetu, et al., “Production of high-energy Li-ion batteries comprising silicon-containing anodes and insertion-type cathodes”, Nature Commun., 12 (2021). A slight modification was made to the estimations after taking cell tabs and packaging components into consideration to make them more realistic at the cell level.

As shown in the graphs above, transition from graphite and silicon can yield drastic improvement in both metrics. At the areal capacity of 10 mAh/cm<sup>2</sup>, the transition from the graphite/NCM811 chemistry to that of Si/NCM811 can boost gravimetric energy density from 342 Wh/kg to 536 Wh/kg, while the increase is much greater for volumetric density (817 Wh/kg to 1568 Wh/kg). At the industry with the typical areal capacity (>3 mAh/cm<sup>2</sup>), a Si/NCM811 cell is estimated to yield 395 Wh/kg and 1123 Wh/L, which is way above the current energy goal. Again, this is estimation and more like an ideal case since Si is mechanically unstable during electrochemical cycling due to its drastic volumetric changes. With micro-scale (or even nano-scale) structure tuning, this can be mitigated, leading to better capacity retention.

------------------------------------------------------------------------

<h2>&#9672; Electrolyte</h2>

<div class="columns">
  <div class="column">
    -Electrolyte acts as a medium for ion transport between the cell cathode and anode during (dis-)charging. It can be in liquid, solid or even polymer gel-type. Liquid non-aqueous electrolyte, most commonly used, consists of salt(s) dissolved in solvent(s) along with additive(s).
    
    -Ionic transport (i.e. ionic conductivity) is the key aspect of the non-aqueous Li-ion battery electrolyte. It is important for the electrolyte to possess high dielectric constant for salt dissolution, low viscosity for good ion transport, and chemical/thermal stability over a wide operating voltage/temperature range. When inserted in a cell, reductive and oxidative stability against anode and cathode (i.e. wide electrochemical stability window) is also desired for safe/stable operation of the cell.
    
    -As no single salt and solvent mixture can provide many of desired characteristics above, electrolyte studied typically consists of multiple salts and/or solvents mixed. A good example is lithium hexafluorophosphate (LiPF6) dissolved in mixture of cyclic carbonate like ethylene carbonate (for high dielectric constant) and aliphatic carbonate such as diethyl, dimethyl, or ethyl methyl carbonate (for low viscosity and melting point).
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Electrolyte.png?raw=true' alt="Capacity" style="width:500px; height:auto;">
  </div>
</div>

<br>
<h2><li> Liquid Electrolyte </li></h2>

<h3><li> Solvent </li></h3>
The key criteria for the solvent are following: It should have 1) high dielectric constant to be able to dissolve enough salts to reach desired concentration, 2) low viscosity for facile transport of ions, 3) wide electrochemical potential range, and 4) good chemical stability against the anode and the cathode. Others include the wide temperature range of operation and safety (e.g. flash point). Most nonaqueous electrolytes commonly used until recent are either esters and ethers. 
<br><br>
Here is the table of properties for some of commonly studied solvents:
<br><br>
|Type|Solvent Name|Viscosity &eta; (cP)|Dielectric constant &epsilon;|E<sub>0, red</sub> (V vs. Li/Li<sup>+</sup>)|E<sub>0, ox</sub> (V vs. Li/Li<sup>+</sup>)|HOMO/LUMO|T<sub>F</sub> (<sup>o</sup>C)|
|:-------------|:-----------------|:-----------------|:----------|:--------------|:----------|:-------------|:-----------|
|<b>Linear Carbonate</b>b>|Diethyl Carbonate|0.75|2.81|0.07|6.95|-7.63/1.25|25|
||Dimethyl Carbonate|0.59|3.11|0.1|7.06|-7.72/1.19|16|
||Ethyl Methyl Carbonate|0.65|2.96|0.1|6.97|-7.68/1.22|23|
|<b>Cyclic Carbonate</b>b>|Ethylene Carbonate|1.9|89.8|0.27|7.19|-7.92/1.09|143|
||Propylene Carbonate|2.53|64.9|0.22|7.13|-7.87/1.11|116|
||Vinylene Carbonate|1.54|126|0.46|5.79|-6.69/0.46|73|
||Fluoroethylene Carbonate|4.1|107|0.51|7.48|-8.32/0.70|>102|
|<b>Ethers</b>|1,2-Dimethoxyethane (DME)|0.46|7.2|-1.68||-6.70/2.53|5|
||1,3-Dioxolane (DOL)|0.59|7.1|-1.48||-6.63/3.05|-3|
|||||||||
|<b>References</b>|K. Xu et al., Chem. Rev. 104, 4303-4417 (2004) <br> D.S. Hall et al., J. Electrochem. Soc. 165, A2365 (2018)|D.S. Hall et al., J. Electrochem. Soc. 165, A2365 (2018) <br> M. S. Park, et al., Sci. Rep. 4, 3815 (2014)||M. Zhou, Adv. Mater. 33, 2003741 (2021)|Data from Sigma Aldirch product pages| 

<br>
<h3><li> Salt </li></h3>

LiPF<sub>6</sub> has no outstanding property but has the combination of its well-balanced characteristics that meet stringent requirements for commercialization. It also has good anodic stability up to >5V when mixed in carbonates and ionic conductivity. However, its poor thermal stability and moisture sensitivity requires the additive for performance enhancement.

<b>Ion Mobility (Descending order)</b>: LiBF<sub>4</sub> > LiClO<sub>4</sub> > LiPF<sub>6</sub> > LiAsF<sub>6</sub> > LiTFSI

<b>Dissociation Constant (Descending order)</b>: LiTFSI > LiAsF<sub>6</sub> > LiPF<sub>6</sub> > LiClO<sub>4</sub> > LiBF<sub>4</sub>

<br>
<b> - Other salts/additives studied/considered are: </b>

> LiBF<sub>4</sub>: Better thermal and stability against hydrolysis than LiPF<sub>6</sub>. However, it has mediocre ionic conductivity due to its low dissociation ability than LiPF<sub>6</sub>.
    
> LiAsF<sub>6</sub>: Good ionic conductivity and enhanced thermal and anodic stability due to strong As-F bonding. However, AsF<sub>3</sub> byproduct is toxic, hindering its commercialization.

> LiTFSI: Good electrochemical stability against oxidation due to delocalized negative charges in TFSI<sup>-</sup> anions. Also has good ionic conductivity and thermal stability. Al corrosion, however, can make it not very applicable.

> LiFSI: Higher conductivity and better hydrolytic and thermal stability than LiPF<sub>6</sub> in carbonate solvents. Al corrosion not happening at the high potential where the cathode redox happens.

> LiBOB (lithium bis(oxalate)borate): SEI formation at the graphite anode surface through the BOB anion for reversible Li (de-)insertion. Good thermal stability and resistant to Al corrosion at the high potential. However, less versatile for application due to limited solubility in carbonates and low anodic stability (4.2V).

> LiDFOB (lithium difluoro(oxalate)borate): Hybridized form of LiBOB with LiBF<sub>4</sub>. Higher solubility than LiBOB in carbonate electrolyte with less viscosity and higher ionic conductivity. Cell impedance comparable to LiPF<sub>6</sub>-based electrolyte.

> LiPO<sub>2</sub>F<sub>2</sub> (only as additive): Forms the stable interface film both at cathode and anode surface upon cycling, preventing decomposition/oxidation of the electrolyte. This allows impedance control of both cathode and anode and is conducive to cathode structural stability, high-rate capability, and prolonged cell cycling.

Many 18650 cells use the mixture of LiPF<sub>6</sub> and LiFSI inside carbonate electrolyte as the electrolyte. For EV batteries with an increasingly rigorous demand for their performances, some of the salts above are investigated as additive to be mixed with LiPF6 electrolyte, for which its concentration varies from 5-10%.

<br>
<h2><li> Solid Electrolyte </li></h2>

<div class="columns">
  <div class="column">
      A solid electrolyte is a solid ionic conductor that acts as a medium for ion transport between the cell cathode and the anode. These materials should be electrically insulating but ionically conductive, and electrochemically stable with both the cathode and anode. The solid electrolyte can replace the liquid electrolyte and separator of the cell.
Solid electrolytes are attracting a large interest since it enables all-solid-state batteries with excellent thermal stability, high energy density, and fast charge capability. The solid electrolyte materials can be classified into sulfide solid inorganic electrolytes (S-SIE), oxide solid inorganic electrolyte (O-SIE), and solid polymer electrolytes (SPE).
      To be comparable to conventional liquid electrolytes, the ionic conductivity should be in the order of 1 mS/cm at room temperature. S-SIE has generally higher ionic conductivity and forms a good interface with electrodes due to its soft Li-S bonding properties, but has low electrochemical stability due to narrow electrochemical stability window. O-SEI has good electrochemical stability but is difficult to handle in large-scale production. While SPE has low ionic conductivity and requires high temperature to operate, it is stable with lithium metal, forming a good interface with the electrode, and can be applied in a current roll-to-roll process.
  </div>
  <div class="column">
    <img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/LiPS.png?raw=true' alt="Capacity" style="width:700px; height:auto;">
  </div>
</div>

<br>

|Type|Example System|Conductivity (mS/cm)|Advantages|Disadvantages|
|:-------------|:-----------------|:-----------------|:----------|:----|
|Sulfide (S-SIE)|- Li<sub>9.54</sub>Si<sub>1.74</sub>P<sub>1.44</sub>S<sub>11.7</sub>Cl<sub>0.3</sub> <br> - Li<sub>3.833</sub>Sn<sub>0.833</sub>As<sub>0.166</sub>S<sub>4</sub> <br> - Li<sub>6</sub>PS<sub>5</sub>Br - Li<sub>7</sub>P<sub>3</sub>S<sub>11</sub> <br> - Li<sub>10</sub>GeP<sub>2</sub>S<sub>12</sub>|0.1-50|- High ionic conductivity <br> - Good mechanical strength and flexibilty|- Sensitive to moisture and produces H<sub>2</sub>S from decomposition <br> - Poor compatibiltiy with cathode materials due to low oxidation stability|
|Oxide (O-SIE)|- Li<sub>7</sub>La<sub>3</sub>Zr<sub>2</sub>O<sub>12</sub> (Garnet) <br> - Li<sub>0.5</sub>La<sub>0.5</sub>TiO<sub>3</sub> (Perovskite) <br> - Li<sub>3</sub>OCl (Antiperovskite) <br> - LISICON, NASICON|0.01-1|- High chemical and electrochemical stability (High  electrochemical oxidation voltage) <br> - High mechanical strength|- Non-flexible and brittle <br> - Expensive large-scale production (require sintering process)|
|Polymer|- LiTFSI-PEO(Mw=5000000) <br> - LiClO<sub>4</sub>-PEO(Mw=600000) <br> - LiClO<sub>4</sub>-PEO with 5wt&#37; elliptical TiO<sub>2</sub> rods <br> - LiClO4-PEO with 5wt&#37; elliptical TiO<sub>2</sub> rods|0.1-1 (at 90 <sup>o</sup>C)|- Stable with lithium metal <br> - Flexibility and low shear modulus <br> - Easy to produce a large area membrance|- Limited thermal stability <br> - Low ionic conductivity <br> - Low oxidation voltage (< 4V)|


------------------------------------------------------------------------------
<h2><li> References </li></h2>

F. Degen, et al, "Energy consumption of current and future production of lithium-ion and post lithium-ion battery cells", Nature Energy, 8, 1284 (2023)

Naoki Nitta, et al, "Li-ion battery materials: present and future", Mater. Today, 18, 252 (2015) (a in Cathode Comparison Table)

Florian Schipper, et al, "Review—Recent Advances and Remaining Challenges for Lithium Ion Battery Cathodes", J. Electrochem. Soc., 164, A6220 (2017) (b in Cathode Comparison Table)

Hyung-Joo Noh, et al., "Comparison of the structural and electrochemical properties of layered Li[NixCoyMnz]O2 (x = 1/3, 0.5, 0.6, 0.7, 0.8 and 0.85) cathode material for lithium-ion batteries", J. Power Sources, 233, 121 (2013) (c in Cathode Comparison Table)

Sung-Yoon Chung, et al., "Electronically conductive phospho-olivines as lithium storage electrodes", Nature Mater., 1, 123 (2002) (e in Cathode Comparison Table)

Xiao-Guang Yang, et al., "Thermally modulated lithium iron phosphate batteries for mass-market electric vehicles", Nature Energy, 6, 176 (2021) (d in Cathode Comparison Table)

Yonggang Wang, et al., "Nano active materials for lithium-ion batteries", Nanoscale, 2, 1294 (2010) (f in Cathode Comparison Table)

Liangtao Yang, et al., "Concentration-gradient LiMn0.8Fe0.2PO4 cathode material for high performance lithium ion battery", J. Pouwer Sources, 2, 1294 (2015) (g in Cathode Comparison Table)

Arumugam Manthiram, "A reflection on lithium-ion battery cathode chemistry", Nature Commun., 11, 1550 (2020)

Jun Lu, et al, "High‑Performance Anode Materials for Rechargeable Lithium‑Ion Batteries", Electrochemical Energy Reviews, 1:35 (2018)

Hui Cheng, et al, "Recent progress of advanced anode materials of lithium-ion batteries", Journal of Energy Chemistry, 57, 451 (2021)

Kang Xu, "Electrolytes and Interphases in Li-ion Batteries and Beyond", Chem. Rev., 114, 11503 (2014)

E. R. Logan, et al., "A Study of the Physical Properties of Li-Ion Battery Electrolytes Containing Esters", J. Electrochem. Soc., 165, A21 (2018)

Kang Xu, "Nonaqueous Liquid Electrolytes for Lithium-Based Rechargeable Batteries", Chem. Rev., 104, 4303 (2004)

Jiale Xing, et al., "A Review of Nonaqueous Electrolytes, Binders, and Separators for Lithium‑Ion Batteries", Electrochem. Energy Rev., 5:14 (2022)

Hong-Bo Han, et al., "Lithium bis(fluorosulfonyl)imide (LiFSI) as conducting salt for nonaqueous liquid electrolytes for lithium-ion batteries: Physicochemical and electrochemical properties", J. Power Sources, 196, 3623 (2011)

Weimin Zhao, et al., "Toward a stable solid-electrolyte-interfaces on nickel-rich cathodes: LiPO2F2 salt-type additive and its working mechanism for LiNi0.5Mn0.25Co0.25O2 cathodes", J. Power Sources, 380, 149 (2018)

Bowen Yang, et al., "Lithium difluorophosphate as an additive to improve the low temperature performance of LiNi0.5Co0.2Mn0.3O2/graphite cells", Electrochim. Acta, 221, 107 (2016)

https://www.linkedin.com/pulse/application-lipo2f2-electrolyte-additive-lithium-ion-batteries-li/

Qing Zhao, et al, "Designing solid-state electrolytes for safe, energy-dense batteries", Nature Reviews, 5, 229 (2020)

Arumugam Manthiram,"Lithium battery chemistries enabled by solid-state electrolytes", Nature Reviews Materials, 2, 16103 (2017)
