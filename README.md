# 📚 BookBindingOMS

**BookBindingOMS** is a **Book Binding Order Management System** built using **Python, CustomTkinter, and ttkbootstrap**. This application helps in managing bookbinding orders efficiently by collecting order details, tracking progress, and calculating costs automatically.

---

## ✨ Features

✅ **Order Management**: Add, modify, and track bookbinding orders easily.  
✅ **Automated Price Calculation**: Computes total cost based on inputs (number of books, pages, OHP sheets, etc.).  
✅ **Order Status Tracking**: Updates order progress (Pending → In Progress → Completed).  
✅ **Search & Modify Orders**: Easily find and update existing orders.  
✅ **User-Friendly Interface**: Modern UI using **CustomTkinter** and **ttkbootstrap**.  
✅ **CSV-Based Storage**: Orders are saved in `orders.csv` (future upgrade to Excel/SQLite planned).  
✅ **Common Dealers Section**: Separate statistics for frequent customers.  
✅ **Reports & Analytics**: View order history, revenue trends, and completed/pending order stats.  

---

## 📂 Project Structure

```
BookBindingOMS/
├── assets/                    # Icons & UI assets
├── data/
│   ├── orders.csv             # Stores order details
├── modules/
│   ├── __init__.py
│   ├── order_input.py         # Handles new order entry
│   ├── order_manager.py       # Manages and updates orders
│   ├── order_saver.py         # Saves orders to CSV
├── utils/
│   ├── design.py              # UI styling functions
│   ├── display_colors.py      # Predefined color schemes
├── windows/
│   ├── __init__.py
│   ├── confirmation_window.py # Popups for order actions
│   ├── new_order_ui.py        # UI for adding a new order
├── config.py                  # Configuration settings
├── gui.py                     # **Main GUI file (Run this to start the app)**
├── main.py                    # Alternative entry point
├── README.md                  # Project documentation
├── requirements.txt            # Dependencies
├── .gitignore                  # Excludes unnecessary files
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/rudrakshMahurpwar/BookBindingOMS.git
cd BookBindingOMS
```

### 2️⃣ Create & Activate Virtual Environment
#### On Windows:
```sh
python -m venv venv
venv\Scripts\activate
```
#### On Mac/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
python gui.py
```

---

## 🎨 How to Use GUI

1️⃣ **Open the App**: Run `gui.py` to start the program.  
2️⃣ **New Order**: Click "New Order", enter details, and save.  
3️⃣ **Track Orders**: View existing orders, update status, or search for specific orders.  
4️⃣ **Modify Orders**: Edit details of any order if needed.  
5️⃣ **Check Reports**: View order statistics and trends.  

---

## 📸 Screenshots (Coming Soon)
_Add UI screenshots here for better understanding._

---

## 🛠️ Tech Stack
- **Python** (Main Language)
- **CustomTkinter** (Modern UI Framework)
- **ttkbootstrap** (Enhanced UI Components)
- **Pandas** (Data Handling)
- **CSV Storage** (Orders saved in CSV file, future upgrade planned)

---

## 🔥 Future Improvements
✅ **Excel/SQLite Storage** instead of CSV.  
✅ **Dealer Statistics** (Frequent customers section).  
✅ **Order Filtering & Sorting**.  
✅ **PDF Invoice Generation**.  
✅ **Multi-User Access & Login System**.  

---

## 🤝 Contributing
Feel free to fork this repo, submit PRs, or suggest improvements! 🚀

---

## 📜 License
MIT License © 2025 Rudraksh Mahurpwar

---

## ⭐ Show Some Love
If you like this project, give it a **star ⭐** on GitHub! 🙌
