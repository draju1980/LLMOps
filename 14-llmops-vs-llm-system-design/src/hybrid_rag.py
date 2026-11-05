"""Module 14: Hybrid RAG"""
class HybridRAG:
    def __init__(self):
        self.dense_index = {}
        self.sparse_index = {}

    def reciprocal_rank_fusion(self, dense_results, sparse_results, k=60):
        scores = {}
        for i, doc in enumerate(dense_results):
            scores[doc] = scores.get(doc, 0) + 1/(k + i)
        for i, doc in enumerate(sparse_results):
            scores[doc] = scores.get(doc, 0) + 1/(k + i)
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
