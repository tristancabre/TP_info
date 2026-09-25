import streamlit as st

from utils.api_client import api_client
from utils.log_init import get_page_logger

st.title("##Player stats")

logger = get_page_logger("player_stats")

query_params = st.query_params
player_id = int(query_params.get("id_player"))
logger.info(f"player {player_id} stats")

if player_id is not None:
    player_res = api_client.get(f"/player/{player_id}")

if player_res["status code"] == 200:
    player = player_res["data"]
    logger.info("request successfull")

    # ---Profil---
    st.subheader(f"{player['username']}")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Elo rating", player["elo"])
    with col2:
        st.write(f"**Email:** {player['email']}")
        st.checkbox("Pokemon Fan", value=player["pokemon_fan"], disabled=True)
    st.divider()

    # ---Games Played---
    st.subheader("Game History")
    logger.info(f"Fetching match history for player : {player['username']}")
    games_res = api_client.get(f"/game?id_player={player_id}")

    if games_res["status_code"] == 200:
        games_list = games_res["data"]
        logger.info("request successfull")

        if not games_list:
            st.info("No games played yet")
