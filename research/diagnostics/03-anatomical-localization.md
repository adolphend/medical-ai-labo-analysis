# Anatomy and spatial localization

[Diagnostic research index](README.md) · [Acquisition quality](02-acquisition-quality.md) · [Abnormalities](04-abnormality-and-disease-detection.md)

## Responsibility
Detect and localize normal anatomy in the correct coordinate system, including organs, tissues, major vessel territories, brain regions and specific anatomical targets where validated.

| Object and modality | Open material | Publication | Interpretation |
|---|---|---|---|
| CT organs and anatomical structures | [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) | Wasserthal et al., *TotalSegmentator*, Radiology: AI (2023), DOI [10.1148/ryai.230024](https://doi.org/10.1148/ryai.230024) | Pretrained segmentation, 3D can be slow on CPU; commercial task licensing differs |
| Multi-organ / lesion tasks | [MONAI model zoo](https://github.com/Project-MONAI/model-zoo) | [MONAI framework](https://arxiv.org/abs/2211.02701) | Select an exact compatible pretrained bundle; model zoo does not imply universal anatomy |
| Biomedical segmentation methodology | [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) | Isensee et al., *nnU-Net*, Nature Methods (2021), DOI [10.1038/s41592-020-01008-z](https://doi.org/10.1038/s41592-020-01008-z) | Framework alone needs task-specific trained weights |
| Interactive medical regions | [MedSAM](https://github.com/bowang-lab/MedSAM), [LiteMedSAM](https://github.com/bowang-lab/MedSAM/tree/main/LiteMedSAM) | Ma et al., *Segment Anything in Medical Images*, Nature Communications (2024), DOI [10.1038/s41467-024-44824-z](https://doi.org/10.1038/s41467-024-44824-z) | Prompted contours, not automatic semantic identification |
| Brain extraction / tissue parcellation | [ANTsPyNet](https://github.com/ANTsX/ANTsPyNet), [ANTs](https://github.com/ANTsX/ANTs) | Avants et al., *A reproducible evaluation of ANTs similarity metric performance in brain image registration*, NeuroImage (2011), DOI [10.1016/j.neuroimage.2010.09.025](https://doi.org/10.1016/j.neuroimage.2010.09.025) | Registration is not automatically pathology detection |
| Cell and nuclei localization | [Cellpose](https://github.com/MouseLand/cellpose), [QuPath](https://github.com/qupath/qupath) | Stringer et al., *Cellpose*, Nature Methods (2021), DOI [10.1038/s41592-020-01018-x](https://doi.org/10.1038/s41592-020-01018-x) | Microscope images / pathology, not typical clinical CT |
| Nerves / plexuses | [3D Slicer](https://github.com/Slicer/Slicer), [ITK-SNAP](https://github.com/pyushkevich/itksnap) | Fedorov et al., *3D Slicer*, Magnetic Resonance Imaging (2012), DOI [10.1016/j.mri.2012.05.001](https://doi.org/10.1016/j.mri.2012.05.001) | General open viewer/annotation; no validated universal pretrained nerve segmentation established |
| Protein structure (molecular scale) | [OpenFold](https://github.com/aqlaboratory/openfold), [ColabFold](https://github.com/sokrypton/ColabFold) | Mirdita et al., *ColabFold*, Nature Methods (2022), DOI [10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1) | Protein *structure prediction* from sequences is a different workflow from radiology localization, often substantial compute |
| Protein localization inside cells | [CellProfiler](https://github.com/CellProfiler/CellProfiler) | McQuin et al., *CellProfiler 3.0*, PLOS Biology (2018), DOI [10.1371/journal.pbio.2005970](https://doi.org/10.1371/journal.pbio.2005970) | Fluorescence microscopy and cell assays require specified staining/markers |

## Data and geometry contract
Inputs: modality, body region, series identifier, pixel/voxel spacing, orientation, patient-space coordinate frame, preprocessing history. Outputs: semantic region label if supported, mask/bounding box, region measurements, confidence/quality, segmentation method/model/weights version, provenance and operator edits.

## Unresolved gaps
No single tool can reliably localize *all* organs, microstructures, nerves, proteins and systems at once. Proteins and subcellular features generally require fundamentally different acquisitions. System-specific nerve segmentation, small-vessel tracing and combinatorial anatomical relationships demand dedicated reviews and datasets.

## Evaluation
Dice/IoU and HD95 for masks; localization error in mm, topology for vessels/nerves, measurement repeatability, out-of-distribution errors, time/RAM and expert agreement. Metrics must use independent ground truth.
