# ==========================================================
# WEATHER DASHBOARD PRO
# Developed By: Puspesh Tripathi
# Features:
# ✔ Modern UI
# ✔ Resizable Window
# ✔ Temperature
# ✔ Feels Like
# ✔ Humidity
# ✔ Pressure
# ✔ Wind Speed
# ✔ Visibility
# ✔ Cloud Coverage
# ✔ Sunrise
# ✔ Sunset
# ✔ Country & City
# ✔ Weather Icons
# ==========================================================

import customtkinter as ctk
import requests
from tkinter import messagebox
from datetime import datetime

# ==========================================================
# API KEY
# ==========================================================
API_KEY = "c9075812865bc040437ddf95e2eca8de"

# ==========================================================
# APP SETTINGS
# ==========================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🌦 Weather Dashboard Pro")
app.geometry("1000x750")
app.minsize(900, 650)

# ==========================================================
# WEATHER ICONS
# ==========================================================
def get_icon(weather):
    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Thunderstorm": "⛈️",
        "Drizzle": "🌦️",
        "Mist": "🌫️",
        "Fog": "🌫️",
        "Snow": "❄️",
        "Haze": "🌤️"
    }
    return icons.get(weather, "🌍")

# ==========================================================
# GET WEATHER
# ==========================================================
def get_weather():

    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Warning", "Please enter city name")
        return

    try:

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={city}&appid={API_KEY}&units=metric"
        )

        data = requests.get(url).json()

        if str(data.get("cod")) != "200":
            messagebox.showerror("Error", "City not found")
            return

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]

        temp = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        wind_speed = data["wind"]["speed"]

        visibility = data.get("visibility", 0) / 1000

        clouds = data["clouds"]["all"]

        city_name = data["name"]
        country = data["sys"]["country"]

        sunrise = datetime.fromtimestamp(
            data["sys"]["sunrise"]
        ).strftime("%I:%M:%S %p")

        sunset = datetime.fromtimestamp(
            data["sys"]["sunset"]
        ).strftime("%I:%M:%S %p")

        updated_time = datetime.now().strftime(
            "%d-%m-%Y %I:%M:%S %p"
        )

        icon = get_icon(weather)

        # Update UI
        weather_icon.configure(text=icon)
        weather_name.configure(text=weather)
        weather_desc.configure(text=description.title())

        temp_label.configure(text=f"{temp}°C")

        city_label.configure(
            text=f"📍 City : {city_name}"
        )

        country_label.configure(
            text=f"🌍 Country : {country}"
        )

        feels_label.configure(
            text=f"🤔 Feels Like : {feels_like}°C"
        )

        humidity_label.configure(
            text=f"💧 Humidity : {humidity}%"
        )

        pressure_label.configure(
            text=f"📈 Pressure : {pressure} hPa"
        )

        wind_label.configure(
            text=f"🌬 Wind Speed : {wind_speed} m/s"
        )

        visibility_label.configure(
            text=f"👁 Visibility : {visibility:.1f} km"
        )

        cloud_label.configure(
            text=f"☁ Cloud Coverage : {clouds}%"
        )

        sunrise_label.configure(
            text=f"🌅 Sunrise : {sunrise}"
        )

        sunset_label.configure(
            text=f"🌇 Sunset : {sunset}"
        )

        updated_label.configure(
            text=f"🕒 Updated : {updated_time}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ==========================================================
# HEADER
# ==========================================================
title = ctk.CTkLabel(
    app,
    text="🌦 WEATHER DASHBOARD PRO",
    font=("Segoe UI", 34, "bold")
)
title.pack(pady=15)

subtitle = ctk.CTkLabel(
    app,
    text="Real Time Weather Monitoring System",
    font=("Segoe UI", 16)
)
subtitle.pack()

# ==========================================================
# SEARCH SECTION
# ==========================================================
search_frame = ctk.CTkFrame(app)
search_frame.pack(pady=20)

city_entry = ctk.CTkEntry(
    search_frame,
    width=350,
    height=45,
    placeholder_text="Enter City Name..."
)
city_entry.pack(side="left", padx=10)

search_btn = ctk.CTkButton(
    search_frame,
    text="Get Weather",
    width=150,
    height=45,
    command=get_weather
)
search_btn.pack(side="left")

# ==========================================================
# MAIN CARD
# ==========================================================
card = ctk.CTkFrame(
    app,
    corner_radius=25
)
card.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

# ==========================================================
# WEATHER ICON
# ==========================================================
weather_icon = ctk.CTkLabel(
    card,
    text="🌤️",
    font=("Segoe UI Emoji", 90)
)
weather_icon.pack(pady=(20, 0))

# ==========================================================
# TEMPERATURE
# ==========================================================
temp_label = ctk.CTkLabel(
    card,
    text="--°C",
    font=("Segoe UI", 60, "bold"),
    text_color="#38BDF8"
)
temp_label.pack()

# ==========================================================
# WEATHER NAME
# ==========================================================
weather_name = ctk.CTkLabel(
    card,
    text="Weather",
    font=("Segoe UI", 28, "bold")
)
weather_name.pack()

weather_desc = ctk.CTkLabel(
    card,
    text="Description",
    font=("Segoe UI", 16)
)
weather_desc.pack(pady=5)

# ==========================================================
# SCROLLABLE DETAILS
# ==========================================================
details = ctk.CTkScrollableFrame(
    card,
    width=800,
    height=280
)
details.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

city_label = ctk.CTkLabel(details, text="📍 City : --", anchor="w", font=("Segoe UI", 18))
city_label.pack(anchor="w", pady=5)

country_label = ctk.CTkLabel(details, text="🌍 Country : --", anchor="w", font=("Segoe UI", 18))
country_label.pack(anchor="w", pady=5)

feels_label = ctk.CTkLabel(details, text="🤔 Feels Like : --", anchor="w", font=("Segoe UI", 18))
feels_label.pack(anchor="w", pady=5)

humidity_label = ctk.CTkLabel(details, text="💧 Humidity : --", anchor="w", font=("Segoe UI", 18))
humidity_label.pack(anchor="w", pady=5)

pressure_label = ctk.CTkLabel(details, text="📈 Pressure : --", anchor="w", font=("Segoe UI", 18))
pressure_label.pack(anchor="w", pady=5)

wind_label = ctk.CTkLabel(details, text="🌬 Wind Speed : --", anchor="w", font=("Segoe UI", 18))
wind_label.pack(anchor="w", pady=5)

visibility_label = ctk.CTkLabel(details, text="👁 Visibility : --", anchor="w", font=("Segoe UI", 18))
visibility_label.pack(anchor="w", pady=5)

cloud_label = ctk.CTkLabel(details, text="☁ Cloud Coverage : --", anchor="w", font=("Segoe UI", 18))
cloud_label.pack(anchor="w", pady=5)

sunrise_label = ctk.CTkLabel(details, text="🌅 Sunrise : --", anchor="w", font=("Segoe UI", 18))
sunrise_label.pack(anchor="w", pady=5)

sunset_label = ctk.CTkLabel(details, text="🌇 Sunset : --", anchor="w", font=("Segoe UI", 18))
sunset_label.pack(anchor="w", pady=5)

updated_label = ctk.CTkLabel(details, text="🕒 Updated : --", anchor="w", font=("Segoe UI", 18))
updated_label.pack(anchor="w", pady=5)

# ==========================================================
# FOOTER
# ==========================================================
footer = ctk.CTkLabel(
    app,
    text="🚀 Developed by Puspesh Tripathi",
    font=("Segoe UI", 14)
)
footer.pack(pady=10)

app.mainloop()