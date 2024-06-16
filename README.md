# Автотесты для веб-сайта онлайн-кинотеатра Flex

> https://flex-kino.com

## FLEX WEB
<img title="FLEX WEB" src="resources/pictures/flex_general_page.jpg"/>

## FLEX Android App
<img title="FLEX Android App" src="resources/pictures/android_general_page.jpg" height="533" width="240"/>

## Особенности проекта
- Автотесты на WEB UI, API и Android App
  - Автотесты WEB UI запускаются через Selenoid
  - Автотесты Android App через BrowserStack или с помощью локального эмулятора
- Сборка проекта в Jenkins
- Отчеты Allure Report
- Интеграция с Allure TestOps
- Оповещения о тестовых прогонах в Telegram
- Отчеты с видео, скриншотами, логами, исходной моделью разметки страницы
- Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira

## Список реализованных проверок:
- WEB UI
  - Авторизация пользователя
  - Переход по разделам в Хедер:
    - Сериалы
    - Фильмы
    - Подборки
    - Тарифы
  - Поиск контента
  - Переход по ссылкам в футере:
    - Документы правообладателей
    - Страница RuStore для Anroid-приложения
- API
  - Авторизация пользователя
  - Раздел Избранное
    - Добавление в избранное
    - Получение списка избранных фильмов
    - Удаление из избранного
  - Получение информации о приложениях
- Android App
  - Авторизация в приложении
  - Проверка Welcome screen
  - Открытие в браузере страницы Документы правообладателей

## Используемый стэк
<img title="Python" src="resources/pictures/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="resources/pictures/icons/pytest-original.svg" height="40" width="40"/> <img title="GitHub" src="resources/pictures/icons/github-original.svg" height="40" width="40"/> <img title="Selenium" src="resources/pictures/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="resources/pictures/icons/selene.png" height="40" width="40"/> <img title="Appium" src="resources/pictures/icons/appium.svg" height="40" width="40"/> <img title="Allure Report" src="resources/pictures/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="resourcesresources/pictures/icons/AllureTestOps.png" height="40" width="40"/> <img title="Jenkins" src="resources/pictures/icons/jenkins-original.svg" height="40" width="40"/> <img title="BrowserStack" src="resources/pictures/icons/browserstack.svg" height="40" width="40"/> <img title="Jira" src="resources/pictures/icons/jira-original.svg" height="40" width="40"/> <img title="PyCharm" src="resources/pictures/icons/pycharm-original.svg" height="40" width="40"/> <img title="Telegram" src="resources/pictures/icons/tg.png" height="40" width="40"/>

## Запуск тестов из терминала
### Для запуска всех автотестов выполнить в cli:
> python -m venv .venv  
> source .venv/bin/activate   
> pip install -r requirements.txt   
> pytest -s -v

### Получение отчета allure:
> allure serve allure-results

## Проект в Jenkins
> [Jenkins](https://jenkins.autotests.cloud/job/amosyakin_flex_kino_project_tests//)

### Запуск автотестов в Jenkins:
1. Открыть [проект](https://jenkins.autotests.cloud/job/amosyakin_flex_kino_project_tests/)

<img title="Jenkins" src="resources/pictures/jenkins_general_page.jpg"/>

2. Нажать кнопку "Build Now"

## Allure отчет
### [Общие результаты](https://jenkins.autotests.cloud/job/amosyakin_flex_kino_project_tests/25/allure/)
<img title="Jenkins" src="resources/pictures/allure_results.jpg"/>

### [Результат прохождения теста](https://jenkins.autotests.cloud/job/amosyakin_flex_kino_project_tests/25/allure/#behaviors)
<img title="Jenkins" src="resources/pictures/allure_results_test_case.jpg"/>

## Интеграция с Allure TestOps
> [Allure TestOps](https://allure.autotests.cloud/project/4283/dashboards)


### [Дашбоард](https://allure.autotests.cloud/project/4283/dashboards)
<img title="Allure TestOps" src="resources/pictures/allure_testops_dashboard.jpg"/>

### [История запусков тестовых наборов](https://allure.autotests.cloud/project/4283/launches)
<img title="Allure TestOps" src="resources/pictures/alluretestops_history_launch.jpg"/>

### [Отображение тест кейса](https://allure.autotests.cloud/launch/39864/tree/645711?treeId=8398)
<img title="Allure TestOps" src="resources/pictures/alluretestops_test_case.jpg"/>

## Интеграция с Jira
### [Ссылка на проект](https://jira.autotests.cloud/browse/HOMEWORK-1259)
<img title="Jira" src="resources/pictures/jira.jpg"/>

## Оповещения в Telegram
<img title="Telegram" src="resources/pictures/telegram_notifications.jpg"/>

## Пример прохождения автотестов WEB UI
<img title="Selenoid" src="resources/pictures/attach_video_test_cases.gif"/>

## Пример прохождения автотестов Android App
<img title="Selenoid" src="resources/pictures/attach_android_video_test_case.gif" height="533" width="240"/>
