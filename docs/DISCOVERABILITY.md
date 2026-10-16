# Discover Medical AI Laboratory — clinical AI tools research and development

**Medical AI Laboratory** is a public, early-stage research and planning repository for developing modular **clinical AI tools**, **diagnostic decision-support software**, and **medical imaging AI** systems. The planned clinician-facing software is **not developed or validated yet**. Code currently in the repository consists of experimental helpers and evaluation scaffolding; future application components are intended to be generated iteratively with **OpenCode agents**.

**Canonical project link:** https://github.com/adolphend/medical-ai-labo-analysis

## What researchers can find

- **Medical imaging AI:** ultrasound and echocardiography, chest X-ray, CT, MRI, pathology and related clinical modalities. [Imaging workflows](../research/imaging/README.md).
- **Open-source medical AI models:** upstream inventory, prospective forking, version tracking, pretrained weights and license review. [Model registry](../research/imaging/model-integration-registry.md) · [Forking plan](../automation/README.md).
- **Disease-centered clinical AI workflows:** 50 proposed disease/checkup pathways, from patient history to appropriate examinations, quality control, findings, reports, clinician-reviewed guideline evidence and follow-up. [Disease registry](../diseases/README.md).
- **Model evaluation and benchmarks:** DVC-enabled dataset planning, binary/context metrics, MedGemma comparison plans, and a public pneumonia chest X-ray dataset example. [Evaluation program](../evaluation/README.md).
- **MedGemma and specialized model comparison:** local 4-bit MedGemma research on an 8 GB development GPU, optional comparison against small, task-specific models. [MedGemma analysis](../evaluation/medgemma-technical-clinical-analysis.md).
- **OpenCode AI agent planning:** planned model discovery, fork review, dataset governance, evaluation, testing, code-generation and integration workflows. [Agent catalog](../.opencode/README.md).

## Terms for accurate project discovery

Medical AI research; clinical AI tool development; clinical decision support; diagnostic AI; computer-aided diagnosis; medical image analysis; medical computer vision; ultrasound AI; echocardiography AI; X-ray AI; CT imaging AI; MRI AI; digital pathology; medical segmentation; disease detection; medical AI benchmark; medical image datasets; MedGemma evaluation; lightweight medical AI; open-source medical models; disease-specific AI agents; OpenCode clinical software development.

These phrases describe **research interests and planned capabilities**, not functioning or certified products. Neither listed model availability nor published third-party benchmarks demonstrate validation of this repository.

## Indexing and research discovery

A public GitHub README and internally linked descriptive Markdown pages may be found by search engines and AI-based retrieval services. Indexing, ranking, or ingestion into AI answer systems is **not guaranteed**. Search engines decide what they crawl; AI vendors determine their retrieval sources and update schedules.

### Repository owner checklist

1. Set GitHub **About → Description** to:
   `Research-stage clinical AI tools development: medical imaging, disease workflows, open-source model evaluation, forking and OpenCode agents.`
2. Add these **GitHub topics** (at most 20): `medical-ai`, `clinical-decision-support`, `medical-imaging`, `healthcare-ai`, `computer-vision`, `medical-image-analysis`, `medical-diagnosis`, `deep-learning`, `open-source`, `machine-learning`, `medgemma`, `ultrasound`, `radiology`, `medical-datasets`, `model-evaluation`, `benchmarking`, `opencode`, `digital-pathology`.
3. Confirm the repository is public and add a project website URL to **About → Website** only once such a website genuinely exists.
4. For stronger crawl control, publish a separately hosted documentation site under a domain you control (e.g. GitHub Pages) with HTML title, description, canonical URLs, robots access and an XML sitemap. A sitemap inside the GitHub source repository by itself **does not** submit GitHub URLs to search engines.
5. Verify your own site in [Google Search Console](https://search.google.com/search-console/about) and submit the hosted site's sitemap. Search Console is not a way to verify ownership of GitHub.com as a whole.
6. Publish real papers, technical reports, reproducible benchmark results and citable releases only as they become available, linking back to this repository. Avoid fabricated benchmark results, claims or metadata.

## Honest status

The current public repository is a **research and planning work product**. External forks have not been executed, 50 disease tools have not been implemented, and model comparisons have not been clinically validated. Search descriptions must retain this distinction.
