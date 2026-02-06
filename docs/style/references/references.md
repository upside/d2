# References Index

Этот файл — каталог референсов. Добавляй сюда новые картинки, чтобы агент понимал:
- **что именно** взять из примера (рамка/материал/сетка/отступы),
- **чего избегать** (копирование уникальных орнаментов/логотипов/шрифтов).

## Как добавлять
1) Положи картинку в нужную папку (ui/items/characters/environments/moodboard/typography)
2) Дай имя по схеме: GROUP_NNN_slug.png
3) Добавь запись ниже (и в references.yaml, если используешь).

## Шаблон записи

### UI_XXX — Короткое название
- Path: `docs/style/references/ui/UI_XXX_....png`
- Tags: `tooltip`, `frame`, `inventory`, `stone`, `bronze`
- Copy:
  - ...
- Avoid:
  - ...
- Notes:
  - ...

---

## Примеры (замени своими)

### UI_001 — Tooltip depth + typography rhythm
- Path: `docs/style/references/ui/UI_001_tooltip_depth.png`
- Tags: `tooltip`, `frame`, `double-border`, `warm-light`
- Copy:
  - двойная рамка + внутренний inset
  - плотный ритм строк, читаемая иерархия
  - тёплый off-white текст, без кислотных цветов
- Avoid:
  - неоновые тени/сильный glow
  - ярко-жёлтый текст "везде"
- Notes:
  - ширина тултипа 320–380px

### UI_002 — Inventory slot (inset)
- Path: `docs/style/references/ui/UI_002_inventory_slot.png`
- Tags: `slot`, `inset`, `stone`, `metal-corners`
- Copy:
  - "вдавленный" слот через inset-shadow
  - одинаковый размер и шаг сетки
- Avoid:
  - разные радиусы/тени в соседних слотах

### ITEM_010 — Armor material language
- Path: `docs/style/references/items/ITEM_010_armor_bronze_trim.png`
- Tags: `armor`, `bronze`, `worn`, `realistic`
- Copy:
  - потёртая бронза, лёгкие царапины, аккуратные блики
- Avoid:
  - пластик/мультяшная заливка
