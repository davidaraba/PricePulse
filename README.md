# 🛍️ PricePulse

An automated sale-tracking tool that monitors fashion retail websites for keyword-specific product discounts and sends real-time SMS alerts using the Twilio API.

---

## 🚀 Features

- 🔍 **Keyword Filtering**: Only tracks products matching your preferred keywords.  
- 💰 **Price Thresholds**: Optional max-price filtering to stay within your budget.  
- 🔁 **Repeat Alert Prevention** *(coming soon)*: Avoids notifying you about the same unchanged discounts.  
- 🧩 **Modular Store Scrapers**: Easily extendable support for new stores via plug-in style scrapers.  
- 📦 **SMS Integration**: Uses Twilio API to send sale alerts directly to your phone.  
- 🧠 **Structured JSON Config**: Define multiple stores, URLs, and keywords in one place.  
- 🕒 **Scheduled Runtime**: Designed for repeated, scheduled executions (e.g., via cron or task scheduler).  

---

## 📁 Project Structure

```
SaleAlertSystem/
├── core/
│   ├── alert_sender.py       # SMS logic using Twilio
│   ├── product.py            # Product data model
│   ├── scheduler.py          # (Optional) Scheduler logic
│   └── store_loader.py       # JSON loader for store configs
├── scrapers/
│   ├── nike.py               # Nike-specific scraper
│   ├── cottonon.py           # Cotton On-specific scraper
│   ├── subtype.py            # Subtype scraper (uses Selenium)
│   └── asos.py               # (Optional) Asos scraper
├── store_list.json           # Config file with all stores & keywords
├── main.py                   # Program entry point
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/sale-alert-system.git
cd sale-alert-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Twilio

Create a `.env` file or export environment variables:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
USER_PHONE_NUMBER=your_verified_number
```

### 4. Edit Your Store List

Modify `store_list.json` to include the stores and keywords you want to track:

```json
[
  {
    "name": "Nike",
    "url": "https://www.nike.com/au/w/sale",
    "keywords": ["dunk", "air force", "vomero"]
  },
  {
    "name": "Cotton On",
    "url": "https://cottonon.com/AU/co/co-sale/sale-mens/",
    "keywords": ["baggy", "cargo"]
  }
]
```

### 5. Run the Script

```bash
python main.py
```

---

## 📌 Future Enhancements

- ✅ Repeated sale tracking to suppress unchanged alerts  
- 🖥️ Web interface for user configuration  
- 📧 Email support as alternative to SMS  
- ⏰ Scheduled automation (via cron jobs)  
- 🧩 More store scrapers (e.g., Subtype, Hype DC, etc.)  

---

## 📷 Screenshots



---

## 📄 License

MIT License — feel free to use, modify, and share.
