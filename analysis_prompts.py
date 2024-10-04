import streamlit as st
import json
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

# Load and preprocess the data
def load_prompts(json_file="sample_json.json"):
    with open(json_file, "r") as file:
        data = json.load(file)
    return [entry['prompt'] for entry in data]

# Function to process text and remove stopwords
def preprocess_text(text):
    stop_words = set(stopwords.words('portuguese'))  # Assuming prompts are in Portuguese
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    return filtered_words

# Keyword frequency analysis
def keyword_analysis(prompts):
    all_words = []
    for prompt in prompts:
        all_words.extend(preprocess_text(prompt))
    word_counts = Counter(all_words)
    return word_counts

# Function to categorize prompts by theme
def categorize_prompts(prompts):
    themes = {
        'trânsito': ['trânsito', 'congestionamento', 'acidente', 'estrada', 'tráfego'],
        'eventos': ['evento', 'festival', 'concerto', 'exposição', 'show'],
        'turismo': ['turista', 'museu', 'atração', 'pontos turísticos', 'sítio']
    }
    
    theme_counts = {theme: 0 for theme in themes}
    
    for prompt in prompts:
        words = preprocess_text(prompt)
        for theme, keywords in themes.items():
            if any(word in keywords for word in words):
                theme_counts[theme] += 1
    
    return theme_counts

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'main'  # Initialize the 'page' state

# Main Page
if st.session_state['page'] == 'main':
    st.title("LLMAveiro Dashboard")

    # Description of the app and an analyze button
    st.write("Bem-vindo ao painel do LLMAveiro! Clique no botão abaixo para analisar os prompts dos usuários.")
    
    if st.button("Ir para análise"):
        st.session_state['page'] = 'analysis'  # Navigate to analysis page

# Analysis Page
elif st.session_state['page'] == 'analysis':
    st.title("Análise de Dados LLMAveiro")

    # Load prompts
    prompts = load_prompts()

    # Keyword Analysis Section
    st.header("Análise de Frequência de Palavras")

    if prompts:
        word_counts = keyword_analysis(prompts)

        # Displaying a histogram
        top_keywords = word_counts.most_common(10)  # Top 10 keywords
        keywords, counts = zip(*top_keywords)

        st.subheader("Palavras Mais Frequentes nos Prompts")

        fig, ax = plt.subplots()
        ax.barh(keywords, counts)
        ax.set_xlabel('Frequência')
        ax.set_title('Palavras Mais Frequentes nos Prompts dos Usuários')
        st.pyplot(fig)

        # Display Word Cloud
        st.subheader("Nuvem de Palavras")
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)
    else:
        st.write("Nenhum prompt disponível para análise.")

    # Theme Analysis Section
    st.header("Análise de Temas")
    theme_counts = categorize_prompts(prompts)

    # Displaying theme counts
    st.subheader("Temas dos Prompts")
    theme_names, theme_values = zip(*theme_counts.items())

    fig, ax = plt.subplots()
    ax.bar(theme_names, theme_values)
    ax.set_xlabel('Temas')
    ax.set_ylabel('Contagem')
    ax.set_title('Distribuição dos Temas nos Prompts dos Usuários')
    st.pyplot(fig)

    # Button to go back to the main page
    if st.button("Voltar para o início"):
        st.session_state['page'] = 'main'  # Navigate back to the main page
