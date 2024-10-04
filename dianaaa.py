st.write(f"☔ **Probabilidade de Precipitação**: {weather['precip_prob']}")


# Botão para Meteorologia e Qualidade do Ar
with col3:
    if st.button("🌤️ Meteorologia"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("🌤️ Tempo e Qualidade do Ar em Aveiro Atualmente")
            
            # Obter dados meteorológicos
            weather = get_weather_data()

            if weather:
                st.write(f"📅 **Dia**: {weather['day_info']}")
                st.write(f"🌡️ **Temperatura Máxima**: {weather['high_temp']}")
                st.write(f"🌡️ **Temperatura Mínima**: {weather['low_temp']}")
                st.write(f"☔ **Probabilidade de Precipitação**: {weather['precip_prob']}")
            else:
                st.error("Erro ao obter os dados meteorológicos.")

            # Obter dados de qualidade do ar
            air_quality, date, aqi_value, quality_type = get_air_quality_data()

            if air_quality != "Erro ao obter os dados":
                st.write(f"🌡️ Índice de Qualidade do Ar: {aqi_value} - {quality_type}")
            else:
                st.error("Erro ao obter os dados de qualidade do ar.")
