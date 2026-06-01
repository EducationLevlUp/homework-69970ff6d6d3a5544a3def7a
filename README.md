# AI Fluency Plan — Домашнее задание

## Описание

Решение домашнего задания **«ai-fluency»**: пройден курс *AI Fluency: Framework & Foundations* от Anthropic на платформе Skilljar и разработан персональный план AI-грамотности.

Курс основан на **4D-фреймворке** Anthropic:

| D | Название | Суть |
|---|----------|------|
| 1 | **Delegation** | Умение делегировать задачи ИИ и знать, когда доверять результату |
| 2 | **Description** | Умение формулировать точные промпты с контекстом и ограничениями |
| 3 | **Discernment** | Критическая оценка выводов ИИ на точность, предвзятость и полноту |
| 4 | **Diligence** | Безопасное, этичное и устойчивое использование ИИ |

## Структура проекта

```
├── README.md                       # Этот файл
├── requirements.txt                # Зависимости (python-docx)
├── Personal_AI_Fluency_Plan_RU.md  # План AI-грамотности (Markdown)
├── Personal_AI_Fluency_Plan_RU.docx # План AI-грамотности (DOCX)
├── AI_FLUENCY_PLAN.md              # Готовый план AI-грамотности (финальный артефакт)
├── generate_plan.py                # Генератор плана (Python-скрипт)
├── generate_docx.py                # Генератор DOCX-версии плана
└── test_generate_plan.py           # Unit-тесты для генератора
```

## Как запустить

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Проверить синтаксис

```bash
python -m compileall .
```

### 3. Запустить генератор плана

```bash
python generate_plan.py
```

По умолчанию создаёт файл `AI_FLUENCY_PLAN.md`.

### 4. Запустить генератор DOCX

```bash
python generate_docx.py
```

Создаёт файл `Personal_AI_Fluency_Plan_RU.docx`.

### 5. Запустить с кастомным автором

```bash
python generate_plan.py --author "Иван Иванов"
```

### 6. Просмотр без записи в файл

```bash
python generate_plan.py --dry-run
```

### 7. Запустить тесты

```bash
python -m pytest test_generate_plan.py -v
```

## Зависимости

- **Python 3.11+** (стандартная библиотека)
- **python-docx** — для генерации DOCX-версии плана (объявлена в `requirements.txt`)
- **pytest** (для тестов, опционально)

Никаких внешних API-ключей, токенов или сетевых запросов не требуется.

## Внешние сервисы

Курс проходил на платформе Skilljar:

- **URL:** https://anthropic.skilljar.com/ai-fluency-framework-foundations
- **Автор курса:** Anthropic (в сотрудничестве с Prof. Joseph Feller и Prof. Rick Dakan)

Для прохождения курса необходим аккаунт на Skilljar. Интеграционная проверка с Skilljar не требуется — это образовательное задание.

## Критерии выполнения

- [x] Пройти курс AI Fluency (изучены материалы 4D-фреймворка)
- [x] Выполнить финальное задание: Build a personal AI fluency plan
- [x] Предоставить разработанный план (`Personal_AI_Fluency_Plan_RU.md` и `Personal_AI_Fluency_Plan_RU.docx`)

## Формат плана

План представлен в форматах **Markdown** и **DOCX** и включает:

1. Личные цели и мотивацию
2. Оценку текущего уровня по каждому измерению 4D (Delegation, Description, Discernment, Diligence)
3. Пошаговый план на 8 недель (4 фазы)
4. Инструменты и ресурсы
5. Метрики прогресса (количественные и качественные)
6. Безопасность и академическую честность
7. Риски и меры смягчения
8. Рефлексию
