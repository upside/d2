---
description: Auto-fix PHP code style via php-cs-fixer
agent: build
---

Run php-cs-fixer in fix mode, then re-run the style check.

```bash
cd server
composer cs:fix
composer cs
```
