API wrapper for https://korrektor.uz

API documentation: [API](https://korrektor.uz/api/)

Foydalanish bo'yicha API yo'riqnoma: https://korrektor.uz/api/

Api token olish uchun [con9799@mail.ru](mailto:con9799@mail.ru) email manzili yoki telegram orqali https://t.me/korrektrobot ning aloqa bo’limiga yozish so’raladi.

## Installation

```bash
pip install korrektor-uz-async
```

## Usage

```python
from korrektor import Client
korr = Client(token='your_token')
# barcha metodlarni async/await yordamida ishlatish mumkin va 
# ular haqida quyidagi metod orqali ma'lumot olish mumkin
info = await korr.info()
print(info)
```

Batafsil ma'lumotlarni https://korrektor.uz/api saytidan olasiz