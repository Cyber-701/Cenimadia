import re

def fix_booleans_in_file(filename):
    """
    Fayldagi 'true' va 'false' so'zlarini avtomatik ravishda
    Python formatiga mos (True / False) qilib tuzatadi.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Katta-kichik harflarga e'tibor bermasdan almashtirish
        fixed_content = re.sub(r'\btrue\b', 'True', content, flags=re.IGNORECASE)
        fixed_content = re.sub(r'\bfalse\b', 'False', fixed_content, flags=re.IGNORECASE)

        # Natijani qayta yozish
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(fixed_content)

        print(f"✅ '{filename}' faylidagi barcha true/false qiymatlar to'g'rilandi.")
    except FileNotFoundError:
        print(f"❌ Fayl topilmadi: {filename}")
    except Exception as e:
        print(f"⚠️ Xatolik yuz berdi: {e}")


# === Foydalanish misoli ===
fix_booleans_in_file('add_sample_movies.py')
