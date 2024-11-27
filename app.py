# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import base64

# # Function to get the base64 encoding of the image
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# # Path to your image
# img_path = 'background2.jpg' 

# # Get base64 encoded image
# img_base64 = get_base64_of_bin_file(img_path)

# # Custom CSS with the embedded image and scrolling effect
# page_bg_img = f'''
# <style>
# .stApp {{
#     background-image: url("data:image/jpg;base64,{img_base64}");
#     background-size: 110%;
#     background-position: center;
#     background-repeat: no-repeat;
# }}

# h1 {{
#     color: white !important;
#     font-size: 45px;
# }}
# </style>
# '''

# # Inject the CSS into your Streamlit app
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Function to fetch the poster and IMDb URL
# def fetch_poster_and_imdb(movie_id):
#     response = requests.get(f"https://www.omdbapi.com/?i={movie_id}&apikey=87c754a")
#     data = response.json()
#     poster = data['Poster']
#     imdb_url = f"https://www.imdb.com/title/{movie_id}/"  # IMDb URL
#     return poster, imdb_url

# # Recommend function
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

#     recommended_movies = []
#     recommended_movie_posters = []
#     recommended_movie_imdb_links = []
#     for movie_tuple in movies_list:
#         movie_id = movies.iloc[movie_tuple[0]].movie_id
#         recommended_movies.append(movies.iloc[movie_tuple[0]].title)
#         poster, imdb_link = fetch_poster_and_imdb(movie_id)  # Get poster and IMDb URL
#         recommended_movie_posters.append(poster)
#         recommended_movie_imdb_links.append(imdb_link)  # Store IMDb link
#     return recommended_movies, recommended_movie_posters, recommended_movie_imdb_links

# # Load movie data and similarity
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # Title with white color and custom styling
# st.title('🎥 Movie Recommender System')

# selected_movie_name = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

# if st.button('Show Recommendation'):
#     with st.spinner('Fetching recommendations...'):
#         names, posters, imdb_links = recommend(selected_movie_name)  # Fetch IMDb links too
#         cols = st.columns(5)

#         for i in range(5):
#             with cols[i]:
#                 st.text(names[i])
#                 st.image(posters[i])
#                 st.markdown(f"[IMDb Link]({imdb_links[i]})")  # Display IMDb link

#     st.success('Here are your recommendations!')




import streamlit as st
import pickle
import pandas as pd
import requests
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = 'background2.jpg'
img_base64 = get_base64_of_bin_file(img_path)

page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: 110%;
    background-position: center;
    background-repeat: no-repeat;
}}
h1 {{
    color: white !important;
    font-size: 45px;
}}
.stAlert {{
    color: white !important;
}}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def fetch_poster_and_imdb(movie_id):
    response = requests.get(f"https://www.omdbapi.com/?i={movie_id}&apikey=87c754a")
    data = response.json()
    poster = data['Poster']
    imdb_url = f"https://www.imdb.com/title/{movie_id}/"
    return poster, imdb_url

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movie_posters = []
    recommended_movie_imdb_links = []
    for movie_tuple in movies_list:
        movie_id = movies.iloc[movie_tuple[0]].movie_id
        recommended_movies.append(movies.iloc[movie_tuple[0]].title)
        poster, imdb_link = fetch_poster_and_imdb(movie_id)
        recommended_movie_posters.append(poster)
        recommended_movie_imdb_links.append(imdb_link)
    return recommended_movies, recommended_movie_posters, recommended_movie_imdb_links

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎥 Movie Recommender System')

selected_movie_name = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations...'):
        names, posters, imdb_links = recommend(selected_movie_name)
        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.markdown(f'<a href="{imdb_links[i]}" target="_blank"><img src="{posters[i]}" width="150"/></a>', unsafe_allow_html=True)

    st.success('Here are your recommendations!')










# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import base64

# # Function to get the base64 encoding of the image
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# # Path to your image
# img_path = 'background2.jpg' 

# # Get base64 encoded image
# img_base64 = get_base64_of_bin_file(img_path)

# # Custom CSS with the embedded image and scrolling effect
# page_bg_img = f'''
# <style>
# .stApp {{
#     background-image: url("data:image/jpg;base64,{img_base64}");
#     background-size: 110%;
#     background-position: center;
#     background-repeat: no-repeat;
#     # animation: backgroundScroll 20s linear infinite;  /* Scroll effect */
#     #  filter: brightness(0.5); 
    
# }}


# @keyframes backgroundScroll {{
#     0% {{ background-position: right top; }}
#     100% {{ background-position: left top; }}
# }}

# h1 {{
#     color: white !important;  /* Ensure title is white */
#     font-size: 45px;
# }}
# </style>
# '''

# # Inject the CSS into your Streamlit app
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Movie recommender app code
# def fetch_poster(movie_id):
#     response = requests.get("https://www.omdbapi.com/?i={}&apikey=87c754a".format(movie_id))
#     data = response.json()
#     return data['Poster']

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

#     recommended_movies = []
#     recommended_movie_posters = []
#     for movie_tuple in movies_list:
#         movie_id = movies.iloc[movie_tuple[0]].movie_id
#         recommended_movies.append(movies.iloc[movie_tuple[0]].title)
#         recommended_movie_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movie_posters

# # Load movie data and similarity
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# # Title with white color and custom styling
# st.title('🎥 Movie Recommender System')

# selected_movie_name = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

# if st.button('Show Recommendation'):
#     with st.spinner('Fetching recommendations...'):
#         names, posters = recommend(selected_movie_name)
#         cols = st.columns(5)

#         for i in range(5):
#             with cols[i]:
#                 st.text(names[i])
#                 st.image(posters[i])

#     st.success('Here are your recommendations!')













# # Function to load and encode the image
# def get_base64_image(image_file):
#     with open(image_file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# # Load the background image
# background_image = get_base64_image('background.jpeg')

# # Function to check if the background image is accessible
# def check_image():
#     try:
#         # Attempt to decode the image
#         _ = base64.b64decode(background_image)
#         return True
#     except Exception as e:
#         return False

# # Set up the CSS for background animation
# def set_css(background_valid):
#     if background_valid:
#         # Use base64 image if valid
#         css = f"""
#         <style>
#         body {{
#             background-color: black;
#             margin: 0;
#             overflow: hidden; /* Hide scrollbars */
#         }}
#         .reportview-container {{
#             background: url('data:image/jpeg;base64,{background_image}') repeat; /* Repeat the background */
#             animation: scrollBackground 20s linear infinite; /* Animate for 20 seconds, infinite loop */
#         }}
        
#         @keyframes scrollBackground {{
#             0% {{
#                 background-position: 0 0; /* Start at the left */
#             }}
#             100% {{
#                 background-position: 100% 0; /* Scroll to the right side */
#             }}
#         }}
        
#         /* Styling for other elements */
#         .stButton>button {{
#             background-color: #FFD700;
#             color: black;
#             font-size: 16px;
#             border-radius: 10px;
#             padding: 10px 24px;
#         }}
        
#         .stText, .stImage {{
#             text-align: center;
#             color: white;
#         }}
#         </style>
#         """
#     else:
#         # Fallback CSS with a solid color
#         css = """
#         <style>
#         body {
#             background-color: #333; /* Fallback color */
#             margin: 0;
#             overflow: hidden; /* Hide scrollbars */
#         }
#         .reportview-container {
#             background: #333; /* Keep the fallback color */
#         }

#         /* Styling for other elements */
#         .stButton>button {
#             background-color: #FFD700;
#             color: black;
#             font-size: 16px;
#             border-radius: 10px;
#             padding: 10px 24px;
#         }

#         .stText, .stImage {
#             text-align: center;
#             color: white;
#         }
#         </style>
#         """
#     return css

# # Check if the background image is valid
# background_valid = check_image()

# # Set the CSS based on image validity
# st.markdown(set_css(background_valid), unsafe_allow_html=True)

# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# import base64

# # Function to get the base64 encoding of the image
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# # Path to your image
# img_path = 'background2.jpg'

# # Get base64 encoded image
# img_base64 = get_base64_of_bin_file(img_path)

# # Custom CSS with the embedded image
# page_bg_img = f'''
# <style>
# .stApp {{
#     background-image: url("data:image/jpg;base64,{img_base64}");
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
# }}
# </style>
# '''

# # Inject the CSS into your Streamlit app
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Movie recommender app code
# def fetch_poster(movie_id):
#     response = requests.get("https://www.omdbapi.com/?i={}&apikey=87c754a".format(movie_id))
#     data = response.json()
#     return data['Poster']

# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

#     recommended_movies = []
#     recommended_movie_posters = []
#     for movie_tuple in movies_list:
#         movie_id = movies.iloc[movie_tuple[0]].movie_id
#         recommended_movies.append(movies.iloc[movie_tuple[0]].title)
#         recommended_movie_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movie_posters

# # Load movie data and similarity
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# st.title('🎥 Movie Recommender System')

# st.markdown("""
#     <style>
#     .title {
#         color: white;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# selected_movie_name = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

# if st.button('Show Recommendation'):
#     with st.spinner('Fetching recommendations...'):
#         names, posters = recommend(selected_movie_name)
#         cols = st.columns(5)

#         for i in range(5):
#             with cols[i]:
#                 st.text(names[i])
#                 st.image(posters[i])

#     st.success('Here are your recommendations!')


