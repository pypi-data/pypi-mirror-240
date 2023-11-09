"""
LayoutLMDocumentQA is a multimodal good for
visual question answering on real world docs lik invoice, pdfs, etc
"""
from transformers import pipeline
from swarms.models.base import AbstractModel


class LayoutLMDocumentQA(AbstractModel):
    """
    LayoutLMDocumentQA for document question answering:

    Args:
        model_name (str, optional): [description]. Defaults to "impira/layoutlm-document-qa".
        task (str, optional): [description]. Defaults to "document-question-answering".

    Usage:
    >>> from swarms.models import LayoutLMDocumentQA
    >>> model = LayoutLMDocumentQA()
    >>> out = model("What is the total amount?", "path/to/img.png")
    >>> print(out)

    """

    def __init__(
        self,
        model_name: str = "impira/layoutlm-document-qa",
        task: str = "document-question-answering",
    ):
        self.pipeline = pipeline(self.task, model=self.model_name)

    def __call__(self, task: str, img_path: str):
        """Call for model"""
        out = self.pipeline(img_path, task)
        out = str(out)
        return out
