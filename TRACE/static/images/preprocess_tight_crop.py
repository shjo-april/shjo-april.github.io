from __future__ import annotations

import os
from typing import Optional, Tuple

from PIL import Image


def tight_crop_rgba_by_alpha(
    in_path: str,
    out_path: Optional[str] = None,
    *,
    alpha_threshold: int = 1,
    padding: int = 0,
    return_bbox: bool = False,
) -> Image.Image | Tuple[Image.Image, Tuple[int, int, int, int]]:
    """
    Tight crop an RGBA PNG using its alpha channel.

    Args:
        in_path: input RGBA PNG path
        out_path: if provided, saves cropped PNG there
        alpha_threshold: pixel is considered "foreground" if alpha > threshold (0~255)
        padding: extra pixels to expand bbox in all directions (clamped to image bounds)
        return_bbox: if True, returns (cropped_image, (left, top, right, bottom))

    Returns:
        cropped PIL Image (and bbox if return_bbox=True)

    Notes:
        - bbox uses PIL convention: (left, top, right, bottom) where right/bottom are exclusive.
        - If the image is fully transparent (no alpha > threshold), it returns the original image.
    """
    img = Image.open(in_path).convert("RGBA")
    w, h = img.size

    alpha = img.getchannel("A")  # 'L' image
    # Create a binary mask: 255 where alpha > threshold else 0
    mask = alpha.point(lambda a: 255 if a > alpha_threshold else 0, mode="L")

    bbox = mask.getbbox()  # None if fully black (no foreground)
    if bbox is None:
        # Fully transparent; decide behavior: return original
        if out_path is not None:
            os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
            img.save(out_path)
        return (img, (0, 0, w, h)) if return_bbox else img

    left, top, right, bottom = bbox

    if padding > 0:
        left = max(0, left - padding)
        top = max(0, top - padding)
        right = min(w, right + padding)
        bottom = min(h, bottom + padding)

    cropped = img.crop((left, top, right, bottom))

    if out_path is not None:
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        cropped.save(out_path)

    return (cropped, (left, top, right, bottom)) if return_bbox else cropped


if __name__ == "__main__":
    # Example usage
    inp = "logo.png"
    out = "logo_cropped.png"
    cropped, bbox = tight_crop_rgba_by_alpha(
        inp,
        out,
        alpha_threshold=4,  # 1~10 seems good for typical anti-aliased logos
        padding=0,          
        return_bbox=True,
    )
    print("Saved:", out)
    print("BBox:", bbox)
    print("New size:", cropped.size)