
```markdown
# 💖 Thanks

# 🔎 Lost & Found Matching System

A simple web app built with **Flask** to help people report **lost items** and **found items**, then match them automatically.

This project can help people recover or report important things like:

- 🪪 National IDs  
- 💳 Bank cards  
- 📱 Phones  
- 👛 Wallets  
- 📄 Documents  
- 🎒 Bags  
- 💻 Electronics  
- 🐾 Animals & Pets  
- 👶 Children  
- 👵 Elders  

It can also help people avoid buying stolen or already-reported items.

---

## ✨ Features

- ✅ View all lost items  
- ✅ View all found items  
- ✅ Register **I Lost** item  
- ✅ Register **I Found** item  
- ✅ Pre-register your item before it gets lost  
- ✅ Upload item photo  
- ✅ Country → District dropdown  
- ✅ Auto matching system  
- ✅ Show matched items immediately  
- ✅ No login / No account needed  
- ✅ No database needed  
- ✅ Saves data in folders as JSON files  

---

## ⚙️ How It Works

### 1. Visitor opens website
The visitor can see:
- Lost items list  
- Found items list  
- Recovered items marked with ⭐ or different color  

---

### 2. User clicks button
The user can choose:
- **I Lost**  
- **I Found**  
- **Pre-register Item**  

---

### 3. Fill form
The user fills details like:
- Country  
- District  
- Type  
- Brand / Model / Name  
- Color  
- Status  
- Quantity / Number  
- Phone number  
- Photo  

**Example:**
```
Type: Document
Name: Bank Card
Color: Orange
Status: Active
Number: 2
```

---

### 4. System matches item
The server checks if there is a similar item in:

- `lost/`  
- `found/`  
- `preregistered/`  

If a match is found, it shows the result and phone number.  
Further confirmation must be done, like receipt, serial number, etc.

---

## 📂 Project Structure

```
lost_found/
│
├── app.py
├── countries.json
│
├── data/
│   ├── lost/
│   ├── found/
│   ├── preregistered/
│   └── matched/
│
├── static/
│   ├── uploads/
│   ├── style.css
│   └── script.js
│
└── templates/
    ├── index.html
    ├── form.html
    ├── matches.html
    └── item.html
```

---

## 🚀 Installation

Clone project:
```bash
git clone https://github.com/zygtek-coders/Heart..git
cd Heart.
```

Install Flask:
```bash
pip install flask
```

Run server:
```bash
python app.py
```

Open browser:
```
http://127.0.0.1:5000
```

---

## 🛠️ Technologies Used

- Python  
- Flask  
- HTML  
- CSS  
- JavaScript  
- JSON storage  

---

## 💡 Why This Project?

Everywhere in the world, many people lose:
- 🐕 Animals & Pets  
- 👶 Children  
- 🪪 IDs & Cards  
- 📱 Phones  
- 📄 Important documents  
- 🎒 Bags  
- 🏍️ Motorcycles  

And many people find them but don’t know the owner.  
This app reduces stress and saves time.

---

## 🔮 Future Improvements

- 📩 SMS notification  
- 💬 WhatsApp notification  
- 🔎 OCR for IDs and cards  
- 🤖 AI image matching  
- 🚫 Stolen item blacklist  
- 🖥️ Admin dashboard  

---

## 👥 Author

- Julliane  
- Shams  
- Aime Shabani  

Thanks to our dear mentors:  
- 🌸 Carolyne  
- 🌼 Alice  
- 🌹 Marion Schleifer  

