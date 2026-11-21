import unittest

from services.stats import calculate_statistics
from services.textPrediction import predict_next_words, generate_sentence


class TestStatistics(unittest.TestCase):
    def test_population_variance_and_std(self):
        result = calculate_statistics([2, 4, 4, 4, 5, 5, 7, 9])
        self.assertAlmostEqual(result["variance"], 4.0)
        self.assertAlmostEqual(result["std"], 2.0)
        self.assertAlmostEqual(result["mean"], 5.0)


class TestMarkov(unittest.TestCase):
    def test_next_word_probabilities(self):
        model = {"hello": ["world", "there", "world"]}
        result = predict_next_words(model, "hello")
        self.assertAlmostEqual(result["world"], 2 / 3)
        self.assertAlmostEqual(result["there"], 1 / 3)
        self.assertAlmostEqual(sum(result.values()), 1.0)

    def test_sentence_generation(self):
        model = {"hello": ["world"], "world": ["again"]}
        self.assertEqual(generate_sentence(model, "hello", 3), "Hello world again.")


if __name__ == "__main__":
    unittest.main()
