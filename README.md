
# **Spell Checker Plugin for Python Comments**

## **Описание проекта**
`spell_check_plugin` — это Python-плагин для проверки орфографии в комментариях Python-файлов. Плагин использует библиотеку `pyspellchecker` и позволяет находить ошибки в комментариях Python-кода. Он поддерживает:
- **однострочные комментарии** (`# ...`).

---

## **Возможности**
- Проверка орфографии только в комментариях Python-кода.
- Поддержка английского языка (встроенный словарь).
- Вывод результатов проверки в удобном текстовом окне.
- Возможность выбора любого `.py` файла для анализа.

---

## **Установка**

### **1. Установка зависимостей**
Скачайте репозиторий и установите все зависимости:

```bash
git clone https://github.com/exf1kzz/my-plugin.git
cd spell_check_plugin
pip install pyspellchecker
```

### **2. Запуск плагина**
Для запуска плагина используйте следующую команду:

```bash
python spell_check_plugin.py
```

```bash
python3 spell_check_plugin.py
```

---

## **Использование**

### **1. В качестве плагина в IDLE**
После запуска плагина откроется окно с пунктом меню **"Spell Checker" → "Check Spelling in Comments"**. Выберите Python-файл, и плагин проверит орфографию в его комментариях.

---

## **Пример работы**

### **Исходный файл `example.py`:**
```python
# This is a correct comment.
# This commntt has an error.
# Another line with mistak.
def some_function():
    pass
```

### **Результат работы плагина:**
```
Spelling Errors Found:

Line 2: 'commntt' is misspelled.
Line 3: 'mistak' is misspelled.
```

---

## **Требования**

- **Python 3.7+**
- **pyspellchecker**: библиотека для проверки орфографии.

---

## **Автор**

- **Имя**: *Малов Григорий Дмитриевич*
- **Группа**: *M3105*

---
