import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Space Biosignatures Reference", layout="wide")

# Title and introduction
st.title("Space Biosignatures Reference")
st.write("A collection of biosignatures that may indicate extraterrestrial life.")


# Biosignature dataset
biosignatures = [
    {"Biosignature": "Methane (CH₄)", "Type": "Chemical", "Found On": "Mars, Titan", 
     "Missions": "Curiosity, JWST", "Description": "Produced by microbial life and geological processes."},
    {"Biosignature": "Phosphine (PH₃)", "Type": "Chemical", "Found On": "Venus (Debated)", 
     "Missions": "TBD", "Description": "Possible indicator of anaerobic life; controversial detection."},
    {"Biosignature": "Carbon Isotope Ratios", "Type": "Isotopic", "Found On": "Mars", 
     "Missions": "Perseverance", "Description": "Microbial life prefers lighter isotopes, creating distinctive ratios."},
    {"Biosignature": "Stromatolites", "Type": "Morphological", "Found On": "Earth (Fossil Record)", 
     "Missions": "N/A", "Description": "Layered rock formations created by microbial mats."},
    {"Biosignature": "Oxygen (O₂) and Ozone (O₃)", "Type": "Atmospheric", "Found On": "Earth, Exoplanets", 
     "Missions": "Hubble, JWST", "Description": "High oxygen levels can indicate photosynthesis."},
    {"Biosignature": "Amino Acids", "Type": "Organic", "Found On": "Meteorites", 
     "Missions": "OSIRIS-REx", "Description": "Building blocks of proteins; essential for life."},
    {"Biosignature": "Biogenic Magnetite", "Type": "Mineralogical", "Found On": "Mars (ALH84001 meteorite)", 
     "Missions": "Mars Sample Return", "Description": "Magnetite crystals with specific morphologies indicative of biological origin."},
    {"Biosignature": "Methyl Bromide (CH₃Br)", "Type": "Chemical", "Found On": "Exoplanets (Hypothetical)", 
     "Missions": "Future Observations", "Description": "Potential biosignature gas that could indicate biological activity."},
    {"Biosignature": "Nitric Oxide (NO)", "Type": "Chemical", "Found On": "Exoplanets (Hypothetical)", 
     "Missions": "Future Observations", "Description": "Emissions from nitrogen-rich atmospheres influenced by stellar activity."}
]

# Convert to Pandas DataFrame
df = pd.DataFrame(biosignatures)

# Sidebar filters
st.sidebar.header("Filter Biosignatures")
biosignature_types = df["Type"].unique().tolist()

# Default to no selection (user must choose)
selected_type = st.sidebar.multiselect("Select Type", options=biosignature_types, default=[])

# Apply filters
filtered_df = df[df["Type"].isin(selected_type)] if selected_type else pd.DataFrame(columns=df.columns)

# Search bar for keyword filtering
search_query = st.sidebar.text_input("Search Biosignatures", "")
if not filtered_df.empty:
    filtered_df = filtered_df[filtered_df.apply(lambda row: search_query.lower() in row.to_string().lower(), axis=1)]

# Display results
st.subheader("Interactive Biosignatures Table")
st.dataframe(filtered_df.reset_index(drop=True).rename(index=lambda x: x + 1), use_container_width=True)

# Expandable descriptions
st.subheader("Detailed Biosignature Descriptions")
for _, row in filtered_df.iterrows():
    with st.expander(f"{row['Biosignature']} ({row['Type']})"):
        st.write(f"**Found On:** {row['Found On']}")
        st.write(f"**Missions:** {row['Missions']}")
        st.write(f"**Description:** {row['Description']}")

# Footer
st.write("🔗 **Data sources:** NASA, ESA, published research articles.")
st.write("<p style='color:grey;'>A project by PY Heng</p>", unsafe_allow_html=True)