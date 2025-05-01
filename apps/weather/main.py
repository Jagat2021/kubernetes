from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

dummy_users = [
    "Alice Johnson", "Bob Smith", "Charlie Lee", "Diana Prince", "Ethan Hunt"
]

sports_products = [
    {"name": "Football", "img": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Football_iu_1996.jpg"},
    {"name": "Tennis Racket", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Tennis_racket_and_balls.jpg"},
    {"name": "Basketball", "img": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Basketball.png"},
    {"name": "Running Shoes", "img": "https://upload.wikimedia.org/wikipedia/commons/2/20/Running_Shoes_Asics_Gel-Kayano_22.JPG"},
    {"name": "Yoga Mat", "img": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Yoga_mat.jpg"}
]

cities_weather = [
    {"city": "New York", "weather": "☀️ Sunny"},
    {"city": "London", "weather": "☁️ Cloudy"},
    {"city": "Tokyo", "weather": "🌧 Rainy"},
    {"city": "Dubai", "weather": "🔥 Hot"},
    {"city": "Sydney", "weather": "🌬 Windy"}
]

def get_html_template(body: str, title: str):
    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #ece9e6, #ffffff);
                color: #333;
                padding: 30px;
                text-align: center;
            }}
            a {{
                color: #007BFF;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .card {{
                display: inline-block;
                background: white;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 15px;
                margin: 10px;
                box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
                width: 180px;
                vertical-align: top;
            }}
            img {{
                border-radius: 8px;
                width: 150px;
                height: 150px;
                object-fit: cover;
            }}
            h1 {{
                color: #333;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        <nav>
            <a href="/">Home</a> |
            <a href="/users">Users</a> |
            <a href="/products">Products</a> |
            <a href="/weather">Weather</a>
        </nav>
        <hr>
        {body}
        <hr>
        <footer>FastAPI Web App • Powered by Python 🚀</footer>
    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
def home():
    return get_html_template("""
        <h2>Welcome to the DevOps!</h2>
        <p>Select a tab to view users, products, or city weather info.</p>
    """, "Home")

@app.get("/users", response_class=HTMLResponse)
def get_users():
    user_html = "".join([
        f'<div class="card"><img src="https://i.pravatar.cc/150?img={i+10}"><br>{name}</div>'
        for i, name in enumerate(dummy_users)
    ])
    return get_html_template(user_html, "Users")

@app.get("/products", response_class=HTMLResponse)
def get_products():
    product_html = "".join([
        f'<div class="card"><img src="{item["img"]}"><br>{item["name"]}</div>'
        for item in sports_products
    ])
    return get_html_template(product_html, "Sports Products")

@app.get("/weather", response_class=HTMLResponse)
def get_weather():
    random.shuffle(cities_weather)
    weather_html = "".join([
        f'<div class="card"><strong>{entry["city"]}</strong><br>{entry["weather"]}</div>'
        for entry in cities_weather
    ])
    return get_html_template(weather_html, "City Weather")