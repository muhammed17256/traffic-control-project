import os

# اسم الملف الذي ستُحفظ فيه البيانات
DATA_FILE = "database.txt"

def save_data(admin_name, cipher_text):
    """دالة لحفظ اسم المسؤول والشفرة في ملف نصي"""
    try:
        with open(DATA_FILE, "a", encoding="utf-8") as file:
            file.write(f"المسؤول: {admin_name} | الشفرة: {cipher_text}\n")
        print("\n[+] تم حفظ البيانات بنجاح!")
    except Exception as e:
        print(f"\n[-] حدث خطأ أثناء حفظ البيانات: {e}")

def main():
    print("=" * 40)
    print("      برنامج إدارة وحفظ الشفرات      ")
    print("=" * 40)
    
    # إدخال البيانات من المستخدم
    admin_name = input("ادخل اسم المسؤول: ").strip()
    cipher_text = input("ادخل الشفرة (السيفرة): ").strip()
    
    # التأكد من أن الحقول ليست فارغة
    if admin_name and cipher_text:
        save_data(admin_name, cipher_text)
    else:
        print("\n[-] خطأ: لا يمكن ترك اسم المسؤول أو الشفرة فارغاً!")

if __name__ == "__main__":
    main()