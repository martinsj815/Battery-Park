---
layout: default
title: Battery Park
description: Battery Chemsitry to Technology 
---

# N/P Ratio

The N/P ratio is a crucial cell design parameter that can influences the utilization level of the electrodes, thereby affecting overall performance and cell-level energy density. The N/P ratio represents the capacity ratio between the anode and cathode. The optimal N/P ratio depends on the electrode's electrochemical reaction mechanism, reaction efficiency, and the decay rate of the cathode and anode during cycling. This parameter must be optimized based on the operating environment.


|Anode Type|N/P Ratio|Comments|
|:-------------|:-----------------|:-----------------|
|Graphite|N/P > 1|- An excess cathode can cause excess lithium ions to deposit on the anode surface during charging, forming dendrites. This reduces battery cycle performance and can lead to short circuits. Thus, an excess anode is benefical for preventing lithium deposition on the anode surface during overcharge, thereby improving cycle life and safety. <br><br> - E.g.: N/P ratio is 1.08 with NCM811 @ W. Zhao et al., Materials Today Energy, 34, 101301 (2023)|
|Li<sub>4</sub>Ti<sub>5</sub>O<sub>12</sub>(LTO)|N/P < 1|- LTO has a stable structure, high intercalation potential (1.55V vs Li/Li<sup>+</sup>), and excellent cycle performance, and does not exhibit lithium plating with excess lithium ions from the cathode. Therefore, designing cells with excess cathode capacity and limited anode capacity (N/P < 1) can mitigate electrolyte degradation due to a high cathode potential when the battery is near or at full charge. <br><br> - E.g.: N/P ratio is 0.68 with NCM111 @ 'Comprehensive guide to battery cathode and anode capacity design', 2022, tycorun.com|
|Si|1 < N/P < 2|- If the anode is highly overbalanced, only a small amount of silicon will be lithiated, resulting in a high anode potential at the end of charge. To reach the same full cell voltage, the cathode material may be overcharged, accelerating degradation due to side reactions in the cathode or electrolyte depletion. <br><br> - E.g.: NP ratio is 1.15-1.4 with NCM811 @ F. Reuter et al., Journal of The Electrochemical Society, 166, 14, A3265-A3271 (2019)|
|Li metal|N/P ~ 1|- A thick Li metal anode (N/P > 2.5) provides a stable initial cycle. However, continued cycling leads to a thick SEI layer build-up, increasing cell polarization. When this becomes dominant, it results in electrolyte depletion and a sudden drop in capacity. Conversely, for N/P ratio close to 1, which effectively balances the lithium consumption rate, electrolyte depletion rate, and SEI accumulation rate under realistic conditions, cell polarization is minimized, extending cell cycle life. <br><br> - E.g.: N/P ratio is 1 with NMC622 @ C. Niu et al., Nature Energy, 6, 723-732 (2021)|

-------------------------------------------------------------------

# Cell connection layout (mS-nP)

- For high-voltage packs, cells are connected in series to form a series-connected module (SCM).

  <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script>
  $$ {v_{pack} = m_{series} * v_{cell}} $$

- For high-current packs, cells are connected in parallel to form a parallel-connected module (PCM). Capacity scales with the number of cells in parallel.

  $$ {i_{pack} = n_{parallel} * i_{cell}} $$

- Total internal resistance of the pack can be estimated from the cell assuming the same open-circuit voltage and internal resistance:
 
  $$ {R_{pack} = \frac{m_{series}}{n_{parallel}} * R_{cell}} $$

- Total pack energy and power can also be calculated:
 
  $$ {E_{pack} = m_{series} * n_{parallel} * Q_{cell} * v_{cell}} $$
    
  $$ {P_{pack} = m_{series} * n_{parallel} * i_{cell} * v_{cell}} $$


<img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/Cell%20in%20Series%20and%20Parallel.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">


--------------------------------------------------------------------
    
# Designing cell: Energy density vs Power capability?

When designing the cell, the trade-off between energy density and power capability needs to be considered as both cannot go hand in hand. To increase the cell energy density, thicker and denser coating (i.e. higher material loading density) is needed for each electrode layer to store more energy. However, increasing the loading can engender many issues that raise the cell’s internal resistance including concentration polarization and uneven thermal distribution with possible ohmic heating. That is because low porosity, high tortuosity, and high thickness all translate to longer diffusion length of Li ions and possible bottleneck for Li flow in and out the cell. Hence power, which is the measure of how fast the energy can be driven in and out the electrode, is inevitably low for these cells.


|Cell Component|Energy Cell|Power Cell|
|:-------------|:-----------------|:-----------------|
|Electrodes|High coating density & thickness <br> High active material loading percentage <br> Low porosity|Low coating density & thickness <br> Low active material loading percentage <br> High porosity|
|Current collectors|Thinner - Improved adhesion|Thicker - Lower resistance|
|Separator|Thin|Thin|
|Electrolyte|High ionic conductivity|High ionic conductivity|
|Tabs|Thin/Narrow/A few tabs on each electrode (weight consideration)|Thick/Wide/Multiple tabs on each electrode (smoother ion transport)|

<img src='https://github.com/donghee1025/Battery-Park/blob/main2/masthead/power_vs_energy.png?raw=true' alt="Capacity" style="width:1000px; height:auto;">
