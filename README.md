# OhCRap — OCR Challenge

**CTF Challenge for [star.hackademint.org](https://star.hackademint.org/) 2025**

## Challenge Overview

Jérémie needs to access the Supercomputer to launch an emergency virtualization. But he accidentally dropped the post-it note containing his password into his desk trash, where it got mixed up with dozens of useless papers.

To find the right password, you'll need to search through all this mess. Fortunately, Jérémie remembers one detail: the password definitely contains the word **"lyoko"**.

**Challenge Goal:** Find the image containing the password among all the trash!

⚠️ **Note:** The solution may take a few minutes to run.

## What Solvers Get

Participants receive only the `corbeille/` directory containing 500 JPEG images. Each image shows a rotated text string on a colored background. One of these images contains the secret password with "lyoko" embedded in it.

## Files

- **[`generate_trashcan.py`](OhCRap/generate_trashcan.py)** — Generates 500 synthetic rotated text images. One random image contains the secret word with "LyoKO" (mixed case) embedded between random characters.

- **[`solution.py`](OhCRap/solution.py)** — Reference OCR-based solver that:
  - Loads all images from `corbeille/`
  - Applies deskewing by estimating rotation angle
  - Tests 4 rotation candidates (0°, 90°, 180°, 270°)
  - Runs Tesseract OCR on each candidate
  - Searches for "lyoko" (case-insensitive)
  - Prints the filename containing the secret

- **`corbeille/`** — Directory containing the challenge images (what participants access)

- **[`LICENSE`](LICENSE)** — MIT License

- **[`.gitignore`](.gitignore)** — Python project gitignore

## Dependencies

### System Requirements
- **Linux** (Ubuntu/Debian recommended)
- **Tesseract OCR** — Install via:
  ```bash
  sudo apt update && sudo apt install -y tesseract-ocr
  ```

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

The script will print the filename that contains the secret password.

⏱️ **Processing time:** The solution may take several minutes to complete as it processes all images with multiple rotation candidates.

## Technical Details

### Image Generation
- Each image is 256×256 pixels
- Random background color (RGB 150-255)
- Random text color (RGB 0-100)
- Text rotated randomly between -70° and 70°
- Secret format: `[3 random chars] + "LyoKO" + [3 random chars]`

### Solution Approach
1. **Deskewing:** Uses OpenCV's `minAreaRect` to estimate text rotation
2. **Multi-rotation:** Tests 4 orientations (0°, 90°, 180°, 270°) to handle rotation ambiguity
3. **OCR:** Applies Tesseract to extract text from each rotated variant
4. **Search:** Case-insensitive search for "lyoko" in extracted text

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
- Processing 500 images with 4 rotation candidates each (2000 OCR operations) takes time — be patient!

## License

MIT License — See [LICENSE](LICENSE) for details.

Copyright (c) 2025 MatthiasBienvenu

---

**Happy Hacking! 🎯**

*Part of star.hackademint.org CTF 2025*
