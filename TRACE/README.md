# TRACE: Your Diffusion Model Is Secretly an Instance Edge Detector

### [ICLR 2026 Oral Presentation](https://iclr.cc/)

[![Project Page](https://img.shields.io/badge/Project-Page-gold?style=for-the-badge)](https://shjo-april.github.io/TRACE)
[![Paper](https://img.shields.io/badge/Paper-PDF-red?style=for-the-badge)](https://openreview.net/pdf?id=BjElYlJKMj)
[![arXiv](https://img.shields.io/badge/arXiv-2025.xxxxx-b31b1b?style=for-the-badge)](https://arxiv.org/abs/2503.07982)
[![Code](https://img.shields.io/badge/Code-GitHub-black?style=for-the-badge)](https://github.com/shjo-april/TRACE)

**[Sanghyun Jo](https://shjo-april.github.io/)<sup>1*</sup>, [Ziseok Lee](https://ziseoklee.github.io/)<sup>2*</sup>, [Wooyeol Lee](https://thisiswooyeol.github.io/)<sup>2</sup>, [Jonghyun Choi](https://ppolon.github.io/)<sup>2</sup>, [Jaesik Park](https://jaesik.info/)<sup>2†</sup>, [Kyungsu Kim](https://aibl.snu.ac.kr/team/pi-information)<sup>2†</sup>**

<sup>1</sup>OGQ &nbsp; <sup>2</sup>Seoul National University  
<sup>*</sup>Equal contribution &nbsp; <sup>†</sup>Corresponding authors

---

## 🌟 Highlights

- **Key Discovery**: Text-to-image diffusion models secretly encode instance boundaries in self-attention maps during denoising.
- **TRACE Framework**: Annotation-free instance edge extraction via Instance Emergence Point (IEP) + Attention Boundary Divergence (ABDiv) + One-step distillation.
- **Results**: +5.1 AP on COCO (unsupervised instance seg.), +7.1 PQ on VOC (tag-supervised panoptic seg.), 81× faster inference.

## 📂 Project Page Structure

```
TRACE/
├── index.html              # Main project page
├── README.md               # This file
└── static/
    ├── css/
    │   └── style.css       # Stylesheet
    └── images/
        ├── method_overview.png
        ├── observation.png
        ├── uis_results.png
        ├── wps_results.png
        ├── qualitative.png
        └── diffusion_vs_nondiffusion.png
```

## 🖼️ Adding Images

Place your figure images in `static/images/`. The page expects the following files:

| File | Description |
|------|-------------|
| `method_overview.png` | Figure 4: TRACE method overview |
| `observation.png` | Figure 1: Instance cues in diffusion attention |
| `uis_results.png` | Table 1: UIS results |
| `wps_results.png` | Table 2: WPS results |
| `qualitative.png` | Figure 2: Qualitative comparison |
| `diffusion_vs_nondiffusion.png` | Table 5 + Figure 8: Backbone comparison |

> **Tip**: Export figures from the paper at 2× resolution for crisp display on Retina screens.

## 🚀 Deployment

This project page is designed for **GitHub Pages**:

1. Push this folder to your `shjo-april.github.io` repo under `/TRACE/`
2. Enable GitHub Pages in repository settings
3. Access at `https://shjo-april.github.io/TRACE`

## 📝 Updating Links

In `index.html`, update the `href` attributes in the hero action buttons:

- **Paper**: Link to OpenReview PDF (`https://openreview.net/pdf?id=BjElYlJKMj`)
- **Code**: Link to GitHub repository (`https://github.com/shjo-april/TRACE`)
- **OpenReview**: Link to OpenReview forum (`https://openreview.net/forum?id=BjElYlJKMj`)
- **arXiv**: Link to arXiv preprint (`https://arxiv.org/abs/2503.07982`)
- **Video**: Link to presentation video (YouTube/Bilibili)
- **Demo**: Link to Huggingface demo space

## 📖 Citation

```bibtex
@inproceedings{jo2026trace,
  title     = {TRACE: Your Diffusion Model Is Secretly an Instance Edge Detector},
  author    = {Jo, Sanghyun and Lee, Ziseok and Lee, Wooyeol and Choi, Jonghyun and Park, Jaesik and Kim, Kyungsu},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2026},
  note      = {Oral Presentation}
}
```

## 📜 License

This project page template is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
