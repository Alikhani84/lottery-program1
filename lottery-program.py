import random

# تابع ساخت شماره موبایل رندوم با ۰۹ شروع
def generate_random_phone():
    return "09" + "".join(random.choices("0123456789", k=9))

# گرفتن تعداد شرکت‌کننده و برنده از کاربر
total = int(input("تعداد شرکت‌کننده‌ها رو وارد کن: "))
winners_count = int(input("تعداد برنده‌ها رو وارد کن: "))

# بررسی معتبر بودن مقدارها
if winners_count > total:
    print("🚫 تعداد برنده‌ها نمی‌تونه بیشتر از تعداد شرکت‌کننده‌ها باشه!")
else:
    # ساخت شماره‌های تصادفی
    participants = [generate_random_phone() for _ in range(total)]

    # انتخاب برنده‌ها
    winners = random.sample(participants, winners_count)

    # نمایش لیست شماره‌ها
    print("\n📱 لیست شماره‌های شرکت‌کننده:")
    for i, p in enumerate(participants, start=1):
        print(f"{i}. {p}")

    # نمایش برنده‌ها
    print("\n🎉 شماره‌های برنده:")
    for w in winners:
        print(w)
        