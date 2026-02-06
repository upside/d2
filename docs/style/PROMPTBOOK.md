# Promptbook — графика и UI в одном стиле (v0.1)

> Используй как “шаблон промпта”. Всегда начинай с **STYLE ANCHOR** и **NEGATIVE**.

## 0) STYLE ANCHOR (вставлять всегда)

dark fantasy, grounded realism, warm golden candlelight, worn bronze and leather, dark stone, subtle dust/smoke, carved runic motifs, premium game UI kit look, cinematic lighting, high detail, sharp readable shapes, consistent materials and palette

## 0.1) NEGATIVE (вставлять всегда)

no modern SaaS UI, no flat design, no neon glow, no sci-fi HUD, no pastel, no anime, no comic outlines, no low-res, no text, no logos, no watermark

---

## 1) UI: рамка/панель (9-slice)

**Шаблон:**
Generate a {W}x{H} UI panel frame, 9-slice friendly.
Materials: dark stone base with worn bronze corner plates, subtle scratches, soft inner shadow.
Keep center area clean and darker for readability.
Transparent background outside the frame. No text. {STYLE ANCHOR}. {NEGATIVE}.

**Пример:**
Generate a 512x512 UI panel frame, 9-slice friendly… (и т.д.)

---

## 2) UI: кнопки (набор состояний)

Generate a set of 6 button assets (SM/MD/LG × default/hover/pressed), consistent style.
Worn bronze + leather inlay, subtle bevel, readable silhouette.
No text. Transparent background. {STYLE ANCHOR}. {NEGATIVE}.

---

## 3) Инвентарь слот

Generate 64x64 inventory slot assets: empty, hover, selected, locked.
Stone + bronze frame, deep inner cavity, subtle glow on hover (warm, not neon).
Transparent background. {STYLE ANCHOR}. {NEGATIVE}.

---

## 4) Сокеты

Generate socket UI: 24x24 empty socket, 24x24 socket with soft highlight, 24x24 locked socket.
Deep inset, bronze rim, readable at small size.
Transparent background. {STYLE ANCHOR}. {NEGATIVE}.

---

## 5) Руны/камни (иконки)

Generate rune stone icons, consistent set, each icon centered, 64x64, same lighting and material.
Carved symbols, worn edges, subtle glow in engraved lines (very subtle).
Transparent background. {STYLE ANCHOR}. {NEGATIVE}.

---

## 6) Предметы (иконки экипировки)

Generate a fantasy item icon, 512x512, centered, clean silhouette, consistent warm lighting.
Materials: polished steel + worn bronze details, realistic texture.
Transparent background. {STYLE ANCHOR}. {NEGATIVE}.

---

## 7) Мокап страницы (для верстки)

Generate a landing page mockup background in the same style: dark stone panels, bronze ornaments, space for logo, login form area, and two buttons area.
No text. Keep areas clean and rectangular for HTML overlay.
1920x1080. {STYLE ANCHOR}. {NEGATIVE}.

---

## 8) “Стиль держится” — правило серии

Для серии ассетов (руны 30+, зелья 20+, кнопки 10+):
- всегда один STYLE ANCHOR
- фиксированные размеры и сетка
- одинаковый “белый баланс” (тёплый)
- одинаковая интенсивность текстуры (лучше чуть меньше)
