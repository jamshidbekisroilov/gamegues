# 🎯 Number Guessing Game — GUI versiyasi

Bu kichik o‘yin foydalanuvchidan 1 dan 100 gacha bo‘lgan sonni taxmin qilishni so‘raydi. Har bir taxmin uchun kompyuter "Juda katta", "Juda kichik" yoki "To‘g‘ri topdingiz!" degan javobni beradi. O‘yin **Tkinter GUI** interfeysi orqali alohida oynada ishlaydi.

## 🖼️ Interfeys

- Chiroyli grafik oynada raqam kiritish maydoni
- Taxmin tugmasi
- Natijani ko‘rsatuvchi matn
- Pastki qismda xizmatlar banneri va muallif ma’lumotlari

## 🛠️ Texnologiyalar

- Python 3.13+
- Tkinter (standart GUI kutubxonasi)
- PyInstaller (kompilyatsiya uchun)

## 📦 .exe fayl yaratish

Agar siz o‘yinni `.exe` faylga aylantirmoqchi bo‘lsangiz:

```bash
pyinstaller --onefile --windowed gameguess.py