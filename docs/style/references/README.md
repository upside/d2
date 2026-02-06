# Reference Images Pack

Эта директория — «якоря» стиля для агента: UI, предметы, персонажи, окружение.
Задача: чтобы агент не "угадывал", а сверялся с референсами по ID.

## Куда класть картинки
- UI:        docs/style/references/ui/
- Items:     docs/style/references/items/
- Characters:docs/style/references/characters/
- Envs:      docs/style/references/environments/
- Moodboard: docs/style/references/moodboard/
- Typography:docs/style/references/typography/

Дополнительно полезно:

- **Сеты экипировки**: `docs/style/references/items/equipment_sets/` — референсы целостных наборов (единый металл/кожа/орнамент на всём наборе).

## Как называть файлы
Формат: <GROUP>_<NNN>_<short_slug>.png

Группы:
- UI_###         — интерфейс (панели, рамки, кнопки, слоты, тултипы)
- ITEM_###       — предметы (оружие, броня, руны, камни, зелья)
- CHAR_###       — персонажи (силуэты, позы, одежда)
- ENV_###        — окружение (сцены, локации, освещение)
- MOOD_###       — общий вайб/палитры/материалы
- TYPE_###       — типографика/цифры/таблички

Примеры:
- UI_001_tooltip_depth.png
- UI_002_inventory_slot.png
- ITEM_010_armor_bronze_trim.png
- MOOD_003_warm_candlelight.png

## Как ссылаться в задачах
Пиши: "Ориентируйся на UI_001 и UI_002 (обязательно)."
И добавляй «что именно копировать» и «чего избегать» (см. references.md).

## Важно
Референсы могут включать скриншоты из игр — это ОК для внутреннего мудборда,
но не стоит публиковать их как ассеты проекта. Для релиза используйте оригинальные ассеты.
