# Test Custom Integration for Casa De Ratton

# 🌧️ Thailand Weather Alerts (TMD)

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Custom%20Integration-blue)
![Status](https://img.shields.io/badge/status-experimental-orange)
![License](https://img.shields.io/badge/license-MIT-green)

An **unofficial Home Assistant custom integration** that parses the **Thailand Meteorological Department (TMD)** RSS warning feed and exposes real-time weather alerts directly inside Home Assistant.

Built for users in Thailand who want automated awareness of storms and severe weather without refreshing government websites like it’s 2004.

---

## ✨ Features

- ✅ **Alert Count Sensor**  
  Tracks the number of active weather warnings.

- 📄 **Detailed Alert Attributes**  
  Includes alert title, summary, and publication date.

- ⛈️ **Storm Detection Binary Sensor**  
  Automatically turns ON when storm-related keywords are detected.

- 🌏 **Regional Filtering**
  Monitor alerts for:
  - Northern
  - Northeastern
  - Central
  - Eastern
  - Southern (East Coast)
  - Southern (West Coast)
  - Entire Thailand

---

## 📦 Installation

### Manual Installation

1. Open your **Home Assistant configuration directory**.

2. Create a folder named:

custom_components (if it does not already exist)

3. Copy or clone this repository’s `tmd_alerts` folder into:

custom_components/tmd_alerts

4. Restart Home Assistant.

---

## ⚙️ Configuration

1. Navigate to:

2. Click **➕ Add Integration**

3. Search for:

Thailand Weather Alerts (TMD)


4. Select your desired **Region**
5. Finish setup.

No YAML required. Because suffering is optional.

---

## 🧩 Entities

| Entity | Description | Attributes |
|-------|-------------|------------|
| `sensor.tmd_weather_alerts` | Number of active alerts for the selected region | `alerts` (titles + summaries) |
| `binary_sensor.storm_warning_active` | Turns ON when storm-related alerts are detected | — |

---

## ⚙️ Technical Details

| Item | Value |
|------|------|
| Update Interval | Every **10 minutes** (600 seconds) |
| Data Source | Thailand Meteorological Department RSS Feed |
| Architecture | `DataUpdateCoordinator` + executor jobs |
| Performance | Fully asynchronous |

Designed to keep Home Assistant responsive while still delivering timely warnings.

---

## ⚠️ Disclaimer

This project is **not affiliated with**, maintained by, or endorsed by the **Thailand Meteorological Department (TMD)**.

It is provided **as-is** for informational purposes only.

During severe weather events, always rely on **official government announcements**.

---

## 👨‍💻 Developer

**@simplemice**

---

## ⭐ Support

If this integration helps you:

- ⭐ Star the repository
- 🐛 Report issues
- 💡 Submit improvements

Pull requests are welcome.

---

## 📜 License

MIT License — do whatever you want, just don’t blame the developer if the weather wins.









