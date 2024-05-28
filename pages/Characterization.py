import os
import numpy as np
import pandas as pd
import dash
from dash import Dash, dash_table, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import dash_mantine_components as dmc
from collections import OrderedDict
from dash.exceptions import PreventUpdate
import math

dash.register_page(
    __name__, name="Characterization", top_nav=True, path="/characterization"
    )

layout = html.Div([
                    dbc.Row([
                        dcc.Markdown('* Non-invasive tests', style={'font-size':'25px', 'margin-bottom':"20px", 'textAlign':'justify','font-weight':'bold'}),
                         html.Div(('- The following “in-cell” non-invasive tests are designed to track the cell performance changes over cell lifetime by measuring its dynamic and thermodynamic properties. They are done prior to actual disassembly of cells.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px', 'margin-bottom':"20px"}),
                         dcc.Markdown(('- **Capacity Test:** Capacity basically represents the amount of electric charge stored in a cell and is one of the key parameters in Li-ion batteries. Hence, measuring its decay over the cell life is important. For charge, CC-CV (constant current – constant voltage) profile is used – constant current used until a voltage limit is reached and constant voltage is applied until current becomes negligible. For discharge, constant current (galvanostatic) is most common due to its easy interpretability and repeatability. A range of C-rates at various temperatures needs to be carefully considered for performance evaluation.'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),
                         dcc.Markdown(('- **galvanostatic intermittent titration technique (GITT):** Discharge/charge is done in steps at designated pulse current and lengths, each followed by prolonged relaxation periods for systematic adjustment for cell’s SoC as electrolyte concentration gradient changes along with solid phase redistribution. Much accurate OCV can be obtained by clearing out the kinetic contribution in a cell’s behavior. The technique is employed to measure Li ion diffusion coefficient and structurally driven (e.g. phase transformation, stress) OCV hysteresis and understand ageing behavior.'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),
                         dcc.Markdown(('- **Pseudo-OCV:** Discharge/charge is performed at very low constant current rate to avoid electrode polarization and ohmic loss despite that there still is hysteresis. “Pseudo-OCV” can be measured by taking an average of the charge and discharge profiles.'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),           
                         dcc.Markdown(('- **EVS test (Electrochemistry voltage spectroscopy):** The technique is used to determine the degradation mechanism of the cell. It can either be done using incremental capacity (IC) method dQ/dV or different voltage analysis dV/dQ, whichever reflects the degradation in the cell better for its origins and mechanisms. IC curve reveals the phase transformations as the peaks shown are associated with voltage plateaus while the DV curve better presents the single-phase regions.'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),      
                         dcc.Markdown(('- **Pulse power test:** Hybrid pulse power characterization (HPPC) is a widely adopted technique to measure the voltage drop from a current load applied to a cell. The resistance (ΔV/ ΔI) from the pulse is then characterized into three different categories: Ohmic resistance, Charge transfer resistance, and Polarization resistance, of which their ratio is dependent upon the cell design.'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),   
                         dcc.Markdown(('- **EIS (Electrochemical impedance spectroscopy):** A sinusoidal ac potential (or current) is applied over a wide range of frequencies (e.g. between 10 kHz and 10 MHz) to the cell, inducing perturbation of the system in equilibrium to measure its sinusoidal current (or voltage) response. The output behavior has linear correlation with the input signal (linear Butler-Volmer kinetics) as the input signal being small as contrast to pulse power test that uses large current loads causing non-linear behavior.'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),   
                         dcc.Markdown(('- **Pulsed multisine test:** Pulsed multisine test combines a wide-range frequency measurements over the high pulse current tests for which its profile is constructed by superimposing the base pulse profile for discharge/charge with a multisine wave with distinct multi-frequency bandwidth depending on the application. The test usually involves obtaining a cell’s voltage response to a multisine current followed by applying an equivalent circuit model to obtain resistance parameters. The test is better than the EIS as it can be more applicable towards the automotive duty cycles despite its estimation accuracy not as good as that of EIS. Also, when compared to the pulse power test, the obvious advantage is that the resistance parameters (e.g. RO, RCT, and RP) can be better separable.'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),                                                                                           
                        ],
                    style={'textAlign':'justify', 'margin-left':'40px', 'margin-right':'60px'},
                    ),
                    html.Br(),               
                    dmc.Divider(size="md", variant="dotted", color="grey"),       
                    html.Br(), 
                    dbc.Row([
                         dcc.Markdown('* Post-mortem characterization', style={'font-size':'25px', 'margin-bottom':"20px", 'textAlign':'justify','font-weight':'bold'}),
                         html.Div(('- The following techniques are utilized for electrochemically tested cell materials after cell disassembly. They are typically treated carefully with appropriate solvents (under inert atmosphere) before conducting any measurement.'), 
                                 style={'textAlign':'justify', 'margin-left':'20px','font-size':'16px', 'margin-bottom':"20px"}),
                         dcc.Markdown((r''' **Note - $$\star$$: Imaging information $$\qquad$$ $$\ast$$: Elemental information $$\qquad$$ $$\oplus$$: Structural/Chemical/Molecular information**
                                       '''), 
                                  dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'20px', 'font-size':'16px', 'margin-bottom':"20px"}),                         
                         dcc.Markdown(('''- **Optical microscopy (OM):  $$\star$$ ** Employed to image an overall landscape of the sample surface through the reflectance of visible light on the surface. However, due to its limited resolution (> 0.2 um), observing finer features such as cracks and defects is challenging.
                                       '''), 
                                  dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),
                         dcc.Markdown((r'''- **Scanning electron microscopy (SEM) $$\star\ast$$ :** SEM takes advantage of the short wavelength of the electrons that are accelerated through the magnetic lens, allowing high resolution visualization of the local region of the sample. Secondary and back-scattered electrons from the sample are collected through separate detectors; the former provides surface information with great details and resolution, while the latter displays more imaging contrast among elements coming from the high sensitivity in atomic number differences. SEM imaging can be supplemented by the analytical method such as XEDS (X-ray energy dispersive technique) for chemical composition study and is primarily employed for ageing/degradation mechanism study of the electrode.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),
                         dcc.Markdown((r'''- **Transmission electron microscopy (TEM) $$\star\ast$$ :** TEM offers spatial resolution much higher than SEM down to atomic resolution as it uses high electron energy, typically 80-300 kV. Although large sample survey is limited due to much localized area viewing with smaller field of view than SEM, the technique provides plethora of sample’s structural characteristics including crystallography, defect type, domain formation, and stress distribution. By employing state-of-the-art techniques like 4D-STEM/EELS, atomic-scale electronic structure and chemistry of the sample can also be revealed. For best data acquisition, sample preparation (i.e. cleanliness and sample thickness <20 nm) is key and can be time-consuming. Further, for many e-beam sensitive battery materials, to avoid beam damage, data acquisition may require cryogenic setup and fast acquisition detectors (e.g. direct electron detector), both of which can be quite costly to equip.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),       
                         dcc.Markdown((r'''- **X-ray diffraction (XRD) $$\oplus$$: ** Monochromatic X-ray incident on the sample gets diffracted after going through interaction with the crystal and is recorded using the detector. Constructive interference between the sample lattice and X-ray impinged upon the sample will generate the characteristic peaks. The technique is quite widely used for structural analysis of electrode active materials with some level of periodicity/crystallinity to determine the origins and mechanisms of their electrochemical behaviors upon cycling and ageing.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),       
                         dcc.Markdown((r'''- **X-ray photoelectron spectroscopy (XPS) $$\oplus$$:** The sample is irradiated by X-ray that emits electrons from a sample surface by transfer of photo energy. The emitted electrons are counted by measuring their kinetic energies, each of which is the fingerprint of its element of origin. XPS is the surface-sensitive technique and used primarily to find oxidation states and chemical environments of the sample surfaces. A depth profile with ion sputtering is possible but only in the extent of nm’s from the surface. The technique hence is quite popular to obtain the composition details on the SEI and/or decomposition mechanism of the particle surface.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}), 
                         dcc.Markdown((r'''- **X-ray fluorescence (XRF) $$\ast$$:** A primary X-ray from the tube is irradiated on the sample with sufficient energy, electrons from inner orbital shells get excited towards the outer shell followed by outer shell electrons promptly filling up the vacancies left. This generates fluorescent X-rays that are characteristic of the elements of interest, which are displayed as characteristic energy peaks in the spectrum. The technique is applied to various electrode systems for compositional analysis.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),       
                         dcc.Markdown((r'''- **X-ray absorption fine structure (XAFS) $$\oplus$$:** The technique involves the excitation of the core electron to be ejected outside the atom when the incident x-ray has an energy equal or greater than that of the binding energy of a core electron, including an absorption edge. Each element has its characteristic absorption profiles. XAFS spectrum displays absorption coefficient as a function of energy near and just above the absorption edges and can be divided into two parts: x-ray absorption near-edge spectroscopy (XANES) and extended x-ray absorption fine-structure spectroscopy (EXAFS). The former gives information about oxidation state and coordination structure of the absorbing atom, while the latter is concerned about bond distances and coordination with neighboring atoms. XAFS is a quite popular technique for the battery analysis, especially for elucidating the reaction mechanism of the electrodes by understanding their structural and electronic evolution.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),   
                         dcc.Markdown((r'''- **Fourier transform infrared spectroscopy (FTIR) $$\oplus$$:** The technique involves sample interaction (either absorption or emission) with infrared radiation. The interferogram signal that is reflected from (or transmitted through) the same surface after interaction is collected by the detector at high resolution in the selected spectral range before being processed using a Fourier transformation to generate final resulting spectrum for the analysis and interpretation. The technique is good for sample composition/chemistry analysis with different bands characteristic of bonds at various modes or molecules at their vibrational states.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),   
                         dcc.Markdown((r'''- **Raman spectroscopy (RS) $$\oplus$$: ** When the incident monochromatic light interacts with the sample (either molecular vibration, phonons, or others) it undergoes inelastic scattering known as Raman scattering. (As opposed to much intense elastic scattering called Rayleigh scattering.) Raman shift is basically the energy difference between the scattered light and incident light, provides information about vibrational modes of molecules and thus helps identifying the sample structure. Raman has versatile applications for battery analysis including chemical and structural evolution of electrode and molecular configurations of electrolyte and polymeric materials.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}), 
                         dcc.Markdown((r'''- **Secondary ion mass spectrometry (SIMS) $$\oplus$$: ** Primary ions are sputtered onto the sample surface to eject secondary ions, which are collected and analyzed by the mass spectrometer/analyzer for the elemental and molecular composition analysis. TOF-SIMS (Time of Flight SIMS) uses time of flight mass analyzer that separates ions by their mass – that is velocity and time of flight - given that they all possess the same kinetic energy. SIMS is particularly powerful for characterizing different types of thin layers including coating, passivation layer, SEI, etc., and investigating cell aging.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),   
                         dcc.Markdown((r'''- **Inductively coupled plasma optical emission spectrometry (ICP-OES) $$\ast$$:** The method uses inductively coupled plasma to excite atoms and ions that emit electromagnetic radiation characteristic of the element. ICP-OES has a wide window of element detection and sensitivity including Li although the composition analysis of the entire sample can be quite limited. Like SIMS, the application of the method is mostly for understanding the aging/degradation mechanism of the cell through elemental detection in various parts within the cell.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}), 
                         dcc.Markdown(('''- **Nuclear magnetic resonance (NMR) $$\oplus$$:** The sample placed in a strong magnetic field is perturbed by the weak external radio frequency field. The excited nuclei with certain magnetic moment having energy transfer coinciding with radio frequency emits the energy at same frequency with spins coming back to their origin. The measured signal is then processed to generate a spectrum. There are NMRs both for liquids (e.g. electrolyte) and solids (e.g. electrodes) and full analysis of the sample can yield structural, chemical, thermodynamic, electronic, and magnetic information. Hence, it can be quite powerful for understanding novel chemistry behind Li-ion battery operation.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),       
                         dcc.Markdown(('''- ** Gas chromatography Mass Spectrometry (GC-MS) $$\oplus$$: ** The technique involves the process of separating components in a mixture by first injecting a gaseous and liquid sample into a carrier gas and passing through a stationary phase inside a column. Components, then, depending on their retention times or rates of passing, will be detected separately using mass spectrometer, which displays the chromatogram with quantity of each component detected vs retention time. GC-MS is used for post-mortem analysis of electrolytes and gas evolution in extreme charge-discharge conditions.'''), 
                                      dangerously_allow_html=True, mathjax=True,
                                style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),          
                        ],
                    style={'textAlign':'justify', 'margin-left':'40px', 'margin-right':'60px'},
                    ),
                    html.Br(), 
                    
                    html.Br(),               
                    dmc.Divider(size="md", variant="dotted", color="grey"),       
                    html.Br(), 
                    dbc.Row([
                        dcc.Markdown('* References', style={'font-size':'25px', 'margin-bottom':"10px", 'textAlign':'justify','font-weight':'bold'}),
                        dcc.Markdown(('- Thomas Waldmann, et al., "Review—Post-Mortem Analysis of Aged Lithium-Ion Batteries: Disassembly Methodology and Physico-Chemical Analysis Techniques", _**J. Electrochem. Soc.**_, 163, A2149-A2164 (2016)'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),  
                        dcc.Markdown(('- Matthew Newville, "Fundamentals of XAFS", _**Reviews in Mineralogy and Geochemistry**_, 78, 33 (2014)'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),            
                        dcc.Markdown(('- https://www.spectro.com/xrf-principle'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),      
                        dcc.Markdown(('- https://www.edmundoptics.com/knowledge-center/application-notes/lasers/basic-principles-of-raman-scattering-and-spectroscopy/'), dangerously_allow_html=True,
                                 style={'textAlign':'justify', 'margin-left':'30px', 'font-size':'16px'}),                               
                        ], style={'textAlign':'justify', 'margin-left':'40px', 'margin-right':'60px'},
                        ),                       
             html.Div(id='Options-content'),
            ]
    )
