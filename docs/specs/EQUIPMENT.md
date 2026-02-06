# Equipment & Loadout (v0)

This document defines **character equipment slots** ("paper doll"), the minimum viable rules for equipping items, and what an **item set** must include when we ask an agent to **generate a starter gear set**.

## Equipment slots

The character has **10** equipment slots:

1. **Head** — helmet / hood / hat
2. **Body** — chest armor / robe / cuirass
3. **Belt** — belt / sash
4. **Boots** — boots / greaves
5. **Gloves** — gloves / gauntlets
6. **Left hand** — shield / off-hand item *(or a 1H weapon if dual-wield is enabled for a class; default: not enabled)*
7. **Right hand** — weapon
8. **Amulet** — amulet / talisman
9. **Ring (left)**
10. **Ring (right)**

> Naming note: **Left/Right** is from the character perspective (not the viewer).


## Inventory grid footprint (W×H)

Besides the equipment *slot* (Head/Body/Weapon…), each item also has an **inventory grid footprint** `W×H`
(columns × rows). The authoritative mapping and composition rules live in:
`docs/style/ASSET_SPECS.md` → **Размер предметов в сетке инвентаря (W×H)**.

Quick reference:
- Ring / Amulet: **1×1**
- Belt: **1×2**
- Helm / Gloves / Boots: **2×2**
- Body armor: **2×3**
- Shields: **2×2 … 2×4**
- Weapons: **1×2 … 2×6**


## Equip rules (MVP)

### Hands

- **1H weapon** can be equipped in **Right hand**.
- **Shield / off-hand** can be equipped in **Left hand**.
- **2H weapon** occupies **both hands** (Left hand becomes locked/empty).
- Default (MVP): **no dual-wield** (no weapon-in-left) unless a class explicitly enables it.

### Jewelry

- The character can wear **1 amulet**.
- The character can wear **2 rings**, one per slot.
- (Optional, later) Unique constraint: same unique ring cannot be worn twice.

### Armor

- Exactly one item per armor slot: Head/Body/Belt/Boots/Gloves.

## Item taxonomy (for assets & UI)

These are the **categories** we expect in UI and in generated icon packs:

- **Headgear** (Head)
- **Chest armor** (Body)
- **Belt** (Belt)
- **Boots** (Boots)
- **Gloves** (Gloves)
- **Weapon (1H)** (Right hand)
- **Weapon (2H)** (Both hands)
- **Shield / Off-hand** (Left hand)
- **Amulet** (Amulet)
- **Ring** (Ring left/right)

## Starter gear set definition

When the product asks for a **starter-level gear set** (level 1–5 vibe), the deliverable **must include**:

- **Head**: 1 item
- **Body**: 1 item
- **Belt**: 1 item
- **Boots**: 1 item
- **Gloves**: 1 item
- **Right hand**: 1 item (**1H weapon** recommended for starter sets)
- **Left hand**: 1 item (**shield/off-hand** recommended for starter sets)
- **Amulet**: 1 item
- **Ring left**: 1 item
- **Ring right**: 1 item

Total: **10 items** per set.

### Suggested starter themes

Pick one theme per set to keep cohesion:

- **Wanderer leather** (brown leather, simple iron fittings)
- **Militia iron** (iron/steel with cloth padding)
- **Acolyte linen** (cloth/linen with small bronze details)

## Asset requirements (summary)

For icon generation constraints (transparent background, framing, etc.), see:

- `docs/style/ASSET_SPECS.md`
- `docs/style/PROMPTBOOK.md`
