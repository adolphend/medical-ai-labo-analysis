# Open-source stacks organized by diagnostic specialty.

[Research index](../README.md) · [Academic references](../evidence/references.md)

### Specialty-specific open-source stacks

| Diagnostic branch | Components | Peer-reviewed research | First evaluable prototype |
|---|---|---|---|
| **Radiology** | [Orthanc](https://github.com/orthanc-server/orthanc) + [OHIF](https://github.com/OHIF/Viewers) + [pydicom](https://github.com/pydicom/pydicom) + optionally [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) | Jodogne 2018, DOI [10.1007/s10278-018-0082-y](https://doi.org/10.1007/s10278-018-0082-y); Wasserthal 2023, DOI [10.1148/ryai.230024](https://doi.org/10.1148/ryai.230024) | Deidentified study ingest, metadata QC, visualization and physician annotation; CPU-only segmentation may be slow |
| **Pathology** | [QuPath](https://github.com/qupath/qupath) + [HistoQC](https://github.com/choosehappy/HistoQC) | Bankhead 2017, DOI [10.1038/s41598-017-17204-5](https://doi.org/10.1038/s41598-017-17204-5) | Slide QC and reproducible cell/tissue measurements on small regions |
| **Clinical laboratory** | [OpenELIS Global 2](https://github.com/DIGI-UW/OpenELIS-Global-2) + [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | Clinical need supported by W0/W1; **no peer-reviewed outcome paper for this pairing verified in this review** | Synthetic laboratory result chain and acknowledgement monitoring |
| **Cardiology / ECG** | [WFDB](https://github.com/MIT-LCP/wfdb-python) + [NeuroKit2](https://github.com/neuropsychology/NeuroKit) | Makowski et al. 2021, DOI [10.3758/s13428-020-01516-y](https://doi.org/10.3758/s13428-020-01516-y) | ECG lead import, signal quality and feature extraction with no deep model training |
| **Clinical text** | [medSpaCy](https://github.com/medspacy/medspacy) + [HAPI FHIR](https://github.com/hapifhir/hapi-fhir) | Eyre et al. 2021, [publication](https://arxiv.org/abs/2106.07799) | Rule-based negation, section and uncertainty extraction, with explicit human confirmation |
