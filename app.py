import streamlit as st
import re

# Nagłówek ankiety
st.title('Ankieta')

# Pole do wprowadzenia adresu e-mail
email = st.text_input('Podaj swój adres e-mail')

# Pole do wprowadzenia nazwiska
nazwisko = st.text_input('Podaj swoje nazwisko')

# Lista wyboru stanowiska
stanowiska = ['Student', 'Nauczyciel', 'Naukowiec', 'Inżynier', 'Menadżer', 'Inne']
stanowisko = st.selectbox('Wybierz swoje stanowisko', stanowiska)

# Pytanie, czy użytkownik ma swoje publikacje
ma_publikacje = st.radio('Czy posiadasz swoje publikacje?', ('Tak', 'Nie'))

# Lista pól tekstowych na publikacje, jeśli odpowiedź to "Tak"
publikacja1 = publikacja2 = publikacja3 = ""
if ma_publikacje == 'Tak':
    publikacja1 = st.text_input('Podaj tytuł publikacji 1')
    publikacja2 = st.text_input('Podaj tytuł publikacji 2')
    publikacja3 = st.text_input('Podaj tytuł publikacji 3')

# Funkcja do walidacji adresu e-mail
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Przycisk do przesłania odpowiedzi
if st.button('Prześlij odpowiedzi'):
    # Walidacja: wszystkie pola muszą być wypełnione
    if not email:
        st.error('Adres e-mail jest obowiązkowy.')
    elif not is_valid_email(email):
        st.error('Podaj prawidłowy adres e-mail.')
    elif not nazwisko:
        st.error('Nazwisko jest obowiązkowe.')
    elif not stanowisko:
        st.error('Stanowisko jest obowiązkowe.')
    elif ma_publikacje == 'Tak' and not (publikacja1 or publikacja2 or publikacja3):
        st.error('Musisz podać przynajmniej jedną publikację, jeśli zaznaczysz "Tak".')
    else:
        # Zbieranie wyników
        st.write('**Podsumowanie ankiety:**')
        st.write(f'E-mail: {email}')
        st.write(f'Nazwisko: {nazwisko}')
        st.write(f'Stanowisko: {stanowisko}')
        
        if ma_publikacje == 'Tak':
            st.write('Publikacje:')
            if publikacja1:
                st.write(f'1. {publikacja1}')
            if publikacja2:
                st.write(f'2. {publikacja2}')
            if publikacja3:
                st.write(f'3. {publikacja3}')
        else:
            st.write('Brak publikacji')

        st.success('Dziękujemy za przesłanie odpowiedzi!')
