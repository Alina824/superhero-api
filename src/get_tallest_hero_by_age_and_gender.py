import requests

# адрес задаём переменной для удобства изменения
API_URL = "https://akabab.github.io/superhero-api/api/all.json"


# преобразуем формат ["6'8", "203 cm"] в число (203)
def parse_height(height_list):
    if not height_list or len(height_list) < 2:
        return 0
    # проверяем, что рост присутствует и не равен нулю
    cm = height_list[1]
    if not cm or cm == "0 cm":
        return 0
    # отсекаем единицы измерения
    try:
        return int(cm.replace(" cm", ""))
    except ValueError:
        return 0


# проверка, что поле работа не пустое
def has_a_job_check(occupation):
    return occupation and occupation != "-"


def get_tallest_hero_by_age_and_gender(gender: str, has_a_job: bool):
    response = requests.get(API_URL)
    response.raise_for_status()  # выбрасываем исключение при ошибке

    heroes = response.json()
    matches = []
    for hero in heroes:
        # получаем пол и работу
        hero_gender = hero.get("appearance", {}).get("gender", "")
        occupation = hero.get("work", {}).get("occupation", "")
        # сверяем полученный пол с требуемым
        if hero_gender.lower() != gender.lower():
            continue
        """В случаях, если работы нет и она требуется, либо есть, а быть не должно - пропускаем"""""
        if (has_a_job or has_a_job_check(occupation)) and not (has_a_job and has_a_job_check(occupation)):
            continue
        matches.append(hero)

    # проверка, что список подошедщих под фильтр не пуст
    if not matches:
        return None

    # ищем максимум по росту
    tallest = matches[0]
    for hero in matches:
        if parse_height(hero["appearance"]["height"]) > parse_height(tallest["appearance"]["height"]):
            tallest = hero

    return tallest