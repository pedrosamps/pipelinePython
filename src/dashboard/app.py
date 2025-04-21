import streamlit as st
import pandas as pd

df = pd.read_excel('C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Python-projetos\\pipelinePython\\data\\dados.xlsx')

# Título da aplicação
st.title('📊 Pesquisa de Mercado - Notebooks no Mercado Livre')

# Melhorar o layout com colunas para KPIs
st.subheader('💡 KPIs principais')
col1, col2, col3 = st.columns(3)

# KPI 1: Número total de itens
total_itens = df.shape[0]
col1.metric(label="🖥️ Total de Notebooks", value=total_itens)

# KPI 2: Número de marcas únicas
unique_brands = df['Marca'].nunique()
col2.metric(label="🏷️ Marcas Únicas", value=unique_brands)

# KPI 3: Preço médio novo (em reais)
average_new_price = df['Preço'].mean()
col3.metric(label="💰 Preço Médio (R$)", value=f"{average_new_price:.2f}")

# Marcas mais frequentes
st.subheader('🏆 Marcas mais encontradas até a 5ª página')
col1, col2 = st.columns([4, 2])
top_brands = df['Marca'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
col2.write(top_brands)

# Preço médio por marca
st.subheader('💵 Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['Preço'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('Marca')['Preço'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Satisfação média por marca
st.subheader('⭐ Satisfação média por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['Número de classificação da revisão'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('Marca')['Número de classificação da revisão'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)