"""Overall Score
"""

from deepeval.test_case import LLMTestCase
from deepeval.singleton import Singleton
from deepeval.test_case import LLMTestCase
from deepeval.metrics.answer_relevancy import AnswerRelevancyMetric
from deepeval.metrics.conceptual_similarity import ConceptualSimilarityMetric
from deepeval.metrics.factual_consistency import FactualConsistencyMetric
from deepeval.metrics.base_metric import BaseMetric
from deepeval.evaluator import assert_test


class OverallScoreMetric(BaseMetric, metaclass=Singleton):
    def __init__(self, minimum_score: float = 0.5):
        self.minimum_score = minimum_score
        self.answer_relevancy = AnswerRelevancyMetric()
        self.factual_consistency_metric = FactualConsistencyMetric()
        self.conceptual_similarity_metric = ConceptualSimilarityMetric()

    def __call__(self, test_case: LLMTestCase):
        score = self.measure(test_case=test_case)
        self.success = score > self.minimum_score
        return score

    def measure(
        self,
        test_case: LLMTestCase,
    ) -> float:
        metadata = {}
        if test_case.context is not None:
            factual_consistency_score = self.factual_consistency_metric.measure(
                test_case
            )
            metadata["factual_consistency"] = float(factual_consistency_score)

        if test_case.input is not None:
            answer_relevancy_score = self.answer_relevancy.measure(test_case)
            metadata["answer_relevancy"] = float(answer_relevancy_score)

        if test_case.expected_output is not None:
            conceptual_similarity_score = (
                self.conceptual_similarity_metric.measure(test_case)
            )
            metadata["conceptual_similarity"] = float(
                conceptual_similarity_score
            )

        overall_score = sum(metadata.values()) / len(metadata)

        self.success = bool(overall_score > self.minimum_score)
        return overall_score

    def is_successful(self) -> bool:
        return self.success

    @property
    def __name__(self):
        return "Overall Score"


def assert_overall_score(
    query: str,
    output: str,
    expected_output: str,
    context: str,
    minimum_score: float = 0.5,
):
    metric = OverallScoreMetric(minimum_score=minimum_score)
    test_case = LLMTestCase(
        input=query,
        actual_output=output,
        expected_output=expected_output,
        context=context,
    )
    assert_test(test_case, metrics=[metric])
