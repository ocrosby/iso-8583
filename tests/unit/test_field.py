import pytest

from src.iso8583.field import FieldBuilder, Field


@pytest.fixture
def builder() -> FieldBuilder:
    return FieldBuilder()


class TestFieldBuilder:
    def test_field_builder_constructor(self, builder):
        assert builder.get_instance() is None

    def test_build(self, builder):
        builder.build()

        assert builder.get_instance() is not None

    def test_build_definition(self, builder):
        builder.build()
        builder.build_definition('test')

        assert builder.get_instance().definition == 'test'


class TestField:
    def test_is_alpha_affirmative(self):
        assert Field('a..11').is_alpha()

    def test_is_alpha_negative(self):
        assert not Field('n.6').is_alpha()

    def test_is_numeric_affirmative(self):
        assert Field('n.6').is_numeric()

    def test_is_numeric_negative(self):
        assert not Field('a..11').is_numeric()

    def test_is_lvar_affirmative(self):
        assert Field('n.l6').is_lvar()

    def test_is_lvar_negative_llvar(self):
        assert not Field('a..11').is_lvar()

    def test_is_lvar_negative_lllvar(self):
        assert not Field('a...991').is_lvar()