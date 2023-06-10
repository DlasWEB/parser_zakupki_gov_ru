## parser_zakupki_gov_ru

<p align="center">
      <img src="https://github.com/DlasWEB/parser_zakupki_gov_ru/master/img_for_readme/logo.jpg" alt="Лого проекта">
</p>

## Описание

Данный репозиторий содержит скрипт на python для парсинга сайта https://zakupki.gov.ru, с целью автоматизации извлечения основной информации о закупке и скачивания сопутствующей документации к закупке.  

## Установка

1. Для использования клонируете данный репозиторий, открывайте проект в Pycharm или другом редакторе кода. 
2. Устанавливайте необходимые зависимости (`Requests`, `BeautifulSoup`, `Selenium`) с помощью pip. 
3. Качайте `chromedriver` (скрипт настроен именно под него).
4. В файле `main.py` обновите путь, который указан в переменной `absolute_path_to_folder_with_script` на соответствующий вашей системе.
5. Проверьте все ли файлы и папки указаны в списке `files_for_remove`, чтобы не удалилось ничего лишнего при выполнении скрипта.

## Использование

<p align="center">
      <img src="https://github.com/DlasWEB/parser_zakupki_gov_ru/master/img_for_readme/01.jpg" alt="Лого проекта">
</p>

1. Занесите ссылки на аукционы в файл `urls.txt` в формате `https://zakupki.gov.ru/epz/order/notice/zk20/view/common-info.html?regNumber=0744200000223004677`.
2. Запустите скрипт.
3. Если все настроено правильно, то по итогу в папке `data` будут папки (в качестве имен номер закупки) с базовой информацией о закупке и документами, приложенными к ней.

## P.S.

Скрипт достаточно простой и создан в учебных целях для освоения языка python и его библиотек. В коммерческих целях не использовался.
   
## Разработчики
   
- [Денис Ласкин](https://github.com/DlasWEB)
   
## Лицензия
   
Проект **[parser_zakupki_gov_ru](https://github.com/DlasWEB/parser_zakupki_gov_ru)** распространяется под лицензией GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.