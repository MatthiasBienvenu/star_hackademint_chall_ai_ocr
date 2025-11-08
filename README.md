# OhCRap — OCR Challenge

**CTF Challenge for [star.hackademint.org](https://star.hackademint.org/) 2025**

## Challenge Overview

Gwilherm accidentally dropped a post-it note with his password into the trash. The trash now contains hundreds of synthetic paper images, and only one contains the actual password. The password includes his first name "gwilherm" with random capitalization mixed throughout.

**Challenge Goal:** Find the image containing the password among all the trash!

## What Solvers Get

Participants receive only the `corbeille/` directory containing 500 PNG images. Each image shows a rotated text string on a colored background. One of these images contains the secret password with "gwilherm" embedded in it.

## Files

- **[`generate_trashcan.py`](OhCRap/generate_trashcan.py)** — Generates 500 synthetic rotated text images. One random image contains the secret word with "gWILheRm" (mixed case) embedded between random characters.

- **[`solution.py`](OhCRap/solution.py)** — Reference OCR-based solver that:
  - Loads all images from `corbeille/`
  - Applies deskewing by estimating rotation angle
  - Tests 4 rotation candidates (0°, 90°, 180°, 270°)
  - Runs Tesseract OCR on each candidate
  - Searches for "gwilherm" (case-insensitive)
  - Prints the filename containing the secret

- **`corbeille/`** — Directory containing the challenge images (what participants access)

- **[`LICENSE`](LICENSE)** — MIT License

- **[`.gitignore`](.gitignore)** — Python project gitignore

## Dependencies

### Python Requirements
- **Python 3.8+**
- **Packages:**
  ```bash
  pip install pillow numpy opencv-python pytesseract
  ```

## Usage

### For Challenge Authors

**Generate the challenge images:**
```bash
cd OhCRap
python generate_trashcan.py
```

This creates 500 images in `corbeille/`, with one containing the secret password.

**Note:** [`generate_trashcan.py`](OhCRap/generate_trashcan.py) uses `Arial.TTF` font. Ensure it's available or adjust the font path if needed.

### For Solvers

**Run the OCR solver:**
```bash
cd OhCRap
python solution.py
```

The script will print the filename (e.g., `42.png`) that contains the secret password.

## Technical Details

### Image Generation
- Each image is 256×256 pixels
- Random background color (RGB 150-255)
- Random text color (RGB 0-100)
- Text rotated randomly between -70° and 70°
- Secret format: `[5 random chars] + "gWILheRm" + [3 random chars]`

### Solution Approach
1. **Deskewing:** Uses OpenCV's `minAreaRect` to estimate text rotation
2. **Multi-rotation:** Tests 4 orientations (0°, 90°, 180°, 270°) to handle rotation ambiguity
3. **OCR:** Applies Tesseract to extract text from each rotated variant
4. **Search:** Case-insensitive search for "gwilherm" in extracted text

## Challenge Difficulty

- **Easy to Medium** — Requires basic OCR knowledge and image preprocessing
- **Skills tested:**
  - Image processing (rotation correction)
  - OCR usage (Tesseract)
  - Python automation
  - Pattern matching

## Notes

- OCR accuracy depends on rotation correction, contrast, and preprocessing quality
- The [`unrotate`](OhCRap/solution.py) function compensates for rotation ambiguity by testing 4 candidates
- Tuning thresholds, font size, or adding additional preprocessing (denoising, contrast adjustment) may improve results
- Alternative solutions using different OCR engines or machine learning approaches are possible

## License

MIT License — See [LICENSE](LICENSE) for details.

Copyright (c) 2025 MatthiasBienvenu

---

**Happy Hacking! 🎯**

*Part of star.hackademint.org CTF 2025*
