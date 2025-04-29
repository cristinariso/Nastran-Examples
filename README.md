# Nastran Examples

This repository contains examples of structural dynamics and aeroelastic analyses using Nastran, which I used in my AE 6200 - Advanced Aeroelasticity class at Georgia Tech to teach how to carry out such analyses and interpret the results. The lecture slides are also included in this repository. The examples are based on the Pazy wing aeroelastic benchmark case analyzed as part of my contributions to the Large Deflection Working Group of the Third AIAA Aeroelastic Prediction Workshop (AePW3).

## Folder Structure

Folder `00_Slides` contains the lecture slides.

Folder `01_Modal` contains examples of analyses using the Nastran linear modal analysis solver SOL 103.

Folder `02_Flutter` contains examples of analyses using the Nastran linear flutter analysis solved SOL 145.

The slides present modal and flutter analyses of the Pazy wing with the original flexible tip rod and no tip mass. The folders also contain the analysis files for the model variant with a rigid tip rod used for the AePW3 results. 

## Additional Examples

I plan to add more examples as I develop similar lectures for other types of analyses.

## References

If you use or adapt the lecture slides for your work, please give proper credit by referencing this repository and including a link. 

If you use Nastran analysis examples from this repository, I kindly ask that you cite the relevant papers listed below, where appropriate.

The Pazy Wing aeroelastic benchmark case and its original finite element model (FEM) with flexible tip rod were developed in:

Avin, O., Raveh, D. E., Drachinsky, A., Ben-Shmuel, Y., and Tur, M., "Experimental Aeroelastic Benchmark of a Very Flexible Wing," AIAA Journal, 2022. DOI: https://doi.org/10.2514/1.J060621

The modified FEM with a rigid tip rod and the flutter analysis models based on the two FEM variants and the doublet-lattice method (DLM) were developed in:

Riso, C., and Cesnik, C. E. S., "Impact of Low-Order Modeling on Aeroelastic Predictions for Very Flexible Wings," Journal of Aircraft, 2023. DOI: https://doi.org/10.2514/1.C036869

If you are interested in a summary of the studies conducted on the Pazy wing as part of the AePW3, you can find it in:

Ritter et al., "Collaborative Pazy Wing Analyses for the Third Aeroelastic Prediction Workshop," AIAA SciTech Forum, 2024. DOI: https://doi.org/10.2514/6.2024-0419

The workshop website is https://nescacademy.nasa.gov/workshops/AePW3/public/ 

## Feedback

If you have suggestions for improving the materials in this repository, please feel free to get in touch. 

## Contact

Cristina Riso (criso@gatech.edu)
