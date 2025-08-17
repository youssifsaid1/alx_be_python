def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # القائمة تبدأ فاضية

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))  # هنا الرقم بيتحول لـ int
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # إضافة عنصر للقائمة
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"✅ '{item}' has been added to the shopping list.")

        elif choice == 2:
            # إزالة عنصر من القائمة
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ '{item}' has been removed from the shopping list.")
            else:
                print(f"⚠️ '{item}' not found in the shopping list.")

        elif choice == 3:
            # عرض العناصر الموجودة في القائمة
            if shopping_list:
                print("\n🛒 Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("📭 The shopping list is empty.")

        elif choice == 4:
            # الخروج من البرنامج
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
