from pathlib import Path
import fitz
from llm_describer import describe_with_llm


def table_to_str(table_data):
    """
    Convert table rows to structured text for better RAG retrieval.
    Keeps rows and columns clear.
    """
    lines = []

    for row in table_data:
        clean_row = [
            str(cell).strip() if cell is not None else ""
            for cell in row
        ]

        lines.append(" | ".join(clean_row))

    return "\n".join(lines)


def rect_overlaps_any(bbox, areas):

    rect = fitz.Rect(bbox)
    return any(rect.intersects(fitz.Rect(area)) for area in areas)


def process_pdf(file_path, min_text_chars=20):


    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    results = []
    doc = fitz.open(str(path))

    for page_num, page in enumerate(doc, start=1):

        table_areas = []

        for table_index, table in enumerate(page.find_tables(), start=1):
            try:
                table_data = table.extract()

                if not table_data:
                    continue

                # raw structured table text
                raw_table_text = table_to_str(table_data)

                # save RAW table for exact retrieval
                results.append(
                    f"[PAGE {page_num} | TABLE_RAW]:\n{raw_table_text}"
                )

                # LLM summary for semantic retrieval
                table_summary = describe_with_llm(
                    raw_table_text,
                    "table"
                )

                if table_summary:
                    results.append(
                        f"[PAGE {page_num} | TABLE_SUMMARY]: {table_summary}"
                    )

                # save bbox so text blocks inside table are skipped
                table_areas.append(table.bbox)

            except Exception as e:
                print(
                    f"Table extraction error "
                    f"(page {page_num}, table {table_index}): {e}"
                )
        for img_index, img in enumerate(page.get_images(full=True), start=1):
            try:
                xref = img[0]
                image_info = doc.extract_image(xref)

                if not image_info:
                    continue

                image_bytes = image_info["image"]
                image_ext = image_info.get("ext", "png")

                image_description = describe_with_llm(
                    image_bytes,
                    "image",
                    hint=f"page {page_num}, image {img_index} ({image_ext})"
                )

                if image_description:
                    results.append(
                        f"[PAGE {page_num} | IMAGE]: {image_description}"
                    )

            except Exception as e:
                print(
                    f"Image extraction error "
                    f"(page {page_num}, image {img_index}): {e}"
                )

        for block in page.get_text("blocks"):
            block_text = block[4].strip()
            block_bbox = block[:4]

            
            if len(block_text) < min_text_chars:
                continue

            
            if rect_overlaps_any(block_bbox, table_areas):
                continue

            results.append(
                f"[PAGE {page_num} | TEXT]: {block_text}"
            )

    doc.close()

    return results