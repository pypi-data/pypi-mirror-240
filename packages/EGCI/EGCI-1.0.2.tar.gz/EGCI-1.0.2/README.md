# EGCI (Ecoacoustics Glabal Complexity Index)

The EGCI python package provides a tool for calculating the Ecoacoustic Global Complexity Index (EGCI), an innovative approach for quantifying the complexity of audio segments recorded by acoustic sensors in environments with high biodiversity, such as the Amazon rainforest. It is an unsupervised method for robust characterization of ecoacoustic richness.

## Features

EGCI Calculation: Compute the Ecoacoustic Global Complexity Index using a combination of Entropy, Divergence, and Statistical Complexity, enabling a holistic assessment of the biodiversity of an acoustic environment.

Visualization: Helps to visualize the ecoacoustic dynamics of the rainforest by mapping each audio segment, of varying lengths, as a single point in a 2D-plane, aiding in the understanding of the soundscape.

Unsupervised Method: The EGCI employs unsupervised methods, eliminating the need for individual species labeling. This makes the package well-suited for handling large amounts of raw audio data and provides a robust characterization of ecoacoustic richness.

## Citation
If you use the EGCI package in your research or work, please consider citing the original article:
Colonna JG, Carvalho JRH, Rosso OA (2020) Estimating ecoacoustic activity in the Amazon rainforest through Information Theory quantifiers. PLOS ONE 15(7): e0229425. https://doi.org/10.1371/journal.pone.0229425

## How to use

```python 
import numpy as np
import soundfile as sf
import EGCI
import matplotlib.pyplot as plt

# download a record file from this url: "https://drive.google.com/file/d/1QL5GimLjGLKBIiMzoa7VXlCR4GCpWBwc/view?usp=drivesdk"
# load this record
x, fs = sf.read('Adenomera andre.wav') # record of an anuran call

lag = 256 # time lag
C, H, J = EGCI.index(x, lag=lag) # C is the EGCI

boundaries_C, boundaries_H = EGCI.boundaries(lag) # these boundaries are only useful for plotting

plt.figure()
plt.plot(boundaries_H, boundaries_C, '--k')
plt.scatter(H, C, marker='.', s=100, label='Adenomera andre')
plt.xlabel('Entropy')
plt.ylabel('EGCI (Complexity)')
plt.xlim([0, 1])
plt.ylim([0, np.max(boundaries_C)+0.01])
plt.title('Adenomera andre.wav')
plt.legend(loc = 'best')
plt.show()
```
