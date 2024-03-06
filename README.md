# Introduction
The purpose of this reporsitory is to introduce the chirp spectrum, a close ally of the Fourier transform and the Z-transform. 
It is known that the Fourier transform is the Z-transform that is computed on the unit circle. 
Traditionally, the chirp z-transform, as defined in papers such as (rabiner1969chirp), is the spectrum computed at any circular or helical path on the z-plane.

We have noticed usually that, when the word chirp occurs, it is often confused with the chirp signal, which is a linearly-swept frequency (co)sine signal generated over a certain time period. 
But no such confusion/relation needs to exist, as the name possibly just alludes to the fact that the basis sequences are "swept" across the z-plane. 

This repository contains analysis experiments that reflect/explain the chirp spectrum. 
For more information on the analysis and practical applications, please look into: 
> "Joysingh, S. J., Vijayalakshmi, P., & Nagarajan, T. (2024). Significance of Chirp MFCC as a Feature in Speech and Audio Applications. arXiv preprint arXiv:2402.12239." [Link](https://arxiv.org/abs/2402.12239)

In the paper, we explore the analysis of chirp magnitude, and phase spectrum, point out it's advantages, and also apply the theory for a few classification tasks. 

If you have found this repository useful in your work, please consider citing.

# References
- (rabiner1969chirp) Rabiner, L., Schafer, R. W., & Rader, C. (1969). The chirp z-transform algorithm. IEEE transactions on audio and electroacoustics, 17(2), 86-92.
