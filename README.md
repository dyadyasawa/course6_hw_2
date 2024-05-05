Django-проект интернет-магазина.

Создано приложение catalog. Базовый шаблон вынесен в templates/catalog_app/base.html.
В базовый шаблон внедрен подшаблон, он находится в templates/catalog_app/include/inc_base.html.
На странице home реализовано наполнение карточек товаров перебором таблицы базы данных db_course_6.
База данных предварительно создана посредством PostgreSQL.

В management/commands/fill_db реализована кастомная команда для очистки и заполнения по новой базы данных
db_course_6 с обнулением инкремента. Данные для заполнения берутся из json-файлов в папке fixture.
Образцы карточек, кнопок и т.п. взяты в Bootstrap 5.
Изображения, размещенные на страницах товаров находятся в media/product.
Текст описания товара в карточках ограничен 100 символами.
Для выводимого изображения на странице реализовали шаблонный фильтр, который преобразует переданный путь
в полный путь для доступа к медиафайлу.

В users/management/commands/create_su создана кастомная команда для создания суперпользователя.
Реализована аутентификация, также создана группа moderators с кастомными правами
Присутствует кеширование, согласно поставленной задаче.
Личные данные вынесены в переменные окружения.