import os

from langchain_community.document_loaders import PyPDFLoader


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts all the text from the pdf files
    Args:
        file_path (str): Path to the pdf file
    Returns:
        str: The extracted text from all the pages
    Raises:
        FileNotFoundError
        RuntimeError
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Pdf file not found:{file_path}")
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load()
        if not pages:
            return ""
        return "".join(page.page_content for page in pages)
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from Pdf {e}")
