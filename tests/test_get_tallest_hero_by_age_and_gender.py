import pytest
from src.get_tallest_hero_by_age_and_gender import get_tallest_hero_by_age_and_gender as get_tallest_hero


def test_male_with_job():
    hero = get_tallest_hero("Male", True)
    # проверяем, что возвращённое значение не пустое и соответствует фильтру: мужчина с работой
    assert hero is not None
    assert hero["appearance"]["gender"] == "Male"
    assert hero["work"]["occupation"] != "-"


def test_register():
    hero = get_tallest_hero("male", False)
    # проверка регистронезависимости
    assert hero is not None
    assert hero["appearance"]["gender"] == "Male"
    assert hero["work"]["occupation"] == "-" or not hero["work"]["occupation"]


def test_female_with_job():
    hero = get_tallest_hero("Female", True)
    # проверяем, что возвращённое значение не пустое и соответствует фильтру: женщина с работой
    assert hero is not None
    assert hero["appearance"]["gender"] == "Female"
    assert hero["work"]["occupation"] != "-"


def test_male_without_job():
    hero = get_tallest_hero("Male", False)
    # проверяем, что возвращённое значение не пустое и соответствует фильтру: мужчина без работы
    assert hero is not None
    assert hero["appearance"]["gender"] == "Male"
    assert hero["work"]["occupation"] == "-" or not hero["work"]["occupation"]


def test_female_without_job():
    hero = get_tallest_hero("Female", False)
    # проверяем, что возвращённое значение не пустое и соответствует фильтру: женщина без работы
    assert hero is not None
    assert hero["appearance"]["gender"] == "Female"
    assert hero["work"]["occupation"] == "-" or not hero["work"]["occupation"]


def test_invalid_gender():
    hero = get_tallest_hero("Invalid_gender", True)
    assert hero is None


def test_returns_height():
    hero = get_tallest_hero("Male", True)
    height = hero["appearance"]["height"][1]
    assert "cm" in height