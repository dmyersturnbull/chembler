import pytest

from mandos.cli import Commands, What

from . import get_test_resource


class TestPredictionSearch:
    def test_find(self):
        df, triples = Commands.search_for(What.prediction, get_test_resource("inchis.txt"), None)
        # TODO double-check
        assert len(df) == 4
        assert len(triples) == 1
        assert triples[0].object_id == "CHEMBL2093872"
        assert triples[0].compound_name.lower() == "alprazolam"


if __name__ == "__main__":
    pytest.main()
