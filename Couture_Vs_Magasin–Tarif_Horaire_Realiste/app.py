import streamlit as st

st.title("🧵 Couture vs Magasin – Tarif horaire réaliste")

# --- Machine ---
st.sidebar.header("Machine")
machine_prix = st.sidebar.number_input("Prix machine (€)", 0.0, 2000.0, 300.0)
machine_projets = st.sidebar.number_input("Nombre de projets prévus avec la machine", 1, 500, 100)
cout_machine = machine_prix / machine_projets

# --- Patron ---
st.sidebar.header("Patron")
patron_prix = st.sidebar.number_input("Prix du patron (€)", 0.0, 50.0, 12.0)
patron_uses = st.sidebar.number_input("Nombre d'utilisations prévues", 1, 20, 5)
cout_patron = patron_prix / patron_uses

# --- Projet ---
st.header("Projet Couture")
nom_projet = st.text_input("Nom du projet", "Blouse boho")
prix_tissu = st.number_input("Prix du tissu (€)", 0.0, 200.0, 25.0)
prix_mercerie = st.number_input("Prix mercerie (€)", 0.0, 100.0, 5.0)
heures_passées = st.number_input("Nombre d'heures passées", 0.0, 100.0, 10.0)
prix_magasin = st.number_input("Prix estimé du vêtement en magasin (€)", 0.0, 500.0, 50.0)
nom_magasin = st.text_input("Nom du magasin", "Sézane")

# --- Calculs ---
cout_total = prix_tissu + prix_mercerie + cout_patron + cout_machine
diff = prix_magasin - cout_total

# Tarif horaire réaliste : combien tu “gagnes par heure” en cousant plutôt qu’en achetant
tarif_horaire_reel = diff / heures_passées if heures_passées > 0 else 0

# --- Résultats ---
st.subheader(f"Résultats pour {nom_projet}")
st.write(f"💰 Coût total couture : {cout_total:.2f} €")
st.write(f"🛍️ Prix magasin ({nom_magasin}) : {prix_magasin:.2f} €")
st.write(f"⏱️ Tarif horaire réaliste : {tarif_horaire_reel:.2f} €/h")


# Message sur économies ou surcoût
if diff > 0:
    st.success(f"🎉 Tu as économisé {diff:.2f} € par rapport à {nom_magasin} !")
else:
    st.warning(f"💖 Tu as investi {-diff:.2f} € de plus que chez {nom_magasin}, mais c’est unique et fait main !")
if tarif_horaire_reel > 10:
    st.success("💎 Wow super tarif horaire !")
elif tarif_horaire_reel > 0:
    st.info("😉 Cela a pris pas mal de temps mais tu as gagné un peu d’argent par rapport au magasin, bravo !")
else:
    st.warning("😅 C’est un hobby… ton salaire horaire est négatif, mais le plaisir n’a pas de prix !")
