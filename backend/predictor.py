import random

# ---------------------------
# 🎨 COLOR DATABASE (YOUR DATA)
# ---------------------------
COLOR_DB = {

("fair","warm"): ["#FFDAB9","#FF7F50","#FFC30B","#FFDB58","#E2725B","#F5DEB3","#FF8C00","#D4AF37","#FFE5B4","#F4A460"],

("medium","warm"): ["#FFB000","#B7410E","#CC5500","#808000","#FF4040","#008080","#A0522D","#FF8C00","#DAA520","#C68642"],

("dusky","warm"): ["#E1AD01","#E97451","#556B2F","#CD7F32","#8B2500","#FF4500","#5C4033","#B87333","#800020","#228B22"],

("dark","warm"): ["#FFB000","#FF4500","#8B0000","#B87333","#CD7F32","#808000","#FFD700","#654321","#3B2F2F","#A52A2A"],


("fair","cool"): ["#FFB6C1","#E6E6FA","#C8A2C8","#87CEEB","#B0E0E6","#98FF98","#AFEEEE","#D3D3D3","#DDA0DD","#ADD8E6"],

("medium","cool"): ["#4169E1","#50C878","#FF00FF","#8A2BE2","#722F37","#0F52BA","#008080","#9400D3","#36454F","#9932CC"],

("dusky","cool"): ["#673147","#800020","#000080","#4B0082","#36454F","#722F37","#FF00FF","#50C878","#9400D3","#000000"],

("dark","cool"): ["#4169E1","#0F52BA","#4B0082","#FF00FF","#800020","#722F37","#000080","#50C878","#000000","#708090"],


("fair","neutral"): ["#FFC0CB","#FFDAB9","#D3D3D3","#FFFFF0","#BC8F8F","#E6E6FA","#98FF98","#87CEEB","#FFB6C1","#FFFDD0"],

("medium","neutral"): ["#008080","#FF7F50","#FF007F","#00A86B","#8B0000","#000080","#808000","#FFDB58","#915F6D","#D8BFD8"],

("dusky","neutral"): ["#50C878","#800020","#008080","#8E4585","#FFDB58","#B7410E","#3B2F2F","#FF4040","#000080","#556B2F"],

("dark","neutral"): ["#50C878","#4169E1","#800020","#8E4585","#FFDB58","#B87333","#CD7F32","#8B0000","#000080","#556B2F"]

}

# ---------------------------
# 👗 OUTFITS
# ---------------------------
OUTFITS = {
    "male": {
        "casual": ["T-shirt + Jeans", "Polo + Chinos", "Hoodie + Joggers", "Casual Shirt + Shorts", "Denim Jacket + Tee", "Printed Shirt + Jeans", "Oversized Tee + Cargo", "Sweatshirt + Jeans", "Tank + Shorts", "Casual Kurta"],
        "formal": ["Formal Shirt + Trousers", "Blazer + Pants", "3-piece Suit", "Tie + Shirt Combo", "Waistcoat Set", "Slim Fit Suit", "Office Shirt + Chinos", "Blazer + Jeans", "Formal Kurta Set", "Classic Suit"],
        "party": ["Printed Shirt + Black Jeans", "Shiny Shirt + Trousers", "Blazer + Tee", "Dark Shirt + Denim", "Velvet Blazer", "Party Kurta", "Designer Shirt", "Slim Fit Outfit", "Black on Black", "Casual Blazer Look"],
        "wedding": ["Sherwani", "Kurta Set", "Indo-Western", "Designer Sherwani", "Silk Kurta", "Wedding Suit", "Ethnic Jacket Set", "Traditional Dhoti Set", "Royal Kurta", "Classic Ethnic Wear"]
    },

    "female": {
        "casual": ["Kurti + Leggings", "Top + Jeans", "Summer Dress", "Oversized Tee + Pants", "Crop Top + Skirt", "Casual Saree", "Salwar Set", "Denim Jacket Look", "Maxi Dress", "Tank + Jeans"],
        "formal": ["Pant Suit", "Blazer Dress", "Formal Saree", "Shirt + Trousers", "Pencil Skirt + Top", "Office Kurti", "Formal Gown", "Structured Dress", "Blazer + Pants", "Elegant Saree"],
        "party": ["Gown", "Lehenga", "Party Saree", "Cocktail Dress", "Sequin Dress", "Designer Saree", "Crop Top + Lehenga", "Mini Dress", "Fusion Wear", "Stylish Gown"],
        "wedding": ["Silk Saree", "Bridal Lehenga", "Designer Saree", "Heavy Anarkali", "Kanjeevaram Saree", "Wedding Gown", "Ethnic Lehenga", "Traditional Saree", "Royal Outfit", "Bridal Wear"]
    }
}


# ---------------------------
# ✨ STYLING TIPS
# ---------------------------
TIPS = [
    "Add contrast for impact",
    "Keep accessories minimal",
    "Focus on fit over brand",
    "Confidence is your best style",
    "Balance light & dark tones",
    "Use layering smartly",
    "Highlight your best features",
    "Choose clean silhouettes",
    "Stick to 2–3 main colors",
    "Let one piece stand out"
]


# ---------------------------
# 🎯 MAIN FUNCTION
# ---------------------------
def get_recommendations(gender, skin_tone, undertone, occasion):

    gender = gender.lower()
    skin_tone = skin_tone.lower()
    undertone = undertone.lower()
    occasion = occasion.lower()

    # 🎨 COLORS
    palette = COLOR_DB.get((skin_tone, undertone), ["Black", "White", "Grey"])
    
    # 👗 OUTFITS
    outfit_list = OUTFITS.get(gender, OUTFITS["male"])
    outfits = outfit_list.get(occasion, outfit_list["casual"])

    # attach styling tips
    outfit_cards = []
    for o in outfits:
        outfit_cards.append({
            "name": o,
            "tip": random.choice(TIPS)
        })

    return {
        "palette": palette,          # exactly 10 colors
        "outfits": outfit_cards      # 10 outfits with tips
    }